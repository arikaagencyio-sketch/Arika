"""Output synthesis — the reasoning step of the BOIS pipeline.

This module closes `EXECUTION_STAGES`' `output_synthesis` stage, which sits between
`agent_activation` and `governance_validation` and previously had no implementation:
`agent_prompt()` built a prompt nothing consumed, and `AgentResult` was a dataclass
nothing produced. BOIS could route, retrieve, score, validate, and remember — but it
could not think.

Design mirrors `09_Finance/finos-plugin/src/ai-agents/runtime.ts`'s `ClaudeAgentRuntime`
deliberately, so the repo has one reasoning shape across both grandfathered code layers:

- lazy client construction (build without a key; raise only on invoke)
- structured JSON output enforced against a schema
- the agent's own registry entry supplies the system prompt
- retrieved evidence is passed as the user message, never invented

Governance rule this module must not violate (`bois/documentation/`):
    missing retrieval evidence -> stop in a retrieval failure state,
    never generate generic branding output.

Accordingly this module never fabricates evidence, and refuses to synthesize against an
incomplete retrieval bundle.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional

from ..governance.policy import AGENT_OUTPUT_CONTRACT
from ..models import AgentResult, AgentTask, DynamicBrandContext, RetrievalBundle
from ..orchestration.registry import agent_prompt


DEFAULT_MODEL = "claude-opus-4-8"
DEFAULT_MAX_TOKENS = 2048
MAX_EVIDENCE_PER_SOURCE = 6


class SynthesisError(RuntimeError):
    """Raised when synthesis cannot be performed safely."""


def _output_schema() -> Dict[str, Any]:
    """JSON schema for a single agent's output.

    Every field in AGENT_OUTPUT_CONTRACT is required — that is the whole point of the
    contract. `confidence` and `evidence_gaps` are runtime metadata, not brand reasoning.
    """
    properties: Dict[str, Any] = {}
    for field in AGENT_OUTPUT_CONTRACT:
        if field == "memory_updates":
            properties[field] = {
                "type": "array",
                "items": {"type": "string"},
                "description": "Durable facts worth persisting to brand memory.",
            }
        elif field == "validation_risks":
            properties[field] = {
                "type": "array",
                "items": {"type": "string"},
                "description": "Governance risks, contradictions, or unsupported claims. Do not smooth these over.",
            }
        else:
            properties[field] = {
                "type": "string",
                "description": f"{field.replace('_', ' ').capitalize()}, grounded in retrieved evidence.",
            }

    properties["confidence"] = {
        "type": "number",
        "minimum": 0,
        "maximum": 1,
        "description": "Confidence in this output given the evidence actually retrieved.",
    }
    properties["evidence_gaps"] = {
        "type": "array",
        "items": {"type": "string"},
        "description": "Claims the retrieved evidence does not support. State them; never fill them in.",
    }

    return {
        "type": "object",
        "additionalProperties": False,
        "required": list(AGENT_OUTPUT_CONTRACT) + ["confidence", "evidence_gaps"],
        "properties": properties,
    }


def _evidence_text(result: Any) -> str:
    """Extract readable evidence from a RetrievalResult.

    RetrievalGate emits two shapes (see `core/retrieval/gated_retriever.py`):
      - retrieval_mode="local_hybrid" -> {"excerpt", "tags", "section_hint", ...}
      - retrieval_mode="memory"       -> {"source", "event"}
    """
    evidence = result.evidence or {}
    excerpt = str(evidence.get("excerpt", "")).strip()
    if excerpt:
        return excerpt
    event = evidence.get("event")
    if event:
        return json.dumps(event, default=str)[:600]
    return ""


def _format_evidence(bundle: Optional[RetrievalBundle]) -> str:
    if bundle is None:
        return "NO RETRIEVAL BUNDLE PROVIDED."
    lines: List[str] = []
    for source, results in bundle.results_by_source.items():
        lines.append(f"\n## Source: {source}")
        if not results:
            lines.append("(no evidence retrieved for this source)")
            continue
        for result in results[:MAX_EVIDENCE_PER_SOURCE]:
            text = _evidence_text(result)
            if not text:
                continue
            lines.append(f"- [{result.paragraph_id} | {result.retrieval_mode} | score {result.score:.3f}] {text}")
    return "\n".join(lines) if lines else "(retrieval bundle contained no evidence)"


def _build_user_message(task: AgentTask, context: DynamicBrandContext) -> str:
    return "\n".join(
        [
            f"# Brand task\n{context.task}",
            f"\n# Your objective as {task.agent_id}\n{task.objective}",
            f"\n# Client context",
            f"- client_id: {context.client_id}",
            f"- sector: {context.sector or '(unknown)'}",
            f"- geography: {context.geography or '(unknown)'}",
            f"- audience: {context.audience or '(unknown)'}",
            f"- deliverable: {context.deliverable or '(unknown)'}",
            f"- positioning_objective: {context.positioning_objective or '(none stated)'}",
            f"- communication_goal: {context.communication_goal or '(none stated)'}",
            f"- campaign_objective: {context.campaign_objective or '(none stated)'}",
            "\n# Constraints (binding)",
            *[f"- {c}" for c in task.constraints],
            "\n# Retrieved evidence — reason ONLY from this",
            _format_evidence(context.retrieval_bundle),
            (
                "\n# Rules\n"
                "- Ground every claim in the evidence above and cite the paragraph id where you rely on it.\n"
                "- If the evidence does not support something, put it in evidence_gaps and lower your confidence.\n"
                "- Do NOT invent client facts, competitors, metrics, or brand history.\n"
                "- Return every required field. An honest 'the evidence does not establish this' is a valid value."
            ),
        ]
    )


class BrandAgentRuntime:
    """Runs a BOIS AgentTask through Claude and returns a real AgentResult.

    Lazily constructs the Anthropic client so the whole pipeline (routing, retrieval,
    governance, scoring) remains importable and testable without an API key — the same
    property finos's runtime has, and the reason bois' test/smoke paths keep working
    with no credentials present.
    """

    def __init__(self, model: str = DEFAULT_MODEL, max_tokens: int = DEFAULT_MAX_TOKENS):
        self.model = model
        self.max_tokens = max_tokens
        self._client: Any = None

    def _get_client(self) -> Any:
        if self._client is not None:
            return self._client
        try:
            from anthropic import Anthropic  # imported lazily; see class docstring
        except ImportError as exc:  # pragma: no cover - depends on environment
            raise SynthesisError(
                "The 'anthropic' package is not installed. Install BOIS' dependencies: "
                "pip install -r 12_Branding/bois/requirements.txt"
            ) from exc

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise SynthesisError(
                "ANTHROPIC_API_KEY is not set — cannot invoke BOIS agents. "
                "Routing, retrieval, governance, and scoring all run without it; only "
                "output synthesis requires a key."
            )
        self._client = Anthropic(api_key=api_key)
        return self._client

    def run(self, task: AgentTask, context: DynamicBrandContext) -> AgentResult:
        """Synthesize one agent's output. Never proceeds on incomplete evidence."""
        bundle = context.retrieval_bundle
        if bundle is None or not bundle.is_complete:
            missing = bundle.missing_sources if bundle else ["(no bundle)"]
            # The architecture's non-negotiable rule: stop, do not generate generic output.
            raise SynthesisError(
                f"Retrieval incomplete for {task.agent_id}; missing sources: {missing}. "
                "BOIS must stop in a retrieval failure state rather than generate generic branding output."
            )

        client = self._get_client()
        response = client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=agent_prompt(task.agent_id),
            messages=[{"role": "user", "content": _build_user_message(task, context)}],
        )

        payload = self._parse(response, task)
        confidence = float(payload.pop("confidence", 0.0))
        evidence_gaps = payload.pop("evidence_gaps", []) or []

        validation_notes: List[str] = []
        risks = payload.get("validation_risks") or []
        if isinstance(risks, list):
            validation_notes.extend(str(r) for r in risks)
        validation_notes.extend(f"evidence gap: {g}" for g in evidence_gaps)

        return AgentResult(
            task_id=task.task_id,
            agent_id=task.agent_id,
            stage="output_synthesis",
            status="complete" if not evidence_gaps else "complete_with_gaps",
            confidence=confidence,
            outputs=payload,
            validation_notes=validation_notes,
        )

    def _parse(self, response: Any, task: AgentTask) -> Dict[str, Any]:
        text = ""
        for block in getattr(response, "content", []):
            if getattr(block, "type", None) == "text":
                text = block.text
                break
        if not text:
            raise SynthesisError(f"{task.agent_id} returned no text block.")

        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            start, end = text.find("{"), text.rfind("}")
            if start == -1 or end <= start:
                raise SynthesisError(f"{task.agent_id} returned unparseable output: {text[:200]}")
            parsed = json.loads(text[start : end + 1])

        missing = [f for f in AGENT_OUTPUT_CONTRACT if f not in parsed]
        if missing:
            raise SynthesisError(
                f"{task.agent_id} output is missing contract fields: {missing}. "
                "These are validated by BrandGovernancePolicy and cannot be omitted."
            )
        return parsed

    def run_all(self, tasks: List[AgentTask], context: DynamicBrandContext) -> List[AgentResult]:
        """Run every activated agent's task in the orchestrator's routed order."""
        return [self.run(task, context) for task in tasks]

    @staticmethod
    def output_schema() -> Dict[str, Any]:
        """Exposed so the schema can be asserted in tests without an API key."""
        return _output_schema()
