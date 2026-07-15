---
name: finance-cfo-agent
department: "09"
description: Strategic CFO — capital allocation, scaling strategy, runway, and institutional readiness. Advisory; reasoning delegated to finos-plugin's cfo-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: cfo-agent
risk_class: 3
triggers:
  - type: manual
  - type: event
    on: REVENUE_RECEIVED
  - type: event
    on: LOW_RUNWAY_ALERT
  - type: event
    on: GROWTH_CAPACITY_EVALUATED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [GROWTH_CAPACITY_EVALUATED, RISK_ESCALATED, FINANCIAL_REPORT_GENERATED]
---

# CFO Agent — Finance (09)

Delegates to finos-plugin's `cfo-agent` (`09_Finance/finos-plugin/src/ai-agents/index.ts`).
The runtime dynamic-imports finos's built `dist/` and runs it through finos's own
`ClaudeAgentRuntime`; this file exists so the agent is visible to the unified
registry, declares its triggers, and carries its Constitution risk class.
Capital/strategy actions are Class 3 — human sign-off required before any
recommended action is executed.
