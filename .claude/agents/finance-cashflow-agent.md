---
name: finance-cashflow-agent
department: "09"
description: Liquidity, inflows/outflows, burn, runway, receivables and payables monitoring. Advisory; reasoning delegated to finos-plugin's cashflow-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: cashflow-agent
risk_class: 3
triggers:
  - type: manual
  - type: event
    on: REVENUE_RECEIVED
  - type: event
    on: EXPENSE_APPROVED
  - type: event
    on: PAYROLL_EXECUTED
  - type: event
    on: CASHFLOW_WARNING
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [CASHFLOW_WARNING, LOW_RUNWAY_ALERT, LIQUIDITY_POSITION_UPDATED]
---

# Cashflow Agent — Finance (09)

Delegates to finos-plugin's `cashflow-agent`. This file registers the agent in the
unified runtime, declares its event triggers, and carries its Class 3 risk. See
`finance-cfo-agent.md` for the delegation pattern.
