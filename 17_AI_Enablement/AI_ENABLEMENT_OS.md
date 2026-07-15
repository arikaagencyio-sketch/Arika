# AI Enablement — Department OS

**Department:** AI Enablement (17)
**Position in flow:** Strategic/organization-wide layer, sitting above Automation (16)'s execution layer. Reports into Agency Governance (00).
**Mandate:** Own the agency's organization-wide AI transformation offer — AI Transformation Systems — readiness, roadmap, governance, and change management, distinct from Automation (16)'s specific workflow/agent builds.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

**Newly created department (2026-06-30)**, promoted from a category inside the Offer (02) catalog after the owner decided Draft 28's "AI Enablement" division deserved its own department. Its founding offer — AI Transformation Systems — is the highest setup-fee-ceiling offer in the entire catalog and has a real, source-named path to a $500,000-$5,000,000 "Whale Client" tier (`Agency Pricing Architure. Draft 28.md`'s own Whale Client Offers list).

**Relationship to Automation (16) — the clearest two-offer sequencing relationship in the Offer catalog, not a duplicate.** This department's offer (AI Transformation Systems) builds the organization-wide readiness assessment, roadmap, and governance framework; Automation (16)'s AI Workflow Infrastructure offer builds the specific workflows/agents that roadmap commissions. Sequenced, not competing: this department sells the "what and why," Automation sells the "build it."

## 2. Status

**Content seeded from Offer's catalog, not yet operationally run.** Full offer engineering exists (`02_Offer/OEOS - AI Enablement Division - AI Transformation Systems (Claude-Synthesized). Draft 40.md`) — Phase 1 (offer identity, though missing a Monetizable Components row in the source itself) and Phase 2 (positioning, shared with Automation's AI Workflow Infrastructure offer) are real, owner-sourced from Draft 28; Phases 3-12 are Claude-synthesized, owner-approved as-is 2026-06-30. No real AI transformation engagements have run yet.

**4 agents built 2026-07-15 (§5). The chain is wired and its most important gate is BLOCKED — correctly.**

### 🔴 The governance gate has no reviewer: Legal (10) does not exist

`Draft 40` Phase 10 requires a **"governance-framework legal/compliance review gate"**, and §11's RACI names **Legal (10)** as Consulted on AI transformation roadmap & governance.

**Legal (10) has no source content and no agents.** So this department's central compliance immutable — *"a governance/risk framework (model risk, data privacy, bias/fairness) required before any production AI deployment"*, **the most rigorous of any offer in the catalog** — points at a department that cannot perform the review.

`ai-enablement-governance-gate` therefore returns **`blocked`** on every run, with `legal_review.reviewer_available: false`. **That is the agent working, not failing.** The honest options are the owner's: build Legal (10) into a department that can review, name **external counsel** as the reviewer of record, or do not deploy production AI at a client. **The gate does not route around this** — Phase 10 makes it a gate, not a milestone, and *later* means *after the client's customers' data is already flowing through a model*.

### The partial delegability ban (owner-confirmed)

§5 flags **governance/risk-framework design** as *"requiring senior expertise — one of the two hardest-to-delegate deliverable types in the entire Offer catalog, alongside Consulting & Advisory's (15) advisory content."*

