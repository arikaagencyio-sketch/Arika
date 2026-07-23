# AEIT_04 — Architectural Gap & Duplication Report (Analysis)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Status:** Findings register. Every finding cites a real `file:line` or `file §section`. Severity is
**architectural** (impact on long-term coherence), annotated with current operational impact where
it differs (often "low in fact, high in principle" — a solo, 0-client business).

> This is the reconcile-first heart of Phase Zero. Coherence findings feed **AEIT_05**
> (reconciliation decisions); activation/build findings feed **AEIT_10** (roadmap). Nothing here is
> fixed in Phase Zero — findings are *proposed* resolutions pending Owner ratification.

Severity key: 🔴 High · 🟠 Medium · 🟡 Low-but-structural.

---

## Category A — Ownership contradictions & duplication

### A1 🟠 ICP / prospect scoring — one capability, four claimants, one contradicted field
- **Evidence:** Sector (01) classifies ICP and runs the 90-pt scorecard, emitting `ICP_CLASSIFIED`
  and `PROSPECT_SCORED` to Sales/Marketing (`01_Sector/SECTOR_OS.md:89-90,162`; doctrine
  "Sector determines truth" `:16,:94`). But the canonical CRM field `ICP_fit_score` is owned by
  **Sales (05)** (`00_Agency_Governance/CRM_SCHEMA.md:23`). Marketing (03 §3) and ClientPartner (06)
  also define their own scoring.
- **Contradiction:** the field owner (Sales) is not the capability owner (Sector). Downstream,
  `sector-icp-fit → sales-lead-qualification` is wired correctly, so the *pipeline* is right but the
  *ownership metadata* is wrong.
- **Impact:** low now (0 leads); high once leads flow — ambiguous ownership of a scoring number is a
  classic source of silent divergence.
- **Proposed resolution (→ AEIT_05):** Sector owns ICP **classification/fit** and *sets*
  `ICP_fit_score`; Sales owns downstream **qualification decisioning** and *consumes* it. Update
  `CRM_SCHEMA.md:23` owner attribution to "set by Sector (01), consumed by Sales (05)". Marketing &
  ClientPartner scoring reference the Sector scorecard rather than redefining it. **Owner: Governance
  (00), ratified by the Owner.**

