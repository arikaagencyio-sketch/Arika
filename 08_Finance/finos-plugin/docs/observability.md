# Observability

FinOS observability must show both technical health and financial health.

## Technical Signals

- Event ingestion rate, failure rate, and processing latency.
- Ledger posting success/failure rate.
- MCP tool latency and error rate.
- Database query latency.
- Workflow execution latency and retries.
- Integration sync freshness.
- Audit hash-chain verification status.

## Financial Signals

- Cash position freshness.
- 13-week forecast freshness.
- Risk signal count by severity.
- Reserve target breach count.
- Approval backlog by role.
- Budget threshold breach count.
- Unreconciled transaction count.
- Forecast variance by period.

## Recommended Stack

- OpenTelemetry for traces and metrics.
- Prometheus for metrics.
- Grafana for dashboards.
- Loki or equivalent for logs.
- Alertmanager/PagerDuty/Opsgenie for critical liquidity and system alerts.

## Critical Alerts

- `LOW_RUNWAY_ALERT` critical when runway is below 60 days.
- `CASHFLOW_WARNING` warning when 13-week closing cash trends negative.
- `RESERVE_TARGET_BREACHED` warning when emergency, tax, or payroll reserves are below policy.
- `LEDGER_POSTING_FAILED` critical when an event cannot be reconciled.
- `AUDIT_CHAIN_INVALID` critical when audit hashes fail verification.
- `INTEGRATION_STALE` warning when banking/payment data is older than policy.