Unlike 15 — where the ban covers **the entire offer** — **this ban is specific**: it covers governance design only. Readiness, roadmap, and adoption are **not** senior-bound and got real agents. So `ai-enablement-governance-gate` **gates but never designs**; its `framework_authored_by` enum carries `agent_generated_INVALID` as a value for the sole purpose of naming that failure if it ever occurs. **An agent-authored governance framework is not a governance framework — it is the appearance of one, which is worse than none, because a visible framework stops anyone asking whether there is a framework.**

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| AI Transformation Systems | Organization-wide AI readiness assessment, roadmap, governance framework, training/change management | Offer engineered (`Draft 40`); chain wired 2026-07-15 (§5), **not yet delivered** |
| AI Governance Framework | Risk, data-privacy, fairness review structure required before any production AI deployment — the most rigorous compliance immutable of any offer in the catalog | **Designed (`Draft 40`), never tested — and its legal review gate has no reviewer (§2).** The *gate* is now enforced as code (`ai-enablement-governance-gate`, Class 3); the *framework itself* remains senior-human work by §5's ban |
| AI Opportunity Assessment | Named in Draft 28's Gateway Offers list — goal: *"introduce transformation"* | **⚠️ CONTESTED — 16 vs. 17, open owner decision.** Routed to this department 2026-07-15 by division, then contradicted the same day by `Draft 35` Phase 12, which names **"AI Opportunity Audit" as a standalone entry offer productized from offer #6 (Automation)** — *"same audit-as-entry-offer pattern as offer #10."* **Draft 40 strengthens 17's claim but does not settle it:** the Gateway's stated goal *"introduce transformation"* is **this offer's exact word** (#11 = *AI **Transformation** Systems*), and #11 owns an *"AI Readiness Assessment System"* (Phase 3) plus an *"AI Readiness Assessment Report"* (Phase 6). Against that, *"AI **Opportunity**"* is Draft 35's phrase, not Draft 40's — Draft 40 says **Readiness**, never *Opportunity*. **The name itself is split across two divisions and neither offer is engineered for it.** Deliberately left contested rather than resolved in the department that would benefit. See `02_Offer/OFFER_OS.md` |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| AI Transformation Systems delivery | Signed engagement | Readiness Assessment → Roadmap & Strategy Design → Governance Framework Build (parallel) → Phased Implementation (coordinated with Automation's offer) → Training & Change Management → Adoption Measurement | Transformation roadmap + governed, adopted AI capability | Mary Thuo | `Draft 40` (synthesized) |

## 5. Agent Roster

**4 agents, built 2026-07-15.** `Draft 40`'s functional role labels (AI Governance Lead, Change Management Lead, Strategy Lead) describe AI-assisted execution the owner performs solo, **not hires**. See `11_HR_People_Ops/HR_OS.md` for real staffing.

**Governance/risk-framework design is explicitly senior-bound** (`Draft 40`) — one of the two hardest-to-delegate deliverable types in the catalog, alongside Consulting & Advisory (15)'s advisory content. **The ban is honored by shape:** three agents do this department's work; the fourth only *gates* work a human must author.

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `ai-enablement-readiness-assessor` | 2 | `AI_TRANSFORMATION_REQUESTED` → `AI_READINESS_ASSESSED` / `AI_NOT_READY` | The Phase 3 immutable: data quality · team AI-literacy · process maturity. **No roadmap exists until this passes** |
| `ai-enablement-roadmap-architect` | 2 | `AI_READINESS_ASSESSED` → `AI_ROADMAP_READY` | The phased roadmap — the *"what and why"*; `commissioned_builds` hands the *"build it"* to Automation (16) |
| `ai-enablement-governance-gate` | **3** | `AI_ROADMAP_READY` → `AI_GOVERNANCE_APPROVED` / `AI_GOVERNANCE_BLOCKED` | **Gates production deployment. Never designs the framework.** Currently blocked — no legal reviewer exists (§2) |
| `ai-enablement-adoption-tracker` | 2 | `AI_GOVERNANCE_APPROVED` → `PILOT_VALIDATED` / `ROLLOUT_BLOCKED` / `ADOPTION_AT_RISK` | The staged-QA gate + real adoption measurement against trained headcount |

**`ai-enablement-governance-gate` is Class 3** — the highest-stakes gate any agent in this repo holds. It authorizes AI to run in production against real people's data at a real client: model risk, data privacy, bias/fairness, with consequences for the client's *customers*, who never chose to be part of an AI deployment. Per the Constitution, Class 3+ requires human sign-off **with no exceptions carved out by convenience or urgency** — and per Phase 10, a **lawyer** too. Correctly, it is the gate an agent has the *least* authority over: it can only block or recommend.

### Chain

`AI_TRANSFORMATION_REQUESTED` → readiness → roadmap → **⟨governance gate — BLOCKED, no reviewer⟩** → *(16 builds)* → adoption/staged-rollout gate

### The two-offer sequencing with Automation (16) — the clearest in the registry

`Draft 40` Phase 2: *"Offer #6 (Automation) builds specific AI workflows/agents into existing operations — the execution layer. Offer #11 (AI Enablement) is organization-wide AI transformation: readiness, roadmap, training, governance, change management — the strategic/capability layer… offer #11's roadmap likely commissions offer #6's specific workflow builds as implementation."*

This department sells the **"what and why"**; Automation sells the **"build it."** Phase 3 lists *"Workflow Implementation System (shared with/handed off to offer #6)"* as a core system of this offer, and §11's RACI makes **Automation (16) Accountable** for the implementation handoff. `ai-enablement-roadmap-architect`'s `commissioned_builds` is that handoff, made real.

> **⚠️ Still unconfirmed** (`Draft 40` Phase 2's own words): *"Worth confirming with the owner whether these should be sold bundled or as separate entry points."* The agents do not assume a bundle.

### No re-diagnosis

Readiness reuses prior findings rather than re-running them — Audits (14)'s offer #10 has an `automation` sub-audit feeding `process_maturity`, and Automation (16)'s `automation-workflow-architect` already records `audit_state` and `current_stack`. Same discipline 14 applies delegating its acquisition sub-audit to 06, and 15 reusing 14's audit: **re-running a diagnostic the client already paid for is billing twice for one finding.**

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Pilot-to-rollout success rate | Departments passing pilot validation ÷ departments attempting rollout | `Draft 40` (staged-QA: no org-wide rollout without a validated pilot) | Mary Thuo | Per-engagement | *(unset — no real data yet)* |
| Adoption rate (post-training) | Active AI tool usage ÷ trained headcount | `Draft 40` | Mary Thuo | Monthly during engagement | *(unset)* |

## 8. Decision Log

- 2026-07-15 — **The delegability ban here is PARTIAL, unlike 15's** (owner-confirmed). §5 flags **governance/risk-framework design** as senior-bound — not the whole offer, the way `Draft 38` Phase 12 does for Consulting & Advisory. So readiness, roadmap, and adoption got real agents; **only the governance framework is gated rather than authored.** `ai-enablement-governance-gate` carries `framework_authored_by: agent_generated_INVALID` as an enum value solely to name that failure if it ever occurs. — Claude Code (Opus 4.8)
- 2026-07-15 — **The governance gate blocks and names Legal (10) as the hole** (owner-confirmed). Phase 10's *"governance-framework legal/compliance review gate"* + §11's RACI (Legal 10 Consulted) point at a department with **zero source content and no agents**. The gate returns `blocked` with `reviewer_available: false` rather than softening the immutable to advisory or having Claude attempt the review — **Claude is not counsel, the agency has no legal source material, and this touches real client data-privacy exposure.** Owner's options: build Legal (10), name external counsel, or don't deploy production AI at a client. — Claude Code (Opus 4.8)
- 2026-07-15 — **"AI Opportunity Assessment" left CONTESTED, deliberately** (owner-confirmed). `Draft 40` strengthens 17's claim — the Gateway's goal *"introduce transformation"* is this offer's exact word, and #11 owns an *"AI Readiness Assessment System"* — but does not settle it: `Draft 35` Phase 12's *"AI Opportunity Audit"* remains the most direct textual claim, and **Draft 40 says "Readiness", never "Opportunity"**. The name is split across two divisions. **Not resolved in the department that would benefit from resolving it.** — Claude Code (Opus 4.8)

## 9. Risk / Incident Log

*(No incidents — no engagement has ever run.)*

**The organizational Doubter is now enforced as code.** `Draft 40` Phase 9 flags organization-level skepticism as *"a distinct, organization-vs-individual version"* of Automation's individual **Doubter** — *"skeptical teams resist adoption even after leadership buy-in."* `ai-enablement-adoption-tracker` scores it structurally:

> **`leadership_bought_in: yes` + `teams_bought_in: no` is the signature — and it is the most dangerous state this offer has, because it looks like success from the top.** The people who sponsor the engagement are enthusiastic; the people who must use the thing are not. Every status report is green and adoption is 4%.

A `strong_signal` emits `ADOPTION_AT_RISK` to `client-success-health-retention` (07). The other archetypes: **Unrealistic Client** (org-wide transformation in weeks) and **Micromanager** (governance-conscious over-control). **The Micromanager slows delivery; the organizational Doubter makes it worthless while looking fine.** The Micromanager is the *safe* failure mode.

### Standing risks (structural, not incidents)

- **🔴 The governance gate is blocked with no path forward inside this department.** Its required legal reviewer, Legal (10), does not exist (§2). This is the agency's highest-stakes dead-end: offer #11 carries the **highest setup-fee ceiling in the catalog** ($250,000+) and a **real, source-named path to Draft 28's $500K–$5M whale tier** — and none of it can lawfully reach production without a review nobody can perform.
- **This department has the catalog's most rigorous compliance immutable and the least tested one.** §3 states it plainly: *"Designed, not yet tested against a real engagement."* Phases 3-12 are **Claude-synthesized**; the gate has never caught anything and the archetypes have never been observed.
- **Cross-border data handling is live, not theoretical.** The agency operates from **Kenya** (`13_Tech_Stack/TECHSTACK_OS.md`; Zoho org country KE, currency KES). Any client AI deployment touching personal data raises jurisdiction questions the agency has **no legal capability to answer** — the same hole as above, from a second direction.
- **Two real source gaps in Phase 1/11:** this is **the only offer of 11 missing a "Monetizable Components" row** in Draft 28's table, and Phase 11 has **no master-chart row of its own** (unlike offer #6's "AI Automation" row) — so its tiers are synthesized *within* a stated range, not sourced. The offer with the highest price ceiling has the thinnest pricing provenance.

## 10. Standards & SOPs Index

Full offer-engineering detail lives in `02_Offer/OEOS - AI Enablement Division - AI Transformation Systems (Claude-Synthesized). Draft 40.md` — cited here rather than duplicated.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| AI transformation roadmap & governance | AI Enablement (17) | AI Enablement (17) | Offer (02), Legal (10) | Automation (16), Operations (08) |
| Workflow implementation handoff | AI Enablement (17) | Automation (16) | Offer (02) | Client Success (07) |

## 12. Triggers / Automation Hooks

The chain runs on `arika-runtime` (`GLOBAL_OS.md` §5): 4 agents, manual + event, plus one monthly cron (`ai-enablement-adoption-tracker`, `47 8 1 * *` — adoption is measured monthly during an engagement, per §7).

**Known gaps — flagged, not worked around:**

1. **`AI_TRANSFORMATION_REQUESTED` has no emitter.** A human signs the engagement; nothing publishes the event. The chain starts with a manual `arika run ai-enablement-readiness-assessor`.

2. **🔴 `AI_GOVERNANCE_APPROVED` will never fire in the current state** — the gate is Class 3, requires human **and legal** sign-off, and its legal reviewer does not exist (§2). So `ai-enablement-adoption-tracker`'s primary trigger is unreachable by design until Legal (10) is built or external counsel is named. **This is not a broken link; it is the immutable holding.** `operations-state-monitor` (08) should read it as such.

3. **⚠️ The monthly cron is declared, not scheduled.** Same standing issue as every department: the runtime isn't booted as a daemon, and its **25 cron triggers still have 1 approval-matrix row between them** (`00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`, `16_Automation/AUTOMATION_OS.md` §12).

## 13. Existing OS Sub-Layer

No department-local code. The 4 agents (§5) run on the shared `arika-runtime`; their memory stream is `17_AI_Enablement/_memory/runtime.jsonl`. The offer-engineering content (`Draft 40`) remains the canonical design reference.

**Worth noting the recursion:** this department sells organization-wide AI transformation — readiness, governance, adoption — and **the agency has never run its own governance framework over `arika-runtime`**, its own 100-agent AI deployment. `16_Automation/AUTOMATION_OS.md` §12's finding (25 cron triggers, 1 approval-matrix row) is exactly the kind of thing this department's own `ai-enablement-governance-gate` exists to catch at a client. **Arika would not currently pass its own gate.**

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offer #11) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-06-30 — Department created, promoted from Offer (02)'s "AI Enablement" division category per owner decision. Seeded from `Draft 40` (offer #11, AI Transformation Systems), owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-15 — **Department built: 4 agents wired onto `arika-runtime`** (§5) — `ai-enablement-readiness-assessor` (2), `ai-enablement-roadmap-architect` (2), **`ai-enablement-governance-gate` (3)**, `ai-enablement-adoption-tracker` (2). **The Class 3 gate is the highest-stakes any agent in this repo holds** — it authorizes AI to run in production against real people's data at a real client — and it is correctly the one an agent has the *least* authority over: it can only block or recommend. §9 upgraded from placeholder: the organizational Doubter is now structurally detected via `leadership_bought_in: yes` + `teams_bought_in: no` — **the most dangerous state this offer has, because it looks like success from the top.** — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 4 agents (§5) write to `17_AI_Enablement/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope. **Empty** — no engagement has ever run. Note what this stream would need to be, given the department's own doctrine: an auditable record of **who authorized which AI deployment, on what governance basis, reviewed by whom**. That is precisely what `ai-enablement-governance-gate`'s output schema captures, and precisely what the agency cannot yet produce for its own AI deployment (§13).

**Feedback Loop.** Both §7 KPIs are **unset and uncalibratable** — pilot-to-rollout success rate and post-training adoption rate each need a delivered engagement, and none exists. **Never report a rate without a real numerator and denominator**; `ai-enablement-adoption-tracker`'s `measurement_basis` enforces that (`self_reported` is not `measured`, `estimated` is a guess wearing a percentage sign).

Two loops are wired and honest about their reach:
- `ai-enablement-adoption-tracker` → `ADOPTION_AT_RISK` → `client-success-health-retention` (07), on the organizational-Doubter signature.
- `ai-enablement-roadmap-architect` → `commissioned_builds` → `automation-workflow-architect` (16). **The strategic layer commissioning the execution layer** — the registry's clearest sequencing relationship, made real.

**Cadence.** Adoption is measured **monthly during an engagement** (§7), which is the department's only clock-driven work. Delivery is per-engagement, 30–90 days (Phase 7 — *"not recommended below 30 days: governance and training cannot be safely compressed"*, a hard constraint, not a risk). Phase 8's **bi-weekly steering-committee review** is a real cadence this department owns and **has no calendar tool to run** — see the gap recorded in `13_Tech_Stack/TECHSTACK_OS.md` §9, found while building Consulting & Advisory (15) and equally binding here. Against the **Operational Calendar** for adoption, the **Strategic Calendar** for steering reviews.

**⚠️ The honest state:** the monthly cron is **declared, not scheduled** (§12), and the chain's main path is **blocked at the governance gate by design** until Legal (10) exists or external counsel is named. This department is wired end-to-end and **cannot currently deliver its own offer** — which is the correct behavior, not a defect.
