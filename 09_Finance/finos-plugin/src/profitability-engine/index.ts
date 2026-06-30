import { ratio, subtractMoney } from "../shared/money.js";
import type { ClientProfitability, Money } from "../shared/types.js";

export class ProfitabilityEngine {
  calculateClientProfitability(input: {
    entityId: string;
    clientId: string;
    revenue: Money;
    deliveryCost: Money;
    acquisitionCost: Money;
    averageMonthlyRevenue?: Money;
  }): ClientProfitability {
    const grossProfit = subtractMoney(input.revenue, input.deliveryCost);
    const contributionProfit = subtractMoney(grossProfit, input.acquisitionCost);
    const grossMarginPct = (ratio(grossProfit, input.revenue) ?? 0) * 100;
    const contributionMarginPct = (ratio(contributionProfit, input.revenue) ?? 0) * 100;
    const ltvToCac = ratio(input.revenue, input.acquisitionCost);
    const paybackMonths =
      input.averageMonthlyRevenue && input.averageMonthlyRevenue.amountMinor > 0
        ? input.acquisitionCost.amountMinor / input.averageMonthlyRevenue.amountMinor
        : null;

    const riskFlags: string[] = [];
    if (grossMarginPct < 20) riskFlags.push("gross_margin_below_20_percent");
    if (ltvToCac !== null && ltvToCac < 3) riskFlags.push("ltv_cac_below_3x");
    if (contributionMarginPct < 0) riskFlags.push("negative_contribution_margin");

    return {
      entityId: input.entityId,
      clientId: input.clientId,
      revenue: input.revenue,
      deliveryCost: input.deliveryCost,
      acquisitionCost: input.acquisitionCost,
      grossMarginPct,
      contributionMarginPct,
      ltvToCac,
      paybackMonths,
      riskFlags
    };
  }
}
