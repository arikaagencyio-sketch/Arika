# Deployment

## Local Development

```bash
npm install
docker compose up -d
npm run dev:mcp
```

HTTP mode:

```bash
npm run dev:http
```

## Production Topology

- FinOS API/MCP service on Node.js.
- PostgreSQL for relational state, ledger, event store, forecasts, approvals, risk, and audit.
- NATS or Kafka for high-throughput event streaming.
- Redis for workflow queues and cache.
- Object storage for invoices, receipts, contracts, payroll evidence, and audit support files.
- OpenTelemetry collector and metrics/log stack.

## Environment Variables

- `FINOS_DATABASE_URL`
- `FINOS_EVENT_STORE`
- `FINOS_MCP_TRANSPORT`
- `FINOS_HTTP_HOST`
- `FINOS_HTTP_PORT`
- `FINOS_JWT_ISSUER`
- `FINOS_AUDIT_HASH_SECRET`

## Release Gates

Before production:

1. Ledger balance tests pass.
2. Event replay produces the same financial state.
3. Allocation rules total no more than 100%.
4. Approval thresholds are entity-specific and reviewed.
5. Tax reserve rates are jurisdiction-specific and reviewed by a qualified professional.
6. Banking/payment integrations use idempotency keys.
7. Audit hash-chain verification is enabled.
8. Runway, DSCR, margin, concentration, and reserve breach alerts route to humans.
