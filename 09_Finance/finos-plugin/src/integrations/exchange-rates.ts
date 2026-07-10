export interface ExchangeRateQuote {
  from: string;
  to: string;
  rate: number;
  asOf: string;
  source: string;
}

export interface ExchangeRateProvider {
  getRate(from: string, to: string): Promise<ExchangeRateQuote>;
}

const DEFAULT_CACHE_TTL_MS = 6 * 60 * 60 * 1000;

/**
 * Live, keyless rate source (open.er-api.com — the free, no-signup mirror of
 * exchangerate-api.com, refreshed daily) — the real source picked for
 * GO_LIVE_CHECKLIST.md item 9. ECB-only sources (e.g. frankfurter.dev) were
 * tried first and rejected: they don't publish a KES rate at all. Swap the
 * provider passed into ZohoBooksConnector if the owner later prefers a
 * different one (e.g. a paid source with an SLA or intraday updates).
 */
export class OpenErApiExchangeRateProvider implements ExchangeRateProvider {
  private readonly cache = new Map<string, { quote: ExchangeRateQuote; expiresAt: number }>();

  constructor(
    private readonly baseUrl: string = "https://open.er-api.com/v6/latest",
    private readonly cacheTtlMs: number = DEFAULT_CACHE_TTL_MS
  ) {}

  async getRate(from: string, to: string): Promise<ExchangeRateQuote> {
    const key = `${from}_${to}`;
    const cached = this.cache.get(key);
    if (cached && cached.expiresAt > Date.now()) {
      return cached.quote;
    }

    const url = `${this.baseUrl}/${encodeURIComponent(from)}`;
    const response = await fetch(url);
    const body = (await response.json().catch(() => undefined)) as
      | { result: string; time_last_update_utc: string; rates: Record<string, number> }
      | undefined;

    if (!response.ok || !body || body.result !== "success") {
      throw new Error(`Exchange rate lookup failed (${from}->${to}): HTTP ${response.status}`);
    }

    const rate = body.rates[to];
    if (typeof rate !== "number") {
      throw new Error(`Exchange rate lookup returned no rate for ${to}`);
    }

    const quote: ExchangeRateQuote = {
      from,
      to,
      rate,
      asOf: body.time_last_update_utc,
      source: "open.er-api.com"
    };
    this.cache.set(key, { quote, expiresAt: Date.now() + this.cacheTtlMs });
    return quote;
  }
}

/**
 * Fixed-rate provider for tests and manual emergency fallback only — never
 * the default in production, since invoicing needs a real, refreshed rate,
 * not a hardcoded one.
 */
export class FixedExchangeRateProvider implements ExchangeRateProvider {
  constructor(
    private readonly rate: number,
    private readonly from = "USD",
    private readonly to = "KES"
  ) {}

  async getRate(from: string, to: string): Promise<ExchangeRateQuote> {
    if (from !== this.from || to !== this.to) {
      throw new Error(`FixedExchangeRateProvider only supports ${this.from}->${this.to}`);
    }
    return {
      from,
      to,
      rate: this.rate,
      asOf: new Date().toISOString().slice(0, 10),
      source: "fixed-fallback (not live)"
    };
  }
}
