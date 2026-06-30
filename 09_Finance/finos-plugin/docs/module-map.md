# Module Map

The user-facing module names from the architecture brief map to implementation directories under `src/`.

| Required module | Implementation path | Primary outputs |
|---|---|---|
| `/core-ledger` | `src/core-ledger` | Double-entry journal posting, balance validation, trial balance. |
| `/event-bus` | `src/event-bus` | Event publication, subscriptions, event history interface. |
| `/cashflow-engine` | `src/cashflow-engine` | 13-week cashflow forecasts, burn, runway. |
| `/allocation-engine` | `src/allocation-engine` | Revenue allocation plans, residual handling, reserve recommendations. |
| `/risk-engine` | `src/risk-engine` | Liquidity, runway, DSCR, margin, concentration, and forecast risk signals. |
| `/forecasting-engine` | `src/forecasting-engine` | Base, upside, downside, crisis scenarios. |
| `/treasury-system` | `src/treasury-system` | Cash position, reserve adequacy, restricted/unrestricted liquidity. |
| `/reporting-system` | `src/reporting-system` | Executive financial reports with decisions and risk narrative. |
| `/ai-agents` | `src/ai-agents` | CFO, cashflow, risk, profitability, treasury, compliance, leakage agents. |
| `/integrations` | `src/integrations` | CRM, payment, banking, accounting, payroll, marketing, internal connectors. |
| `/workflows` | `src/workflows` | Revenue allocation, tax reserve, expense approval, liquidity workflows. |
| `/financial-governance` | `src/financial-governance` | Approval hierarchy, budget checks, segregation-of-duties enforcement. |
| `/compliance-engine` | `src/compliance-engine` | Tax reserve calculation, audit readiness checks. |
| `/profitability-engine` | `src/profitability-engine` | Client profitability, gross margin, contribution margin, LTV:CAC, CAC payback. |
| `/dashboard-system` | `src/dashboard-system` | CEO, CFO, treasury, profitability, cashflow, risk, operations dashboards. |
| `/api-layer` | `src/api-layer` | MCP tools, HTTP routes, shared tool contracts. |
| `/rules-engine` | `src/rules-engine` | Threshold evaluation and risk signal generation. |
| `/audit-system` | `src/audit-system` | Append-only hash-chain audit records. |

Database structures live in `database/schema.sql`. Operational documentation lives in `docs/`.
