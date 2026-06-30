import type { AllocationEngine } from "../allocation-engine/index.js";
import type { ComplianceEngine } from "../compliance-engine/index.js";
import type { FinancialEventBus } from "../event-bus/index.js";
import type { FinancialGovernanceService } from "../financial-governance/index.js";
import type { RiskEngine } from "../risk-engine/index.js";
import type { ExpensePayload, RevenueReceivedPayload } from "../shared/types.js";

export class FinancialWorkflowOrchestrator {
  constructor(
    private readonly eventBus: FinancialEventBus,
    private readonly allocationEngine: AllocationEngine,
    private readonly complianceEngine: ComplianceEngine,
    private readonly governance: FinancialGovernanceService,
    private readonly riskEngine: RiskEngine
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
    });

    void this.riskEngine;
  }
}
