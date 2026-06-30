# Global Operating System — The Agency

**Version:** v0.1-skeleton
**Last updated:** 2026-06-30
**Status:** Structural skeleton complete. Department content is largely unmigrated raw drafts. See §9.

---

## 1. Identity

This repository is the Agency's own command center — the operating system the agency runs itself on, and the pattern it can extend to run client businesses. It is not a deliverable; it is the agency's internal nervous system: strategy, governance, knowledge, and (progressively) the agents/workflows that execute daily operations.

**Mission (placeholder — confirm with owner):** Operate as an AI-native agency that runs its own departments and client engagements through documented, repeatable, auditable systems rather than ad hoc effort.

**What this repo is NOT:** a client deliverable, a finished strategy document, or a fully built automation platform. As of v0.1 it is the *structure* the agency's real source-of-truth content gets poured into — deliberately built before that content, per the agency's own stated principle of "preparing the room before adding the source of truth."

---

## 2. How to Use This Repo

This section is the anti-hallucination contract. Any reader — human or AI agent, on any platform — should follow this order:

1. **Read this file (`GLOBAL_OS.md`) first.** It is the single global root. `CLAUDE.md` and `AGENTS.md` are thin pointers into this file — they carry no independent authority.
2. **Read the relevant department's `{DEPT}_OS.md`** for the department your task touches (see Department Index, §4). Each department file is the local source of truth for that department's capabilities, workflows, agents, KPIs, decisions, and risks.
3. **Only then consult the raw archive** (the loose `Draft N.md` files still living in each department folder) — and only via the specific pointers the department's `{DEPT}_OS.md` gives you. Do not free-associate across the 350+ raw drafts directly; they are unedited, unstructured brainstorm exports and have not been verified, deduplicated, or fact-checked against real agency data.
4. **When you complete meaningful work**, log it in the relevant department's Decision Log or Changelog (§15 of the department template) rather than only stating it in conversation — this is how the system avoids re-deriving or contradicting itself across sessions.
5. **If something is missing or contradictory**, flag it rather than guessing. Open Gaps are tracked explicitly in §11 below and per-department.

This applies identically whether you are a human, Claude Code, Claude Chat/Projects, a Claude Code worker, or another agent platform (e.g. Codex via `AGENTS.md`).

---

## 3. Operating Constitution (Summary)

Full version: `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` (**not yet written — placeholder, tracked as an open gap in §11**).

Until that file exists, these load-bearing rules apply by default:

- **No silent invention.** When source material is missing, say so — don't fabricate agency-specific facts (numbers, client names, pricing, legal terms).
- **Department ownership is local.** Each department's `{DEPT}_OS.md` is authoritative for that department; the global file does not duplicate department-level detail, only indexes and connects it.
- **Structure before content.** This v0.1 pass deliberately leaves most registries empty/placeholder. Do not backfill them with guessed values — backfill requires real agency data or an explicit content-migration pass.
- **Human sign-off required** for anything touching real client commitments, contracts, money movement, or public-facing claims, until a formal risk-class/approval matrix exists (tracked in §11).

---

## 4. Department Index / Map

