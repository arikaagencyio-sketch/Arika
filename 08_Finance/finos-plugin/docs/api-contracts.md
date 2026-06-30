# API Contracts

The MCP and HTTP layers expose the same capability set.

## MCP Tools

### `get_cash_position`

Input:

```json
{ "entityId": "agency-main" }
```

Output: current unrestricted cash, restricted cash, reserve cash, pending inflows, pending outflows, net liquidity, and runway days.

### `forecast_cashflow`

Input:

```json
{
  "entityId": "agency-main",
  "horizonDays": 91,
  "scenario": "downside"
}
```

Output: rolling cash forecast with daily inflow, outflow, net movement, projected cash, confidence, drivers, assumptions, and runway.

### `allocate_capital`

Input:

```json
{
  "entityId": "agency-main",
  "amountMinor": 1000000,
  "currency": "USD",
  "revenueStream": "recurring",
  "clientId": "client_123"
}
```

Output: allocation plan with operations, payroll, tax, emergency reserve, growth, profit, and acquisition buckets.

### `approve_expense`

Input:

```json
{
  "expenseId": "exp_123",
  "amountMinor": 125000,
  "currency": "USD",
  "category": "software",
  "description": "Automation platform",
  "requestedBy": "ops_lead",
  "departmentId": "delivery",
  "budgetRemainingMinor": 500000
}
```

Output: approval request, required approver role, status, and reason.

### `detect_financial_risk`

Input:

```json
{ "entityId": "agency-main", "debtServiceCoverageRatio": 1.1 }
```

Output: risk signals with severity, threshold, current value, and recommended actions.

### `calculate_client_profitability`

Input:

```json
{
  "clientId": "client_123",
  "revenueMinor": 5000000,
  "deliveryCostMinor": 2500000,
  "acquisitionCostMinor": 800000,
  "averageMonthlyRevenueMinor": 1000000,
  "currency": "USD"
}
```

Output: gross margin, contribution margin, LTV:CAC, CAC payback, and risk flags.

### `generate_financial_report`

Input:

```json
{
  "reportType": "ceo",
  "periodStart": "2026-05-01",
  "periodEnd": "2026-05-31"
}
```

Output: KPI set, risk set, recommended decisions, and narrative.

### `analyze_runway`

Output: runway days, status, and recommended liquidity actions.

### `monitor_liquidity`

Output: cash position, risk count, critical risks, and next review cadence.

### `evaluate_growth_capacity`

Input:

```json
{
  "minimumRunwayDays": 180,
  "minimumGrossMarginPct": 40,
  "forecastAccuracyPct": 85
}
```

Output: growth gate result and failed/passed conditions.

## HTTP Routes

- `GET /health`
- `GET /cash-position`
- `POST /forecast-cashflow`
- `POST /allocate-capital`
- `POST /approve-expense`
- `POST /detect-risk`
- `POST /client-profitability`
- `POST /financial-report`

Production HTTP deployment must add authentication, authorization, idempotency keys, request signing for webhooks, and OpenTelemetry trace propagation.
