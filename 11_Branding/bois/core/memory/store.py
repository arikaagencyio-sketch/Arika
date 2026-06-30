from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from ..models import ClientObject


MEMORY_STREAMS = {
    "client": "client-memory",
    "campaign": "campaign-memory",
    "visual": "visual-memory",
    "narrative": "narrative-memory",
    "governance": "governance-memory",
    "market": "market-memory",
    "trend": "trend-memory",
    "stakeholder": "stakeholder-memory",
}


class JsonMemoryStore:
    """Append-only JSONL memory store for stateful brand cognition."""

    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        for stream_dir in MEMORY_STREAMS.values():
            (self.root / stream_dir).mkdir(parents=True, exist_ok=True)

    def client_path(self, client_id: str) -> Path:
        return self.root / "client-memory" / f"{client_id}.json"

    def save_client(self, client: ClientObject) -> None:
        path = self.client_path(client.client_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(asdict(client), f, indent=2, ensure_ascii=False)

    def load_client(self, client_id: str) -> Optional[ClientObject]:
        path = self.client_path(client_id)
        if not path.exists():
            return None
        with path.open("r", encoding="utf-8") as f:
            return ClientObject(**json.load(f))

    def append_event(
        self,
        client_id: str,
        stream: str,
        event_type: str,
        payload: Dict[str, Any],
        source: str = "bois",
    ) -> Path:
        if stream not in MEMORY_STREAMS:
            raise ValueError(f"Unsupported memory stream: {stream}")
        path = self.root / MEMORY_STREAMS[stream] / f"{client_id}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "client_id": client_id,
            "stream": stream,
            "event_type": event_type,
            "source": source,
            "payload": payload,
        }
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        return path

    def read_events(self, client_id: str, streams: Optional[Iterable[str]] = None) -> List[Dict[str, Any]]:
        selected = list(streams or MEMORY_STREAMS.keys())
        events: List[Dict[str, Any]] = []
        for stream in selected:
            if stream not in MEMORY_STREAMS:
                continue
            path = self.root / MEMORY_STREAMS[stream] / f"{client_id}.jsonl"
            if not path.exists():
                continue
            with path.open("r", encoding="utf-8") as f:
                for raw in f:
                    events.append(json.loads(raw))
        return sorted(events, key=lambda e: e.get("timestamp", ""))

    def query_events(self, client_id: str, query_terms: Iterable[str], streams: Optional[Iterable[str]] = None) -> List[Dict[str, Any]]:
        terms = [t.lower() for t in query_terms if t]
        matches: List[Dict[str, Any]] = []
        for event in self.read_events(client_id, streams=streams):
            searchable = json.dumps(event, ensure_ascii=False).lower()
            if all(term in searchable for term in terms):
                matches.append(event)
        return matches

