# Consulting & Advisory — Department OS

**Department:** Consulting & Advisory (15)
**Position in flow:** The agency's Embedded-Partnership-stage layer — sits at the top of the offer-ascension model, downstream of every other offer. Reports into Agency Governance (00).
**Mandate:** Own the agency's executive-access advisory offer — Revenue Growth Advisory — and any future advisory/consulting products, distinct from the infrastructure-build offers that feed into it.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

**Newly created department (2026-06-30)**, promoted from a category inside the Offer (02) catalog after the owner decided Draft 28's "Consulting & Advisory" division deserved its own department. Its founding offer — Revenue Growth Advisory — is the only offer in the entire catalog with "Time-to-Result: Immediate" and an explicit ban on doing implementation work itself (advisory recommends; execution is delivered by other departments/offers). Structurally, this is the most plausible operational expression of "Embedded Partnership" in the agency's 5-stage ascension path (`00_Agency_Governance/AGENCY_VISION.md`).

## 2. Status

**Content seeded from Offer's catalog, not yet operationally run.** Full offer engineering exists (`02_Offer/OEOS - Consulting and Advisory Division - Revenue Growth Advisory (Claude-Synthesized). Draft 38.md`) — Phase 1 (offer identity) and Phase 11 (pricing) are real, owner-sourced (from Draft 28, and the only one of the synthesized batch where Phase 1 and the master pricing chart fully agree without conflict); Phases 2-10/12 are Claude-synthesized, owner-approved as-is 2026-06-30. No real advisory engagements have run yet.

**3 agents built 2026-07-15 (§5) — and this is the one department where the agents deliberately do NOT do the department's work.**

### The delegability ban — this department's defining constraint

Every other staffed department got agents that perform its core function. **15 cannot, and the ban is its own** (`Draft 38` Phase 12, owner-approved):

> **"Customized: all actual advice content — inherently senior-expertise-bound, the lowest delegability of any offer captured so far. Requires senior expertise: the entire offer (cannot be junior-staffed or productized the way infrastructure offers can)."**

If a human junior may not produce the advice, **an agent may not either** — and the reason is commercial, not ceremonial. Phase 2 sells *"direct executive access and decision-architecture support, **not generic strategy slides**"* at Phase 1's **"Elite"** value perception, for **$5,000–$100,000+/month**. An AI-generated recommendation delivered as executive advisory *is* the generic strategy slide with better prose. The judgment is the product; automating it destroys the thing being sold.

**The source names the one AI opening that survives**, and the roster is built to it exactly:

> **"Future AI opportunity: AI-assisted decision-log synthesis and pattern-detection across sessions."**

So the agents work **around** the advice: prep the ground (`consulting-advisory-prep`), synthesize what was said (`consulting-decision-log` — the sanctioned opportunity itself), and hold the bans (`consulting-scope-guardian`). **The owner remains the advisor.** This is a real architectural limit on the agency's automation ambition, discovered in the source rather than imposed — and it will still bind after the agency grows beyond solo operation (§5).

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Revenue Growth Advisory | Weekly executive advisory cadence — GTM optimization, revenue diagnostics, scale planning, decision architecture | Offer engineered (`Draft 38`); support chain wired 2026-07-15 (§5), **not yet delivered** |
| VIP consulting day | Single-day intensive add-on, **$10,000-$35,000/day** | **⚠️ Real pricing (Draft 28), still no delivery process — deliberately not invented 2026-07-15.** The gap is genuine: real money attached to work that has never been performed and has no defined shape. Designing a VIP-day process from `Draft 38`'s weekly-cadence patterns would be synthesizing method for a $35K/day product from an offer with **zero delivered engagements** — the same error this repo has repeatedly caught elsewhere. Needs the owner's real intent, not Claude's inference. |
| Growth Workshop | Named in Draft 28's Gateway Offers list — goal: *"strategic authority"* | **⚠️ Unbuilt and effectively unsourced.** Routed here 2026-07-15 by division (this department owns the advisory/consulting division), but **`Draft 38` never mentions a workshop** and Draft 28 gives only the name and a two-word goal — no Phase 1 seed data at all. Same status as *Sales Call Review* in Audits (14): **an open owner decision — is this a real micro-offer, or a name Draft 28 listed without intending a product?** Not engineered, because engineering it would be near-total invention. |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Revenue Growth Advisory cadence | Signed advisory agreement (**human — no emitter**, see §12) | Onboarding (stakeholder mapping, data access) → Weekly Advisory Sessions (**`consulting-advisory-prep` → ⟨human advises⟩ → `consulting-decision-log`**) → `consulting-scope-guardian` routes any execution out → Quarterly Deep Dive → Renewal | Ongoing executive guidance + decision log | Mary Thuo | `Draft 38` (synthesized) |

