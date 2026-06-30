from __future__ import annotations

import json
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENGINE_ROOT = WORKSPACE_ROOT / "bois"
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from bois.core.memory.store import JsonMemoryStore
from bois.core.models import ClientObject
from bois.core.orchestration.engine import BrandCognitiveOrchestrator
from bois.core.retrieval.gated_retriever import LocalHybridRetriever, RetrievalGate


def main() -> int:
    client = ClientObject(
        client_id="sample-nairobi-laundry",
        company_name="Sample Nairobi Laundry",
        sector="laundry services",
        geography="Nairobi",
        audience="urban professionals",
        psychographics=["convenience", "trust", "time scarcity"],
        market_position="premium convenience",
        competitors=["local laundromats", "home washing", "pickup laundry apps"],
        emotional_positioning="relief, polish, and dependable time recovery",
        governance_rules={"tone": "clear, trustworthy, culturally aware"},
    )

    memory = JsonMemoryStore(ENGINE_ROOT / "memory")
    memory.save_client(client)
    retriever = LocalHybridRetriever(ENGINE_ROOT / "knowledge" / "_indexes" / "paragraphs.jsonl")
    gate = RetrievalGate(retriever, memory)
    orchestrator = BrandCognitiveOrchestrator(gate, memory)
    context = orchestrator.assemble_context(
        client=client,
        task="Create a premium launch campaign for Nairobi urban professionals",
        deliverable="launch_campaign",
        positioning_objective="premium convenience and trust",
        communication_goal="make laundry feel reliable, polished, and time-saving",
        campaign_objective="launch with authority and adoption momentum",
    )
    orchestrator.persist_context(context)
    payload = {
        "context_id": context.context_id,
        "activated_agents": context.activated_agents,
        "missing_sources": context.retrieval_bundle.missing_sources if context.retrieval_bundle else [],
        "retrieved_sources": sorted(context.retrieval_bundle.results_by_source.keys()) if context.retrieval_bundle else [],
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

