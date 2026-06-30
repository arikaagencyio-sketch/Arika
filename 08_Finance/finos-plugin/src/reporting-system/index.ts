import { randomUUID } from "node:crypto";
import type { CashPosition, DashboardKpi, FinancialReport, FinancialRiskSignal } from "../shared/types.js";
import { formatMoney } from "../shared/money.js";

export class ReportingSystem {
  generateExecutiveReport(input: {
    entityId: string;
    reportType: FinancialReport["reportType"];
    periodStart: string;
    periodEnd: string;
    position: CashPosition;
    risks: FinancialRiskSignal[];
    extraKpis?: DashboardKpi[];
  }): FinancialReport {
    const kpis: DashboardKpi[] = [
      {
        id: "cash-position",
        label: "Cash Position",
        value: formatMoney(input.position.netLiquidity),
        cadence: "daily",
        status: input.position.netLiquidity.amountMinor > 0 ? "healthy" : "critical",
        explanation: "Net liquidity after pending inflows and outflows."
      },
      {
        id: "runway",
        label: "Runway",
        value: input.position.runwayDays ?? "unknown",
        unit: "days",
        cadence: "daily",
        status: input.position.runwayDays === null ? "watch" : input.position.runwayDays < 60 ? "critical" : "healthy",
        explanation: "Estimated survival duration based on net liquidity and burn."
      },
      ...(input.extraKpis ?? [])
    ];

    const criticalRisks = input.risks.filter((risk) => risk.severity === "critical");
    return {
      id: randomUUID(),
      entityId: input.entityId,
      reportType: input.reportType,
      generatedAt: new Date().toISOString(),
      periodStart: input.periodStart,
      periodEnd: input.periodEnd,
      kpis,
      risks: input.risks,
      decisions: this.recommendDecisions(input.risks),
      narrative: criticalRisks.length
        ? "Financial posture requires immediate executive attention before additional growth commitments."
        : "Financial posture is stable, subject to continued treasury discipline and forecast monitoring."
    };
  }

  private recommendDecisions(risks: FinancialRiskSignal[]): string[] {
    const actions = new Set<string>();
    for (const risk of risks) {
      for (const action of risk.recommendedActions) actions.add(action);
    }
    return [...actions];
  }
}
