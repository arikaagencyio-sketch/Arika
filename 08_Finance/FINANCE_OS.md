# Finance — Department OS

**Department:** Finance (08)
**Position in flow:** Receives billable events/delivery output from Operations (07); reports roll up to Agency Governance (00).
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

**Yes — but code-based, not markdown.** `08_Finance/finos-plugin/` is a TypeScript application scaffold: `src/` with 19 sub-engine folders (ai-agents, cashflow-engine, compliance-engine, core-ledger, forecasting-engine, risk-engine, treasury-system, etc., mostly one stub `.ts` file each), `docs/` (11 markdown design docs), `database/` (1 SQL file), `tests/` (1 file), and a `.codex-plugin/` config. Its own documentation states it was "derived from the Word drafts in the parent workspace." **Open question (not resolved in this pass, tracked in `GLOBAL_OS.md` §11):** whether this stays a code-backed exception to the markdown-first standard, or gets reduced to a markdown spec with a thin code wrapper.

## 14. Raw Archive Pointer

~16 root-level "Draft N.md" files. Existing gap backlog: `08_Finance/00_Workspace_Intelligence_Inventory/`. Migration into the registries above, and reconciliation with `finos-plugin/docs/`, is deferred to a future session.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring. — Claude Code (Sonnet 4.6)