**Note the shape of that chain: the middle step is a human, by doctrine, not by limitation.** Everywhere else in this repo a human gate exists because an action is risky or irreversible. Here the human *is the deliverable*. `⟨human advises⟩` is the only step that cannot be automated later, no matter how capable the runtime becomes.

## 5. Agent Roster

**3 agents, built 2026-07-15 — none of which give advice.** `Draft 38`'s functional role labels (Client Partner, **Strategy Lead — the advisor**) describe AI-assisted execution the owner performs solo, not hires. The offer's immutables **require senior expertise and ban delegation of the advisory content itself** — the lowest-delegability offer in the catalog, and a real constraint on staffing *and* automation even after the agency grows beyond solo operation. See `11_HR_People_Ops/HR_OS.md` for real staffing.

| Agent | Class | Trigger → emits | Role — and what it must never do |
|---|---|---|---|
| `consulting-advisory-prep` | 1 | `ADVISORY_SESSION_SCHEDULED` → `ADVISORY_PREP_READY` / `ADVISORY_CADENCE_AT_RISK` | Assembles the pre-session brief: what changed (sourced from 03/05/08/09), open decisions with `days_open`, data available vs. missing. **Produces questions, never recommendations** — anything that reads as advice becomes a `questions_for_the_advisor` entry instead |
| `consulting-decision-log` | 2 **+ human-gated** | `ADVISORY_SESSION_HELD` → `DECISION_LOGGED` / `ADVISORY_VALUE_AT_RISK` | **The offer's own named AI opportunity.** Synthesizes the session's log entry + detects cross-session patterns. **Never grades the advice** — only whether it was recorded and acted on |
| `consulting-scope-guardian` | 2 | `DECISION_LOGGED` → `ADVISORY_SCOPE_OK` / `ADVISORY_SCOPE_BREACH` / `EXECUTION_HANDOFF_READY` | Holds **both bans** and routes recommended execution to the owning department |

**`consulting-decision-log` is Class 2 + human-gated** because Phase 3 defines the log as *"paper trail for both client value **and agency protection**"* — read literally, it is the record of who decided what when an engagement sours. **An inaccurate log is worse than no log, because it will be believed.** Its `made_by` field (`client` / `advisor_recommended` / `joint` / `unclear`) carries that weight: blurring the two manufactures liability out of nothing, so `unclear` is preferred to a guess. `source_fidelity` forces the same honesty — `reconstructed` must be declared, and `no_source` means no log should be produced at all.

### The two bans, enforced as code

1. **No implementation** (Phase 3, immutable — *"an explicit anti-scope-creep boundary not seen in any other offer"*). Load-bearing, not bureaucratic: this offer bills **$5K–$100K+/mo for judgment** with *Time-to-Result: Immediate* and **no build timeline** (Phase 7). Advisory doing implementation = infrastructure work at advisory prices, with no schedule, no QA gates, no scope doc. The guardian watches for the drift that never announces itself — *"we'll just set that up for you"*, *"I'll draft it between sessions"*.
2. **No delegation of advisory content** (Phase 12) — **binds the agents too, including the guardian itself.**

### The diagnostic boundary (owner-confirmed 2026-07-15)

Phase 4 opens this offer with a *"Diagnostic (condensed audit)"* → **Revenue Diagnostic Brief**. Audits (14)'s **offer #10 is a revenue audit** — the Stage 1 Gateway of the very ascension path this offer tops. **Not two products, and no second diagnostic was built:**
- **Ascended client** → they already bought offer #10's findings. **Reuse them.** Re-auditing is billing twice for one finding.
- **Entered at advisory directly** → route to `audits-scoping` (14), which owns the instrument.

Same discipline 14 applies in delegating its own acquisition sub-audit to 06: **two diagnostics of one thing drift, and the client gets shown both.**

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| Quarterly review attendance rate | Stakeholder attendance ÷ scheduled reviews | `Draft 38` | Mary Thuo | Quarterly | *(unset — no real data yet)* |
| Advisory renewal rate | Renewed engagements ÷ engagements up for renewal | `Draft 38` | Mary Thuo | Per-renewal cycle | *(unset)* |

## 8. Decision Log

