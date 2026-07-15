# Audits & Diagnostics — Department OS

**Department:** Audits & Diagnostics (14)
**Position in flow:** The agency's Gateway — sits upstream of Sales (05), feeding qualified, diagnosed prospects into the offer-ascension model. Reports into Agency Governance (00).
**Mandate:** Own the agency's fast, fixed-fee diagnostic offers — the Revenue Infrastructure Audit and any future audit/diagnostic products — as standalone delivery, distinct from the larger infrastructure-build offers they feed into.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

**Newly created department (2026-06-30)**, promoted from a category inside the Offer (02) catalog after the owner decided Draft 28's "Audits & Diagnostics" division deserved its own department rather than staying purely an offer-internal grouping. Its founding offer — Revenue Infrastructure Audit — is the agency's own named **Gateway Offer**, confirmed in 3 separate places within `02_Offer/Agency Pricing Architure. Draft 28.md` (Entry Tier, Gateway Offers list, Stage 1 of the Ideal Ascension Model), and the most source-confirmed cross-offer relationship in the entire Offer Engineering Registry.

## 2. Status

**Content seeded from Offer's catalog, not yet operationally run.** Full offer engineering exists (`02_Offer/OEOS - Audits and Diagnostics Division - Revenue Infrastructure Audit (Claude-Synthesized). Draft 39.md`) — Phase 1 (offer identity) and Phase 2 (positioning) are real, owner-sourced (from Draft 28); Phases 3-12 are Claude-synthesized, owner-approved as-is 2026-06-30. No real audits have been delivered yet — this department has no operating history of its own.

**Agents built 2026-07-15 (6, see §5) — the delivery chain is wired, not proven.** Every honest caveat above still holds and is now encoded in the agents themselves: no audit has ever been delivered, so there are no benchmarks, no calibrated thresholds, no house report template, and no conversion data. The chain has never run end-to-end. **`AUDIT_ENGAGEMENT_SIGNED` has no emitter** — an audit engagement is signed by a human, and nothing upstream publishes the event, so today the chain starts with a manual run.

**The Gateway claim is partly unbacked.** This department is described as "the agency's Gateway," but Draft 28 names **five** Gateway offers and this department engineers **one** — see §3.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Revenue Infrastructure Audit | Fast (7-14 days), fixed-fee, 7-sub-audit diagnostic (funnel, sales, CRM, automation, acquisition, team, offer) | Offer engineered (`Draft 39`); chain wired 2026-07-15 (§5), **not yet delivered** |
| Sub-audit modularity | Each of the 7 sub-audits is itself a discrete, potentially standalone diagnostic — the most modular backbone of any offer in the catalog | Productized as the **Lite tier** — see the Gateway reconciliation below |

### The Gateway Offer count — reconciled 2026-07-15 (owner-decided)

`Agency Pricing Architure. Draft 28.md` names **five** Gateway offers; this department engineers **one**. Resolved from source where the source allows, flagged where it doesn't:

