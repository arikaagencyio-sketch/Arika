# Sales — Department OS

**Department:** Sales (04)
**Position in flow:** Receives qualified demand from Marketing (03) and ClientPartner Acquisition (05); converts to closed deals; hands off to Client Success (06).
**Mandate:** Own pipeline, conversion, deal execution, and the agency's sales-side AI operations.
**Owner:** *(unassigned — placeholder)*

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Sales is responsible for converting qualified opportunities (from Marketing and ClientPartner Acquisition) into signed, paying clients, and handing them off cleanly to Client Success.

## 2. Status

**Most mature department in the repo.** Has a real, independently-built AI operations sub-layer (§13 below) that should serve as the reference pattern for other departments as they mature. Registry sections below (Capability, Workflow, KPI, etc.) are still structural placeholders pending a formal content-migration pass that reconciles this template against the existing `06_AI_OPERATIONS/` content — they are not yet filled in, even though real source material to fill them from already exists in this department (unlike most others).

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| *(placeholder — to be populated from `06_AI_OPERATIONS/Skill_Library.md` and raw drafts)* | | |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| *(placeholder — likely source: `06_AI_OPERATIONS/04_Routing/Task_Routing_Matrix.md`)* | | | | |

## 5. Agent Roster

See existing `06_AI_OPERATIONS/02_Agent_Roles/Agent_Registry.md` — do not duplicate here; this section will link to specific agents once the registry is reconciled with this template.

## 6. Skill Library Index

See existing `06_AI_OPERATIONS/03_Skills/Skill_Library.md` — same treatment as above.

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder)* | | | | | |

## 8. Decision Log

Live decision log already exists: `06_AI_OPERATIONS/06_AI_Memory_Logs/Decision_Log.md` — use that file going forward rather than duplicating entries here.

## 9. Risk / Incident Log

*(placeholder — none logged yet in this template; check `06_AI_OPERATIONS/05_Escalations_Approvals/Escalation_Rules.md` for related existing content)*

## 10. Standards & SOPs Index

*(placeholder)*

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

*(placeholder — structure only; see `06_AI_OPERATIONS/04_Routing/Task_Routing_Matrix.md` for existing related content to reconcile against)*

## 13. Existing OS Sub-Layer

**Yes — most mature in the repo.** `04_Sales/06_AI_OPERATIONS/` contains:
- `00_Index/` — AI Operations Index, Source Agent Mention Registry, Build Summary, Human Operator Guide
- `01_System_Prompts/` — Master AI Operating Constitution, Agent Runtime Template, Multi-Agent Handoff Template
- `02_Agent_Roles/Agent_Registry.md`
- `03_Skills/Skill_Library.md`
- `04_Routing/Task_Routing_Matrix.md`
- `05_Escalations_Approvals/Escalation_Rules.md`
- `06_AI_Memory_Logs/` — Decision Log, Prompt Evolution Log, Learning Loop Log
- `07_Runtime_Examples/` — Daily Sales Command Run, Client Sales System Build Run, Pipeline Build Runbook

This sub-layer also has its own source-citation lineage (`Master_Source_Registry.csv`, `Master_Source_Paragraph_Index.csv`) mapping synthesized claims back to specific source paragraphs — the strongest anti-hallucination pattern anywhere in this repo. **Recommend other departments adopt this citation pattern once they reach a similar maturity stage.**

## 14. Raw Archive Pointer

~68 root-level "Draft N.md" files plus 2 CSVs and a `.ps1` script live loose at `04_Sales/`. Existing gap backlog: `04_Sales/00_Workspace_Intelligence_Inventory/`. Migration into the registries above is deferred to a future session.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring. — Claude Code (Sonnet 4.6)
