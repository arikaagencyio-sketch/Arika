from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

from ..ingestion.pipeline import load_paragraphs
from ..memory.store import JsonMemoryStore
from ..models import ClientObject, RetrievalBundle, RetrievalResult


REQUIRED_RETRIEVAL_SOURCES = [
    "sector_intelligence",
    "audience_psychology",
    "cultural_context",
    "client_memory",
    "previous_outputs",
    "governance_rules",
]

SOURCE_TAGS = {
    "sector_intelligence": {"sector", "industry"},
    "audience_psychology": {"psychology", "psychographics"},
    "cultural_context": {"culture"},
    "client_memory": {"client_memory"},
    "previous_outputs": {"campaign_memory", "visual_memory", "narrative_memory"},
    "governance_rules": {"governance", "legal"},
    "symbolic_systems": {"symbolic_systems", "visuals"},
    "narrative_systems": {"communication"},
    "distribution_intelligence": {"execution", "marketing"},
}


TOKEN_PATTERN = re.compile(r"[a-zA-Z0-9]+")


def tokenize(text: str) -> List[str]:
    return [m.group(0).lower() for m in TOKEN_PATTERN.finditer(text)]


class LocalHybridRetriever:
    """Keyword + taxonomy retriever used until external embeddings are attached."""

    def __init__(self, paragraph_jsonl: Path):
        self.paragraphs = load_paragraphs(paragraph_jsonl)
        self.doc_freq: Counter[str] = Counter()
        self.tokens_by_id: Dict[str, Counter[str]] = {}
        for p in self.paragraphs:
            tokens = Counter(tokenize(p.text))
            self.tokens_by_id[p.paragraph_id] = tokens
            for token in tokens:
                self.doc_freq[token] += 1
        self.total_docs = max(1, len(self.paragraphs))

    def _score(self, query_tokens: Sequence[str], paragraph_id: str) -> float:
        tokens = self.tokens_by_id[paragraph_id]
        score = 0.0
        for token in query_tokens:
            tf = tokens.get(token, 0)
            if not tf:
                continue
            idf = math.log((self.total_docs + 1) / (self.doc_freq[token] + 1)) + 1
            score += (1 + math.log(tf)) * idf
        return score

    def search(self, query: str, source: str, top_k: int = 8) -> List[RetrievalResult]:
        query_tokens = tokenize(query)
        expected_tags = SOURCE_TAGS.get(source, set())
        scored: List[RetrievalResult] = []
        for p in self.paragraphs:
            tag_overlap = len(expected_tags.intersection(p.tags))
            if expected_tags and tag_overlap == 0:
                continue
            score = self._score(query_tokens, p.paragraph_id) + (tag_overlap * 2.0)
            if p.reinforcement_count > 1:
                score += min(3.0, p.reinforcement_count * 0.2)
            if score > 0:
                scored.append(
                    RetrievalResult(
                        paragraph_id=p.paragraph_id,
                        document_id=p.document_id,
                        score=round(score, 4),
                        retrieval_mode="local_hybrid",
                        evidence={
                            "tags": p.tags,
                            "section_hint": p.section_hint,
                            "reinforcement_count": p.reinforcement_count,
                            "source_path": p.metadata.get("source_path"),
                            "excerpt": p.text[:600],
                        },
                    )
                )
        return sorted(scored, key=lambda r: r.score, reverse=True)[:top_k]


class RetrievalGate:
    def __init__(self, retriever: LocalHybridRetriever, memory_store: JsonMemoryStore):
        self.retriever = retriever
        self.memory_store = memory_store

    def assemble(
        self,
        query: str,
        client: ClientObject,
        required_sources: Iterable[str] = REQUIRED_RETRIEVAL_SOURCES,
        top_k: int = 8,
    ) -> RetrievalBundle:
        required = list(required_sources)
        results_by_source: Dict[str, List[RetrievalResult]] = defaultdict(list)

        enriched_query = " ".join(
            [
                query,
                client.company_name,
                client.sector,
                client.sub_sector,
                client.geography,
                client.audience,
                client.market_position,
                client.emotional_positioning,
                " ".join(client.psychographics),
                " ".join(client.competitors),
            ]
        )

        for source in required:
            if source in {"client_memory", "previous_outputs", "governance_rules"}:
                memory_results = self._retrieve_memory_source(source, client, query)
                results_by_source[source].extend(memory_results)
            if source not in {"client_memory", "previous_outputs"}:
                results_by_source[source].extend(self.retriever.search(enriched_query, source, top_k=top_k))

        missing = [source for source in required if not results_by_source.get(source)]
        return RetrievalBundle(
            query=query,
            required_sources=required,
            results_by_source=dict(results_by_source),
            missing_sources=missing,
        )

    def assert_complete(self, bundle: RetrievalBundle) -> None:
        if not bundle.is_complete:
            missing = ", ".join(bundle.missing_sources)
            raise RuntimeError(f"Retrieval gate failed. Missing required sources: {missing}")

    def _retrieve_memory_source(self, source: str, client: ClientObject, query: str) -> List[RetrievalResult]:
        terms = tokenize(query)[:8]
        if source == "client_memory":
            streams = ["client", "stakeholder", "market"]
        elif source == "previous_outputs":
            streams = ["campaign", "visual", "narrative"]
        else:
            streams = ["governance"]

        events = self.memory_store.query_events(client.client_id, terms, streams=streams)
        if not events and source == "client_memory":
            events = [{"payload": asdict(client), "stream": "client"}]
        if not events and source == "previous_outputs":
            events = [{"payload": {"status": "no_previous_outputs_recorded"}, "stream": "campaign"}]
        if not events and source == "governance_rules" and client.governance_rules:
            events = [{"payload": client.governance_rules, "stream": "governance"}]

        results: List[RetrievalResult] = []
        for idx, event in enumerate(events[:8], start=1):
            results.append(
                RetrievalResult(
                    paragraph_id=f"memory:{client.client_id}:{source}:{idx}",
                    document_id=f"client:{client.client_id}",
                    score=1.0,
                    retrieval_mode="memory",
                    evidence={"source": source, "event": event},
                )
            )
        return results


def save_retrieval_bundle(bundle: RetrievalBundle, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "query": bundle.query,
        "required_sources": bundle.required_sources,
        "missing_sources": bundle.missing_sources,
        "results_by_source": {
            source: [result.__dict__ for result in results]
            for source, results in bundle.results_by_source.items()
        },
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
