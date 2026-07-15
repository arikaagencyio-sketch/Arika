"""JSON-in / JSON-out entry point for BOIS — called by arika-runtime's bois wrapper.

Usage:
    python run_brand_task.py '<json>'
    echo '<json>' | python run_brand_task.py

Input:
    {
      "mode": "define" | "audit" | "govern",   # default "define"
      "client_id": "arika-agency",              # must already have a workspace
      "task": "…",                              # free-text brand task
      "deliverable": "brand_identity_definition",
      "positioning_objective": "", "communication_goal": "", "campaign_objective": "",
      "synthesize": true                        # false => route+retrieve+govern only, no LLM
    }

Output: a JSON object matching arika-runtime's base advisory envelope, plus BOIS-specific
fields. Always prints exactly one JSON object to stdout, even on failure — the wrapper
depends on that.

Design note: `synthesize: false` is a first-class mode, not a degraded one. Routing,
retrieval, governance and scoring are the parts of BOIS that were always real; they run
with no API key. Only `output_synthesis` needs Claude.
"""

from __future__ import annotations

import json
import sys
import traceback
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict, List


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from bois.core.client_workspace import slugify  # noqa: E402
from bois.core.governance.policy import BrandGovernancePolicy  # noqa: E402
from bois.core.grading.engine import BrandScoringEngine  # noqa: E402
from bois.core.memory.store import JsonMemoryStore  # noqa: E402
from bois.core.models import ClientObject  # noqa: E402
from bois.core.orchestration.engine import BrandCognitiveOrchestrator  # noqa: E402
from bois.core.retrieval.gated_retriever import LocalHybridRetriever, RetrievalGate  # noqa: E402


BOIS_ROOT = WORKSPACE_ROOT / "bois"


def _load_client(client_id: str) -> ClientObject:
    path = BOIS_ROOT / "clients" / slugify(client_id) / "memory" / "client.json"
    if not path.exists():
        raise FileNotFoundError(
            f"No BOIS client workspace for '{client_id}' at {path}. "
            "Build one first (see bois/executions/run_arika_agency_brand.py). "
            "BOIS does not invent client objects."
        )
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    known = {f for f in ClientObject.__dataclass_fields__}  # type: ignore[attr-defined]
    return ClientObject(**{k: v for k, v in data.items() if k in known})


def _envelope(
    summary: str,
    risk: str = "low",
    approval: bool = False,
    reasons: List[str] | None = None,
    actions: List[str] | None = None,
    **extra: Any,
) -> Dict[str, Any]:
    payload = {
        "summary": summary,
        "recommendedActions": actions or [],
        "requiresHumanApproval": approval,
        "approvalReasons": reasons or [],
        "riskLevel": risk,
    }
    payload.update(extra)
    return payload


