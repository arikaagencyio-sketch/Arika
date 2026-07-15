---
name: finance-risk-agent
department: "09"
description: Detects instability, margin collapse, overspending, debt pressure, and concentration risk. Advisory; reasoning delegated to finos-plugin's risk-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: risk-agent
risk_class: 3
triggers:
  - type: manual
  - type: event
    on: LOW_RUNWAY_ALERT
  - type: event
    on: MARGIN_DROP_DETECTED
  - type: event
    on: BUDGET_THRESHOLD_EXCEEDED
  - type: event
    on: CLIENT_PROFITABILITY_UPDATED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [RISK_ESCALATED, RESERVE_TARGET_BREACHED, BUDGET_THRESHOLD_EXCEEDED]
---

# Risk Agent — Finance (09)

Delegates to finos-plugin's `risk-agent`. Registered in the unified runtime with
event triggers and Class 3 risk. See `finance-cfo-agent.md` for the pattern.
