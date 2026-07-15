# Automation — Department OS

**Department:** Automation (16)
**Position in flow:** Horizontal support layer — closely tied to Operations (08) and Tech Stack (13), and the execution-layer counterpart to AI Enablement (17)'s strategic layer. Reports into Agency Governance (00).
**Mandate:** Own the agency's process-and-AI-workflow offers — AI Workflow Infrastructure and Business Operating Systems — both as sellable client offers and as the agency's own internal automation capability.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

**Newly created department (2026-06-30)**, promoted from a category inside the Offer (02) catalog after the owner decided Draft 28's "Automation" division deserved its own department. It houses two deliberately distinct offers: **AI Workflow Infrastructure** (the AI/agent execution layer — CRM automation, AI agents, workflow orchestration) and **Business Operating Systems** (the human/process layer — SOPs, dashboards, KPI ownership). These are a real two-offer split within one division, not duplicates — a client with a working team but no documented process needs Business Operating Systems before they need AI agents.

**Dual mandate, not just an offer line.** Because this department's offers are about automating execution, it is also the natural home for the agency's *own* internal automation — once any client-facing automation work matures, the same systems are the candidate first deployment for the agency's internal operations (cross-reference `00_Agency_Governance/AGENCY_VISION.md`'s Automation Vision layer).

## 2. Status

**Content seeded from Offer's catalog, not yet operationally run.** Full offer engineering exists for both founding offers:
- `02_Offer/OEOS - Automation Division - AI Workflow Infrastructure (Claude-Synthesized). Draft 35.md` — Phase 1 and Phase 2 positioning real (Draft 28); Phases 3-12 Claude-synthesized, owner-approved as-is 2026-06-30.
- `02_Offer/OEOS - Automation Division - Business Operating Systems (Claude-Synthesized). Draft 36.md` — Phase 1 real; Phases 2-12 Claude-synthesized, owner-approved as-is 2026-06-30.

No real **client** automation engagements have run yet.

### 🔴 2026-07-15 audit: this department's own automation was dead for 11 days and nobody knew

The single most important fact about this department, found by auditing it rather than reading it:

**The Creative Pipeline routine — `trig_01WyyrXEkFZck1D49tm6BfKv`, described everywhere in this repo as "LIVE as of 2026-07-04" — fired exactly once, at `2026-07-04T14:07:35Z`, and was auto-disabled at `17:07Z` with `ended_reason: auto_disabled_repo_access`.** It then sat dead for **11 days** with `next_run_at` frozen at a timestamp in the past.

Throughout that outage, §12 of this file said *"LIVE as of 2026-07-04"*, `AUTOMATION_APPROVAL_MATRIX.md` called it the one *"real row… made live"*, and `GLOBAL_OS.md`, `DESIGN_OS.md`, and `CONTENT_OS.md` all referenced it as running. **The documentation was the only thing anyone read, and it was wrong.**

The department whose founding offer sells a **"Monitoring/Observability System"** (`Draft 35` Phase 3, a named core system) and **"a dedicated alert channel for automation failures"** (`Draft 35` Phase 8) had **no monitoring of its own**. Its other immutable — **audit-before-automate, "never automate an unmapped process"** — had never been applied to its own estate.

