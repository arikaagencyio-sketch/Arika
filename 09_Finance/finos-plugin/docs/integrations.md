# Integration Architecture

FinOS normalizes external systems into financial events.

## Zoho Books (real, live) — closes GO_LIVE_CHECKLIST.md item 9

`src/integrations/zoho-books.ts`'s `ZohoBooksConnector` is the first real (non-stub)
connector. It is a standalone OAuth client — independent of the claude.ai Zoho
Books session connector, which only this chat session can use — so it needs its
own credentials in `.env`:

- `ZOHO_ORGANIZATION_ID` — real, not secret: `929138528` (Arika Agency, Kenya, KES base).
- `ZOHO_CLIENT_ID` / `ZOHO_CLIENT_SECRET` / `ZOHO_REFRESH_TOKEN` — generated via a
  **Zoho API Console Self Client** (owner action: console.zoho.com/settings, create a
  "Self Client", generate a grant token with `ZohoBooks.fullaccess.all` scope, exchange
  it once for a refresh token). Not fabricatable — a one-time owner-run OAuth step.
- `ZOHO_ACCOUNTS_BASE_URL` / `ZOHO_API_BASE_URL` — must match the account's actual
  Zoho data center (defaults assume the US DC: `accounts.zoho.com` / `www.zohoapis.com`).

Capabilities:
- `pull(since)` — lists invoices modified since `since` and normalizes each into an
  `INVOICE_CREATED` event (plus a `REVENUE_RECEIVED` event when Zoho reports it paid).
  Event ids are deterministic (`zoho-invoice-{id}`), so repeated pulls can't double-post.
- `createInvoiceFromUsdAmount(...)` — the real USD→KES conversion path: `OFFER_OS.md`
  prices offers in USD, but this org's base currency is KES (owner decision, 2026-07-01),
  so this converts at a **live** rate before creating the invoice, and records the
  original USD amount + rate + source in the invoice notes for audit traceability.
- `health()` — confirms the OAuth credentials actually work against the real org.
- Deliberately has **no** `push(event)` auto-wiring: creating a real invoice off an
  internal event would be a live automation crossing `AGENCY_OPERATING_CONSTITUTION.md`
  §5's risk-class gate, which needs an `AUTOMATION_APPROVAL_MATRIX.md` row and human
  sign-off first (`GO_LIVE_CHECKLIST.md` item 11). Call `createInvoiceFromUsdAmount`
  explicitly from an approved, human-gated caller instead.

Exchange rate source: `src/integrations/exchange-rates.ts`'s `OpenErApiExchangeRateProvider`
— live, free, keyless (`open.er-api.com`, refreshed daily). ECB-based sources (e.g.
`frankfurter.dev`) were tried first and rejected: confirmed live that they don't publish
a KES rate at all. This is a real, working default, not a placeholder — but the owner may
prefer a different source later (e.g. a paid one with an SLA or intraday updates); swap
the provider passed into `ZohoBooksConnector`'s constructor if so.

## Connector Contract

Every connector implements:

- `id`: stable connector id.
- `kind`: `crm`, `payments`, `banking`, `accounting`, `payroll`, `marketing`, or `internal_ops`.
- `pull(since)`: returns normalized `FinancialEvent[]`.
- `push(event)`: optional outbound sync for invoice reminders, reserve transfers, or workflow callbacks.
- `health()`: freshness and authorization status.

## Required Connectors

| Domain | Source events | Normalized FinOS events |
|---|---|---|
| CRM | deal closed, client updated, pipeline changed | `INVOICE_CREATED`, `REVENUE_RECEIVED`, `CLIENT_PROFITABILITY_UPDATED` |
| Payment gateways | payment succeeded, failed payment, refund | `REVENUE_RECEIVED`, `CASHFLOW_WARNING` |
| Banking APIs | bank transaction, balance update | `LIQUIDITY_POSITION_UPDATED`, `REVENUE_RECEIVED`, `EXPENSE_SUBMITTED` |
| Accounting systems | chart of accounts, journal entry, reconciliation | ledger sync events and audit records |
| Payroll systems | payroll run, tax withholding, contractor payment | `PAYROLL_EXECUTED`, `TAX_RESERVED` |
| Marketing systems | campaign spend, CAC, channel ROI | `EXPENSE_SUBMITTED`, `MARGIN_DROP_DETECTED`, `BUDGET_THRESHOLD_EXCEEDED` |
| Internal operations | delivery cost, utilization, project status | `CLIENT_PROFITABILITY_UPDATED`, `MARGIN_DROP_DETECTED` |

## Idempotency

Connectors must generate deterministic external references and idempotency keys so repeated webhook delivery cannot duplicate financial events or ledger entries.

## Evidence

Every connector should attach evidence metadata when available:

- source document id
- external transaction id
- invoice number
- bank account reference
- approval reference
- counterparty id
- event signature
