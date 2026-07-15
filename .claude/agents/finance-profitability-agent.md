---
name: finance-profitability-agent
department: "09"
description: Analyzes client, service, campaign, and department profitability and unit economics. Advisory; reasoning delegated to finos-plugin's profitability-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: profitability-agent
risk_class: 3
triggers:
  - type: manual
  - type: event
    on: REVENUE_RECEIVED
  - type: event
    on: EXPENSE_APPROVED
  - type: event
    on: CLIENT_PROFITABILITY_UPDATED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [CLIENT_PROFITABILITY_UPDATED, MARGIN_DROP_DETECTED]
---

# Profitability Agent — Finance (09)

Delegates to finos-plugin's `profitability-agent`. Registered in the unified
runtime with event triggers and Class 3 risk. See `finance-cfo-agent.md`.
