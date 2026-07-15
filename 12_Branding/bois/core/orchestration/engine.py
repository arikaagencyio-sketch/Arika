from __future__ import annotations

import hashlib
from datetime import datetime
from typing import Dict, Iterable, List

from ..governance.policy import AGENT_OUTPUT_CONTRACT
from ..memory.store import JsonMemoryStore
from ..models import AgentResult, AgentTask, ClientObject, DynamicBrandContext
from ..retrieval.gated_retriever import REQUIRED_RETRIEVAL_SOURCES, RetrievalGate
from .registry import AGENT_REGISTRY, BASE_AGENT_SEQUENCE, TRIGGER_RULES


EXECUTION_STAGES = [
    "client_ingestion",
    "context_assembly",
    "agent_activation",
    "output_synthesis",
    "governance_validation",
    "memory_update",
    "evolution_monitoring",
]


class BrandCognitiveOrchestrator:
    """Stateful orchestrator for retrieval-first brand execution."""

    def __init__(self, retrieval_gate: RetrievalGate, memory_store: JsonMemoryStore):
        self.retrieval_gate = retrieval_gate
        self.memory_store = memory_store

    def assemble_context(
        self,
        client: ClientObject,
        task: str,
        deliverable: str,
        positioning_objective: str = "",
        communication_goal: str = "",
        campaign_objective: str = "",
    ) -> DynamicBrandContext:
        query = " ".join(
            [
                task,
                deliverable,
                positioning_objective,
                communication_goal,
                campaign_objective,
                client.sector,
                client.geography,
                client.audience,
            ]
        )
        bundle = self.retrieval_gate.assemble(query=query, client=client, required_sources=REQUIRED_RETRIEVAL_SOURCES)
        self.retrieval_gate.assert_complete(bundle)
        activated = self.route_agents(client=client, deliverable=deliverable)
        context_id = hashlib.sha1(f"{client.client_id}:{task}:{datetime.utcnow().isoformat()}".encode("utf-8")).hexdigest()[:16]
        return DynamicBrandContext(
            context_id=context_id,
            client_id=client.client_id,
            task=task,
            sector=client.sector,
            geography=client.geography,
            audience=client.audience,
            deliverable=deliverable,
            positioning_objective=positioning_objective,
            communication_goal=communication_goal,
            campaign_objective=campaign_objective,
            activated_agents=activated,
            retrieval_bundle=bundle,
        )

    def route_agents(self, client: ClientObject, deliverable: str) -> List[str]:
        activated = list(BASE_AGENT_SEQUENCE)
        activated.extend(self._matches("sector", [client.sector, client.sub_sector, client.market_position]))
        activated.extend(self._matches("deliverable", [deliverable]))
        activated.extend(self._matches("geography", [client.geography]))
        activated.extend(self._matches("audience", [client.audience, " ".join(client.psychographics)]))
        return self._dedupe([agent for agent in activated if agent in AGENT_REGISTRY])

    def build_agent_tasks(self, context: DynamicBrandContext) -> List[AgentTask]:
        tasks: List[AgentTask] = []
        for agent_id in context.activated_agents:
            agent = AGENT_REGISTRY[agent_id]
            retrieval_sources = agent.get("retrieval_sources", REQUIRED_RETRIEVAL_SOURCES)
            tasks.append(
                AgentTask(
                    task_id=f"{context.context_id}:{agent_id}",
                    agent_id=agent_id,
                    stage="agent_activation",
                    objective=str(agent["purpose"]),
                    constraints=[
                        "Use retrieved evidence before recommendation",
                        "Preserve sector, cultural, and psychographic specificity",
                        "Return memory updates for durable brand cognition",
                        "Flag governance risk instead of smoothing over contradictions",
                    ],
                    required_inputs=list(retrieval_sources),
                    expected_outputs=list(AGENT_OUTPUT_CONTRACT),
                    context_filters={
                        "client_id": context.client_id,
                        "sector": context.sector,
                        "geography": context.geography,
                        "audience": context.audience,
                        "deliverable": context.deliverable,
                    },
                )
            )
        return tasks

    def synthesize(
        self,
        context: DynamicBrandContext,
        runtime: "BrandAgentRuntime | None" = None,
    ) -> List[AgentResult]:
        """Run the `output_synthesis` stage — the reasoning step.

        This closes the gap between `agent_activation` and `governance_validation` in
        EXECUTION_STAGES. Requires ANTHROPIC_API_KEY; every other stage does not.

        Results are persisted to the `governance` memory stream so that what each agent
        actually reasoned is durable, per the append-only memory doctrine.
        """
        from ..synthesis.engine import BrandAgentRuntime  # local import keeps orchestration importable without the SDK

        runtime = runtime or BrandAgentRuntime()
        tasks = self.build_agent_tasks(context)
        results = runtime.run_all(tasks, context)

        for result in results:
            self.memory_store.append_event(
                client_id=context.client_id,
                stream="governance",
                event_type="agent_output_synthesized",
                payload={
                    "context_id": context.context_id,
                    "task_id": result.task_id,
                    "agent_id": result.agent_id,
                    "status": result.status,
                    "confidence": result.confidence,
                    "validation_notes": result.validation_notes,
                },
            )
            # Durable brand cognition: the agent's own memory_updates go to the client stream.
            for update in result.outputs.get("memory_updates", []) or []:
                self.memory_store.append_event(
                    client_id=context.client_id,
                    stream="client",
                    event_type="agent_memory_update",
                    payload={"agent_id": result.agent_id, "update": str(update)},
                )

        context.memory_updates.extend(
            {"agent_id": r.agent_id, "updates": r.outputs.get("memory_updates", [])} for r in results
        )
        return results

    def persist_context(self, context: DynamicBrandContext) -> None:
        self.memory_store.append_event(
            client_id=context.client_id,
            stream="client",
            event_type="dynamic_brand_context_created",
            payload={
                "context_id": context.context_id,
                "task": context.task,
                "deliverable": context.deliverable,
                "activated_agents": context.activated_agents,
                "retrieval_sources": context.retrieval_bundle.required_sources if context.retrieval_bundle else [],
            },
        )

    def _matches(self, trigger_type: str, values: Iterable[str]) -> List[str]:
        rules = TRIGGER_RULES.get(trigger_type, {})
        found: List[str] = []
        searchable = " ".join(v.lower() for v in values if v)
        for key, agents in rules.items():
            if key.lower() in searchable:
                found.extend(agents)
        return found

    @staticmethod
    def _dedupe(items: Iterable[str]) -> List[str]:
        seen = set()
        result = []
        for item in items:
            if item in seen:
                continue
            seen.add(item)
            result.append(item)
        return result

