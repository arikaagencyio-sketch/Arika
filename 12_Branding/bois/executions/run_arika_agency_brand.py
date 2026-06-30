from __future__ import annotations

import json
import sys
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENGINE_ROOT = WORKSPACE_ROOT / "bois"
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from bois.core.client_workspace import create_client_workspace
from bois.core.memory.store import JsonMemoryStore
from bois.core.models import ClientObject
from bois.core.orchestration.engine import BrandCognitiveOrchestrator
from bois.core.retrieval.gated_retriever import LocalHybridRetriever, RetrievalGate


def main() -> int:
    # Every field below is sourced from facts already confirmed elsewhere in this
    # repo (AGENCY_VISION.md, AGENCY_REVENUE_TARGETS.md, OFFER_OS.md, SECTOR_OS.md,
    # OWNER_INPUT_NEEDED.md item 12). Fields with no confirmed real source
    # (competitors, visual/typography/color preferences) are left empty rather
    # than invented — tracker item 30's explicitly flagged residual gap.
    client = ClientObject(
        client_id="arika-agency",
        company_name="Arika Agency",
        sector="B2B Revenue Infrastructure / GTM Systems Agency",
        sub_sector="Revenue Operating System Provider for B2B SaaS",
        geography="Kenya-based, serving clients globally",
        audience=(
            "B2B SaaS companies, 3-tier ICP: Tier 1 (Series A-C, $5M-$50M ARR, "
            "50-500 employees, RevOps bottleneck, $15K-$50K/mo retainer budget); "
            "Tier 2 (Post-Seed-Series A, $1M-$10M ARR, founder still selling); "
            "Tier 3 (multi-location niche verticals - Healthcare, Real Estate "
            "Brokerages, Franchise Systems)"
        ),
        psychographics=[
            "RevOps bottleneck frustration (Tier 1)",
            "board-mandated efficiency pressure (Tier 1)",
            "founder drowning in solo-sold growth (Tier 2)",
            "distrust of fragmented vendor stacks",
            "revenue-mathematics literacy over vanity metrics",
        ],
        products=[],
        services=[
            "Revenue System Architecture",
            "Sales Enablement Systems",
            "Outbound Sales Engine",
            "Demand Generation Infrastructure",
            "Brand Positioning Systems",
            "AI Workflow Infrastructure",
            "Business Operating Systems",
            "Strategic Partnership Infrastructure",
            "Revenue Growth Advisory",
            "Revenue Infrastructure Audit",
            "AI Transformation Systems",
        ],
        pricing_model=(
            "ARR-band segmented (4 bands), project fee + monthly retainer hybrid "
            "per offer; first provisional pricing floor computed 2026-06-30 "
            "(see 02_Offer/OFFER_OS.md §10) - part-real/part-synthesized, "
            "low-confidence at the Enterprise band"
        ),
        market_position=(
            "Revenue Infrastructure Partner - explicitly NOT a marketing agency, "
            "sales agency, branding agency, automation agency, lead-generation "
            "agency, or consultant. A unified revenue operating system businesses "
            "plug into, not a vendor they hire."
        ),
        competitors=[],
        communication_style=(
            "Direct, revenue-mathematics-driven, anti-fluff. Every activity is "
            "filtered through: does this create revenue, how much, how fast, what "
            "probability, what operational load, what retention/upsell potential "
            "(ROCBO doctrine, AGENCY_REVENUE_TARGETS.md). Named anti-patterns: no "
            "meaningless meetings, no vanity tasks, no random content, no fake "
            "productivity, no outreach without qualification, no fulfillment "
            "without monetization logic."
        ),
        emotional_positioning=(
            "Infrastructure-grade trust and authority. \"Businesses do not hire "
            "the agency. They plug into a revenue operating system that behaves "
            "like an extension of their internal business brain\" (AGENCY_VISION.md "
            "Core Vision Statement). Operating intensity is explicitly \"do-or-die\", "
            "non-negotiable execution discipline, not aspirational branding."
        ),
        visual_preferences=[],
        typography_preferences=[],
        color_preferences=[],
        campaign_history=[],
        governance_rules={
            "tone": "direct, revenue-mathematics-driven, anti-fluff",
            "operating_discipline": "ROCBO - Revenue-Oriented Cognitive Business Operations",
            "anti_patterns": [
                "no meaningless meetings",
                "no vanity tasks",
                "no random content",
                "no fake productivity",
                "no outreach without qualification",
                "no fulfillment without monetization logic",
            ],
        },
        stakeholder_notes=[
            "Mary Thuo - sole owner, solo-orchestrates sales/execution personally "
            "with AI assistance; not a generic team-of-roles structure.",
            "Targets are treated as non-negotiable (\"do-or-die\" framing), the same "
            "way payroll/bills/KPIs would be for any operating business "
            "(AGENCY_REVENUE_TARGETS.md).",
        ],
        timelines=[],
        deliverables=[],
        active_projects=[],
        memory_embeddings=[],
        retrieval_indexes=[],
    )

    workspace = create_client_workspace(ENGINE_ROOT, client)

    memory = JsonMemoryStore(ENGINE_ROOT / "memory")
    memory.save_client(client)
    retriever = LocalHybridRetriever(ENGINE_ROOT / "knowledge" / "_indexes" / "paragraphs.jsonl")
    gate = RetrievalGate(retriever, memory)
    orchestrator = BrandCognitiveOrchestrator(gate, memory)
    context = orchestrator.assemble_context(
        client=client,
        task=(
            "Define Arika Agency's own core brand identity, positioning, and "
            "voice as BOIS's first real (non-hypothetical) client"
        ),
        deliverable="brand_identity_definition",
        positioning_objective="Revenue Infrastructure Partner, not a fragmented service vendor",
        communication_goal="direct, revenue-mathematics-driven, anti-fluff, infrastructure-grade trust",
        campaign_objective="establish the agency's own brand as the canonical real BOIS client object",
    )
    orchestrator.persist_context(context)

    payload = {
        "client_root": workspace["client_root"],
        "client_memory": workspace["client_memory"],
        "context_id": context.context_id,
        "activated_agents": context.activated_agents,
        "missing_sources": context.retrieval_bundle.missing_sources if context.retrieval_bundle else [],
        "retrieved_sources": sorted(context.retrieval_bundle.results_by_source.keys()) if context.retrieval_bundle else [],
        "flagged_gaps": {
            "competitors": "not yet confirmed by owner - no real competitor set named anywhere in this repo",
            "visual_preferences": "not yet confirmed by owner - no visual identity work exists yet",
            "typography_preferences": "not yet confirmed by owner",
            "color_preferences": "not yet confirmed by owner",
        },
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
