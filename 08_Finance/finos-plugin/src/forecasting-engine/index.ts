import { money } from "../shared/money.js";
import type { CashflowForecast } from "../shared/types.js";

export class ForecastingEngine {
  scenario(forecast: CashflowForecast, scenario: CashflowForecast["scenario"]): CashflowForecast {
    const factors = {
      base: { inflow: 1, outflow: 1 },
      upside: { inflow: 1.18, outflow: 1.08 },
      downside: { inflow: 0.7, outflow: 1.05 },
      crisis: { inflow: 0.45, outflow: 0.9 }
    }[scenario];

    let projectedCash = forecast.openingCash;
    const lines = forecast.lines.map((line) => {
      const inflow = money(line.inflow.amountMinor * factors.inflow, line.inflow.currency);
      const outflow = money(line.outflow.amountMinor * factors.outflow, line.outflow.currency);
      const net = money(inflow.amountMinor - outflow.amountMinor, inflow.currency);
      projectedCash = money(projectedCash.amountMinor + net.amountMinor, projectedCash.currency);
      return {
        ...line,
        inflow,
        outflow,
        net,
        projectedCash,
        confidence: Math.max(0.35, line.confidence - (scenario === "base" ? 0 : 0.15)),
        drivers: [...line.drivers, `${scenario} scenario adjustment`]
      };
    });

    const averageBurn = lines.reduce((sum, line) => sum + Math.max(0, -line.net.amountMinor), 0) / Math.max(lines.length, 1);
    return {
      ...forecast,
      generatedAt: new Date().toISOString(),
      scenario,
      closingCash: projectedCash,
      runwayDays: averageBurn > 0 ? Math.floor(forecast.openingCash.amountMinor / averageBurn) : null,
      lines,
      assumptions: [...forecast.assumptions, `Scenario factor applied: inflow=${factors.inflow}, outflow=${factors.outflow}.`]
    };
  }
}
