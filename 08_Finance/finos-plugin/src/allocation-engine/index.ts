import { randomUUID } from "node:crypto";
import { addMoney, money, percentOf, subtractMoney } from "../shared/money.js";
import type { AllocationPlan, AllocationRule, FinancialEvent, RevenueReceivedPayload } from "../shared/types.js";

export class AllocationEngine {
  constructor(private readonly rules: AllocationRule[]) {}

  planRevenueAllocation(event: FinancialEvent<RevenueReceivedPayload>): AllocationPlan {
    const rule = this.selectRule(event);
    if (!rule) {
      throw new Error(`No allocation rule matched revenue stream ${event.payload.revenueStream}.`);
    }

    const percentTotal = rule.allocations.reduce((total, target) => total + target.percent, 0);
    if (percentTotal > 100) {
      throw new Error(`Allocation rule ${rule.id} exceeds 100%.`);
    }

    const targets = rule.allocations.map((target) => ({
      ...target,
      amount: percentOf(event.payload.amount, target.percent)
    }));

    const allocated = addMoney(targets.map((target) => target.amount));
    const residual = subtractMoney(event.payload.amount, allocated);

    return {
      id: randomUUID(),
      entityId: event.entityId,
      sourceEventId: event.id,
      amount: event.payload.amount,
      targets,
      residual,
      decisionMode: "rules",
      rationale: [
        `Rule '${rule.name}' selected for ${event.payload.revenueStream} revenue.`,
        "Liquidity-first allocation order preserved: taxes, payroll/operations, reserves, growth, profit."
      ]
    };
  }

  recommendDynamicAdjustment(plan: AllocationPlan, runwayDays: number | null): AllocationPlan {
    if (runwayDays === null || runwayDays >= 90) return plan;

    const emergencyBoostMinor = Math.round(plan.residual.amountMinor * 0.5);
    if (emergencyBoostMinor <= 0) return plan;

    const emergencyTarget = plan.targets.find((target) => target.bucket === "emergency_reserve");
    if (!emergencyTarget) return plan;

    emergencyTarget.amount = money(emergencyTarget.amount.amountMinor + emergencyBoostMinor, plan.amount.currency);
    plan.residual = money(plan.residual.amountMinor - emergencyBoostMinor, plan.amount.currency);
    plan.decisionMode = "ai_recommended";
    plan.rationale.push("Runway below 90 days; recommended residual sweep into emergency reserve.");
    return plan;
  }

  private selectRule(event: FinancialEvent<RevenueReceivedPayload>): AllocationRule | undefined {
    return this.rules
      .filter((rule) => rule.enabled)
      .filter((rule) => rule.entityId === event.entityId)
      .filter((rule) => !rule.revenueStream || rule.revenueStream === event.payload.revenueStream)
      .sort((left, right) => right.priority - left.priority)[0];
  }
}
