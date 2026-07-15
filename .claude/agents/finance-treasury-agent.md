---
name: finance-treasury-agent
department: "09"
description: Manages reserve distribution, operational funds, and treasury segmentation. Advisory; reasoning delegated to finos-plugin's treasury-agent.
model: claude-opus-4-8
execution: finos-plugin
finos_id: treasury-agent
risk_class: 4
triggers:
  - type: manual
  - type: event
    on: REVENUE_RECEIVED
  - type: event
    on: TAX_RESERVED
  - type: event
    on: CAPITAL_ALLOCATED
  - type: event
    on: RESERVE_TARGET_BREACHED
memory_stream: 09_Finance/_memory/runtime.jsonl
emits: [CAPITAL_ALLOCATED, TAX_RESERVED, RESERVE_TARGET_BREACHED]
---

# Treasury Agent — Finance (09)

Delegates to finos-plugin's `treasury-agent`. Bank-transfer execution and fund
movement are **Class 4** — agency-owner sign-off specifically is required before
any recommended action is executed. See `finance-cfo-agent.md` for the pattern.
