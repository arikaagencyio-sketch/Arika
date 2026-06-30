from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENGINE_ROOT = WORKSPACE_ROOT / "bois"
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from bois.core.ingestion.pipeline import build_document_theme_index, collect_stage_signals, ingest, load_paragraphs
from bois.core.knowledge.graph_builder import build_graph, build_tag_adjacency, save_graph


def main() -> int:
    corpus_root = WORKSPACE_ROOT
    knowledge_out = ENGINE_ROOT / "knowledge" / "_indexes"
    report = ingest(corpus_root, knowledge_out)
    paragraphs = load_paragraphs(knowledge_out / "paragraphs.jsonl")

    graph = build_graph(paragraphs)
    save_graph(graph, ENGINE_ROOT / "memory_maps" / "knowledge_graph.json")

    theme_index = build_document_theme_index(paragraphs)
    stage_signals = collect_stage_signals(paragraphs)
    tag_adjacency = build_tag_adjacency(paragraphs)

    (ENGINE_ROOT / "memory_maps").mkdir(parents=True, exist_ok=True)
    with (ENGINE_ROOT / "memory_maps" / "document_theme_index.json").open("w", encoding="utf-8") as f:
        json.dump(theme_index, f, indent=2, ensure_ascii=False)
    with (ENGINE_ROOT / "memory_maps" / "stage_signals.json").open("w", encoding="utf-8") as f:
        json.dump(stage_signals, f, indent=2, ensure_ascii=False)
    with (ENGINE_ROOT / "memory_maps" / "tag_adjacency.json").open("w", encoding="utf-8") as f:
        json.dump(tag_adjacency, f, indent=2, ensure_ascii=False)
    with (ENGINE_ROOT / "knowledge" / "_indexes" / "ingestion_report.json").open("w", encoding="utf-8") as f:
        json.dump(asdict(report), f, indent=2, ensure_ascii=False)

    print(json.dumps(asdict(report), indent=2, ensure_ascii=False))
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
