import type { CashPosition, ClientProfitability, FinancialRiskSignal, RiskSeverity } from "../shared/types.js";

export interface ThresholdRule<TContext> {
  id: string;
  name: string;
  severity: RiskSeverity;
  metric: string;
  threshold: number;
  evaluate(context: TContext): number;
  when(value: number, threshold: number): boolean;
  message(value: number, threshold: number): string;
  actions: string[];
}

export class RulesEngine {
  evaluateCashPosition(entityId: string, position: CashPosition): FinancialRiskSignal[] {
    const rules: Array<ThresholdRule<CashPosition>> = [
      {
        id: "runway-under-60",
        name: "Runway below emergency threshold",
        severity: "critical",
        metric: "runwayDays",
        threshold: 60,
        evaluate: (ctx) => ctx.runwayDays ?? Number.POSITIVE_INFINITY,
        when: (value, threshold) => value < threshold,
        message: (value, threshold) => `Runway is ${Math.round(value)} days, below ${threshold} days.`,
        actions: ["Freeze discretionary spend", "Accelerate collections", "Review payroll runway", "Enter emergency liquidity mode"]
      },
      {
        id: "net-liquidity-negative",
        name: "Negative net liquidity",
        severity: "critical",
        metric: "netLiquidityMinor",
        threshold: 0,
        evaluate: (ctx) => ctx.netLiquidity.amountMinor,
        when: (value, threshold) => value < threshold,
        message: () => "Pending outflows exceed available and pending cash inflows.",
        actions: ["Escalate to CFO", "Delay non-critical payables", "Reforecast 13-week cash"]
      }
    ];

    return this.toSignals(entityId, "liquidity", rules, position);
  }

  evaluateProfitability(entityId: string, client: ClientProfitability): FinancialRiskSignal[] {
    const rules: Array<ThresholdRule<ClientProfitability>> = [
      {
        id: "gross-margin-under-20",
        name: "Gross margin below minimum threshold",
        severity: "warning",
        metric: "grossMarginPct",
        threshold: 20,
        evaluate: (ctx) => ctx.grossMarginPct,
        when: (value, threshold) => value < threshold,
        message: (value, threshold) => `Client gross margin is ${value.toFixed(1)}%, below ${threshold}%.`,
        actions: ["Review pricing", "Audit delivery costs", "Restrict scope expansion"]
      },
      {
        id: "ltv-cac-under-3",
        name: "LTV:CAC below scale threshold",
        severity: "warning",
        metric: "ltvToCac",
        threshold: 3,
        evaluate: (ctx) => ctx.ltvToCac ?? 0,
        when: (value, threshold) => value > 0 && value < threshold,
        message: (value, threshold) => `LTV:CAC is ${value.toFixed(2)}, below ${threshold}.`,
        actions: ["Improve retention", "Reduce acquisition cost", "Reassess channel economics"]
      }
    ];

    return this.toSignals(entityId, "margin", rules, client);
  }

  private toSignals<TContext>(
    entityId: string,
    type: FinancialRiskSignal["type"],
    rules: Array<ThresholdRule<TContext>>,
    context: TContext
  ): FinancialRiskSignal[] {
    return rules.flatMap((rule) => {
      const value = rule.evaluate(context);
      if (!rule.when(value, rule.threshold)) return [];
      return [
        {
          id: `${rule.id}-${Date.now()}`,
          entityId,
          type,
          severity: rule.severity,
          title: rule.name,
          message: rule.message(value, rule.threshold),
          metric: rule.metric,
          currentValue: value,
          threshold: rule.threshold,
          detectedAt: new Date().toISOString(),
          recommendedActions: rule.actions
        }
      ];
    });
  }
}