| Draft 28 Gateway offer | Stated goal | Resolution |
|---|---|---|
| Revenue Audit | Diagnose pain | **Offer #10, this department.** Built. |
| Funnel Audit | Show missed revenue | **Not a separate offer — it is offer #10's Lite tier.** `Draft 39` Phase 11 defines Lite as "a single targeted sub-audit (*e.g. funnel-only*)". Source-confirmed, not asserted. Draft 28's Ideal Ascension Model calls the same thing "Funnel **Diagnostic**" — a naming inconsistency within one document, same product. |
| AI Opportunity Assessment | Introduce transformation | **⚠️ REOPENED 2026-07-15 — contested, owner decision.** Routed to **AI Enablement (17)** on 2026-07-15 by division association (offer #11's department). Auditing Automation (16) the same day surfaced **direct textual counter-evidence**: `Draft 35` Phase 12 names **"AI Opportunity Audit" as a standalone entry offer productized from offer #6 (Automation)** — *"same audit-as-entry-offer pattern as offer #10."* The evidence is genuinely split: **"AI Opportunity"** matches Draft 35 (→16); **"Assessment"** matches offer #11's *"AI Readiness Assessment System"* and the stated goal **"Introduce transformation"** is offer #11's own word (→17). Direct text beats division association, but the naming cuts both ways. **The earlier by-division call is downgraded to provisional pending your decision.** |
| Growth Workshop | Strategic authority | **Consulting & Advisory (15)** by division (offer #9's department). Unbuilt — 15 has an OS file and no agents. |
| Sales Call Review | Demonstrate expertise | **⚠️ Genuinely unbuilt and unassigned.** Narrower than offer #10's `sales` sub-audit — a call review is not a sales-process audit — so Lite doesn't absorb it the way it absorbs Funnel Audit. Not OEOS-engineered, no Phase 1 seed data in Draft 28 beyond the name and goal. **Owner decision: is this a real micro-offer (14 or 05), or a name Draft 28 listed without intending a product?** |

**Consequence:** the "agency's Gateway" is, today, **one engineered offer of five named**, and three of the four gaps sit in departments that don't exist yet as agents (15, 17) or aren't assigned (Sales Call Review). Stage 1 of the ascension model is thinner than the pricing architecture implies.

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Revenue Infrastructure Audit delivery | Signed audit engagement (**human — no emitter**, see §12) | Scoping → Data/Access Collection (Day 1-3) → Parallel Sub-Audit Analysis (Day 3-10) → Synthesis & Quantification (Day 10-12) → Report Production (Day 12-13) → Delivery & Review Call (Day 14) | Findings report + ascension-path recommendation | Mary Thuo | `Draft 39` (synthesized) |

## 5. Agent Roster

**6 agents, built 2026-07-15.** They map onto `Draft 39` Phase 5's real functional roles (Client Partner, Strategy Lead, Audit Analysts, QA Specialist) — AI-assisted execution functions the owner currently performs solo, **not hires**. See `11_HR_People_Ops/HR_OS.md` for when real staffing becomes relevant.

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `audits-scoping` | 2 | `AUDIT_ENGAGEMENT_SIGNED` → `AUDIT_SCOPED` | Which sub-audits, which tier, fixed fee + 7-14 day commitment |
| `audits-data-access-gate` | 1 | `AUDIT_SCOPED` → `AUDIT_DATA_READY` / `AUDIT_DATA_INCOMPLETE` | Phase 10's data-completeness gate; sets `quantification_depth` |
| `audits-subaudit-analyst` | 1 | `AUDIT_DATA_READY` → `SUBAUDIT_COMPLETE` | Runs **one** sub-audit against the owning department's standard |
| `audits-quantification` | 2 **+ human-gated** | `SUBAUDIT_COMPLETE` → `FINDINGS_QUANTIFIED` | The immutable quantification rule + Phase 10's second-analyst spot-check |
| `audits-report-producer` | **3** | `FINDINGS_QUANTIFIED` → `AUDIT_REPORT_READY` | The only required deliverable + the executive-clarity gate |
| `audits-ascension-recommender` | 2 | `AUDIT_REPORT_READY` → `ASCENSION_RECOMMENDED` / `NO_ASCENSION_PATH` | Stage 1 → Stage 2, or honestly no path |

**`audits-report-producer` is Class 3** — client-facing *and* money-facing (a paid deliverable carrying financial claims), matching the precedent set by `client-success-offboarding`. Per the Constitution, human sign-off is required at Class 3+ **with no exceptions carved out by convenience or urgency** — the fixed timeline is not a reason to skip it. `audits-quantification` is Class 2 but carries `requires_human_approval: true` because `Draft 39` Phase 10 *itself* requires a second analyst to review every dollar estimate.

### The audit lens vs. the standard — the department's defining rule

Each of the 7 sub-audits names an area **another department already owns the standard for**. This department owns the **audit lens**; it does not own — or restate — the standard:

| Sub-audit | Standard set by | Live agents there? |
|---|---|---|
| `funnel` | Marketing (03) | ✅ `marketing-funnel-architect` |
| `sales` | Sales (05) | ✅ `sales-revenue-operations`, `sales-execution-closing` |
| `crm` | ClientPartner (06) + Sales (05) | ✅ `clientpartner-crm-architect` |
| `automation` | Automation (16) | ✅ **as of 2026-07-15** — `automation-workflow-architect`, `automation-process-architect`, `automation-reliability-monitor` |
| `acquisition` | ClientPartner (06) | ✅ **delegated — see below** |
| `team` | HR (11) | ✅ **as of 2026-07-15** — `PEOPLE_DOCTRINE.md`, `HR_RESEARCH.md`, + 4 agents |
| `offer` | Offer (02) | ✅ `offer-oeos-engineer`, `offer-pricing-floor-analyst` |

**Note the asymmetry:** those agents *design*; they are not auditors. Only 06's is a diagnostic. So the sub-audits are not "already covered" — the owning departments hold the standard an audit judges against, and turning that into "here is what's broken in *this* client's" is 14's job.

**`acquisition` is delegated, not duplicated.** `clientpartner-acquisition-diagnostic` (06) **already is** this sub-audit — it audits a client's real acquisition system with a 12-input intake, a 5-control-point friction diagnosis, and the client-vs-partner separation check. `audits-subaudit-analyst` sets `delegated_to: clientpartner-acquisition-diagnostic` and carries its output through. Two diagnostics of the same thing would drift, and the client would be shown both.

**Updated 2026-07-15 — the `automation` hole closed the same week it was flagged.** Automation (16) was built with 4 agents, so the `automation` sub-audit now has a real standard to judge against: `Draft 35`'s four immutables (audit-before-automate, human-in-the-loop on client-facing AI output, security/data-handling review, a documented manual-override path) and its **<2% automation failure rate** go-live gate, plus `Draft 36`'s process-mapping discipline. Better still, 16's `automation-reliability-monitor` is a genuine **auditor**, not a designer — the same shape as 06's acquisition diagnostic. **`audits-subaudit-analyst` may delegate the `automation` sub-audit to it** where the client's estate needs checking rather than designing.

**Updated 2026-07-15 — the last hole closed the same week it was flagged.** HR (11) was built with a **People Doctrine**, **Kenya labour + payroll research**, and 4 agents. The `team` sub-audit now has real ground: the **Control / Integration / Substance** classification tests, the **real cost of employment** (~7.5% employer add-on plus remittance machinery), the **delegability ceiling** as a structural constraint, and the **hiring-trigger doctrine** (*people are a consequence of revenue, not a route to it*). `hr-engagement-classifier` is a genuine **auditor** of an arrangement — the same shape as 06's acquisition diagnostic and 16's reliability monitor — so **`audits-subaudit-analyst` may delegate the `team` sub-audit to it** where a client's engagements need checking rather than designing.

**All 7 sub-audits now rest on a department with agents.** The Gateway Offer's lens is complete for the first time.

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Audit-to-implementation conversion rate | Audits sold that ascend to a larger offer ÷ total audits delivered | `02_Offer/OFFER_OS.md` §3 (ascension model) | Mary Thuo | Per-audit | *(unset — no real data yet)* |
| Audit delivery timeline adherence | Actual delivery day vs. the 7-14 day target | `Draft 39` | Mary Thuo | Per-audit | *(unset)* |

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

Full offer-engineering detail (backbone systems, immutable components, QA gates, risk register) lives in `02_Offer/OEOS - Audits and Diagnostics Division - Revenue Infrastructure Audit (Claude-Synthesized). Draft 39.md` — cited here rather than duplicated, per the Offer department's existing registry pattern.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Audit delivery | Audits & Diagnostics (14) | Audits & Diagnostics (14) | Offer (02) | Sales (05), Sector (01) |
| Ascension handoff to a larger offer | Audits & Diagnostics (14) | Sales (05) | Offer (02) | Client Success (07) |

## 12. Triggers / Automation Hooks

The chain runs on `arika-runtime` (`GLOBAL_OS.md` §5). Six agents, wired manual + event.

**Known gaps — flagged, not worked around:**

1. **`AUDIT_ENGAGEMENT_SIGNED` has no emitter.** An engagement is signed by a human, and no agent publishes the event. The chain starts with a manual `arika run audits-scoping`. Sales (05) is the natural emitter once a closed-won audit deal can announce itself.

2. **⚠️ The sub-audit fan-in is *dynamic*, and the runtime's join primitive cannot express it.** `Draft 39` Phase 5 runs the scoped sub-audits in parallel and then synthesizes — synthesis must wait for **all of them**. The runtime gained a `type: join` barrier on 2026-07-15 (`waits_for: [A, B, ...]` + `correlate_on`), which fires once every awaited event lands. But it awaits a **fixed set of distinct event types**, and this department's set is **decided at scoping**: a Lite engagement runs one sub-audit, a full-stack runs seven. A barrier hard-wired to all seven would deadlock on every Lite audit; a barrier on fewer would fire early on a full-stack one.

   So `audits-quantification` is wired `type: event` on `SUBAUDIT_COMPLETE` and **fires per sub-audit, not once per audit**. A human synthesizes across them. This is honest but incomplete.

   The real fix is a **counting barrier** — one that reads its expected membership from `AUDIT_SCOPED`'s `scoped_subaudits` at runtime rather than from the spec. It was **not** built, deliberately: this department has never delivered an audit, so a dynamic-fan-in primitive would be designed entirely against a workflow no one has ever run. Build it when a real audit demands it.

3. **In-memory joins don't survive a restart.** Even where the fixed barrier applies, it holds state in-process. An audit spans **7-14 days**; the runtime does not. Any cross-day barrier needs the durable bus `EventBus` was designed to be swapped for.

## 13. Existing OS Sub-Layer

No department-local code layer. The 6 agents (§5) run on the shared `arika-runtime`; their memory stream is `14_Audits_Diagnostics/_memory/runtime.jsonl`. The offer-engineering content (`Draft 39`) remains the canonical design reference.

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offer #10) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-06-30 — Department created, promoted from Offer (02)'s "Audits & Diagnostics" division category per owner decision. Seeded from `Draft 39` (offer #10, Revenue Infrastructure Audit), owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-15 — **Department built: 6 agents wired onto `arika-runtime`** (§5), covering scoping → data gate → sub-audit analysis → quantification → report → ascension. `audits-report-producer` is **Class 3** (client- and money-facing paid deliverable, matching `client-success-offboarding`'s precedent); `audits-quantification` is human-gated because `Draft 39` Phase 10 itself requires a second-analyst review of every dollar estimate. — Claude Code (Opus 4.8)
- 2026-07-15 — **Gateway Offer count reconciled** (§3, owner-decided). Draft 28 names 5 Gateway offers; this department engineers 1. **Funnel Audit resolved from source as offer #10's Lite tier** (`Draft 39` Phase 11 defines Lite as "a single targeted sub-audit (e.g. funnel-only)") — also resolving Draft 28's internal "Funnel Audit" vs. "Funnel Diagnostic" naming inconsistency. AI Opportunity Assessment → AI Enablement (17), Growth Workshop → Consulting & Advisory (15), both by division. **Sales Call Review flagged as genuinely unbuilt and unassigned — open owner decision.** — Claude Code (Opus 4.8)
- 2026-07-15 — **Sub-audit boundary set: this department owns the audit lens, not the standard** (§5). Each of the 7 sub-audit areas is judged against the owning department's documented standard. **`acquisition` delegated to 06's existing `clientpartner-acquisition-diagnostic`** rather than duplicated — it already is that sub-audit; two diagnostics of the same thing would drift and the client would be shown both. `automation` (16) and `team` (11) flagged as resting on departments with no agents. — Claude Code (Opus 4.8)
- 2026-07-15 — **Dynamic sub-audit fan-in flagged as unwireable** (§12). The runtime's new `join` barrier awaits a fixed set of event types; this department's set is decided at scoping (1 sub-audit on Lite, 7 on full-stack), so a fixed barrier would deadlock or fire early. Quantification fires per sub-audit and a human synthesizes. A counting barrier was deliberately **not** built — no audit has ever been delivered, so it would be designed against a workflow no one has run. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 6 agents (§5) write to `14_Audits_Diagnostics/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope (`{timestamp, agent, department, stream, event_type, source, payload}`) — the same format every other department's agents use. **The stream is empty**: no agent has been run against a real engagement.

**Feedback Loop.** Both §7 KPIs are **unset and uncalibratable** — audit-to-implementation conversion and delivery-timeline adherence each need delivered audits to have a value at all, and none exist. Until then there is no threshold to miss and no loop to run. The first delivered audit sets the first real data point; thresholds should be derived from actual runs rather than assumed now (the same discipline applied to bois' 15 uncalibrated thresholds in `12_Branding/BRANDING_OS.md`).

**Cadence.** Per-engagement, not calendared — this department's work is triggered by a signed engagement, not by a clock. It touches two of the 7 Cognitive Calendars (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4): the **Pipeline Calendar** (an audit is Stage 1 of the ascension model and feeds Stage 2 opportunities via `audits-ascension-recommender`) and the **Cash Flow Calendar** (fixed-fee, one-time, fast — `Draft 28` names Stage 1's revenue role as "fast cash flow, low operational load"). Neither link is live; both are structural until an audit is actually sold.
