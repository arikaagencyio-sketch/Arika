import type { FinancialEvent, RevenueReceivedPayload } from "../shared/types.js";
import type { IntegrationConnector } from "./index.js";
import { OpenErApiExchangeRateProvider, type ExchangeRateProvider } from "./exchange-rates.js";

export interface ZohoBooksConfig {
  entityId?: string;
  organizationId?: string;
  clientId?: string;
  clientSecret?: string;
  refreshToken?: string;
  accountsBaseUrl?: string;
  apiBaseUrl?: string;
}

interface ZohoInvoiceRecord {
  invoice_id: string;
  invoice_number: string;
  customer_id: string;
  customer_name: string;
  status: string;
  total: number;
  balance: number;
  currency_code: string;
  date: string;
  last_modified_time: string;
  reference_number?: string;
}

/**
 * Owner-approved defaults (2026-07-07) for every invoice this connector
 * creates. Zoho Books' own org-wide "default terms" preference silently
 * fails to save via its API (confirmed live — returns success but the
 * value never persists), so these are applied per-invoice here instead.
 */
export const DEFAULT_INVOICE_TERMS =
  "Payment is due upon receipt of this invoice unless otherwise agreed in writing. Please reference the invoice number with your payment. For questions regarding this invoice, contact support@arikaagency.com.";
export const DEFAULT_INVOICE_THANK_YOU_NOTE = "Thank you for your business!";

export interface CreateUsdInvoiceRequest {
  customerId: string;
  amountUsdMinor: number;
  description: string;
  referenceNumber?: string;
  invoiceDate?: string;
}

export interface CreateUsdInvoiceResult {
  zohoInvoiceId: string;
  zohoInvoiceNumber: string;
  amountUsdMinor: number;
  amountKesMinor: number;
  exchangeRate: number;
  rateSource: string;
  rateAsOf: string;
}

/**
 * Converts a USD amount (in cents) to KES (in cents) at the given rate.
 * Both currencies price at 2 decimal places in this org, so multiplying
 * minor units directly preserves the minor-unit convention.
 */
export function convertUsdMinorToKesMinor(amountUsdMinor: number, rate: number): number {
  if (!Number.isFinite(amountUsdMinor) || amountUsdMinor < 0) {
    throw new Error("amountUsdMinor must be a non-negative finite number");
  }
  if (!Number.isFinite(rate) || rate <= 0) {
    throw new Error("rate must be a positive finite number");
  }
  return Math.round(amountUsdMinor * rate);
}

/**
 * Normalizes one Zoho Books invoice into FinOS events: always an
 * INVOICE_CREATED, plus a REVENUE_RECEIVED when Zoho reports it fully paid.
 * Event ids are deterministic (derived from the Zoho invoice id) so repeated
 * pulls of the same invoice can't duplicate ledger entries.
 */
export function normalizeZohoInvoice(entityId: string, record: ZohoInvoiceRecord): FinancialEvent[] {
  const amount = { amountMinor: Math.round(record.total * 100), currency: record.currency_code };
  const invoiceCreatedId = `zoho-invoice-${record.invoice_id}`;

  const events: FinancialEvent[] = [
    {
      id: invoiceCreatedId,
      type: "INVOICE_CREATED",
      entityId,
      occurredAt: new Date(record.date).toISOString(),
      source: "zoho-books",
      payload: {
        invoiceId: record.invoice_id,
        invoiceNumber: record.invoice_number,
        clientId: record.customer_id,
        clientName: record.customer_name,
        amount,
        status: record.status
      },
      metadata: { externalReference: record.invoice_id, referenceNumber: record.reference_number }
    }
  ];

  if (record.status === "paid") {
    events.push({
      id: `${invoiceCreatedId}-revenue`,
      type: "REVENUE_RECEIVED",
      entityId,
      occurredAt: new Date(record.last_modified_time).toISOString(),
      source: "zoho-books",
      causationId: invoiceCreatedId,
      payload: {
        amount,
        clientId: record.customer_id,
        invoiceId: record.invoice_id,
        revenueStream: "one_time",
        receivedAt: record.last_modified_time
      } satisfies RevenueReceivedPayload
    });
  }

  return events;
}

/**
 * Real Zoho Books connector — closes GO_LIVE_CHECKLIST.md item 9. Runs as a
 * standalone server-to-server OAuth client (self client grant), independent
 * of any claude.ai session connector: pull() normalizes invoices into FinOS
 * events, createInvoiceFromUsdAmount() issues a real invoice converted from
 * OFFER_OS.md's USD pricing into this org's KES base currency at a live rate
 * (the owner's 2026-07-01 decision — see FINANCE_OS.md §12).
 *
 * Deliberately does not implement the optional `push(event)` hook: wiring
 * invoice creation to auto-fire off an internal event would be a live
 * automation crossing AGENCY_OPERATING_CONSTITUTION.md §5's Risk Class
 * threshold, which needs an AUTOMATION_APPROVAL_MATRIX.md row and human
 * sign-off first (GO_LIVE_CHECKLIST.md item 11). Call
 * createInvoiceFromUsdAmount() explicitly from an approved, human-gated path
 * instead.
 */
export class ZohoBooksConnector implements IntegrationConnector {
  readonly id = "zoho-books";
  readonly kind = "accounting" as const;
  readonly name = "Zoho Books";

  private readonly entityId: string;
  private readonly organizationId?: string;
  private readonly clientId?: string;
  private readonly clientSecret?: string;
  private readonly refreshToken?: string;
  private readonly accountsBaseUrl: string;
  private readonly apiBaseUrl: string;
  private readonly exchangeRates: ExchangeRateProvider;