def run(request: Dict[str, Any]) -> Dict[str, Any]:
    mode = request.get("mode", "define")
    client_id = request.get("client_id", "arika-agency")
    task = request.get("task") or "Define brand identity, positioning, and voice."
    deliverable = request.get("deliverable", "brand_identity_definition")
    should_synthesize = bool(request.get("synthesize", True))

    client = _load_client(client_id)

    # Paths match bois/executions/run_arika_agency_brand.py exactly: the retriever takes
    # the paragraphs JSONL file (not its directory), and memory roots at bois/memory.
    memory_store = JsonMemoryStore(BOIS_ROOT / "memory")
    retriever = LocalHybridRetriever(BOIS_ROOT / "knowledge" / "_indexes" / "paragraphs.jsonl")
    gate = RetrievalGate(retriever, memory_store)
    orchestrator = BrandCognitiveOrchestrator(retrieval_gate=gate, memory_store=memory_store)

    # assemble_context enforces the retrieval gate: incomplete evidence raises rather
    # than degrading into generic output.
    context = orchestrator.assemble_context(
        client=client,
        task=task,
        deliverable=deliverable,
        positioning_objective=request.get("positioning_objective", ""),
        communication_goal=request.get("communication_goal", ""),
        campaign_objective=request.get("campaign_objective", ""),
    )
    orchestrator.persist_context(context)

    policy = BrandGovernancePolicy()
    context_findings = policy.validate_context(context)

    result: Dict[str, Any] = {
        "context_id": context.context_id,
        "client_id": context.client_id,
        "mode": mode,
        "activated_agents": context.activated_agents,
        "retrieval_complete": bool(context.retrieval_bundle and context.retrieval_bundle.is_complete),
        "missing_sources": context.retrieval_bundle.missing_sources if context.retrieval_bundle else ["(no bundle)"],
        "context_findings": [asdict(f) for f in context_findings],
        "synthesized": False,
        "agent_results": [],
        "output_findings": [],
        "evidence_gaps": [],
    }

    if mode == "audit":
        engine = BrandScoringEngine()
        result["scoring_dimensions"] = [d.id for d in engine.dimensions]

    if not should_synthesize:
        return _envelope(
            summary=(
                f"BOIS routed {len(context.activated_agents)} agents for '{client.company_name}' "
                f"with a complete retrieval bundle. Synthesis skipped (synthesize=false): "
                f"no brand reasoning was produced."
            ),
            actions=["Set synthesize=true and provide ANTHROPIC_API_KEY to produce brand reasoning."],
            **result,
        )

    from bois.core.synthesis.engine import BrandAgentRuntime, SynthesisError

    try:
        agent_results = orchestrator.synthesize(context)
    except SynthesisError as exc:
        return _envelope(
            summary=f"BOIS could not synthesize: {exc}",
            risk="medium",
            approval=True,
            reasons=[str(exc)],
            actions=[
                "Install BOIS deps (pip install -r 12_Branding/bois/requirements.txt) and set ANTHROPIC_API_KEY.",
                "Routing, retrieval, governance and scoring already ran and are reported above.",
            ],
            **result,
        )

    result["synthesized"] = True
    result["agent_results"] = [asdict(r) for r in agent_results]

    merged: Dict[str, Any] = {}
    gaps: List[str] = []
    for r in agent_results:
        for key, value in r.outputs.items():
            merged.setdefault(key, []).append({"agent": r.agent_id, "value": value})
        gaps.extend(n for n in r.validation_notes if n.startswith("evidence gap:"))

    output_findings = policy.validate_output({k: str(v) for k, v in merged.items()})
    result["output_findings"] = [asdict(f) for f in output_findings]
    result["evidence_gaps"] = gaps

    governance_passed = BrandGovernancePolicy.passed(output_findings)
    confidences = [r.confidence for r in agent_results] or [0.0]
    mean_conf = sum(confidences) / len(confidences)

    # Escalate on weak evidence or failed governance rather than shipping brand work.
    approval = (not governance_passed) or bool(gaps) or mean_conf < 0.85
    reasons: List[str] = []
    if not governance_passed:
        reasons.append("BOIS governance validation did not pass on the synthesized output.")
    if gaps:
        reasons.append(f"{len(gaps)} evidence gap(s) reported by agents — claims the retrieval bundle does not support.")
    if mean_conf < 0.85:
        reasons.append(f"Mean agent confidence {mean_conf:.2f} is below 0.85.")

    return _envelope(
        summary=(
            f"BOIS synthesized brand reasoning for '{client.company_name}' across "
            f"{len(agent_results)} agents (mean confidence {mean_conf:.2f}). "
            f"Governance {'passed' if governance_passed else 'FAILED'}; {len(gaps)} evidence gap(s)."
        ),
        risk="medium" if approval else "low",
        approval=approval,
        reasons=reasons,
        actions=[
            "Human review required before any brand output reaches a client." if approval
            else "Review synthesized reasoning and persist accepted decisions to BRANDING_OS.md.",
        ],
        governance_passed=governance_passed,
        mean_confidence=round(mean_conf, 4),
        **result,
    )


def main() -> int:
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    try:
        request = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError as exc:
        print(json.dumps(_envelope(f"Invalid JSON input: {exc}", risk="high", approval=True)))
        return 1

    try:
        print(json.dumps(run(request), indent=2, default=str))
        return 0
    except Exception as exc:  # noqa: BLE001 - must always emit one JSON object
        print(
            json.dumps(
                _envelope(
                    summary=f"BOIS run failed: {exc}",
                    risk="high",
                    approval=True,
                    reasons=[str(exc)],
                    traceback=traceback.format_exc(limit=4),
                ),
                indent=2,
            )
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
