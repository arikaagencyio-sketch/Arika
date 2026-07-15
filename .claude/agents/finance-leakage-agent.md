---
name: finance-leakage-agent
department: "09"
description: Detects duplicate expenses, unnecessary subscriptions, anomalies, and operational waste. Advisory; reasoning delegated to finos-plugin's leakage-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: leakage-agent
risk_class: 3
triggers:
  - type: manual
  - type: event
    on: EXPENSE_SUBMITTED
  - type: event
    on: EXPENSE_APPROVED
  - type: event
    on: BUDGET_THRESHOLD_EXCEEDED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [BUDGET_THRESHOLD_EXCEEDED, RISK_ESCALATED]
---

# Leakage Detection Agent — Finance (09)

Delegates to finos-plugin's `leakage-agent`. Registered in the unified runtime
with event triggers and Class 3 risk. See `finance-cfo-agent.md`.