| # | Department | Path | Mandate | Owner | OS File |
|---|---|---|---|---|---|
| 00 | Agency Governance | `00_Agency_Governance/` | Cross-cutting governance, prior gap-analysis archive | *(unassigned)* | — *(governance layer, no department OS file; see §11)* |
| 01 | Sector | `01_Sector/` | Upstream market/industry intelligence — determines "truth" the rest of the agency packages and sells | *(unassigned)* | [`01_Sector/SECTOR_OS.md`](01_Sector/SECTOR_OS.md) |
| 02 | Offer | `02_Offer/` | Offer design, packaging, pricing architecture | *(unassigned)* | [`02_Offer/OFFER_OS.md`](02_Offer/OFFER_OS.md) |
| 03 | Marketing | `03_Marketing/` | Demand generation, content, positioning, channel strategy (includes `360_Agency_Content/` sub-area) | *(unassigned)* | [`03_Marketing/MARKETING_OS.md`](03_Marketing/MARKETING_OS.md) |
| 04 | Sales | `04_Sales/` | Pipeline, conversion, deal execution | *(unassigned)* | [`04_Sales/SALES_OS.md`](04_Sales/SALES_OS.md) |
| 05 | ClientPartner Acquisition | `05_ClientPartner_Acquisition/` | Referral/partner-channel client acquisition (distinct from direct Sales) | *(unassigned)* | [`05_ClientPartner_Acquisition/CLIENTPARTNER_OS.md`](05_ClientPartner_Acquisition/CLIENTPARTNER_OS.md) |
| 06 | Client Success | `06_Client_Success/` | Post-sale client lifecycle: onboarding, journey, retention, health | *(unassigned)* | [`06_Client_Success/CLIENTSUCCESS_OS.md`](06_Client_Success/CLIENTSUCCESS_OS.md) |
| 07 | Operations | `07_Operations/` | Delivery execution, SOPs, capacity, quality control *(new department — confirmed gap)* | *(unassigned)* | [`07_Operations/OPERATIONS_OS.md`](07_Operations/OPERATIONS_OS.md) |
| 08 | Finance | `08_Finance/` | Accounting, cash flow, treasury, forecasting | *(unassigned)* | [`08_Finance/FINANCE_OS.md`](08_Finance/FINANCE_OS.md) |
| 09 | Legal | `09_Legal/` | Contracts, compliance, IP, risk *(new department — confirmed gap, was a phantom workspace in the old completion engine)* | *(unassigned)* | [`09_Legal/LEGAL_OS.md`](09_Legal/LEGAL_OS.md) |
| 10 | HR / People Ops | `10_HR_People_Ops/` | Hiring, onboarding (internal), capacity/utilization *(new department — confirmed gap)* | *(unassigned)* | [`10_HR_People_Ops/HR_OS.md`](10_HR_People_Ops/HR_OS.md) |
| 11 | Branding | `11_Branding/` | Brand architecture, narrative, identity systems | *(unassigned)* | [`11_Branding/BRANDING_OS.md`](11_Branding/BRANDING_OS.md) |
| 12 | Tech Stack | `12_Tech_Stack/` | Tooling/software inventory used across the agency *(new department — confirmed gap)* | *(unassigned)* | [`12_Tech_Stack/TECHSTACK_OS.md`](12_Tech_Stack/TECHSTACK_OS.md) |
| 13 | Cross-Domain Synthesis | `13_Cross_Domain_Synthesis/` | NOT an active department — early whole-agency synthesis draft, kept as historical/reference material (likely origin document for this restructuring; see `AgencyOs Cognitive Framework. Draft 1.md`) | — | — *(reference archive, no OS file)* |

Numbering encodes the agency's own previously-documented operating flow (see §5) directly into the filesystem.

---

## 5. Cross-Department Operating Flow