  private accessToken?: string;
  private accessTokenExpiresAt = 0;

  constructor(config: ZohoBooksConfig = {}, exchangeRates: ExchangeRateProvider = new OpenErApiExchangeRateProvider()) {
    this.entityId = config.entityId ?? process.env.FINOS_DEFAULT_ENTITY_ID ?? "agency-main";
    this.organizationId = config.organizationId ?? process.env.ZOHO_ORGANIZATION_ID;
    this.clientId = config.clientId ?? process.env.ZOHO_CLIENT_ID;
    this.clientSecret = config.clientSecret ?? process.env.ZOHO_CLIENT_SECRET;
    this.refreshToken = config.refreshToken ?? process.env.ZOHO_REFRESH_TOKEN;
    this.accountsBaseUrl = config.accountsBaseUrl ?? process.env.ZOHO_ACCOUNTS_BASE_URL ?? "https://accounts.zoho.com";
    this.apiBaseUrl = config.apiBaseUrl ?? process.env.ZOHO_API_BASE_URL ?? "https://www.zohoapis.com/books/v3";
    this.exchangeRates = exchangeRates;
  }

  private assertConfigured(): { organizationId: string; clientId: string; clientSecret: string; refreshToken: string } {
    if (!this.organizationId || !this.clientId || !this.clientSecret || !this.refreshToken) {
      throw new Error(
        "Zoho Books connector is not configured — set ZOHO_ORGANIZATION_ID, ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, and ZOHO_REFRESH_TOKEN " +
          "(generated via a Zoho API Console Self Client — see finos-plugin/docs/integrations.md)."
      );
    }
    return {
      organizationId: this.organizationId,
      clientId: this.clientId,
      clientSecret: this.clientSecret,
      refreshToken: this.refreshToken
    };
  }

  private async getAccessToken(): Promise<string> {
    const { clientId, clientSecret, refreshToken } = this.assertConfigured();
    if (this.accessToken && this.accessTokenExpiresAt > Date.now() + 30_000) {
      return this.accessToken;
    }

    const params = new URLSearchParams({
      grant_type: "refresh_token",
      client_id: clientId,
      client_secret: clientSecret,
      refresh_token: refreshToken
    });

    const response = await fetch(`${this.accountsBaseUrl}/oauth/v2/token?${params.toString()}`, { method: "POST" });
    const body = (await response.json().catch(() => ({}))) as { access_token?: string; expires_in?: number; error?: string };
    if (!response.ok || !body.access_token) {
      throw new Error(`Zoho OAuth token refresh failed: ${body.error ?? `HTTP ${response.status}`}`);
    }

    this.accessToken = body.access_token;
    this.accessTokenExpiresAt = Date.now() + (body.expires_in ?? 3600) * 1000;
    return this.accessToken;
  }

  private async request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const { organizationId } = this.assertConfigured();
    const token = await this.getAccessToken();
    const url = new URL(`${this.apiBaseUrl}${path}`);
    if (!url.searchParams.has("organization_id")) {
      url.searchParams.set("organization_id", organizationId);
    }

    const response = await fetch(url, {
      ...init,
      headers: {
        Authorization: `Zoho-oauthtoken ${token}`,
        "Content-Type": "application/json",
        ...(init.headers ?? {})
      }
    });

    const body = await response.json().catch(() => undefined);
    if (!response.ok) {
      throw new Error(`Zoho Books API error (${path}): HTTP ${response.status} ${JSON.stringify(body)}`);
    }
    return body as T;
  }

  async pull(since?: string): Promise<FinancialEvent[]> {
    const query = since ? `&last_modified_time=${encodeURIComponent(since)}` : "";
    const body = await this.request<{ invoices: ZohoInvoiceRecord[] }>(`/invoices?per_page=200${query}`);
    return body.invoices.flatMap((record) => normalizeZohoInvoice(this.entityId, record));
  }

  async health(): Promise<{ ok: boolean; message: string }> {
    try {
      const { organizationId } = this.assertConfigured();
      const body = await this.request<{ organization: { organization_id: string; name: string } }>(
        `/organizations/${organizationId}`
      );
      return {
        ok: true,
        message: `Connected to Zoho Books org ${body.organization.name} (${body.organization.organization_id})`
      };
    } catch (error) {
      return { ok: false, message: error instanceof Error ? error.message : String(error) };
    }
  }

  async createInvoiceFromUsdAmount(request: CreateUsdInvoiceRequest): Promise<CreateUsdInvoiceResult> {
    const quote = await this.exchangeRates.getRate("USD", "KES");
    const amountKesMinor = convertUsdMinorToKesMinor(request.amountUsdMinor, quote.rate);

    const body = await this.request<{ invoice: ZohoInvoiceRecord }>(`/invoices`, {
      method: "POST",
      body: JSON.stringify({
        customer_id: request.customerId,
        date: request.invoiceDate,
        reference_number: request.referenceNumber,
        notes: `${DEFAULT_INVOICE_THANK_YOU_NOTE}\n\nPriced at USD ${(request.amountUsdMinor / 100).toFixed(2)}, converted to KES at rate ${quote.rate} (source: ${quote.source}, as of ${quote.asOf}).`,
        terms: DEFAULT_INVOICE_TERMS,
        line_items: [
          {
            name: request.description,
            quantity: 1,
            rate: amountKesMinor / 100
          }
        ]
      })
    });

    return {
      zohoInvoiceId: body.invoice.invoice_id,
      zohoInvoiceNumber: body.invoice.invoice_number,
      amountUsdMinor: request.amountUsdMinor,
      amountKesMinor,
      exchangeRate: quote.rate,
      rateSource: quote.source,
      rateAsOf: quote.asOf
    };
  }
}
