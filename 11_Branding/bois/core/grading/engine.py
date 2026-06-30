from __future__ import annotations

from typing import Dict, List

from ..models import ScoreDimension, ScoreResult


SCORE_DIMENSIONS: List[ScoreDimension] = [
    ScoreDimension("identity_strength", "Identity Strength", 0.08, 75, ["uniqueness", "recognizability", "clarity", "symbolic_strength"]),
    ScoreDimension("narrative_coherence", "Narrative Coherence", 0.08, 75, ["story_logic", "continuity", "semantic_alignment", "message_hierarchy"]),
    ScoreDimension("symbolic_consistency", "Symbolic Consistency", 0.07, 72, ["semiotic_fit", "category_codes", "archetypal_alignment", "meaning_transfer"]),
    ScoreDimension("visual_intelligence", "Visual Intelligence", 0.08, 75, ["symbolism", "emotional_effect", "platform_adaptability", "identity_retention"]),
    ScoreDimension("emotional_resonance", "Emotional Resonance", 0.07, 72, ["felt_relevance", "aspiration", "anxiety_resolution", "empathy"]),
    ScoreDimension("trust_signaling", "Trust Signaling", 0.08, 78, ["proof", "authority", "risk_reduction", "consistency"]),
    ScoreDimension("cultural_alignment", "Cultural Alignment", 0.07, 75, ["regional_adaptation", "language_nuance", "generational_fit", "symbolic_interpretation"]),
    ScoreDimension("psychographic_alignment", "Psychographic Alignment", 0.07, 75, ["values", "identity_aspiration", "motivation", "behavioral_fit"]),
    ScoreDimension("sales_synchronization", "Sales Synchronization", 0.06, 70, ["offer_clarity", "objection_handling", "conversion_logic", "sales_narrative"]),
    ScoreDimension("marketing_synchronization", "Marketing Synchronization", 0.06, 70, ["campaign_fit", "funnel_alignment", "media_strategy", "audience_adaptation"]),
    ScoreDimension("operational_embodiment", "Operational Embodiment", 0.06, 72, ["delivery_fit", "customer_experience", "internal_behavior", "service_reality"]),
    ScoreDimension("behavioral_branding", "Behavioral Branding", 0.05, 70, ["habit_design", "decision_influence", "interaction_pattern", "reinforcement_loop"]),
    ScoreDimension("audience_perception", "Audience Perception", 0.06, 72, ["memorability", "interpretation", "relevance", "belief_creation"]),
    ScoreDimension("authority_positioning", "Authority Positioning", 0.06, 75, ["expertise_signal", "category_leadership", "proof_system", "confidence"]),
    ScoreDimension("market_differentiation", "Market Differentiation", 0.07, 75, ["distinctness", "category_tension", "competitor_separation", "value_logic"]),
]


RECOMMENDATION_LIBRARY = {
    "identity_strength": "Clarify the brand DNA, category role, and recognizability system before expanding expression.",
    "narrative_coherence": "Tighten the message hierarchy and connect proof, tension, transformation, and continuity.",
    "symbolic_consistency": "Reconcile symbolic cues across sector expectations, cultural meaning, and visual expression.",
    "visual_intelligence": "Strengthen typography, color, spatial behavior, and platform adaptation around a single visual logic.",
    "emotional_resonance": "Map audience fears, aspirations, emotional triggers, and desired identity more explicitly.",
    "trust_signaling": "Add proof, authority cues, risk reducers, process transparency, and continuity markers.",
    "cultural_alignment": "Run a regional language, symbol, tone, and generational fit pass before deployment.",
    "psychographic_alignment": "Rebuild the work around values, status logic, motivations, and identity aspirations.",
    "sales_synchronization": "Translate the brand into offer language, objection handling, proof, and conversion narrative.",
    "marketing_synchronization": "Align campaign rhythm, funnel stages, audience adaptation, and media behavior.",
    "operational_embodiment": "Check whether the brand promise is actually supported by service delivery and customer experience.",
    "behavioral_branding": "Design repeated interaction cues that reinforce the desired market belief over time.",
    "audience_perception": "Test whether the intended belief is what the audience is likely to perceive and remember.",
    "authority_positioning": "Increase evidence, expertise signals, category claims, and confidence architecture.",
    "market_differentiation": "Sharpen the contrast against competitors and define the category tension more clearly.",
}


class BrandScoringEngine:
    def score(self, profile_id: str, dimension_scores: Dict[str, float]) -> ScoreResult:
        normalized: Dict[str, float] = {}
        failed: List[str] = []
        recommendations: List[str] = []
        weighted_total = 0.0

        for dimension in SCORE_DIMENSIONS:
            value = max(0.0, min(100.0, float(dimension_scores.get(dimension.id, 0.0))))
            normalized[dimension.id] = value
            weighted_total += value * dimension.weight
            if value < dimension.threshold:
                failed.append(dimension.id)
                recommendations.append(RECOMMENDATION_LIBRARY[dimension.id])

        return ScoreResult(
            profile_id=profile_id,
            total_score=round(weighted_total, 2),
            dimension_scores=normalized,
            failed_dimensions=failed,
            recommendations=recommendations,
        )

    def audit_from_evidence(self, profile_id: str, evidence: Dict[str, object]) -> ScoreResult:
        scores = {}
        for dimension in SCORE_DIMENSIONS:
            metric_hits = 0
            text = str(evidence).lower()
            for metric in dimension.metrics:
                if metric.replace("_", " ") in text or metric in text:
                    metric_hits += 1
            scores[dimension.id] = 55 + (metric_hits / max(1, len(dimension.metrics))) * 40
        return self.score(profile_id, scores)

