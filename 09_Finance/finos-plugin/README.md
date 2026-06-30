# FinOS Plugin

FinOS is a liquidity-first Financial Operating System plugin for a 360-degree agency. It is designed as a capital orchestration layer, not bookkeeping software.

The plugin turns financial activity into immutable events, reconciles every economic action through a double-entry ledger, allocates capital on revenue events, monitors liquidity and runway, detects risk, generates executive reporting, and exposes MCP/API tools for AI-assisted financial operations.

## Operating Doctrine

1. Liquidity before growth.
2. Ledger before dashboard.
3. Event stream before automation.
4. Governance before execution.
5. Forecast downside before scaling upside.
6. Every dollar receives a role, risk class, time horizon, and return expectation.
7. AI recommends, escalates, and orchestrates; humans retain strategic authority over irreversible capital decisions.

## Required Modules

- `core-ledger`: double-entry accounting truth engine.
- `event-bus`: event publishing, subscriptions, and event-store contracts.
- `cashflow-engine`: runway, burn, receivables, payables, and rolling forecasts.
- `allocation-engine`: rule-based and agent-assisted capital allocation.
- `risk-engine`: liquidity, margin, concentration, debt, and operating risk detection.
- `forecasting-engine`: base, upside, downside, and crisis scenario forecasts.
- `treasury-system`: reserve structure, cash positioning, account segmentation, and liquidity controls.
- `reporting-system`: CEO, CFO, treasury, risk, cashflow, profitability, and operations dashboards.
- `ai-agents`: CFO, cashflow, risk, profitability, treasury, compliance, and leakage agents.
- `integrations`: CRM, payments, banks, accounting, payroll, marketing, and internal system adapters.
- `workflows`: invoice, approval, allocation, reporting, liquidity alert, and emergency mode workflows.
- `financial-governance`: RBAC, approval hierarchy, budget enforcement, separation of duties.
- `compliance-engine`: tax reserves, audit readiness, documentation integrity.
- `profitability-engine`: client, service, department, and campaign economics.
- `dashboard-system`: real-time KPI contracts and dashboard view models.
- `api-layer`: MCP and HTTP interfaces.
- `rules-engine`: configurable policy and threshold evaluation.
- `audit-system`: immutable audit trail and hash-chain integrity.

## Quick Start

```bash
npm install
npm run build
docker compose up -d
npm run dev:mcp
```

## MCP Tools

The MCP layer exposes:

- `get_cash_position`
- `forecast_cashflow`
- `allocate_capital`
- `approve_expense`
- `detect_financial_risk`
- `calculate_client_profitability`
- `generate_financial_report`
- `analyze_runway`
- `monitor_liquidity`
- `evaluate_growth_capacity`

## Source Intelligence

The implementation is derived from the Word drafts in the parent workspace. See `docs/source-intelligence.md` for the source doctrine, document-level mapping, and the architectural decisions preserved from the drafts.
