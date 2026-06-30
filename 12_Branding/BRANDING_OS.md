# Branding — Department OS

**Department:** Branding (12)
**Position in flow:** Horizontal support layer — feeds Marketing, Sales, Client Success, and Agency Governance with brand architecture, narrative, and identity systems.
**Mandate:** Own brand definition, positioning, narrative engineering, and visual/identity systems for the agency and (as a service) for clients.
**Owner:** *(unassigned — placeholder)*

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Branding defines and governs how the agency (and client brands it manages) present themselves — architecture, narrative, positioning, visual cognition, cultural intelligence.

## 2. Status

Has a **partially-real code build** (`bois/`, Python — see §13). A sibling dead duplicate (`branding-os/`, an empty TypeScript-style scaffold with only a README) was deleted during this restructuring's cleanup phase. Registries below are structural placeholders.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| *(placeholder — `bois/core/` working modules suggest: governance, grading, ingestion, knowledge, memory, orchestration, presentation, retrieval — to be confirmed against actual content)* | | |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 5. Agent Roster

*(placeholder — `bois/agents/` exists as a folder; maturity unconfirmed, reconcile during content migration)*

## 6. Skill Library Index

*(placeholder)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder)* | | | | | |

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

`bois/documentation/COGNITIVE_INFRASTRUCTURE_ARCHITECTURE.md` exists and documents the `bois/` subsystem's intended architecture — worth reviewing as input when this section is built out.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

*(placeholder — structure only)*

## 13. Existing OS Sub-Layer

**Partially — code-based, not markdown.** `11_Branding/bois/` ("Brand Operating Intelligence System") is a Python application: 44 subfolders total, most empty scaffolds, but `core/` contains genuinely working code (21 `.py` files covering governance, grading, ingestion, knowledge, memory, orchestration, presentation, retrieval). `__pycache__/` directories under it were removed during cleanup. Its sibling `branding-os/` (a same-concept scaffold in a different naming/language convention) was confirmed dead — only a README, 18 fully empty subfolders — and was **deleted** during this restructuring.

**Decision (2026-06-30):** same resolution as Finance's `finos-plugin` (see `09_Finance/FINANCE_OS.md` §13) — `bois/` is **retained as a grandfathered code-backed exception**, not converted or deleted. `bois/documentation/COGNITIVE_INFRASTRUCTURE_ARCHITECTURE.md` remains the canonical spec for what the working `core/` code does; this department's registry sections above should be populated from that document during the future content-migration pass where it overlaps with raw drafts. If `bois/` development stalls for an extended period, downgrade it to a markdown-only spec library rather than carrying unmaintained code indefinitely — deferred until there's signal either way.

## 14. Raw Archive Pointer

~40 root-level "Draft N.md" files. Existing gap backlog: `12_Branding/00_Workspace_Intelligence_Inventory/`. Migration into the registries above, and reconciliation with `bois/documentation/`, is deferred to a future session.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring; dead `branding-os/` duplicate and `bois/` `__pycache__` directories removed in cleanup. — Claude Code (Sonnet 4.6)
