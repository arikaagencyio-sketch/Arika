import type { CurrencyCode, Money } from "./types.js";

export function money(amountMinor: number, currency: CurrencyCode = "USD"): Money {
  if (!Number.isFinite(amountMinor)) {
    throw new Error("Money amount must be finite.");
  }
  return { amountMinor: Math.round(amountMinor), currency };
}

export function assertSameCurrency(values: Money[]): CurrencyCode {
  const [first] = values;
  if (!first) return "USD";
  for (const value of values) {
    if (value.currency !== first.currency) {
      throw new Error(`Currency mismatch: expected ${first.currency}, received ${value.currency}.`);
    }
  }
  return first.currency;
}

export function addMoney(values: Money[]): Money {
  const currency = assertSameCurrency(values);
  return money(values.reduce((total, value) => total + value.amountMinor, 0), currency);
}

export function subtractMoney(left: Money, right: Money): Money {
  assertSameCurrency([left, right]);
  return money(left.amountMinor - right.amountMinor, left.currency);
}

export function multiplyMoney(value: Money, factor: number): Money {
  return money(value.amountMinor * factor, value.currency);
}

export function percentOf(value: Money, percent: number): Money {
  return multiplyMoney(value, percent / 100);
}

export function ratio(numerator: Money, denominator: Money): number | null {
  assertSameCurrency([numerator, denominator]);
  if (denominator.amountMinor === 0) return null;
  return numerator.amountMinor / denominator.amountMinor;
}

export function formatMoney(value: Money): string {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: value.currency
  }).format(value.amountMinor / 100);
}