**Resolved 2026-07-15:** the repo was pushed to GitHub (origin had been 5 days stale, and repo access was the stated disable reason), the routine was re-enabled, and a forced run fired successfully at `2026-07-15T09:36:46Z` **without re-tripping the auto-disable** — `ended_reason` cleared, `next_run_at` advanced to a real future time. **Not yet proven across the scheduled cadence** — one forced run is not a restored cron. `automation-reliability-monitor` (§5) now exists precisely so the next outage is found by an agent rather than by an audit 11 days later.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| AI Workflow Infrastructure | AI/agent execution layer — CRM automation, AI agents, workflow orchestration, internal copilots | Offer engineered (`Draft 35`), not yet delivered |
| Business Operating Systems | Process/documentation layer — SOPs, dashboards, KPI ownership, org-design clarity | Offer engineered (`Draft 36`), not yet delivered |
| Internal automation (agency's own operations) | Same systems as above, applied to Arika Agency itself | **🔴 Was "Not started — a future opportunity, not yet scoped" until 2026-07-15. That was stale, and this department was the last to know.** `arika-runtime` — **90 agents, 21 cron triggers, 134+ event bindings, one join barrier** — *is* the agency's internal automation, built 2026-07-14/15. **11 of the 12 department OS files reference it; this one didn't** — the department that owns internal automation was the only one unaware it exists. Corrected. See §12 for what the department actually owes it: governance rows and monitoring, neither of which existed. |
| Automation estate monitoring (the agency's own) | Watching whether the agency's own automations are actually running — cloud routines and runtime triggers alike | **Built 2026-07-15** (`automation-reliability-monitor`, §5) — created in response to the 11-day silent outage in §2. Never existed before; that is why the outage was invisible. |
| Engagement Layer (DM/comment automation) | Converts published content engagement into leads: comment/keyword trigger → DM → lead-magnet delivery → email/CRM capture → Sales pipeline handoff. Proposed platform: ManyChat | Proposed, not built — no ManyChat account exists yet (see `00_Agency_Governance/OWNER_INPUT_NEEDED.md`) |
| Creative Pipeline Automation (Design 19 trigger) | A durable cloud routine (Anthropic's cloud-routine infrastructure, cron-scheduled, minimum hourly interval) polls Content (04)'s real Notion content-brief database for a status match, then invokes Design (19)'s real agent chain (Storyboard Generator → Production Engine Coordinator), pausing before any credit-spending generation step for human review | **Fully specified, not yet live — blocked on 2 real prerequisites** (§12, `00_Agency_Governance/OWNER_INPUT_NEEDED.md` items 54-55): (1) a Notion MCP connector must be connected specifically for the cloud-routines system at `https://claude.ai/customize/connectors` — a different connection scope than whatever gives Notion access in an interactive chat session; (2) the real "Publishing Status" field's select options need verifying/setting — the database has zero real content in it yet, and "Distribution Prep" is currently only a workflow *stage name* (`04_Content/CONTENT_OS.md` §4), not confirmed as an actual Notion select value |
| Creative Pipeline Automation (Experience Engineering 20 trigger) | The equivalent automation for Experience Engineering (20) — Design's pipeline reaching an "Assemble" stage for an experience-scale project would invoke Experience Engineering's Narrative Architect | **Cannot be specified yet, not just unbuilt** — Experience Engineering has no real project (tracker item 51 fully open) and no real field/flag anywhere distinguishing "experience-scale" from "single-asset" work, so there is no real condition to poll for. Revisit once item 51 resolves. |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| AI Workflow Infrastructure delivery | Signed engagement | Discovery → Architecture Design → Build → Integration & Testing → Deployment & Training → Monitoring/Optimization | Deployed, monitored AI automations | Mary Thuo | `Draft 35` (synthesized) |
| Business Operating Systems delivery | Signed engagement | Discovery → Process Mapping → Redesign → Dashboard/KPI Build → Rollout & Training → Optimization | SOP library + dashboard system | Mary Thuo | `Draft 36` (synthesized) |
| Engagement Layer (DM automation) | Published content receives a qualifying comment/keyword | Post → Comment/keyword trigger → automated DM → lead-magnet delivery (guide/checklist/audit/template) → collect email/company/role → CRM (ClickUp) → Sales pipeline | Captured lead in CRM, attributed to source content | Mary Thuo | Design (19)/Content (04) founding planning session, 2026-07-01 |
| Creative Pipeline Automation (Design 19) | Cloud routine polls Notion hourly; a content brief's Publishing Status equals "Ready for Design" | Cloud routine detects match → drafts storyboard per `.claude/agents/design-storyboard-generator.md` → drafts planning-only Production Engine recommendation per `.claude/agents/design-production-engine-coordinator.md` → posts both as a Notion comment → **hard-gates here (no OpenArt/Canva connector attached to this session at all)** → human reviews comment and manually runs actual generation → Enhancement/Upscale → Canva Assembler | A drafted storyboard + tool recommendation, awaiting human-run generation | Mary Thuo | This session, 2026-07-04 — **live**, routine `trig_01WyyrXEkFZck1D49tm6BfKv` |

## 5. Agent Roster

**4 agents, built 2026-07-15.** They map onto `Draft 35`/`Draft 36`'s real functional role labels (Automation Engineer, Integration Specialist, Process Analyst, Dashboard/BI Engineer) — AI-assisted execution functions the owner currently performs solo, **not hires**. See `11_HR_People_Ops/HR_OS.md` for when real staffing becomes relevant.

The roster is deliberately **two-sided**, matching this department's dual mandate (§1): two agents sell the offers, two govern the agency's own estate.

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `automation-reliability-monitor` | 1 | daily cron `17 8 * * *` → `AUTOMATION_HEALTHY` / `_DEGRADED` / `_SILENTLY_DEAD` | **Internal.** Audits the agency's own estate — cloud routines, runtime triggers, matrix coverage, doc/reality drift |
| `automation-approval-gate` | 2 **+ human-gated** | `AUTOMATION_PROPOSED` → `AUTOMATION_GATE_PASSED` / `_BLOCKED` | **Internal.** Enforces "no automation goes live without a row" + the 4 immutables |
| `automation-workflow-architect` | 2 | `WORKFLOW_INFRASTRUCTURE_REQUESTED` → `WORKFLOW_ARCHITECTURE_DESIGNED` | **Client-facing.** Offer #6, AI Workflow Infrastructure — the execution layer |
| `automation-process-architect` | 2 | `BUSINESS_OS_REQUESTED` → `BUSINESS_OS_DESIGNED` | **Client-facing.** Offer #7, Business Operating Systems — the process layer |

**`automation-reliability-monitor` is the agent this department most needed and least had.** It is the only scheduled agent in the repo whose job is to check that the *other* scheduled things ran. It carries the 2026-07-04 outage as a worked example in its own prompt, so the failure class stays legible: **an automation that is disabled is not the problem; an automation that is disabled and still believed to be running is.**

**`automation-approval-gate` is human-gated by construction** — it recommends; a person activates. It never switches anything on, consistent with `Draft 35`'s manual-override immutable.

### Boundaries with the two neighbouring monitors

| Agent | Owns |
|---|---|
| `marketing-ops-governor` (03) | Automation reliability **inside Marketing** — its workflow uptime, integration health, incident response |
| `operations-state-monitor` (08) | Where the **business** is, and whether the chain between departments is intact |
| `automation-reliability-monitor` (16) | Whether the **machinery is switched on** — agency-wide cloud routines, runtime triggers, matrix coverage |

A department can be perfectly aligned (08 reports green) and completely un-automated. Only 16 sees that — which is exactly what happened for 11 days.

### The client-offer split (`Draft 36` Phase 2 — a real division, not duplicates)

`automation-process-architect` (#7) is the **process/documentation layer**; `automation-workflow-architect` (#6) is the **AI/agent execution layer** that runs inside it. The source's own rule: *"A client with a working team but no documented process needs Business Operating Systems before they need AI agents."* Offer #6's **audit-before-automate** immutable makes #7 its prerequisite, so `precedes_offer_6` is a first-class field — recommending #7 first is a legitimate, common outcome even when the client came asking for AI.

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Automation failure rate | Failed automation runs ÷ total runs | `Draft 35` (QA gate: target <2%) | Mary Thuo | Continuous, post-deployment | *(unset — no real data yet)* |
| SOP adherence rate | Measured adoption ÷ documented process | `Draft 36` | Mary Thuo | Weekly | *(unset)* |

## 8. Decision Log

- 2026-07-01 — Added the Engagement Layer (comment/keyword-triggered DM automation, proposed platform ManyChat) as a new capability, per the Design (19)/Content (04) founding planning session. No ManyChat account exists yet — documented as proposed, not live. See §3, §4.
- 2026-07-04 — **Creative Pipeline Automation designed** for Design (19), per owner request to build real automations for the now-live Design/Experience Engineering agent rosters. Fully specified (trigger, cron-based cloud-routine mechanism, human gate before credit spend, Risk Class 2 with a deliberately stricter human gate) but **not activated** — 2 real prerequisites (Notion MCP connector for cloud routines; Publishing Status field verification) are owner action items, tracked as `OWNER_INPUT_NEEDED.md` items 54-55. The equivalent automation for Experience Engineering (20) could not be specified at all — no real project exists yet to define a trigger condition against (tracker item 51). Confirmed this repo has a real GitHub remote (`arikaagencyio-sketch/Arika`), resolving what would otherwise have been a third blocker.

## 9. Risk / Incident Log

### INCIDENT 2026-07-04 → 2026-07-15 — Creative Pipeline routine dead 11 days, undetected

**The agency's first real incident, and it went unnoticed for its entire duration.** No longer a placeholder section.

| | |
|---|---|
| **What** | Cloud routine `trig_01WyyrXEkFZck1D49tm6BfKv` (Design Creative Pipeline Automation) |
| **Created** | 2026-07-04T13:26:48Z |
| **Fired** | **Once.** 2026-07-04T14:07:35Z — the first scheduled run |
| **Died** | 2026-07-04T17:07:19Z — auto-disabled, `ended_reason: auto_disabled_repo_access` |
| **Detected** | 2026-07-15, by a departmental audit — **11 days later** |
| **Detected by** | A human reading the API. **No agent, alert, or check existed.** |
| **Impact** | Low in fact, high in principle: the Notion brief database it polls is real and **empty**, so nothing was missed. Had a brief been marked "Ready for Design" any time in those 11 days, it would have sat unprocessed with every document asserting the pipeline was running. |
| **Root cause** | The routine reads agent instructions from `https://github.com/arikaagencyio-sketch/Arika`. Repo access failed; the platform auto-disabled after repeated failures. Contributing: **origin was 5 days stale** (last push 2026-07-10) and had never received the agent-runtime work at all. |
| **Why undetected** | **Nothing watched it.** `enabled: false` and `ended_reason` are only visible via the trigger API, which nothing read. Every OS file asserted "LIVE" from the day it was written and was never re-checked against reality. |
| **Fix applied** | Pushed the repo (2 commits, origin `c8141c5` → `b8e830c`), re-enabled the routine, forced a run: fired 2026-07-15T09:36:46Z **without re-tripping the auto-disable**; `ended_reason` cleared; `next_run_at` advanced to a real future time. |
| **Verification status** | **Partial, and stated as such.** One forced run proves repo access works now. It does **not** prove the hourly cron survives — that needs an unattended scheduled run to land. |
| **Prevention** | `automation-reliability-monitor` (§5), daily cron, checks `enabled` / `ended_reason` / `last_fired_at` vs. cron across the whole estate and reports `doc_reality_drift`. **This is the control that did not exist.** |
| **Rollback/fallback that existed** | Both were documented in the matrix and both worked as designed. **The gap was never rollback — it was detection.** |

**The lesson, recorded because it generalizes:** the matrix requires rollback and fallback before activation. It does **not** require an answer to *"how will anyone know this stopped?"* — and that is the question this incident turned on. `automation-approval-gate` now asks it: if `log_destination` is a document a human must remember to read, that is the failure that already happened.

**A second-order finding:** this incident is also evidence about the repo's own reliability discipline. The claim "LIVE as of 2026-07-04" was written on 2026-07-04 and was true for **3 hours and 41 minutes**. Nothing in the OS convention distinguishes *"we turned this on"* from *"this is still on."* Every future §12 "live" claim should carry a last-verified date, not just an activation date.

---

*(Prior note, retained: `Draft 35` flags a hard immutable constraint — human-in-the-loop required for any client-facing AI output, no fully autonomous deployment without a review gate. Carries forward into any real incident logging once delivery begins. The Engagement Layer (§3, §4) is a concrete future instance of this constraint: it acts on real customer messages, so per `GLOBAL_OS.md` §3's Class 3+ sign-off rule, it needs a real row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` before it goes live — not created in this pass, since ManyChat isn't connected yet.)*

**Creative Pipeline Automation's own risk note (2026-07-04):** classified Risk Class 2 (internal creative production, not client-facing/financial/contractual), but given a human gate anyway — stricter than the class technically requires — because it can spend OpenArt's real, scarce credit pool (Free plan, 40 credits total) autonomously if left ungated. The gate sits before any generation step, not after. Real row: `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`.

## 10. Standards & SOPs Index

Full offer-engineering detail lives in `Draft 35` and `Draft 36` — cited here rather than duplicated.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| AI workflow delivery | Automation (16) | Automation (16) | Offer (02), AI Enablement (17) | Operations (08) |
| Business Operating Systems delivery | Automation (16) | Automation (16) | Offer (02) | Operations (08) |
| Internal automation deployment (agency's own ops) | Automation (16) | Mary Thuo | Operations (08), Tech Stack (13) | All departments |

## 12. Triggers / Automation Hooks

> **⚠️ Convention change (2026-07-15):** every claim below carries a **last-verified** date, not just an activation date. The claim *"LIVE as of 2026-07-04"* sat in this section for 11 days while the routine was dead (§9). An activation date says someone turned it on. It says nothing about now.

**Creative Pipeline Automation (Design 19) — re-enabled 2026-07-15. Last verified: 2026-07-15T09:36:46Z (forced run, succeeded). Scheduled cadence NOT yet proven since restoration.** Real trigger: Content (04)'s Notion content-brief database (`collection://1f0ed36e-a548-4743-9947-f408f8811140`), "Publishing Status" field equals the literal value **"Ready for Design."** Real mechanism: a durable Anthropic cloud routine, `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron (`7 * * * *`), repo `https://github.com/arikaagencyio-sketch/Arika`, Notion connector attached (connector_uuid `f957ca4d-bcce-43a2-9f31-9b6954efeee1`) — deliberately no OpenArt/Canva connector, so the credit-spend gate is enforced by the session's tool access, not just its instructions. First scheduled run `2026-07-04T14:07:00Z`.

Each run: queries the content-brief database for "Ready for Design" pages; for each match, reads `.claude/agents/design-storyboard-generator.md` and `.claude/agents/design-production-engine-coordinator.md` in this repo and follows their instructions to draft a 7-field storyboard and a planning-only Production Engine recommendation (tool choice per stage, no actual generation call possible); posts both as a Notion comment on the brief for owner review. It does not change the brief's own status, make git commits, or spend any OpenArt/Canva credit — a human moves the brief forward after reviewing the comment.

Both build blockers resolved same session: the Notion cloud-routines connector was already attached (the earlier "zero connectors" reading was stale), and "Publishing Status" was converted from a native status property (which doesn't accept custom options via the available schema-update API) to a plain select with the new "Ready for Design" option — the database had 0 rows, so no data loss. Full history: `OWNER_INPUT_NEEDED.md` items 54-55 (Resolved table), `GO_LIVE_CHECKLIST.md` Phase 9.

**⚠️ The routine reads agent files from GitHub, and that is now a live coupling worth understanding.** It reads `.claude/agents/design-storyboard-generator.md` and `design-production-engine-coordinator.md` from `origin/master` and follows their prose. Since 2026-07-15 both files carry runtime frontmatter — **bodies untouched**, so the routine's instructions still resolve, and the production coordinator's new `requires_human_approval: true` *reinforces* the routine's planning-only rule rather than conflicting with it. But note the shape of the dependency: **the routine runs whatever is on `origin/master`, not what is on this machine.** An unpushed local change is invisible to it; a pushed one takes effect on the next run with no review step. That coupling caused the outage (stale/inaccessible origin) and it has no test.

**Creative Pipeline Automation (Experience Engineering 20) — cannot be specified yet.** No real trigger condition exists to poll for until tracker item 51 (first real project) resolves.

### 🔴 The runtime's 21 cron triggers have 1 matrix row between them

`arika-runtime` declares **21 `schedule` triggers** across the roster (20 before this department; `automation-reliability-monitor` is the 21st). `AUTOMATION_APPROVAL_MATRIX.md` holds **one** real row — for the Creative Pipeline routine.

The matrix rule is unconditional: *"No automation goes live without a row in this matrix."*

**This is not a live breach — it is one command away from being one.** The runtime is a local Node process; nobody has booted it as a persistent service, and it has no `ANTHROPIC_API_KEY`. Its cron triggers are therefore **declared, not scheduled** — inert. The moment someone runs `npx tsx src/index.ts` with a key, **21 automations begin firing with no matrix rows, no defined rollback, and no fallback.**

That is luck, not compliance. `automation-approval-gate` is instructed to return `blocked` on any request to boot the runtime as a daemon until rows exist. **Rows were not written in this pass** — deciding whether that is 21 rows or one covering row (with a shared rollback: disable the scheduler; and fallback: `arika run <name>` manually) is an owner call, and writing 21 rows for agents that have never run once would be documenting an intention as a fact. **The runtime is safe to use manually today; it is not approved to run unattended.**

### The hybrid model's cloud mirror was never built

`GLOBAL_OS.md` §5 records the owner's runtime decision: **local runtime for build/test/manual runs + Anthropic cloud routines for always-on scheduled production**, with each spec's `schedule` trigger *mirrored into a cloud routine*.

Reality: **21 schedule triggers, 1 cloud routine — and that routine is not derived from any of them.** It is a bespoke prompt that reads two agent files and follows their prose; it predates the runtime and knows nothing about it. So the two halves of the hybrid model are not connected: the runtime's schedules live in a process that never runs, and the cloud routine that does run isn't generated from a spec.

This department owns that gap. Closing it means a real mechanism — spec `schedule` trigger → generated cloud routine — which does not exist and was not built here. Flagged, not faked.

## 13. Existing OS Sub-Layer

**Corrected 2026-07-15.** This said *"None yet — code-based automation not built,"* which was false: **`arika-runtime/` at the repo root is the agency's internal automation layer**, and this department's own §3 mandate covers it. It is not department-local — it is shared infrastructure serving all 13 staffed departments — but 16 is the department accountable for its **governance rows** (§12) and its **estate monitoring** (§5), neither of which existed before this pass.

The 4 agents (§5) run on it; their memory stream is `16_Automation/_memory/runtime.jsonl`. The offer-engineering content (`Draft 35`, `Draft 36`) remains the canonical design reference for the two client offers.

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offers #6-7) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-07-15 — **🔴 INCIDENT FOUND AND CLOSED: the agency's only automation had been dead for 11 days** (§9). `trig_01WyyrXEkFZck1D49tm6BfKv` fired **once** (2026-07-04T14:07:35Z) and was auto-disabled 3h41m later — `ended_reason: auto_disabled_repo_access` — while this file, the approval matrix, `GLOBAL_OS.md`, `DESIGN_OS.md`, and `CONTENT_OS.md` all said "LIVE". **The department selling a "Monitoring/Observability System" and a "dedicated alert channel for automation failures" (`Draft 35` Phases 3, 8) had no monitoring of its own.** Fixed: repo pushed (origin was 5 days stale and had never received the runtime work — repo access was the stated disable reason), routine re-enabled, forced run succeeded at 2026-07-15T09:36:46Z without re-tripping the auto-disable. **Verification is partial and stated as such** — one forced run proves repo access, not that the hourly cron survives. §12 now carries a **last-verified date convention**: the claim "LIVE as of 2026-07-04" was true for 3 hours and 41 minutes. — Claude Code (Opus 4.8)
- 2026-07-15 — **Department built: 4 agents wired onto `arika-runtime`** (§5), deliberately two-sided per §1's dual mandate — `automation-reliability-monitor` (Class 1, daily cron — **the control whose absence made the outage invisible**), `automation-approval-gate` (Class 2, human-gated), `automation-workflow-architect` (offer #6), `automation-process-architect` (offer #7). Boundaries set against `marketing-ops-governor` (03, marketing-scoped) and `operations-state-monitor` (08, business state vs. machinery state) — a department can report green on 08 and be entirely un-automated, which is exactly what happened. — Claude Code (Opus 4.8)
- 2026-07-15 — **🔴 §3 corrected: "Internal automation — not started, not yet scoped" was stale.** `arika-runtime` (90 agents, 21 cron triggers) **is** the agency's internal automation, built 2026-07-14/15. **11 of 12 department OS files referenced it; this one — the department that owns internal automation — was the only one that didn't.** §13's "code-based automation not built" corrected for the same reason. — Claude Code (Opus 4.8)
- 2026-07-15 — **🔴 Governance gap flagged, not papered over (§12): 21 runtime cron triggers, 1 matrix row.** Not a live breach only because the runtime is a local process nobody has booted with a key — the triggers are declared, not scheduled. One `npx tsx src/index.ts` away from 21 ungoverned automations firing. Rows deliberately **not** written: whether it's 21 rows or one covering row is an owner call, and writing rows for agents that have never run would document an intention as a fact. `automation-approval-gate` returns `blocked` on any request to daemonize the runtime until rows exist. **Also flagged: the hybrid model's cloud mirror was never built** — 21 schedule triggers, 1 cloud routine, and that routine isn't spec-derived. — Claude Code (Opus 4.8)
- 2026-07-04 — **Creative Pipeline Automation went live.** Both prerequisites resolved same session: Notion connector for cloud routines confirmed already attached (stale "zero connectors" reading corrected); "Publishing Status" converted from a native status property to a plain select with a new "Ready for Design" option (0 rows, no data loss). Real routine created and enabled: `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron, Notion-only connector (no OpenArt/Canva — the credit-spend gate is enforced by omission, not just instruction). Closes tracker items 54-55 and `GO_LIVE_CHECKLIST.md` Phase 9 items 41-43. — Claude Code (Sonnet 5)
- 2026-07-04 — **Creative Pipeline Automation specified** for Design (19) — real Notion-trigger + cron cloud-routine mechanism, human gate before credit spend, Risk Class 2. Real row added to `AUTOMATION_APPROVAL_MATRIX.md`. Not activated — 2 real prerequisites tracked as `OWNER_INPUT_NEEDED.md` items 54-55. Experience Engineering (20)'s equivalent automation flagged as un-specifiable until a first real project exists (item 51). Cross-referenced from `19_Design/DESIGN_OS.md` §12 and `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` §12. — Claude Code (Sonnet 5)
- 2026-06-30 — Department created, promoted from Offer (02)'s "Automation" division category per owner decision. Seeded from `Draft 35` (offer #6, AI Workflow Infrastructure) and `Draft 36` (offer #7, Business Operating Systems), both owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-01 — Added the Engagement Layer capability (Post → Comment/keyword trigger → DM → lead-magnet delivery → CRM capture → Sales), proposed platform ManyChat, per the new Design (19) department's founding planning session. Flagged as needing an `AUTOMATION_APPROVAL_MATRIX.md` row before going live, consistent with the existing human-in-the-loop constraint in §9. — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 4 agents (§5) write to `16_Automation/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope. **This stream matters more here than in any other department**: it is the only durable record of whether the agency's automations were actually running on a given day. The 11-day outage (§9) is precisely what an unbroken `automation-reliability-monitor` stream would have made undeniable — and there was no stream, because there was no agent.

**Feedback Loop.** Both §7 KPIs remain **unset**, and honestly so:
- **Automation failure rate** — `Draft 35` Phase 10 sets a **<2% go-live gate**, but the estate has no failure-rate data because almost nothing has ever run. The one real automation has **two data points**: one success (2026-07-04) and one success after an 11-day death (2026-07-15). **Do not report 0%.** There is no baseline.
- **SOP adherence rate** — needs a delivered offer #7 engagement. None exists.

The one loop that *is* real: `automation-reliability-monitor` → `AUTOMATION_SILENTLY_DEAD` → `automation-approval-gate`, and both hand to `operations-state-monitor` (08). It is wired and has never fired in anger.

**Cadence.** This department runs against two of the 7 Cognitive Calendars (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4): the **Operational Calendar** — `automation-reliability-monitor`'s daily `17 8 * * *` check is the department's only true clock-driven work — and the **Pipeline Calendar** for the two client offers, which are engagement-triggered, not calendared. Client delivery is per-engagement (14-60 days for offer #6, 30-90 for offer #7); none has ever run.

**⚠️ Note the recursion, and don't let it hide:** `automation-reliability-monitor` is itself a cron trigger on the runtime — so it is subject to the exact failure it exists to detect. **If the runtime isn't booted, the monitor doesn't run, and nothing reports that the monitor isn't running.** Today that is true: the runtime is not a daemon, so the monitor is declared, not scheduled. Until the runtime runs persistently (which needs matrix rows first, §12), **the estate's only monitor is a human choosing to run `arika run automation-reliability-monitor`.** That is the honest state, and it is a weaker guarantee than this section would otherwise imply.
