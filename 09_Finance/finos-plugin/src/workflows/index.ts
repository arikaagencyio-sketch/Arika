import type { AllocationEngine } from "../allocation-engine/index.js";
import type { AgentRegistry } from "../ai-agents/index.js";
import type { ClaudeAgentRuntime } from "../ai-agents/runtime.js";
import type { AuditSystem } from "../audit-system/index.js";
import type { ComplianceEngine } from "../compliance-engine/index.js";
import type { FinancialEventBus } from "../event-bus/index.js";
import type { FinancialGovernanceService } from "../financial-governance/index.js";
import type { RiskEngine } from "../risk-engine/index.js";
import type { ExpensePayload, FinancialEvent, RevenueReceivedPayload } from "../shared/types.js";

export class FinancialWorkflowOrchestrator {
  constructor(
    private readonly eventBus: FinancialEventBus,
    private readonly allocationEngine: AllocationEngine,
    private readonly complianceEngine: ComplianceEngine,
    private readonly governance: FinancialGovernanceService,
    private readonly riskEngine: RiskEngine,
    private readonly agents: AgentRegistry,
    private readonly agentRuntime: ClaudeAgentRuntime,
    private readonly audit: AuditSystem
  ) {}

  register(): void {
    this.eventBus.subscribe<RevenueReceivedPayload>("REVENUE_RECEIVED", async (event) => {
      const allocation = this.allocationEngine.planRevenueAllocation(event);
      const taxReserve = this.complianceEngine.calculateTaxReserve(event, 15);

      await this.eventBus.publish({
        type: "CAPITAL_ALLOCATED",
        entityId: event.entityId,
        source: "allocation-engine",
        causationId: event.id,
        correlationId: event.correlationId ?? event.id,
        payload: { allocation }
      });

      await this.eventBus.publish({
        type: "TAX_RESERVED",
        entityId: event.entityId,
        source: "compliance-engine",
        causationId: event.id,
        correlationId: event.correlationId ?? event.id,
        payload: { taxReserve }
      });

      await this.invokeAgents(event);
    });

    this.eventBus.subscribe<ExpensePayload>("EXPENSE_SUBMITTED", async (event) => {
      const approval = this.governance.approveExpense({ entityId: event.entityId, expense: event.payload });
      await this.eventBus.publish({
        type: approval.status === "auto_approved" ? "EXPENSE_APPROVED" : "BUDGET_THRESHOLD_EXCEEDED",
        entityId: event.entityId,
        source: "financial-governance",
        causationId: event.id,
        correlationId: event.correlationId ?? event.id,
        payload: { approval }
      });

      await this.invokeAgents(event);
    });

    void this.riskEngine;
  }

  /**
   * Runs every agent whose listensTo includes this event's type through Claude, and
   * writes each recommendation (or failure) to the hash-chained audit trail. Advisory
   * only — nothing here auto-executes a recommendation. Per AGENCY_OPERATING_CONSTITUTION.md
   * §5, acting on these requires a real AUTOMATION_APPROVAL_MATRIX.md row first.
   */
  private async invokeAgents(event: FinancialEvent): Promise<void> {
    const relevantAgents = this.agents.forEvent(event.type);

    for (const spec of relevantAgents) {
      try {
        const recommendation = await this.agentRuntime.run(spec, event);
        this.audit.record({
          entityId: event.entityId,
          actorId: spec.id,
          action: "agent_recommendation_generated",
          resourceType: "financial_event",
          resourceId: event.id,
          metadata: { recommendation }
        });
      } catch (error) {
        this.audit.record({
          entityId: event.entityId,
          actorId: spec.id,
          action: "agent_invocation_failed",
          resourceType: "financial_event",
          resourceId: event.id,
          metadata: { error: error instanceof Error ? error.message : String(error) }
        });
      }
    }
  }
}
