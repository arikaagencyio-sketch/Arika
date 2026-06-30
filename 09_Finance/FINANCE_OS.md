# Finance — Department OS

**Department:** Finance (09)
**Position in flow:** Receives billable events/delivery output from Operations (08); reports roll up to Agency Governance (00).
**Mandate:** Own accounting, cash flow, treasury, forecasting, and financial compliance for the agency.
**Owner:** *(unassigned — placeholder)*

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Finance accounts for and forecasts the agency's money — revenue, costs, margins, cash flow, treasury, tax compliance.

## 2. Status

Has an independently-built **code scaffold** (`finos-plugin/`, TypeScript), structurally complete (19 engine folders) but unimplemented at the logic level (mostly 1 stub file per engine). This is flagged as an exception to the markdown-first standard the rest of this restructuring uses (see §13 and the open-gap note in `GLOBAL_OS.md` §11) — not resolved in this pass. Registries below are structural placeholders.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| *(placeholder — `finos-plugin` engine folder names suggest: ledger, cashflow, treasury, forecasting, risk, compliance, allocation — to be confirmed against actual content)* | | |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 5. Agent Roster

*(placeholder — `finos-plugin/src/ai-agents/` exists as a folder but content maturity unconfirmed; reconcile during content migration)*

## 6. Skill Library Index

*(placeholder)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder)* | | | | | |

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty; `finos-plugin/src/risk-engine/` and `compliance-engine/` exist as folders but are unconfirmed/stub-level)*

## 10. Standards & SOPs Index

`finos-plugin/docs/` has 11 markdown files documenting the code scaffold's intended design — worth reviewing as input when this section is built out.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

*(placeholder — structure only)*

## 13. Existing OS Sub-Layer

**Yes — but code-based, not markdown.** `09_Finance/finos-plugin/` is a TypeScript application scaffold: `src/` with 19 sub-engine folders (ai-agents, cashflow-engine, compliance-engine, core-ledger, forecasting-engine, risk-engine, treasury-system, etc., mostly one stub `.ts` file each), `docs/` (11 markdown design docs), `database/` (1 SQL file), `tests/` (1 file), and a `.codex-plugin/` config. Its own documentation states it was "derived from the Word drafts in the parent workspace."

**Decision (2026-06-30):** `finos-plugin/` is **retained as a grandfathered code-backed exception**, not converted or deleted. Rationale: it represents real prior implementation effort and the markdown-first standard governs how *new* department capability gets specified, not a mandate to retroactively gut working code. Going forward: `finos-plugin/docs/` remains the canonical description of what the code does (code is the implementation, docs are the spec — not the reverse); this department's KPI Dictionary, Capability Registry, and Standards sections (above) should be populated from `finos-plugin/docs/` during the future content-migration pass rather than re-derived from the raw "Draft N.md" files where they overlap. If `finos-plugin` development stalls for an extended period, downgrade it to a markdown-only spec library (preserving the docs, archiving the unfinished code) rather than carrying an unmaintained half-built app indefinitely — that decision is deferred until there's signal either way.

## 14. Raw Archive Pointer

~16 root-level "Draft N.md" files. Existing gap backlog: `09_Finance/00_Workspace_Intelligence_Inventory/`. Migration into the registries above, and reconciliation with `finos-plugin/docs/`, is deferred to a future session.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring. — Claude Code (Sonnet 4.6)
