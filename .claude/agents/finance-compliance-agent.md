---
name: finance-compliance-agent
department: "09"
description: Maintains tax reserves, audit readiness, documentation integrity, and approval traceability. Advisory; reasoning delegated to finos-plugin's compliance-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: compliance-agent
risk_class: 4
triggers:
  - type: manual
  - type: event
    on: REVENUE_RECEIVED
  - type: event
    on: EXPENSE_APPROVED
  - type: event
    on: PAYROLL_EXECUTED
  - type: event
    on: TAX_RESERVED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [TAX_RESERVED, RISK_ESCALATED, AUDIT_TRAIL_RECORDED]
---

# Compliance Agent — Finance (09)

Delegates to finos-plugin's `compliance-agent`. Tax filing and entity-structure
representations are **Class 4** — agency-owner sign-off specifically is required.
See `finance-cfo-agent.md` for the delegation pattern.
