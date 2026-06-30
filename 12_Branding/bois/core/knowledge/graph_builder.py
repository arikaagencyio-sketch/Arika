from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

from ..models import ParagraphRecord


ENTITY_PATTERNS = {
    "stage": re.compile(r"\b(stage|phase|layer|mode)\s+\d+\b", flags=re.IGNORECASE),
    "system": re.compile(r"\b[a-zA-Z0-9\-\s]{2,}system\b", flags=re.IGNORECASE),
    "agent": re.compile(r"\b[a-zA-Z0-9\-\s]{2,}agent\b", flags=re.IGNORECASE),
    "framework": re.compile(r"\b[a-zA-Z0-9\-\s]{2,}framework\b", flags=re.IGNORECASE),
}


def _extract_entities(text: str) -> List[Tuple[str, str]]:
    entities: List[Tuple[str, str]] = []
    for kind, pattern in ENTITY_PATTERNS.items():
        for m in pattern.finditer(text):
            entities.append((kind, m.group(0).strip()))
    return entities


def build_graph(paragraphs: List[ParagraphRecord]) -> Dict[str, List[Dict[str, str]]]:
    nodes: Dict[str, Dict[str, str]] = {}
    edges: List[Dict[str, str]] = []

    def add_node(node_id: str, node_type: str, label: str) -> None:
        if node_id not in nodes:
            nodes[node_id] = {"id": node_id, "type": node_type, "label": label}

    for p in paragraphs:
        doc_node = f"doc:{p.document_id}"
        para_node = f"para:{p.paragraph_id}"
        add_node(doc_node, "document", p.document_id)
        add_node(para_node, "paragraph", p.paragraph_id)
        edges.append({"source": doc_node, "target": para_node, "type": "contains"})

        for tag in p.tags:
            tag_node = f"tag:{tag}"
            add_node(tag_node, "tag", tag)
            edges.append({"source": para_node, "target": tag_node, "type": "tagged_as"})

        for kind, value in _extract_entities(p.text):
            entity_id = f"{kind}:{value.lower()}"
            add_node(entity_id, kind, value)
            edges.append({"source": para_node, "target": entity_id, "type": "mentions"})

        if p.reinforcement_count > 1:
            rep_node = f"rep:{p.text_hash}"
            add_node(rep_node, "reinforcement", p.text_hash)
            edges.append({"source": para_node, "target": rep_node, "type": "reinforces"})

    return {"nodes": list(nodes.values()), "edges": edges}


def save_graph(graph: Dict[str, List[Dict[str, str]]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)


def build_tag_adjacency(paragraphs: List[ParagraphRecord]) -> Dict[str, Dict[str, int]]:
    adjacency: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for p in paragraphs:
        for i, left in enumerate(p.tags):
            for right in p.tags[i + 1 :]:
                adjacency[left][right] += 1
                adjacency[right][left] += 1
    return {k: dict(v) for k, v in adjacency.items()}

