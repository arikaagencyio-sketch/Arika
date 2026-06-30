from __future__ import annotations

from typing import Dict, List


AGENT_REGISTRY: Dict[str, Dict[str, object]] = {
    "master_orchestrator": {
        "purpose": "Classify work, assemble retrieval context, activate specialists, synchronize outputs, validate continuity, and update memory.",
        "responsibilities": [
            "Task classification",
            "Retrieval gate enforcement",
            "Agent activation",
            "Cross-agent synthesis",
            "Governance handoff",
            "Memory persistence",
        ],
        "memory_access": ["client", "campaign", "visual", "narrative", "governance", "market", "trend", "stakeholder"],
        "validation": ["retrieval_complete", "agent_outputs_present", "governance_passed"],
    },
    "sector_intelligence_agent": {
        "purpose": "Map industry structure, category behavior, trust mechanics, maturity, authority codes, and economic dynamics.",
        "memory_access": ["market", "client"],
        "retrieval_sources": ["sector_intelligence", "governance_rules"],
    },
    "audience_cognition_agent": {
        "purpose": "Interpret audience psychology, identity aspirations, anxieties, motivation, buying logic, and behavioral patterns.",
        "memory_access": ["client", "stakeholder", "market"],
        "retrieval_sources": ["audience_psychology", "client_memory"],
    },
    "cultural_intelligence_agent": {
        "purpose": "Analyze geography, language nuance, regional behavior, generational codes, symbolic sensitivities, and cultural adaptation.",
        "memory_access": ["market", "trend", "stakeholder"],
        "retrieval_sources": ["cultural_context", "symbolic_systems"],
    },
    "brand_identity_agent": {
        "purpose": "Build brand DNA, archetypes, personality systems, emotional positioning, embodiment rules, and identity continuity.",
        "memory_access": ["client", "visual", "narrative", "governance"],
        "retrieval_sources": ["client_memory", "sector_intelligence", "audience_psychology"],
    },
    "narrative_engineering_agent": {
        "purpose": "Create messaging systems, story frameworks, persuasion logic, semantic hierarchies, and narrative continuity.",
        "memory_access": ["narrative", "campaign", "client"],
        "retrieval_sources": ["narrative_systems", "audience_psychology", "previous_outputs"],
    },
    "visual_cognition_agent": {
        "purpose": "Translate strategic cognition into symbolic systems, moodboards, typography logic, color psychology, and art direction.",
        "memory_access": ["visual", "client", "governance"],
        "retrieval_sources": ["symbolic_systems", "cultural_context", "previous_outputs"],
    },
    "brand_governance_agent": {
        "purpose": "Audit continuity, consistency, emotional alignment, symbolic coherence, cultural alignment, and operational embodiment.",
        "memory_access": ["governance", "client", "visual", "narrative", "campaign"],
        "retrieval_sources": ["governance_rules", "client_memory", "previous_outputs"],
    },
    "brand_evolution_agent": {
        "purpose": "Track market, cultural, semantic, platform, generational, and trend shifts that require brand adaptation.",
        "memory_access": ["trend", "market", "client"],
        "retrieval_sources": ["cultural_context", "sector_intelligence"],
    },
    "sales_alignment_agent": {
        "purpose": "Synchronize offers, conversion psychology, objections, trust signaling, sales narrative, and offer positioning.",
        "memory_access": ["client", "campaign", "market"],
        "retrieval_sources": ["sector_intelligence", "audience_psychology", "client_memory"],
    },
    "marketing_synchronization_agent": {
        "purpose": "Align campaigns, funnels, media strategy, content systems, audience adaptation, and marketing rhythm.",
        "memory_access": ["campaign", "client", "narrative"],
        "retrieval_sources": ["audience_psychology", "distribution_intelligence", "previous_outputs"],
    },
    "distribution_intelligence_agent": {
        "purpose": "Analyze platform behavior, channel psychology, algorithmic communication, format behavior, and distribution adaptation.",
        "memory_access": ["campaign", "market", "trend"],
        "retrieval_sources": ["distribution_intelligence", "cultural_context"],
    },
    "brand_production_agent": {
        "purpose": "Turn strategy into scripts, storyboards, presentations, launch systems, production logic, and execution assets.",
        "memory_access": ["campaign", "visual", "narrative"],
        "retrieval_sources": ["previous_outputs", "narrative_systems", "symbolic_systems"],
    },
    "psychographic_intelligence_agent": {
        "purpose": "Model values, aspirations, emotional triggers, identity signals, status logic, and motivation patterns.",
        "memory_access": ["client", "stakeholder", "market"],
        "retrieval_sources": ["audience_psychology", "client_memory"],
    },
    "symbolic_systems_agent": {
        "purpose": "Engineer symbolic codes, semiotic systems, archetypal signals, category cues, and meaning transfer.",
        "memory_access": ["visual", "narrative", "governance"],
        "retrieval_sources": ["symbolic_systems", "cultural_context", "sector_intelligence"],
    },
    "semantic_intelligence_agent": {
        "purpose": "Control meaning, vocabulary, category language, semantic drift, message precision, and linguistic continuity.",
        "memory_access": ["narrative", "governance", "client"],
        "retrieval_sources": ["narrative_systems", "previous_outputs", "governance_rules"],
    },
    "trend_intelligence_agent": {
        "purpose": "Assess trend relevance, platform change, cultural movement, visual evolution, and timing risk.",
        "memory_access": ["trend", "market"],
        "retrieval_sources": ["cultural_context", "sector_intelligence"],
    },
    "brand_calendar_agent": {
        "purpose": "Build cadence, launch rhythm, seasonal systems, campaign timing, content pacing, and memory reinforcement loops.",
        "memory_access": ["campaign", "client", "trend"],
        "retrieval_sources": ["previous_outputs", "distribution_intelligence", "client_memory"],
    },
    "trust_authority_agent": {
        "purpose": "Engineer credibility signals, proof systems, authority positioning, risk reduction, and trust reinforcement.",
        "memory_access": ["client", "market", "governance"],
        "retrieval_sources": ["sector_intelligence", "audience_psychology", "governance_rules"],
    },
    "presentation_intelligence_agent": {
        "purpose": "Generate stakeholder-ready narrative decks with market logic, strategic rationale, visual reasoning, and roadmap clarity.",
        "memory_access": ["client", "campaign", "visual", "narrative", "governance"],
        "retrieval_sources": ["sector_intelligence", "audience_psychology", "cultural_context", "previous_outputs"],
    },
}