- 2026-07-15 — **The delegability ban binds agents, not just juniors** (owner-confirmed). `Draft 38` Phase 12 says *"requires senior expertise: the entire offer (cannot be junior-staffed or productized)"*. Read as covering AI: if a human junior may not produce the advice, an agent may not either. The reasoning is commercial — Phase 2 sells *"not generic strategy slides"* at Phase 1's "Elite" perception; an AI-generated recommendation delivered as executive advisory **is** the generic strategy slide. **Consequence: this is the only staffed department whose agents deliberately do not perform its core function.** The roster was built to the one AI opening the source itself names (*"AI-assisted decision-log synthesis and pattern-detection across sessions"*). — Claude Code (Opus 4.8)
- 2026-07-15 — **No second diagnostic built** (owner-confirmed). Phase 4's *"Diagnostic (condensed audit)"* overlaps Audits (14)'s offer #10. Rule set: an **ascended client already has offer #10's findings — reuse them, don't re-audit**; a client entering at advisory directly gets **routed to `audits-scoping` (14)**. Same discipline 14 applies delegating its acquisition sub-audit to 06. — Claude Code (Opus 4.8)
- 2026-07-15 — **VIP consulting day and Growth Workshop left unbuilt, deliberately** (owner-confirmed). The VIP day has **real Draft 28 pricing ($10K–$35K/day) and no delivery process** — inventing one from `Draft 38`'s cadence patterns would synthesize method for a $35K/day product from an offer with zero delivered engagements. Growth Workshop has **no Phase 1 seed data at all** beyond a name and *"strategic authority"*; `Draft 38` never mentions a workshop. Both are open owner decisions. — Claude Code (Opus 4.8)

## 9. Risk / Incident Log

*(No incidents — no engagement has ever run.)*

**The three archetypes are now enforced as code**, not just noted. `consulting-decision-log`'s `archetype_signals` scores each per session, and any `strong_signal` emits `ADVISORY_VALUE_AT_RISK` to `client-success-health-retention` (07) — because all three end at the same place: **§7's advisory renewal rate**, months later.

