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

No real automation engagements (client or internal) have run yet.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| AI Workflow Infrastructure | AI/agent execution layer — CRM automation, AI agents, workflow orchestration, internal copilots | Offer engineered (`Draft 35`), not yet delivered |
| Business Operating Systems | Process/documentation layer — SOPs, dashboards, KPI ownership, org-design clarity | Offer engineered (`Draft 36`), not yet delivered |
| Internal automation (agency's own operations) | Same systems as above, applied to Arika Agency itself once mature enough to deploy internally | Not started — flagged as a future opportunity, not yet scoped |
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

*(placeholder — the offer-engineering files use functional role labels — Automation Engineer, Integration Specialist, Process Analyst, Dashboard/BI Engineer — describing AI-assisted execution functions the owner currently performs solo, not real hires. See `11_HR_People_Ops/HR_OS.md` for when real staffing becomes relevant.)*

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

*(placeholder — empty. Note: `Draft 35` flags a hard immutable constraint — human-in-the-loop required for any client-facing AI output, no fully autonomous deployment without a review gate. Carries forward into any real incident logging once delivery begins. The Engagement Layer (§3, §4) is a concrete future instance of this constraint: it acts on real customer messages, so per `GLOBAL_OS.md` §3's Class 3+ sign-off rule, it needs a real row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` before it goes live — not created in this pass, since ManyChat isn't connected yet.)*

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

**Creative Pipeline Automation (Design 19) — LIVE as of 2026-07-04.** Real trigger: Content (04)'s Notion content-brief database (`collection://1f0ed36e-a548-4743-9947-f408f8811140`), "Publishing Status" field equals the literal value **"Ready for Design."** Real mechanism: a durable Anthropic cloud routine, `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron (`7 * * * *`), repo `https://github.com/arikaagencyio-sketch/Arika`, Notion connector attached (connector_uuid `f957ca4d-bcce-43a2-9f31-9b6954efeee1`) — deliberately no OpenArt/Canva connector, so the credit-spend gate is enforced by the session's tool access, not just its instructions. First scheduled run `2026-07-04T14:07:00Z`.

Each run: queries the content-brief database for "Ready for Design" pages; for each match, reads `.claude/agents/design-storyboard-generator.md` and `.claude/agents/design-production-engine-coordinator.md` in this repo and follows their instructions to draft a 7-field storyboard and a planning-only Production Engine recommendation (tool choice per stage, no actual generation call possible); posts both as a Notion comment on the brief for owner review. It does not change the brief's own status, make git commits, or spend any OpenArt/Canva credit — a human moves the brief forward after reviewing the comment.

Both build blockers resolved same session: the Notion cloud-routines connector was already attached (the earlier "zero connectors" reading was stale), and "Publishing Status" was converted from a native status property (which doesn't accept custom options via the available schema-update API) to a plain select with the new "Ready for Design" option — the database had 0 rows, so no data loss. Full history: `OWNER_INPUT_NEEDED.md` items 54-55 (Resolved table), `GO_LIVE_CHECKLIST.md` Phase 9.

**Creative Pipeline Automation (Experience Engineering 20) — cannot be specified yet.** No real trigger condition exists to poll for until tracker item 51 (first real project) resolves.

## 13. Existing OS Sub-Layer

None yet — code-based automation not built. The offer-engineering content (`Draft 35`, `Draft 36`) is the canonical design reference.

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offers #6-7) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-07-04 — **Creative Pipeline Automation went live.** Both prerequisites resolved same session: Notion connector for cloud routines confirmed already attached (stale "zero connectors" reading corrected); "Publishing Status" converted from a native status property to a plain select with a new "Ready for Design" option (0 rows, no data loss). Real routine created and enabled: `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron, Notion-only connector (no OpenArt/Canva — the credit-spend gate is enforced by omission, not just instruction). Closes tracker items 54-55 and `GO_LIVE_CHECKLIST.md` Phase 9 items 41-43. — Claude Code (Sonnet 5)
- 2026-07-04 — **Creative Pipeline Automation specified** for Design (19) — real Notion-trigger + cron cloud-routine mechanism, human gate before credit spend, Risk Class 2. Real row added to `AUTOMATION_APPROVAL_MATRIX.md`. Not activated — 2 real prerequisites tracked as `OWNER_INPUT_NEEDED.md` items 54-55. Experience Engineering (20)'s equivalent automation flagged as un-specifiable until a first real project exists (item 51). Cross-referenced from `19_Design/DESIGN_OS.md` §12 and `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` §12. — Claude Code (Sonnet 5)
- 2026-06-30 — Department created, promoted from Offer (02)'s "Automation" division category per owner decision. Seeded from `Draft 35` (offer #6, AI Workflow Infrastructure) and `Draft 36` (offer #7, Business Operating Systems), both owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-01 — Added the Engagement Layer capability (Post → Comment/keyword trigger → DM → lead-magnet delivery → CRM capture → Sales), proposed platform ManyChat, per the new Design (19) department's founding planning session. Flagged as needing an `AUTOMATION_APPROVAL_MATRIX.md` row before going live, consistent with the existing human-in-the-loop constraint in §9. — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

*(placeholder — structure only, no agent roster exists yet to generate real memory/feedback entries; see §5, which describes only offer-engineering functional role labels — Automation Engineer, Integration Specialist, Process Analyst, Dashboard/BI Engineer — for AI-assisted execution the owner currently performs solo, not a real agent roster.)* Once this department has a real or code-based agent roster (per the Tier 1 pattern in `05_Sales/SALES_OS.md` §16), this section should define: **Memory** (where Decision/Learning/Prompt-Evolution logs live), **Feedback Loop** (what happens when a §7 KPI misses threshold), and **Cadence** (which of the 7 Cognitive Calendars — `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — this department's workflows run against, and how often).