BASE_AGENT_SEQUENCE = [
    "sector_intelligence_agent",
    "audience_cognition_agent",
    "cultural_intelligence_agent",
    "brand_identity_agent",
    "narrative_engineering_agent",
    "visual_cognition_agent",
    "brand_governance_agent",
]


TRIGGER_RULES: Dict[str, Dict[str, List[str]]] = {
    "sector": {
        "fintech": ["trust_authority_agent", "brand_governance_agent"],
        "healthcare": ["trust_authority_agent", "cultural_intelligence_agent", "brand_governance_agent"],
        "luxury": ["symbolic_systems_agent", "visual_cognition_agent", "psychographic_intelligence_agent"],
        "laundry": ["sector_intelligence_agent", "audience_cognition_agent", "distribution_intelligence_agent"],
        "b2b": ["trust_authority_agent", "sales_alignment_agent", "presentation_intelligence_agent"],
    },
    "deliverable": {
        "visual_identity": ["visual_cognition_agent", "symbolic_systems_agent", "brand_governance_agent"],
        "campaign": ["marketing_synchronization_agent", "narrative_engineering_agent", "brand_production_agent"],
        "launch_campaign": ["marketing_synchronization_agent", "distribution_intelligence_agent", "brand_calendar_agent"],
        "presentation": ["presentation_intelligence_agent", "trust_authority_agent", "brand_governance_agent"],
        "sales_system": ["sales_alignment_agent", "trust_authority_agent", "semantic_intelligence_agent"],
    },
    "geography": {
        "nairobi": ["cultural_intelligence_agent", "semantic_intelligence_agent"],
        "kenya": ["cultural_intelligence_agent", "distribution_intelligence_agent"],
        "multi_market": ["cultural_intelligence_agent", "brand_evolution_agent", "trend_intelligence_agent"],
    },
    "audience": {
        "professionals": ["psychographic_intelligence_agent", "trust_authority_agent"],
        "enterprise": ["trust_authority_agent", "presentation_intelligence_agent", "brand_governance_agent"],
        "founders": ["audience_cognition_agent", "sales_alignment_agent", "narrative_engineering_agent"],
    },
}


def agent_prompt(agent_id: str) -> str:
    agent = AGENT_REGISTRY[agent_id]
    return (
        f"You are {agent_id}. Purpose: {agent['purpose']} "
        "Use retrieved evidence before producing any recommendation. "
        "Return strategic reasoning, psychological reasoning, cultural reasoning, symbolic reasoning, "
        "operational implications, validation risks, and memory updates."
    )

