# Integration Architecture

FinOS normalizes external systems into financial events.

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
