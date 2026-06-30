import { addMoney, money, subtractMoney } from "../shared/money.js";
import type { CashPosition, Money } from "../shared/types.js";

export interface TreasuryBalanceInput {
  entityId: string;
  unrestrictedCash: Money[];
  restrictedCash: Money[];
  reserveCash: Money[];
  pendingInflows: Money[];
  pendingOutflows: Money[];
  averageDailyBurnMinor?: number;
}

export interface ReservePolicy {
  entityId: string;
  operatingReserveMonths: number;
  emergencyReserveMonths: number;
  payrollCyclesMinimum: number;
  monthlyCoreOpex: Money;
  payrollCycleCost: Money;
}

export class TreasurySystem {
  calculateCashPosition(input: TreasuryBalanceInput): CashPosition {
    const unrestrictedCash = addMoney(input.unrestrictedCash);
    const restrictedCash = addMoney(input.restrictedCash);
    const reserveCash = addMoney(input.reserveCash);
    const pendingInflows = addMoney(input.pendingInflows);
    const pendingOutflows = addMoney(input.pendingOutflows);
    const netLiquidity = subtractMoney(addMoney([unrestrictedCash, reserveCash, pendingInflows]), pendingOutflows);
    const runwayDays =
      input.averageDailyBurnMinor && input.averageDailyBurnMinor > 0
        ? Math.floor(netLiquidity.amountMinor / input.averageDailyBurnMinor)
        : null;

    return {
      entityId: input.entityId,
      asOf: new Date().toISOString(),
      unrestrictedCash,
      restrictedCash,
      reserveCash,
      pendingInflows,
      pendingOutflows,
      netLiquidity,
      runwayDays
    };
  }

  evaluateReservePolicy(position: CashPosition, policy: ReservePolicy): string[] {
    const findings: string[] = [];
    const monthlyOpex = policy.monthlyCoreOpex.amountMinor;
    const emergencyTarget = monthlyOpex * policy.emergencyReserveMonths;
    const operatingTarget = monthlyOpex * policy.operatingReserveMonths;
    const payrollTarget = policy.payrollCycleCost.amountMinor * policy.payrollCyclesMinimum;

    if (position.reserveCash.amountMinor < emergencyTarget) {
      findings.push("Emergency reserve is below target.");
    }
    if (position.unrestrictedCash.amountMinor < operatingTarget) {
      findings.push("Operating liquidity is below target.");
    }
    if (position.restrictedCash.amountMinor < payrollTarget) {
      findings.push("Payroll protection reserve is below minimum cycle target.");
    }

    return findings;
  }

  emptyPosition(entityId: string, currency = "USD"): CashPosition {
    const zero = money(0, currency);
    return {
      entityId,
      asOf: new Date().toISOString(),
      unrestrictedCash: zero,
      restrictedCash: zero,
      reserveCash: zero,
      pendingInflows: zero,
      pendingOutflows: zero,
      netLiquidity: zero,
      runwayDays: null
    };
  }
}
