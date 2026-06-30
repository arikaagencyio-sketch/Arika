from __future__ import annotations

from typing import Dict, List

from ..models import ClientObject, DynamicBrandContext


PRESENTATION_SECTIONS = [
    "market_analysis",
    "sector_analysis",
    "audience_psychology",
    "positioning_rationale",
    "emotional_territory",
    "symbolic_reasoning",
    "typography_reasoning",
    "color_reasoning",
    "narrative_systems",
    "campaign_logic",
    "governance_logic",
    "implementation_roadmap",
]


class PresentationIntelligenceEngine:
    def outline(self, client: ClientObject, context: DynamicBrandContext) -> Dict[str, object]:
        return {
            "client_id": client.client_id,
            "company_name": client.company_name,
            "deck_type": context.deliverable,
            "required_sections": PRESENTATION_SECTIONS,
            "narrative_arc": [
                "category reality",
                "audience cognition",
                "strategic tension",
                "brand logic",
                "identity system",
                "execution roadmap",
                "governance and continuity",
            ],
            "quality_standard": [
                "engineered",
                "psychologically informed",
                "culturally aligned",
                "strategically rigorous",
                "market-specific",
            ],
        }

    def slide_requirements(self) -> List[Dict[str, str]]:
        return [
            {"section": section, "must_explain": self._requirement_for(section)}
            for section in PRESENTATION_SECTIONS
        ]

    @staticmethod
    def _requirement_for(section: str) -> str:
        requirements = {
            "market_analysis": "Show the market condition, category tension, and competitive frame.",
            "sector_analysis": "Explain trust mechanics, authority patterns, risk, maturity, and economic behavior.",
            "audience_psychology": "Map motivations, fears, aspirations, status logic, and decision behavior.",
            "positioning_rationale": "Connect market gap, audience need, competitor contrast, and claim logic.",
            "emotional_territory": "Define the emotional state the brand should create and own.",
            "symbolic_reasoning": "Explain symbols, category codes, cultural readings, and semiotic risks.",
            "typography_reasoning": "Tie type choices to authority, tone, accessibility, and memorability.",
            "color_reasoning": "Tie color to emotion, category expectation, cultural meaning, and recognition.",
            "narrative_systems": "Show message hierarchy, story logic, proof, tension, and transformation.",
            "campaign_logic": "Show rhythm, channel behavior, conversion path, and reinforcement loops.",
            "governance_logic": "Define what must stay stable, what can adapt, and approval checks.",
            "implementation_roadmap": "Translate strategy into phases, owners, assets, and validation moments.",
        }
        return requirements[section]

