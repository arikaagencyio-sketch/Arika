# Operations — Department OS

**Department:** Operations (08)
**Position in flow:** Receives scoped engagements from Client Success (07); executes delivery; hands billable events to Finance (09). **And** — orchestrates execution across every department.
**Mandate:** Own delivery execution, SOPs, capacity planning, and quality control — **and** the agency's own real-time execution: the daily to-do, the 7 Cognitive Calendars, focus, and cross-department state.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.
> **Read [`OPERATIONS_CONSTITUTION.md`](OPERATIONS_CONSTITUTION.md) before operating in this department** — it carries the doctrine (ROCBO, the 5 Foundational Realities, the 7 Calendars, the dual scope, the anti-patterns, and the honest gap list).

---

## 1. Identity

Operations is where **action lives**. Not planning, not brainstorming, not strategy. Every other department decides *what is true* and *what should happen*; Operations decides **what is happening today, and whether it is actually getting done.**

The discipline has a real, owner-given name (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md`): **Revenue-Oriented Cognitive Business Operations (ROCBO)**.

It answers the Vision's Layer 7 question — *"Can we deliver without breaking the system?"* — but its real remit is broader: it is the **execution and orchestration layer over the whole OS**, running **two books at once**:

| Scope | Meaning |
|---|---|
| **Agency Operations** | Running Arika itself — daily to-do, revenue heartbeat, focus, capacity, opportunity selection, cross-department state |
| **Client Operations** | Delivering for clients — engagements, projects, timelines, QA, delivery risk |

*Naming note:* the source material's **"Integrated Revenue Intelligence System (IRIS)"** (`05_Sales/…Draft 9`) is conceptually the same as the Vision's *Revenue Intelligence and Execution System* — treated as an **alias for the unified system**, not a separate department. See the constitution §1.

## 2. Status

**Deliberately built last, and now live (2026-07-14).** This department was left blank on purpose: it is not a peer department with its own slice of the flow — it is the layer that plugs the full scope together, so it could only be written once every other department had a real, runnable agent layer to orchestrate. That condition was met on 2026-07-14 (7 departments, 40 agents live).

**It still has zero raw drafts** — that hasn't changed and doesn't need to. Instead, Operations is grounded in the **contracts its neighbours already wrote for it**, all real and confirmed:

| Source | What it contributes |
|---|---|
| `AGENCY_REVENUE_TARGETS.md` | ROCBO, the 7 Cognitive Calendars, the $1M/$35K targets, the daily target table, Path A/B deal math, pipeline scoring vars, the anti-patterns |
| `AGENCY_VISION.md` | The 5 Foundational Realities, Layer 7 (Operations) + Layer 9 (Intelligence), the Financial Orchestration Layer, the closed-loop logic |
| `AGENCY_OPERATING_CONSTITUTION.md` | The supreme Class 0–4 risk model |
| `CRM_SCHEMA.md` | The **live** ClickUp `Project` pipeline (`scoped → in-delivery → review → complete`) |
| `07_Client_Success/CLIENTSUCCESS_OS.md` §10 | The reconciled "CS scopes, Operations executes" handoff + the `SCOPE_DEFINED` event |
| `02_Offer/OFFER_OS.md` §3 (OEOS) | Per-offer delivery: Internal Execution Journey, Deliverable Engineering, Timeline Architecture, Communication Architecture, QA System, risk register |
| `01_Sector/SECTOR_OS.md` | The real 7-stage client engagement model + agency maturity arc |

**No agency facts were invented.** Every genuine gap is listed in the constitution §7 and §7 below.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| **Daily command / focus engine** | Turns the real $35K/day targets into today's ranked actions; reports the revenue gap; rejects anti-pattern work | **Live** (`operations-daily-command`) — targets real, actuals unmeasured |
| **7 Cognitive Calendar synchronization** | Keeps Revenue · Pipeline · Operational · Cash Flow · Capacity · Opportunity · Strategic informing each other; surfaces cross-calendar conflicts | **Live** (`operations-calendar-orchestrator`) — reasoned, not dashboard-fed |
| **Opportunity filtering** | "Is this opportunity worth the system energy it consumes?" — the 7 revenue-mathematics questions + anti-pattern rejection | **Live** (`operations-opportunity-filter`) |
| **Capacity gating** | Prevents overselling past fulfilment ability | **Live but constrained** (`operations-capacity-planner`) — **no capacity model exists**; agent flags rather than invents |
| **Cross-department state** | "What is actually happening vs. what we think is happening" — real-time state, broken links, alignment | **Live** (`operations-state-monitor`) |
| **Delivery scheduling** | Scoped engagement → sequenced plan against OEOS timeline architecture; drives the live Project pipeline | **Live** (`operations-delivery-scheduler`) |
| **Delivery QA** | OEOS Phase 10 quality gates; releases the billable event to Finance | **Live** (`operations-delivery-qa`) |
| **Delivery risk** | Client-constraint archetypes + risk register + blocker escalation | **Live** (`operations-delivery-risk`) |
| **SOP architecture** | The department's originally-stated primary purpose | **Open** — the constitution is the first real SOP; per-workflow SOPs accrue as real runs happen |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| **Daily command loop** (agency) | Daily 06:00 → 07:00 (Mon–Fri) | `operations-state-monitor` reports state → `operations-daily-command` ranks today's actions against the daily target table | Today's focus + ranked actions + revenue gap | Mary Thuo |
| **Weekly calendar sync** (agency) | Monday 07:00 | `operations-calendar-orchestrator` reads all 7 calendars → surfaces conflicts → `recommended_sequence` | Synchronized calendars + named conflicts | Mary Thuo |
| **Opportunity intake gate** (agency) | `OPPORTUNITY_PROPOSED` / `EXPANSION_IDENTIFIED` / `PROSPECT_SCORED` | `operations-opportunity-filter` (7 questions, anti-patterns) → if `pursue`, `operations-capacity-planner` must clear it | pursue / defer / decline + capacity verdict | Mary Thuo |
| **Client delivery chain** (client) | `SCOPE_DEFINED` from Client Success | `operations-delivery-scheduler` (plan + Project → in-delivery) → `operations-delivery-risk` (monitor) → `operations-delivery-qa` (gates → review → complete) → `DELIVERY_COMPLETE` → Finance (09) | Delivered engagement + billable event | Mary Thuo |
| **Risk escalation** (client) | `QA_FAILED` / archetype detected / non-payment | Classify severity (4-tier: Critical <4hr → Low <1wk) → route (relationship → CS 07; money → Finance 09; schedule → scheduler) | Mitigation + escalation | Mary Thuo |

**The rule:** *state before plan.* No day gets planned before `operations-state-monitor` reports.

## 5. Agent Roster

**Live in the Arika Runtime as of 2026-07-14** — 8 advisory-first agents (`.claude/agents/operations-*.md`, memory → `08_Operations/_memory/runtime.jsonl`). The largest roster in the repo, because Operations carries the dual scope.

**Agency-side (running the business):**

| Agent | Owns | Class |
|---|---|---|
| `operations-state-monitor` | "Where we are at" across all 21 departments; broken links; alignment | 1 |
| `operations-daily-command` | Today's to-do/focus vs. the $35K/day targets; the revenue gap | 1 |
| `operations-calendar-orchestrator` | The 7 Cognitive Calendars + cross-calendar conflicts | 1 |
| `operations-opportunity-filter` | The 7 questions; anti-pattern rejection; pursue/defer/decline | 1 |
| `operations-capacity-planner` | Can we deliver without breaking? (**flags the missing model**) | 1 |

**Client-side (delivery):**

| Agent | Owns | Class |
|---|---|---|
| `operations-delivery-scheduler` | `SCOPE_DEFINED` → delivery plan → Project `in-delivery` | 2 |
| `operations-delivery-risk` | Constraint archetypes, risk register, blocker escalation | 2 |
| `operations-delivery-qa` | OEOS QA gates → Project `complete` → `DELIVERY_COMPLETE` to Finance | 2 |

**Not a separate agent, by design:** "AI Orchestration / Tool-Use / Multi-Agent Orchestration" — `arika-runtime/` provides that substrate natively (same call as Sales' §5).

## 6. Skill Library Index

*(none yet — skills accrue from real runs. The constitution is the first real standard; per-workflow SOPs are §10's open item.)*

## 7. KPI Dictionary (department-local)

**The daily target table is Operations' primary KPI set** — real, owner-confirmed targets (`AGENCY_REVENUE_TARGETS.md`), **but nothing has been measured against them yet**. They are targets, not history.

| Metric | Daily target | Status |
|---|---|---|
| Revenue Closed | $35,000 | Real target · **no actuals** |
| Quotations Sent | $150,000 | Real target · no actuals |
| Discovery Calls | 12 | Real target · no actuals |
| Qualified Prospects | 25 | Real target · no actuals |
| Outbound Contacts | 300 | Real target · **flag if real capacity contradicts** |
| Follow-Ups | 50 | Real target · no actuals |
| Proposals | 7 | Real target · no actuals |
| Closed Deals | 5 (≥$7K each) — or 7 quotations ≥$5K | Real target · no actuals |

**Delivery KPIs** come from the engagement's own OEOS spec, not an agency-wide standard (Offer #1's real examples: data accuracy <1% error, uptime 99.9%, forecast variance <±15%, dashboard latency <1hr/<24hr).

**⚠️ Carried inconsistency — reported, never smoothed:** $35K/day × ~21.7 business days ≈ **$759K–$770K/month, ~23–24% short of the $1M target.** Unresolved by the owner; `operations-daily-command` reports the gap every run.

## 8. Decision Log

- **2026-07-14 — Operations defined as the execution/orchestration layer over the whole OS, not a peer department.** Owner's direction: it was left blank deliberately, to be built last, from scratch, once every department was aligned — "it was to plug in the full scope."
- **2026-07-14 — Adopted ROCBO as the department's doctrine** and the 5 Foundational Realities as its constitution's backbone; both already existed in owner-confirmed governance files.
- **2026-07-14 — Confirmed the dual scope** (agency operations AND client operations) as co-equal; neither may starve the other.
- **2026-07-14 — IRIS classified as an alias for the unified system, not a separate department** — it appears in one draft (itself generic AI output) and is conceptually identical to the Vision's Revenue Intelligence and Execution System.
- **2026-07-14 — Capacity model confirmed as a genuine gap, not filled.** `operations-capacity-planner` must flag it on every run rather than invent utilization/headcount figures.

## 9. Risk / Incident Log

*(empty — no incidents yet.)* The department's live risk framework is the OEOS client-constraint archetypes + the 17-item risk register shape, with the 4-tier severity response protocol (Critical <4hr → Low <1 week) — see `operations-delivery-risk`. Known standing risk: **asset-collection delay is the #1 timeline blocker (Critical)**.

## 10. Standards & SOPs Index

**[`OPERATIONS_CONSTITUTION.md`](OPERATIONS_CONSTITUTION.md) is this department's primary standard** — ROCBO, the dual scope, the 5 Foundational Realities, the 7 Calendars, Revenue Mathematics + the 7 questions, the anti-patterns, the real targets, the gap list, authority/risk, and execution discipline.

Core rules extracted:
- **Action over analysis** — a run that produces no next action failed.
- **State before plan** — never plan a day without reading where the business is.
- **Everything must be linked** (Sector's doctrine) — Sector → Insight → Opportunity → Offer → Client → Project → Result. *"If anything is not connected, it's noise."*
- **Every activity answers the 7 questions**, or it doesn't go on the list.
- **Reject:** meaningless meetings · vanity tasks · random content · fake productivity · outreach without qualification · fulfilment without monetization logic.
- **Advisory-first** — Operations produces the list, the plan, the gate, the state. A human executes.
- **Operations orchestrates; it does not overrule** a department's mandate. It surfaces conflicts.

**Open:** per-workflow SOPs (the department's originally-stated primary purpose) accrue as real runs happen — this was always meant to be written from execution, not theory.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Daily command / focus | Operations (08) | Mary Thuo | Sales (05), Finance (09) | All departments |
| Cognitive calendar sync | Operations (08) | Mary Thuo | Finance (09) | Sales (05), Client Success (07) |
| Opportunity gating | Operations (08) | Mary Thuo | Sector (01), Offer (02), Sales (05) | Finance (09) |
| Capacity gating | Operations (08) | Mary Thuo | Client Success (07) | Sales (05) |
| Cross-department state | Operations (08) | Operations (08) | — | Mary Thuo, all departments |
| Delivery scheduling | Operations (08) | Operations (08) | Client Success (07), Offer (02) | Finance (09) |
| Delivery QA / billable release | Operations (08) | Operations (08) | Offer (02) | Finance (09), Client Success (07) |
| Delivery risk | Operations (08) | Operations (08) | Client Success (07) | Mary Thuo |
| Invoicing (from `DELIVERY_COMPLETE`) | Finance (09) | **Mary Thuo (Class 3)** | Operations (08) | Client Success (07) |

## 12. Triggers / Automation Hooks

**Live (Arika Runtime, 2026-07-14).**

| Trigger | Type | Fires |
|---|---|---|
| daily `0 6 * * 1-5` | schedule | `operations-state-monitor` (state first) |
| daily `0 7 * * 1-5` | schedule | `operations-daily-command` (then plan) |
| Monday `0 7 * * 1` | schedule | `operations-calendar-orchestrator`, `operations-capacity-planner` |
| `OPPORTUNITY_PROPOSED` · `EXPANSION_IDENTIFIED` · `PROSPECT_SCORED` | event | `operations-opportunity-filter` |
| `OPPORTUNITY_FILTERED` | event | `operations-capacity-planner` |
| `SCOPE_DEFINED` (from Client Success 07) | event | `operations-delivery-scheduler` |
| `DELIVERY_SCHEDULED` · `QA_GATE_REQUESTED` | event | `operations-delivery-qa` |
| `PROJECT_IN_DELIVERY` · `QA_FAILED` | event | `operations-delivery-risk` |
| manual | CLI | any of the eight |

**Emitted:** `STATE_REPORTED` · `ALIGNMENT_BROKEN` · `DAILY_PLAN_SET` · `CALENDARS_SYNCED` · `CALENDAR_CONFLICT_FLAGGED` · `OPPORTUNITY_FILTERED` · `CAPACITY_ASSESSED` · `OVERSELL_RISK_FLAGGED` · `DELIVERY_SCHEDULED` · `PROJECT_IN_DELIVERY` · `QA_PASSED` / `QA_FAILED` · **`DELIVERY_COMPLETE`** (→ Finance 09) · `DELIVERY_RISK_FLAGGED` · `DELIVERY_BLOCKED`.

**Governance:** every agent is advisory (Class 1–2). **No automation acts** — invoicing from `DELIVERY_COMPLETE` is **Class 3** and needs a row in `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` plus human sign-off. Operations enforces that gate; it does not bypass it — and urgency is explicitly not an exception.

## 13. Existing OS Sub-Layer

**Yes, as of 2026-07-14 — doctrine + agents.** [`OPERATIONS_CONSTITUTION.md`](OPERATIONS_CONSTITUTION.md) (the doctrine) plus 8 runtime agent specs (`.claude/agents/operations-*.md`) run by the unified **Arika Runtime** (`arika-runtime/`). No department-local plugin/code — the agents are `execution: prompt`.

## 14. Raw Archive Pointer

**None — and by design.** This department never had, and does not need, a raw draft archive. It was built from the **cross-department contracts** listed in §2 rather than from its own brainstorm material — which is appropriate, since Operations is the execution of everyone else's decisions, not a source of new doctrine.

## 15. Changelog

- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap (no prior home for delivery/operations SOPs). — Claude Code (Sonnet 4.6)
- 2026-07-14 — **Operations built and made live — the execution/orchestration layer over the whole OS.** Per the owner's direction, this department was deliberately held blank until every other department had a real agent layer to orchestrate; that condition was met (7 departments, 40 agents). Wrote [`OPERATIONS_CONSTITUTION.md`](OPERATIONS_CONSTITUTION.md) — doctrine assembled entirely from **existing owner-confirmed sources**, nothing invented: **ROCBO** + the **7 Cognitive Calendars** + the daily target table + Path A/B deal math + the anti-patterns (`AGENCY_REVENUE_TARGETS.md`); the **5 Foundational Realities** + Layer 7/9 + the Financial Orchestration Layer (`AGENCY_VISION.md`); the Class 0–4 risk model (`AGENCY_OPERATING_CONSTITUTION.md`); the live `Project` pipeline (`CRM_SCHEMA.md`); and the delivery contracts already written by Client Success (07) and Offer (02). Authored **8 advisory-first agents** across the confirmed **dual scope** — agency-side (`state-monitor`, `daily-command`, `calendar-orchestrator`, `opportunity-filter`, `capacity-planner`) and client-side (`delivery-scheduler`, `delivery-risk`, `delivery-qa`). **Closed the last live gap in the chain:** Client Success's `SCOPE_DEFINED` now has a listener, and `DELIVERY_COMPLETE` hands the billable event to Finance (09). Classified **IRIS** as an alias for the unified system, not a 22nd department. **Genuine gaps flagged, not filled:** no capacity model exists (agent flags every run), SLA templates remain theory-only, no BI/dashboard is connected, the $35K×5-day vs $1M/month math gap (~23–24%) stays reported, and the Vision's 11-stage vs Client Success's 9-stage lifecycle conflict stays flagged. Populated every previously-placeholder section (§2–§13) and added §16. 48 agents register in `arika list`; `npm test` 8/8; live model calls pending `ANTHROPIC_API_KEY`. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory:** all 8 agents append JSONL to `08_Operations/_memory/runtime.jsonl` (the runtime's bois-compatible envelope) on every run. This stream is uniquely important: it is the agency's **execution record** — the only proof of what actually happened, as opposed to what a department's OS file says should happen. `operations-state-monitor` reads *every* department's memory stream, making this the closest thing the repo has to a system-wide operational history.

**Feedback Loop:** Operations is itself the agency's primary feedback loop (the source material's own diagnosis: *"Most teams don't fail because they lack strategy. They fail because they lack execution discipline and feedback loops."*). Concretely — a missed daily target surfaces as `revenue_gap` in `operations-daily-command`; a cross-calendar contradiction surfaces as a `conflict` from `operations-calendar-orchestrator`; a broken chain surfaces as a `broken_link` from `operations-state-monitor`; `ALIGNMENT_BROKEN` is the highest-severity signal in the system, per the Vision's *"if alignment breaks, revenue collapses."* Each closes back into the next day's plan.

**Cadence:** **daily** (Mon–Fri) — state at 06:00, command at 07:00 = the **Revenue Calendar heartbeat**. **Weekly** (Mon 07:00) — calendar synchronization + capacity review = the **Operational/Capacity Calendars**. **Event-driven** — opportunity gating and the whole client-delivery chain. Maps across all 7 Cognitive Calendars (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §The 7 Cognitive Calendars) — Operations is the department that *runs* them rather than merely referencing one.