| Archetype | Signal the agent watches |
|---|---|
| **Doubter** (Phase 9, highest risk) | `decisions_not_acted_on` + `days_open` — an executive who doesn't act, visible in data long before renewal |
| **Result Ghoster** | Value delivered vs. value acknowledged (also found in offer #2, `Draft 32` — a cross-offer pattern) |
| **Advisory-as-Validation-Only** | Sessions where every decision is `made_by: client` and `advisor_guidance` never changed an outcome |

**"Advisory-as-Validation-Only" is this department's own contribution to the agency's risk vocabulary** — `Draft 38` surfaced it as *"a genuinely new risk pattern… not covered by the original prompt's 7 named archetypes"*, i.e. **a real gap in the OEOS prompt's archetype list**, not an offer-specific footnote. It is the sharpest of the three because it is invisible in every conventional metric: the client attends, pays, renews once, and extracts nothing — a rubber stamp with an invoice. It fails quietly, and only the `made_by` field catches it.

**⚠️ All three are Claude-synthesized (Phase 9) and have never been observed in a real engagement.** They are designed patterns. The first real advisory client tests whether they exist at all.

### Standing risk: the delegability ban vs. the agency's own automation thesis

This department is a **structural counterexample** to the pattern the other 14 staffed departments follow. If the advisory content can never be delegated — not to a junior, not to an agent (§2) — then **this offer's capacity is permanently bounded by one person's calendar**, while §11 pricing scales to **$100,000+/mo** and the ascension model puts this at the top of every client's path. Every other offer gets cheaper to deliver as the runtime improves. This one does not, ever.

That is not a problem to solve; it is the offer's nature, and arguably what the "Elite" value perception is buying. **But it should be a conscious constraint on how many advisory clients the agency ever sells**, not a surprise discovered at the fourth simultaneous engagement.

## 10. Standards & SOPs Index

Full offer-engineering detail lives in `02_Offer/OEOS - Consulting and Advisory Division - Revenue Growth Advisory (Claude-Synthesized). Draft 38.md` — cited here rather than duplicated.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Advisory delivery | Consulting & Advisory (15) | Consulting & Advisory (15) | Offer (02) | All departments (advisory may touch any function) |
| Implementation handoff (advisory recommends, never executes) | Consulting & Advisory (15) | Receiving department (varies by recommendation) | Offer (02) | Client Success (07) |

## 12. Triggers / Automation Hooks

The support chain runs on `arika-runtime` (`GLOBAL_OS.md` §5): 3 agents, manual + event, plus one weekly cron (`consulting-decision-log`, `41 8 * * 5`, for cross-session pattern detection).

**Known gaps — flagged, not worked around:**

1. **`ADVISORY_SESSION_SCHEDULED` and `ADVISORY_SESSION_HELD` have no emitter.** A session is scheduled and held by humans; nothing publishes either event. The chain starts with a manual `arika run consulting-advisory-prep`. Real emitters would need a calendar integration — **no calendar tool is in `13_Tech_Stack/TECHSTACK_OS.md` §3 at all**, which is itself a finding: the weekly cadence is this offer's central immutable and the agency has no registered calendar.

2. **`ADVISORY_SESSION_HELD` needs a session record to be useful.** `consulting-decision-log` sets `source_fidelity` to `verbatim_source` / `summarized_source` / `reconstructed` / `no_source` — and today the honest value would be `no_source`, because nothing captures advisory sessions. **No transcription/recording tool is registered either.** Until one is, the decision log is a template waiting for input, and `no_source` correctly means it should produce nothing at all.

3. **⚠️ The weekly cron is declared, not scheduled.** Same standing issue as every other department: the runtime isn't booted as a daemon, and its **24 cron triggers still have 1 approval-matrix row between them** (`00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`, `16_Automation/AUTOMATION_OS.md` §12).

## 13. Existing OS Sub-Layer

No department-local code. The 3 agents (§5) run on the shared `arika-runtime`; their memory stream is `15_Consulting_Advisory/_memory/runtime.jsonl`. The offer-engineering content (`Draft 38`) remains the canonical design reference.

## 14. Raw Archive Pointer

No department-local raw drafts. Source content lives in `02_Offer/` — see `02_Offer/OFFER_OS.md` §3 (Offer Engineering Registry, offer #9) and `Agency Pricing Architure. Draft 28.md` for the original seed material.

## 15. Changelog

- 2026-06-30 — Department created, promoted from Offer (02)'s "Consulting & Advisory" division category per owner decision. Seeded from `Draft 38` (offer #9, Revenue Growth Advisory), owner-approved as-is the same day. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-15 — **Department built: 3 agents wired onto `arika-runtime`** (§5) — `consulting-advisory-prep` (Class 1), `consulting-decision-log` (Class 2 + human-gated), `consulting-scope-guardian` (Class 2). **The first department where the agents deliberately do not do the department's work** (§2, §8): its own Phase 12 bans delegating advisory content, so the roster was built to the single AI opening the source names. `⟨human advises⟩` sits in the middle of §4's chain **by doctrine, not by limitation** — the only step in this repo that cannot be automated later no matter how capable the runtime becomes. §9 upgraded from placeholder: the three archetypes are now schema-enforced, and *"Advisory-as-Validation-Only"* — this department's own contribution to the agency's risk vocabulary — is caught via `made_by`, the only field where a rubber-stamp engagement is visible. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 3 agents (§5) write to `15_Consulting_Advisory/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope. **The decision log is the department's real memory** — §5's `consulting-decision-log` produces the Phase 3 immutable (*"paper trail for both client value and agency protection"*), and the JSONL stream is where cross-session pattern detection reads from. **Both are empty**: no session has ever been held.

**Feedback Loop.** §7's two KPIs are **unset and uncalibratable** — quarterly review attendance and advisory renewal rate both need delivered engagements, and none exist. But the **leading indicators are wired**, which is unusual for a department with no data: `consulting-decision-log` → `ADVISORY_VALUE_AT_RISK` → `client-success-health-retention` (07) fires on any archetype `strong_signal`, **months before** a renewal conversation. §7's renewal rate is a lagging measure of exactly what §9's three archetypes predict.

The second loop is the scope one: `consulting-scope-guardian` → `EXECUTION_HANDOFF_READY` → Operations (08) / Sales (05) / Audits (14) / Automation (16). **This is the offer's implementation ban made constructive** — a ban with no destination is just a wall.

**Cadence.** The **weekly advisory cadence is itself an immutable** (Phase 3: *"non-negotiable — the offer's value proposition is consistent access, not project check-ins"*), making this the only department whose delivery cadence is a contractual promise rather than an operating preference. `consulting-advisory-prep` reports `cadence_state`, and `cadence_broken` is a **real finding** — the offer failing at the exact thing it sells. Against the **Strategic Calendar** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4) for the quarterly deep dive, and the **Pipeline Calendar** for renewals.

**⚠️ Two honest holes** (§12): the weekly cron is **declared, not scheduled** (the runtime isn't booted), and **no calendar or transcription tool is registered in `13_Tech_Stack/TECHSTACK_OS.md` §3 at all** — so the cadence this department enforces has no system of record, and the decision log has no session input. Today `source_fidelity` would honestly read `no_source`, which correctly means the log should produce nothing.
