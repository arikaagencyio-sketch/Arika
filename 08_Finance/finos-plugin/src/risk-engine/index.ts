import { randomUUID } from "node:crypto";
import { RulesEngine } from "../rules-engine/index.js";
import type { CashPosition, CashflowForecast, ClientProfitability, FinancialRiskSignal, Money } from "../shared/types.js";

export class RiskEngine {
  constructor(private readonly rules = new RulesEngine()) {}

  detectFinancialRisk(input: {
    position: CashPosition;
    forecast?: CashflowForecast;
    clientProfitability?: ClientProfitability[];
    revenueByClient?: Array<{ clientId: string; revenue: Money }>;
    debtServiceCoverageRatio?: number;
  }): FinancialRiskSignal[] {
    const signals: FinancialRiskSignal[] = [...this.rules.evaluateCashPosition(input.position)];

    for (const client of input.clientProfitability ?? []) {
      signals.push(...this.rules.evaluateProfitability(input.position.entityId, client));
    }

    signals.push(...this.detectConcentration(input.position.entityId, input.revenueByClient ?? []));

    if (input.debtServiceCoverageRatio !== undefined && input.debtServiceCoverageRatio < 1.25) {
      signals.push({
        id: randomUUID(),
        entityId: input.position.entityId,
        type: "debt",
        severity: "critical",
        title: "DSCR below bankability threshold",
        message: `DSCR is ${input.debtServiceCoverageRatio.toFixed(2)}x, below 1.25x.`,
        metric: "debtServiceCoverageRatio",
        currentValue: input.debtServiceCoverageRatio,
        threshold: 1.25,
        detectedAt: new Date().toISOString(),
        recommendedActions: ["Reduce debt load", "Improve operating cash flow", "Pause discretionary capital deployment"]
      });
    }

    if (input.forecast && input.forecast.closingCash.amountMinor < 0) {
      signals.push({
        id: randomUUID(),
        entityId: input.position.entityId,
        type: "liquidity",
        severity: "critical",
        title: "Forecasted cash deficit",
        message: "13-week forecast projects negative closing cash.",
        metric: "forecastClosingCashMinor",
        currentValue: input.forecast.closingCash.amountMinor,
        threshold: 0,
        detectedAt: new Date().toISOString(),
        recommendedActions: ["Run downside liquidity playbook", "Accelerate receivables", "Defer non-essential payables"]
      });
    }

    return signals;
  }

  private detectConcentration(entityId: string, rows: Array<{ clientId: string; revenue: Money }>): FinancialRiskSignal[] {
    const total = rows.reduce((sum, row) => sum + row.revenue.amountMinor, 0);
    if (total <= 0) return [];

    return rows.flatMap((row) => {
      const concentration = row.revenue.amountMinor / total;
      if (concentration <= 0.2) return [];
      return [
        {
          id: randomUUID(),
          entityId,
          type: "client_dependency",
          severity: concentration > 0.35 ? "critical" : "warning",
          title: "Client concentration above institutional threshold",
          message: `${row.clientId} represents ${(concentration * 100).toFixed(1)}% of revenue.`,
          metric: "clientRevenueConcentration",
          currentValue: concentration,
          threshold: 0.2,
          detectedAt: new Date().toISOString(),
          recommendedActions: ["Diversify acquisition", "Create expansion pipeline", "Reduce dependency through recurring revenue mix"]
        }
      ];
    });
  }
}