### A2 🟡 "CRM" means three different things
- **Evidence:** (1) Governance canonical object model `CRM_SCHEMA.md` (Arika's own, in ClickUp);
  (2) a **dead duplicate** — the pre-existing empty ClickUp "Sales CRM" space `901511301824`,
  "two structures, both empty" (`13_Tech_Stack/TECHSTACK_OS.md:78`); (3) a **client-facing CRM**
  Arika *sells* as a deliverable (`06_ClientPartner_Acquisition/CLIENTPARTNER_OS.md` §3, 22 entities).
- **Impact:** navigational/naming confusion; the dead ClickUp template is deletion-pending dead weight.
- **Proposed resolution:** keep the three explicitly named and separated — *Agency CRM* (canonical,
  Governance-owned), *client-CRM deliverable* (ClientPartner product), and delete the empty "Sales
  CRM" template. Add to `AEIT_10` cleanup. **Owner: Tech Stack (13) for deletion; Governance for naming.**

---

## Category B — Terminology drift (one concept, many words)

### B1 🟡 client / customer / account
- **Evidence:** canonical entity is **"Client"** (`CRM_SCHEMA.md`), but "customer" appears **13×
  across 7 department OS files** (Sales 4, ClientPartner 3, Design 2, Content 1, Marketing 1,
  Automation 1, Experience Eng 1), and "account" leaks via `CRM_SCHEMA.md:12` ("becomes a billing
  account") and the dead ClickUp template ("Accounts/Contacts").
- **Proposed resolution (→ AEIT_05):** **"Client"** is the one canonical term for the entity;
  "account" is reserved strictly for the billing/finance sense; "customer" is deprecated. A
  glossary entry in the canonical model (`AEIT_06`). **Owner: Governance (00).**

### B2 🟠 "Critical" is overloaded (risk vs priority)
- **Evidence:** Sales uses Low/Medium/High/**Critical** for risk; the Constitution uses a **5-class
  numeric** risk system; Sector's 90-pt scorecard *also* uses Low/Medium/High/**Critical** but as a
  **priority band**, not risk (`01_Sector/SECTOR_OS.md:68,:89`). `SALES_OS.md` §mapping papers over
  it, but "Critical" denotes two different things repo-wide.
- **Proposed resolution (→ AEIT_05):** risk = the Constitution's **5-class numeric** everywhere;
  prospect priority bands renamed (e.g. **P1–P4** or "priority: high/urgent") so "Critical" never
  means two things. **Owner: Governance (00).**

### B3 🟡 "pipeline" is overloaded
- **Evidence:** the **Pipeline (Probability) Calendar** (one of the 7), Sales **pipeline stages**,
  and ClientPartner's **3 pipelines** (Acquisition/Partner/Delivery) all share the word.
- **Proposed resolution:** qualify every use ("Pipeline Calendar", "Sales pipeline",
  "Acquisition pipeline"). Glossary entry. **Owner: Governance (00).** (Low priority.)

---

## Category C — Dead / dormant / drifting systems

### C1 🔴 The scheduled-automation estate has never fired, and the docs disagree on its size
- **Evidence:** the runtime's schedule triggers are "**declared, not scheduled** — inert"; the
  moment someone runs it with a key, they "begin firing with no matrix rows"
  (`16_Automation/AUTOMATION_OS.md:170`). Count **drifts across docs**: `AUTOMATION_OS.md:164,:196`
  say **21**; the 2026-07-19 commit (`9669862`) reconciles to **28**. No daemon exists; crons only
  register while a foreground `npm start` holds — which has never been left running.
- **Impact:** low now (nothing runs); high the instant activation happens without governance.
- **Proposed resolution (→ AEIT_10):** treat activation as a gated event — close Approval Matrix
  rows (C2) and reconcile the count to a single verified number *before* the runtime is ever booted
  persistently. **Owner: Automation (16) + Governance (00).**

### C2 🔴 Approval-Matrix coverage: ~21–28 armed automations, 1 real row
- **Evidence:** "The runtime's 21 cron triggers have 1 matrix row between them"
  (`AUTOMATION_OS.md:164`); `AUTOMATION_APPROVAL_MATRIX.md` holds 1 real + template rows.
- **Proposed resolution (→ AEIT_10):** one matrix row per armed automation
  (trigger/action/risk-class/rollback/human-gate) is a **hard precondition** of activation.
  **Owner: Governance (00).**

### C3 🔴 `ANTHROPIC_API_KEY` unset — the entire agent layer is unrunnable
- **Evidence:** "`ANTHROPIC_API_KEY` is not set. Every `prompt` agent in the repo — 93 of them —
  depends on Claude, and the key exists nowhere" (`13_Tech_Stack/TECHSTACK_OS.md:173`).
- **Proposed resolution (→ AEIT_10):** activation task #1; until then, every "live agent" claim is
  structure-ahead-of-reality and should be labelled as such. **Owner: Tech Stack (13).**

### C4 🟠 Phantom memory streams
- **Evidence:** many OS files claim a `_memory/runtime.jsonl` (Automation §13/§16, Sector §16,
  Consulting, Audits), but **only two exist on disk** — `12_Branding/_memory/runtime.jsonl` and
  `19_Design/_memory/runtime.jsonl`, both from *manual* runs. Most logged streams are fictional
  because the agents have never executed.
- **Impact:** the "Learn" meta-capability (`AEIT_03` §2) rests on streams that don't exist.
- **Proposed resolution:** the unified memory protocol is designed in IntOS (`AEIT_07`); until agents
  run, OS files should mark memory streams "planned, not yet written". **Owner: Governance (00).**

### C5 🟠 The one automation that ever ran died undetected for 11 days
- **Evidence:** Creative Pipeline routine `trig_01WyyrXEkFZck1D49tm6BfKv` fired once
  (2026-07-04T14:07Z), auto-disabled 3h41m later (`ended_reason: auto_disabled_repo_access`),
  detected **11 days later** (`AUTOMATION_OS.md:26-30,:108-125`). Root cause: it reads agent
  instructions from a GitHub origin that was stale and lacked repo access. The monitoring control
  that would have caught it (`automation-reliability-monitor`) **did not exist** at the time.
- **Impact:** low in fact (the Notion brief DB it polls is empty), high in principle.
- **Status:** monitor now built; scheduled cadence "**not yet proven since restoration**" — needs an
  unattended run to land. Carry into `AEIT_10` verification.

### C6 🟡 Two dead root Python scripts
- **Evidence:** `agency_intelligence_extractor.py` and `agency_workspace_completion_engine.py` need
  rewrite — hardcoded dates/paths, a phantom "Legal Drafts" workspace reference, regex-only, no LLM
  (`GLOBAL_OS.md` §11).
- **Proposed resolution:** archive or rewrite; do not re-run as-is. **Owner: Governance (00).**

---

## Category D — Compliance & infrastructure drift

### D1 🟠 Zoho (load-bearing) missing from the DPA sub-processor register; Books trial expired
- **Evidence:** Zoho serves email + invoicing (Zoho Books), is "the single most load-bearing
  vendor", yet is **absent from the DPA sub-processor register** (Annex B lists ClickUp only); the
  Books Premium trial has **expired** (`13_Tech_Stack/TECHSTACK_OS.md` §9 Decision Log; Legal DPA).
- **Proposed resolution (→ AEIT_10):** add Zoho to the sub-processor register (a Legal-review item)
  and resolve the Books plan. **Owner: Legal (10) + Tech Stack (13).**

### D2 🟡 No calendar/transcription tool despite an offer selling a weekly advisory cadence
- **Evidence:** Consulting & Advisory (15) sells a contractually-immutable weekly advisory cadence,
  but no calendar or transcription tool is registered (`TECHSTACK_OS.md` §3).
- **Proposed resolution:** register/select tooling before that offer is sold live. **Owner: Tech Stack (13).**

### D3 🟠 Legal non-existence blocks a downstream governance gate
- **Evidence:** AI Enablement (17)'s Class-3 governance gate requires a legal-reviewed framework;
  Legal has no engaged counsel and the agency does not legally exist (`GLOBAL_OS.md` §4, dept 17;
  `10_Legal/LEGAL_OS.md` §8, counsel instructed 2026-07-19, reply awaited).
- **Proposed resolution (→ AEIT_10):** legal existence + counsel engagement are upstream gates for
  several capabilities; sequence accordingly. **Owner: Legal (10).**

---

## Summary — what feeds where

| Finding | Type | Feeds |
|---|---|---|
| A1, A2, B1, B2, B3 | Coherence (ownership/terminology) | **AEIT_05** (reconciliation) |
| C1, C2, C3, C5, D1, D2, D3 | Activation / build / compliance | **AEIT_10** (roadmap, reality-gated) |
| C4, C6 | Hygiene | AEIT_07 (memory protocol) / AEIT_10 (cleanup) |

## Decision Log
- **2026-07-22 — Gap register compiled.** 13 findings across 4 categories, all cited; routed to
  reconciliation (AEIT_05) vs roadmap (AEIT_10). — Claude Code (Opus 4.8)

## Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
