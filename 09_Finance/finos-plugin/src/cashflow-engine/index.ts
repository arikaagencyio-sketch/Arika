import { addMoney, money, subtractMoney } from "../shared/money.js";
import type { CashPosition, CashflowForecast, CashflowForecastLine, Money } from "../shared/types.js";

export interface CashScheduleItem {
  date: string;
  amount: Money;
  direction: "inflow" | "outflow";
  confidence: number;
  driver: string;
}

export class CashflowEngine {
  forecast(position: CashPosition, schedule: CashScheduleItem[], horizonDays = 91): CashflowForecast {
    const lines: CashflowForecastLine[] = [];
    let projectedCash = position.netLiquidity;
    const start = new Date(position.asOf);

    for (let offset = 0; offset < horizonDays; offset++) {
      const date = new Date(start);
      date.setUTCDate(start.getUTCDate() + offset);
      const key = date.toISOString().slice(0, 10);
      const items = schedule.filter((item) => item.date === key);
      const inflow = addMoney(items.filter((item) => item.direction === "inflow").map((item) => item.amount));
      const outflow = addMoney(items.filter((item) => item.direction === "outflow").map((item) => item.amount));
      projectedCash = subtractMoney(addMoney([projectedCash, inflow]), outflow);

      lines.push({
        date: key,
        inflow,
        outflow,
        net: subtractMoney(inflow, outflow),
        projectedCash,
        confidence: items.length ? Math.min(...items.map((item) => item.confidence)) : 0.8,
        drivers: items.map((item) => item.driver)
      });
    }

    const averageDailyBurn = this.averageDailyNetOutflow(lines);
    const runwayDays = averageDailyBurn > 0 ? Math.floor(position.netLiquidity.amountMinor / averageDailyBurn) : null;

    return {
      entityId: position.entityId,
      generatedAt: new Date().toISOString(),
      scenario: "base",
      horizonDays,
      openingCash: position.netLiquidity,
      closingCash: projectedCash,
      runwayDays,
      lines,
      assumptions: [
        "Forecast uses committed receivables, payables, payroll, tax obligations, recurring revenue, and known operational schedules.",
        "Default horizon is 13 weeks because that is the institutional treasury operating window."
      ]
    };
  }

  burnRate(lines: CashflowForecastLine[], days = 30): Money {
    const sample = lines.slice(0, days);
    const outflows = addMoney(sample.map((line) => line.outflow));
    return money(Math.round(outflows.amountMinor / Math.max(sample.length, 1)), outflows.currency);
  }

  private averageDailyNetOutflow(lines: CashflowForecastLine[]): number {
    if (!lines.length) return 0;
    const total = lines.reduce((sum, line) => sum + Math.max(0, -line.net.amountMinor), 0);
    return total / lines.length;
  }
}
