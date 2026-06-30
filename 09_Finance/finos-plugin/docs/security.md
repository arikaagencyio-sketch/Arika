# Security And Governance

FinOS handles sensitive financial data and must be deployed with institutional controls.

## Access Control

- Use RBAC with roles for founder, CEO, CFO, controller, treasury, operations lead, department owner, accountant, auditor, and read-only investor.
- Apply least privilege by entity, department, ledger account, integration, and report type.
- Enforce separation of duties: no single actor should authorize, execute payment, reconcile, and report the same transaction.

## Authentication

- MCP and HTTP deployments must require authenticated access outside local development.
- HTTP APIs should use JWT or mTLS.
- Webhook sources must use signature verification and replay protection.

## Data Protection

- Encrypt data in transit with TLS.
- Encrypt secrets with a managed secret store.
- Encrypt sensitive fields and evidence documents at rest.
- Store only tokenized external account identifiers where possible.

## Auditability

- Write append-only audit logs for approvals, ledger posts, allocation overrides, report generation, integration changes, and policy changes.
- Chain audit records with hashes.
- Corrections should be compensating events, not destructive edits.

## Financial Integrity

- All journal entries must balance.
- Restricted cash must be tracked separately from unrestricted cash.
- Tax and payroll reserves are not available for discretionary allocation.
- Approval policy changes require audit records and appropriate authority.