Primary flow (inherited from the agency's own prior self-analysis in `00_Agency_Governance/_archive_2026-06-03_completion_index/00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md`):

```
Sector → Offer → Marketing → Sales → Client Success → Operations → Finance → (Management/Governance)
```

Support layers running horizontally across all of the above: **Branding** (supports Marketing, Sales, Client Success, Governance), **ClientPartner Acquisition** (feeds Sales and distribution, parallel to Marketing-driven demand), **Legal**, **HR/People Ops**, **Tech Stack**, and **Agency Governance** (governs all layers).

**Worked example — new client onboarding** (illustrative; workflow not yet built):
1. Marketing or ClientPartner Acquisition generates a qualified opportunity → handoff to `04_Sales/`
2. Sales closes the deal → handoff to `06_Client_Success/` for onboarding
3. Client Success defines scope/expectations → handoff to `07_Operations/` for delivery
4. Operations executes → generates billable events → handoff to `08_Finance/`
5. Finance invoices and tracks revenue → reports roll up to Agency Governance

**Worked example — new capability/offer launch**:
1. `01_Sector/` identifies a market opportunity
2. `02_Offer/` packages it into a sellable offer with pricing
3. `03_Marketing/` builds demand-generation content for it
4. `04_Sales/` and `05_ClientPartner_Acquisition/` sell it

Neither workflow is implemented as an executable automation yet — both are documented here as the intended shape, to be built out in each department's Workflow Index (§4 of the department template).

---

## 6. Curated Registry Index

Rather than maintaining 41 separate top-level registries (see `REGISTRY_TAXONOMY_REFERENCE.md` for the full future-state ontology), this v0.1 skeleton embeds a curated subset of the most operationally load-bearing registries as **standard sections inside every department's `{DEPT}_OS.md`**:

| Registry | Lives as department section | Cross-department rollup |
|---|---|---|
| Capability | §3 Capability Registry | *(none yet — would live in Agency Governance)* |
| Workflow | §4 Workflow Index | *(none yet)* |
| Agent | §5 Agent Roster | *(none yet)* |
| Skill | §6 Skill Library Index | *(none yet)* |
| KPI/Metrics | §7 KPI Dictionary (department-local) | *(none yet — agency-wide KPI dictionary is an open gap, §11)* |
| Decision | §8 Decision Log | *(none yet)* |
| Risk/Incident | §9 Risk/Incident Log | *(none yet)* |
| Standards | §10 Standards & SOPs Index | *(none yet)* |
| Governance/RACI | §11 RACI/Ownership | *(none yet — agency-wide RACI is an open gap, §11 below)* |
| Trigger/Automation | §12 Triggers/Automation Hooks | *(none yet)* |
| Knowledge | §14 Raw Archive Pointer | *(none yet)* |

A department-local registry section being empty/placeholder is expected at v0.1 — it means "structure exists, content pending," not "doesn't apply." Cross-department rollups (a true agency-wide Capability Registry, KPI Dictionary, etc.) are listed as open gaps in §11 and are deliberately deferred until department-local content is real.

---

## 7. Command Center Overview

The agency operates on a **Plugin = Department** model: each department is treated as a self-contained capability module with its own identity, knowledge base, tools, workflows, memory, communication protocols, permissions, and triggers — conceptually equivalent to a traditional business department, but built to be operated by AI agents as much as by people.

Concrete agents, skills, and workflows are NOT all built today — they are built progressively, per department, as real operational need and real source content justify them. Two departments already have a head start, built independently before this restructuring:

- **Sales** (`04_Sales/06_AI_OPERATIONS/`) — the most mature example in the repo: system prompts, an Agent Registry, a Skill Library, a Task Routing Matrix, Escalation Rules, AI Memory Logs (Decision/Learning/Prompt-Evolution), and Runtime Examples, with source-paragraph citation lineage back to the raw drafts. **This is the reference pattern** other departments should normalize toward as they mature.
- **Marketing** (`03_Marketing/Elite_Marketing_Agentic_OS/`) — a markdown-only agent-card catalog: master architecture doc, an agent catalog YAML, 11 individual Agent Cards, skill/workflow rulebooks, and a 30/60/90 rollout plan.

Finance (`08_Finance/finos-plugin/`) and Branding (`11_Branding/bois/`) each built code-based scaffolds instead of markdown — flagged as exceptions to the markdown-first standard; whether they get reduced to markdown specs with thin code wrappers, or kept as code-backed exceptions, is an open design question (§11 below), not resolved in this pass.

---

## 8. Platform Entry Points

- **`/CLAUDE.md`** — thin pointer for Claude Code. Points here, then to department OS files. No department logic lives in it.
- **`/AGENTS.md`** — thin pointer for other agent platforms (Codex and similar conventions). Same content as `CLAUDE.md`, platform-neutral wording.
- Either file could be deleted without breaking navigation — `GLOBAL_OS.md` is the real root, not a Claude-specific artifact. This is the concrete realization of the agency's platform-neutrality requirement: the system must work from Claude Chat, Claude Code, Claude Code workers, or any other LLM agent that can read markdown.

---

## 9. Raw Archive & Content Migration Status

**As of v0.1, the overwhelming majority of this repo's actual content (~350+ files) is unmigrated.** Each department folder still contains its original "Draft N.md" files — raw, unedited exports of prior brainstorming conversations — loose at the folder root, alongside the new `{DEPT}_OS.md` skeleton file. These drafts are conceptually rich but largely generic (agency-relevant theory, not filled-in agency-specific numbers/clients/pricing) and have not been deduplicated, fact-checked, or structured.

Each department also retains its pre-existing `00_Workspace_Intelligence_Inventory/` subfolder (auto-generated by a prior pass — see `09_HR...` no, see `agency_workspace_completion_engine.py` at repo root) containing a gap-resolution backlog specific to that department. These are the starting input for the future content-migration pass, not yet acted upon.

**Content migration — turning raw drafts into populated registries — is explicitly deferred to a future session.** Treat any department's registry sections as structurally complete but substantively empty until that pass happens.

---

## 10. Versioning / Changelog

Simple convention: bump the version header (§ top of this file) on structural changes (new departments, renamed registries, changed flow). Log entries below, newest first.

### Changelog

- **2026-06-30 — v0.1-skeleton** — Initial restructuring: renamed 9 existing department folders to numbered names reflecting the agency's operating flow, created 4 new department folders for confirmed gaps (Operations, Legal, HR/People Ops, Tech Stack), merged `360 Agency Content` into Marketing, archived two redundant auto-generated extraction passes, deleted confirmed-dead folders (`branding-os`, orphaned empty `Marketing Drafts` nested in Sales, `__pycache__` dirs) and one confirmed exact-duplicate file. Wrote this global MD, all 12 department OS files, and platform-agnostic entry points. First git commit. — Claude Code (Sonnet 4.6)

---

## 11. Open Gaps / Known Incomplete Areas

Inherited from the agency's own prior self-analysis (`00_Agency_Governance/_archive_2026-06-03_completion_index/00_MASTER_ARCHITECTURAL_COMPLETION_INDEX.md`, "Required Agency-Wide Closure Systems"), marked against what this v0.1 pass closes vs. leaves open:

| # | System | Status after v0.1 |
|---|---|---|
| 1 | Agency Global Source Registry (source IDs, active/superseded/archive state, owners, cadence) | **Open** — structure for this would live in Agency Governance; not built |
| 2 | Agency Operating Constitution (amendment process, decision rights, risk classes) | **Partially open** — summary stub exists in §3 above; full document not written |
| 3 | Cross-domain RACI | **Open** — each department has an empty RACI placeholder (§11 of its template); no agency-wide rollup |
| 4 | CRM schema connecting Marketing → Sales → Client → Finance | **Open** — not addressed in this pass |
| 5 | KPI dictionary (formula, source, owner, cadence, threshold) | **Open** — each department has an empty placeholder; no agency-wide dictionary |
| 6 | Handoff packet standards between departments | **Partially open** — §5 above sketches the flow narratively; no formal handoff packet spec |
| 7 | Automation approval matrix (trigger, action, risk class, rollback, human gate) | **Open** — each department has an empty Triggers/Automation placeholder; no agency-wide matrix |
| 8 | Memory protocol (historical, operational, decision, execution, learning) | **Partially open** — Decision Log / Changelog patterns exist per department; no unified memory protocol doc |
| 9 | Dashboard spine | **Open** — not addressed in this pass |
| 10 | Versioning/change protocol | **Closed (lightweight)** — see §10 above; sufficient for current volume, may need to formalize later |

**Additional open items surfaced during this restructuring:**
- Department owners are all placeholders — needs real names assigned.
- Finance (`finos-plugin`, TypeScript) and Branding (`bois`, Python) are code-based exceptions to the markdown-first standard — decision on whether to keep, reduce, or replace is deferred.
- `agency_intelligence_extractor.py` and `agency_workspace_completion_engine.py` (repo root) need a rewrite before being re-run: hardcoded dates/paths, a phantom "Legal Drafts" workspace reference that predates this restructuring, and keyword/regex-only classification with no LLM involved.
- Five similarly-titled files in `05_ClientPartner_Acquisition/` need a content-diff pass to confirm/resolve near-duplicates (not done in this pass — see that department's Raw Archive Pointer section).
- `.claude/settings.local.json` still references a now-removed `docx_to_md.py` scratchpad script — harmless but stale, not pruned in this pass.
