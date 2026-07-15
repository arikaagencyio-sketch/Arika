from __future__ import annotations

from typing import Dict, Iterable, List

from ..models import DynamicBrandContext, GovernanceFinding


# Governance-mandatory fields. Every one of these MUST be present in agent output
# before client delivery. This list is validated by `validate_output` below.
MANDATORY_OUTPUT_FIELDS = [
    "strategic_reasoning",
    "emotional_reasoning",
    "symbolic_reasoning",
    "visual_reasoning",
    "psychological_reasoning",
    "cultural_reasoning",
    "positioning_rationale",
    "operational_implications",
]

# Fields that are not governance-mandatory but have real downstream consumers:
# `validation_risks` -> AgentResult.validation_notes, `memory_updates` -> JsonMemoryStore.
SUPPLEMENTARY_OUTPUT_FIELDS = [
    "validation_risks",
    "memory_updates",
]

# The single canonical contract every producer must satisfy. Import this rather than
# re-listing fields: three separate lists previously diverged (agent_prompt asked for 7,
# build_agent_tasks expected 7, governance required 8), which meant emotional_reasoning,
# visual_reasoning, and positioning_rationale were never requested and would have failed
# governance on every run once synthesis was wired.
AGENT_OUTPUT_CONTRACT = MANDATORY_OUTPUT_FIELDS + SUPPLEMENTARY_OUTPUT_FIELDS


class BrandGovernancePolicy:
    def validate_context(self, context: DynamicBrandContext) -> List[GovernanceFinding]:
        findings: List[GovernanceFinding] = []
        bundle = context.retrieval_bundle
        if not bundle or not bundle.is_complete:
            findings.append(
                GovernanceFinding(
                    rule_id="retrieval.required_sources",
                    severity="critical",
                    passed=False,
                    detail=f"Missing retrieval sources: {bundle.missing_sources if bundle else 'all'}",
                    recommendation="Retrieve sector, audience, culture, client memory, prior output, and governance evidence before synthesis.",
                )
            )
        else:
            findings.append(
                GovernanceFinding(
                    rule_id="retrieval.required_sources",
                    severity="info",
                    passed=True,
                    detail="All required retrieval sources are present.",
                )
            )

        if not context.activated_agents:
            findings.append(
                GovernanceFinding(
                    rule_id="orchestration.agent_activation",
                    severity="critical",
                    passed=False,
                    detail="No specialist agents were activated.",
                    recommendation="Run trigger routing from sector, deliverable, geography, and audience.",
                )
            )

        return findings

    def validate_output(self, output: Dict[str, object]) -> List[GovernanceFinding]:
        findings: List[GovernanceFinding] = []
        text = str(output).lower()
        for field in MANDATORY_OUTPUT_FIELDS:
            present = field in output or field.replace("_", " ") in text
            findings.append(
                GovernanceFinding(
                    rule_id=f"output.required_field.{field}",
                    severity="high" if not present else "info",
                    passed=present,
                    detail=f"{field} {'present' if present else 'missing'}",
                    recommendation=None if present else f"Add {field.replace('_', ' ')} before client delivery.",
                )
            )
        findings.extend(self._continuity_checks(text))
        return findings

    def _continuity_checks(self, text: str) -> List[GovernanceFinding]:
        checks = {
            "continuity.narrative": ["narrative", "message", "story", "semantic"],
            "continuity.visual": ["visual", "typography", "color", "symbol"],
            "continuity.culture": ["culture", "regional", "language", "geography"],
            "continuity.sales_marketing": ["sales", "marketing", "campaign", "conversion"],
            "continuity.operations": ["operation", "delivery", "experience", "behavior"],
        }
        findings: List[GovernanceFinding] = []
        for rule_id, terms in checks.items():
            passed = any(term in text for term in terms)
            findings.append(
                GovernanceFinding(
                    rule_id=rule_id,
                    severity="medium" if not passed else "info",
                    passed=passed,
                    detail=f"{rule_id} {'covered' if passed else 'not evidenced'}",
                    recommendation=None if passed else f"Add explicit {rule_id.split('.')[-1]} continuity logic.",
                )
            )
        return findings

    @staticmethod
    def passed(findings: Iterable[GovernanceFinding], max_allowed_severity: str = "medium") -> bool:
        severity_rank = {"info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}
        limit = severity_rank[max_allowed_severity]
        return all(f.passed or severity_rank.get(f.severity, 4) <= limit for f in findings)

