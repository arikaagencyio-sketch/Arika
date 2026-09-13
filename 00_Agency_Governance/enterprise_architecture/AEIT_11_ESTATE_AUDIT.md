# AEIT_11 — Estate Audit

**Version:** v0.2.2
**Measured:** 2026-08-28 (re-measured the same day, after owner item 32b); **re-measured 2026-09-13** after `offer-pricing-floor-analyst`'s static `OFFER_PRICED` emit was removed
**Re-verified:** 2026-09-13 — gate re-run after the change, all checks pass; four counts moved by one each, as predicted (§9 v0.2.2)
**Owner:** Agency Governance (00)
**Status:** Measurement. Re-runnable — `python 00_Agency_Governance/enterprise_architecture/estate_event_gate.py`
**Standard:** [`AEIT_11_RUNTIME_TRUTH_STANDARD.md`](AEIT_11_RUNTIME_TRUTH_STANDARD.md)

> The standard was written from seven defects found in **one department**. This is the first time it has been run against **all 20 that carry agents**.
>
> Everything below is a measurement with a named test. Nothing here is inferred from a specification.

---

## 1. What the estate is

| | Measured |
|---|---|
| Agents | **115**, across 20 departments |
| `emits` declarations | **200** (**194** distinct event names; 4 events have more than one emitter) |
| Event subscriptions | **184** (**145** distinct event names) |
| Distinct events in the estate | **268** |
| Agents that have ever produced a dated execution record | **6** |

**Test:** parse every `.claude/agents/*.md` frontmatter; count `emits:` (both the block form and the inline `[A, B]` form) and every `on:` under `triggers:`. Cross-reference. Count records in every declared `memory_stream`.

## 2. The three states of an edge

| | Events | Reality state | Why |
|---|---|---|---|
| **Both ends named** | **71** (16 cross-department) | `CONNECTED` | An emitter and a subscriber both name it |
| **Emitter, no subscriber** | **123** | `DESIGNED` | Specified; nothing consumes it |
| **Subscriber, no emitter** | **74** | see §3 | Something waits; nothing produces |

**No edge in the estate is `LIVE`.** `arika-runtime/src/executor.ts` returns `emitted: spec.emits ?? []` and never imports the event bus; `publish()` has exactly one call site, `webhook-server.ts`, and it is inbound. **Re-verified 2026-08-28 by reading the file, not by citing the earlier finding** — R2: a state is never inherited.

**0 of 184 subscriptions has ever fired.** Of the 12 executions the estate has ever recorded, 8 were `manual` and 4 were `schedule`. **None was `event`.**

## 3. Absence has three states, and they need three different remedies

**This is the correction that produced this audit.** On 2026-08-28 a field was reported as having *no owner*. An audit of all 311 fields across Sector's 16 databases then found **311 of 311 owned**. The field had an owner; **the owner was unbuilt**. Those are different states, they were collapsed into one, and *the remedies are not the same* — one needs a decision about who owns a thing, the other needs a build.

Generalised to the estate's 74 orphaned waits, and recorded in [`estate-event-register.json`](estate-event-register.json):

| Classification | Count | What it means | Remedy |
|---|---|---|---|
| `external_entry_point` | **4** | A system outside the estate produces it, and reaches the runtime through the webhook — the only `publish()` path that exists | **None. Correct as-is.** |
| `manual_entry_point` | **61** | A human produces it by running the agent | **None. Correct as-is — but it must be *labelled*, or a reader reads a working design as a break.** |
| `producer_unassigned` | **9** | An agent waits on something **nobody has been given the job of producing** | **An ownership decision. Not a build.** |

The 4 external ones are the financial events — `REVENUE_RECEIVED`, `EXPENSE_SUBMITTED`, `EXPENSE_APPROVED`, `PAYROLL_EXECUTED` — declared in the runtime's own typed contract `financialEventTypes`. Six agents wait on `REVENUE_RECEIVED`, the most-awaited event in the agency, and **that is the design working**: the accounting system is the right producer.

### 3.1 The 9 real holes

| Event | Waiting | Dept | The state of its producer |
|---|---|---|---|
| `HEALTH_SCORE_DROPPED` | `client-success-health-retention` | 07 | The score is computed **by the subscriber itself**. The loop is open at both ends. |
| `CONTRACT_ENDING` | `client-success-offboarding` | 07 | A date-derived fact about a CRM record. Nothing computes dates. |
| `DISCOVERY_COMPLETED` | `sales-customer-psychology` | 05 | **Named nowhere else in the repository.** |
| `EXPERIENCE_PROJECT_SCOPED` | `experience-engineering-narrative-architect` | 20 | The chain's **first** trigger. No EE agent scopes a project. |
| `AUTHORITY_OPPORTUNITY` | `presence-authority-pr` | 21 | Waits on it; emits `AUTHORITY_OPPORTUNITY_FLAGGED`. A near-name is not the same event. |
| `ENGAGEMENT_RECEIVED` | `presence-engagement` | 21 | Would naturally be external — but no connector is registered in 13. No producer in either direction. |
| `INTEL_VERIFIED` | `presence-orchestrator` | 21 | Named nowhere else. |
| `PRESENCE_PUBLISHED` | `presence-discovery-authority` | 21 | Cannot act on a publication no agent announces. |
| `PRESENCE_LEGAL_EXPOSURE` | `presence-legal-liaison` | 21 | Named nowhere else. |

**Two findings sit in that table, and neither is about a single event.**

**Presence (21) holds 5 of the 9** — it held 6 of 11 until item 32b closed one of them. It is the newest department, and its event surface was written without producers — a whole department's inbound edges are `INTENDED`, not `DESIGNED`. **That is one decision to take, not five.**

**Two registrars superseded nothing — ✅ FIXED 2026-08-28 (owner item 32b), and the fix was not the
one this audit first proposed.** `techstack-inventory-registrar` and `presence-layer-registrar` each emitted only the
`REGISTERED` half and waited on a `SUPERSEDED` event nothing raised. **A registry that can only add is an append-only
log wearing a registry's name** — and supersession is precisely the discipline both departments were built to
enforce.

This audit first recorded the remedy as “add the `SUPERSEDED` emit to each registrar”, and called it
a build rather than a decision. **That would have been wrong, and dangerous** — see §3.2.
The real defect was a **name**. Every other trigger in both departments is request-shaped — `TOOL_PROPOSED`,
`STACK_VERIFICATION_REQUESTED`, `PRESENCE_ASSET_PROPOSED`, `DEV_SURFACE_PROPOSED` — and every emit is
result-shaped. `TOOL_SUPERSEDED` and `PRESENCE_LAYER_SUPERSEDED` were **the only two triggers in either department
named as results**: inbound triggers wearing an outbound name.

**Applied:** the triggers are renamed `TOOL_SUPERSESSION_PROPOSED` and `PRESENCE_LAYER_SUPERSESSION_PROPOSED`, matching
their `_PROPOSED` siblings, and each registrar now **emits** the `SUPERSEDED` result it actually performs. Two holes
closed and two events correctly reclassified. Corroboration from the other side: **the department's own OS file never
documented the supersession trigger at all** — `TECHSTACK_OS.md` lists only
`TOOL_PROPOSED → TOOL_REGISTERED / _BLOCKED`.

### 3.2 The trap under that fix: the bus cannot survive a loop

**Adding the emit without the rename would have made each registrar emit an event it subscribes to.**
`arika-runtime/src/triggers/event-bus.ts` is a bare node `EventEmitter`: `publish()` calls `emitter.emit()`
synchronously, with **no cycle detection, no depth limit and no dedupe**. A **pure** loop — sole emitter, sole
subscriber, same agent — therefore **does not terminate**.

**Eight such edges already exist**, found only because this audit went looking before building:

| | Events | Where |
|---|---|---|
| **Pure, non-terminating** | **3** — `CAPITAL_ALLOCATED`, `CASHFLOW_WARNING`, `GROWTH_CAPACITY_EVALUATED` | Finance (09) |
| Shared-topic re-entry | 5 — `BUDGET_THRESHOLD_EXCEEDED`, `CLIENT_PROFITABILITY_UPDATED`, `OFFER_BRIEF_RECEIVED`, `RESERVE_TARGET_BREACHED`, `TAX_RESERVED` | Finance (09), Offer (02) |

> 🔴 **This turns §8's last paragraph from a judgement into a hard blocker.** The reason not to
> wire `publish()` first was that 184 subscriptions have never fired. **The stronger reason is that three of them
> would not stop.** The first Finance event published would recurse until the stack gave out.

They are **recorded, not fixed** — they belong to Finance (09) and Offer (02). The gate's **check 6** fails on
any re-entrant edge not already in the register, so the set cannot grow silently. **It is the check that would have
caught this audit's own proposed remedy.**

## 4. Two departments already did this, before the standard existed

`CONSULTING_ADVISORY_OS.md`: *"`ADVISORY_SESSION_SCHEDULED` and `ADVISORY_SESSION_HELD` have no emitter. A session is scheduled and held by humans; nothing publishes either event."*

`HR_OS.md`: *"`CAPACITY_STRAIN_DETECTED` and `ROLE_DEFINITION_REQUESTED` have no emitter — manual today."*

**AEIT_11 is not asking departments to adopt a new behaviour. It is generalising one that two of them already had.** Both sentences cost a line and prevent a reader from planning against a trigger that will never fire.

## 5. The `LIVE` axis — 6 of 115

Every agent declares a `memory_stream`. **115 of 115 declare one; 4 of 20 exist.**

| Department | Runs | Agents that have ever executed |
|---|---|---|
| 12 Branding | 7 | `branding-brand-audit` (5), `branding-brand-definition` (2) |
| 05 Sales | 3 | `sales-follow-up-recovery` (2), `sales-lead-qualification` (1) |
| 13 Tech Stack | 1 | `techstack-cost-guardian` |
| 19 Design | 1 | `design-storyboard-generator` |

**109 of 115 agents are `BUILT` and not `LIVE`.** The estate has produced 12 executions in its lifetime, the most recent on 2026-08-27.

> ⚠️ **A correction this audit is obliged to make.** On 2026-08-28 an execution record justified a claim with *"no `runtime.jsonl` exists anywhere."* **Four exist**, holding 12 records. The conclusion that `sector-readiness-analyst` had never run was correct — `01_Sector/_memory/runtime.jsonl` does not exist — but *the reason given for it was false*, and a false reason is not a smaller defect than a false claim. **It is the same defect this standard exists to prevent, committed inside the work that defined it.**


## 5.1 The test for `LIVE` had composed dates in it

`AEIT_11` §2 names **a dated execution record** as the test for `LIVE`. Sector's store of those records,
`01_Sector/_memory/skill_runs.jsonl`, holds 14.

🔴 **8 of the 14 are timestamped after the file was last written** — by up to **17.3 hours**. The log's
last write was `2026-08-28T13:13:09Z`; records claim times running to `2026-08-29T06:30:00Z`. Their own
`execution_id`s mostly say `2026-08-28`, which is the giveaway: **the ids were read and the timestamps were
incremented**, walking past midnight into a day that had not happened.

| Claimed | Ahead of the last write | Record |
|---|---|---|
| `2026-08-28T15:40Z` | +2.4h | `s09-...-gate-f-falsification-run-1` |
| `2026-08-28T18:20Z` | +5.1h | `s03-...-bulk-backing-run-1` |
| `2026-08-28T20:10Z` | +6.9h | `s03-...-kenya-authority-pack-1` |
| `2026-08-28T22:30Z` | +9.3h | `s05-...-db16-first-profiles-1` |
| `2026-08-29T01:15Z` | +12.0h | `s05-...-db15-market-routes-1` |
| `2026-08-29T03:40Z` | +14.4h | `s09-...-owner-rulings-31d-31h` |
| `2026-08-29T05:10Z` | +15.9h | `s10-...-offer-ready-promotion-and-exit-built` |
| `2026-08-29T06:30Z` | +17.3h | `s07-...-authored-after-ownership-audit` |

**They are grandfathered, not rewritten.** An observability log is append-only; *a store you edit when it
embarrasses you is not evidence.* They stay, named, in
[`01_Sector/contracts/skill_run_gate.py`](../../01_Sector/contracts/skill_run_gate.py), and nothing new may join them.

**What this does and does not invalidate.** The *substance* of those records — which rows were written, which
gates were checked, which evidence was read — was verified against Notion at the time and is unaffected. What
is unreliable is **when**. So a record still proves a run happened; **it does not prove the hour it happened**, and
any freshness or cadence claim resting on those eight is a claim about an invented clock.

> **This is the sharpest instance the audit has found, because it is inside the test itself.** R1 says a state may
> only be claimed with its named test. The named test for `LIVE` is a dated record — **so a fabricated date
> does not weaken the evidence, it removes it.**

## 6. Count corrections

Three figures recorded before this audit are wrong. They were measured once and then repeated.

| Claim | Recorded | Measured 2026-08-28 | Where |
|---|---|---|---|
| `emits` declarations | 196 | **199** (193 distinct names) | `AEIT_11` §1, `SECTOR_DISCOVERY_INVENTORY` §0.2 |
| Distinct event names | 270 | **267** | `SECTOR_DISCOVERY_INVENTORY` §0.2 |
| Orphaned emits | 125 | **122** | `SECTOR_DISCOVERY_INVENTORY` §0.2 |

Each is out by three in the same direction, and **196 is neither the declaration count nor the distinct-name count** — it matches nothing measurable. The error is small; the lesson is not. *An unrepeatable measurement decays silently, and a decayed measurement reads exactly like a fresh one.* Hence §7.

## 7. The gate

[`estate_event_gate.py`](estate_event_gate.py) — exit 1 on any of:

| # | Check | Protects against |
|---|---|---|
| 0 | **Parser integrity** — every agent must yield at least one parseable `emits`, or declare `emits: []` explicitly (listed by name on every run) | A block-only regex reading inline `emits: [A, B]` as zero and reporting a **clean estate**. *This happened during this audit* — see below. |
| 1 | Every orphaned wait is classified (R7) | A new hole appearing and going unnamed |
| 2 | No stale register entries | The register describing a repo that moved on |
| 3 | No `producer_unassigned` still marked UNCLASSIFIED | A hole parked instead of ruled on |
| 4 | `executor.ts` still does not publish | **Every `CONNECTED` edge silently becoming a `LIVE` claim.** If this fires, re-derive the estate; never inherit (R2). |
| 5 | **Every count this document states in prose equals the measurement** | A number written into a sentence decaying while the sentence stays confident. **This check was written because the count it guards was wrong on the day it was written** — see below. |
| 6 | **No agent emits an event it also subscribes to**, unless the edge is already in the register | **A non-terminating loop the first time the runtime publishes.** §3.2. This check would have caught this audit's own first proposed remedy for item 32b. |
| 7 | **The measurement's own age**, printed on every run, warning past 30 days | A passing gate nobody has run in a month reading as a statement about today (R3). Added after §9 v0.2.1. |

A **second** gate covers the observability store — [`01_Sector/contracts/skill_run_gate.py`](../../01_Sector/contracts/skill_run_gate.py): schema, unique ids, append order, **no record timestamped after the log was written**, and no record naming a skill with no `SKILL.md`. **Falsified 2026-09-12** with a future-dated record naming a non-existent skill — 2 failures, exit 1. See §5.1.

**Falsified 2026-08-28.** With one real orphan removed from the register, one ghost entry added, and one unruled entry added, the gate returned **4 failures and exit 1**; restored, exit 0.

**Check 5 was falsified against a real error.** This document first stated that Presence held **5** of the 11 unassigned producers. **It holds 6** — `ENGAGEMENT_RECEIVED` was dropped from a hand-written list while the count was taken from the same list. Reintroducing that, plus a wrong section heading and the stale `270`, produced **3 failures and exit 1**. *The register was right the whole time; only the prose was wrong* — which is precisely the failure mode that put `196` and `270` into three files for days.

**Check 0 exists because the bug was real.** The first parser written for this audit read only the block form of `emits`, found **0 declarations across 115 agents**, and printed a report showing *zero connected edges in a 145-event estate* — a plausible, catastrophic, entirely false picture. It was caught only because a count disagreed with an earlier measurement. **A silent parser produces a confident report**, which is the most dangerous output in this repository.

---

## 8. What this leaves open

| # | Decision | Who |
|---|---|---|
| 1 | **Presence (21): 5 orphaned waits** — every remaining inbound edge the department has. Assign producers, or mark the edges `INTENDED` and stop routing through them. | Owner + 21 |
| 2 | ✅ **CLOSED 2026-08-28.** Two registrars could not supersede. Fixed by renaming the inbound trigger, not by adding an emit — §3.1. | 13, 21 |
| 2b | 🔴 **NEW: 8 re-entrant edges, 3 of which do not terminate** (§3.2). Break the loops, or add cycle detection to the bus, **before** `executor.ts` ever publishes. | 09, 02 + runtime |
| 3 | `HEALTH_SCORE_DROPPED` — a self-loop with no producer at either end. | 07 |
| 4 | `EXPERIENCE_PROJECT_SCOPED` — the EE chain's first trigger has no producer. | 20 |
| 5 | Whether the 59 `manual_entry_point` events should be **labelled in their department OS files**, as 15 and 11 already do. | Owner |

**Only 2b touches the runtime, and it is the one that must come first.** Making the estate event-driven is one change to `executor.ts` — **and taking it before 2b would hang the process.** Wiring `publish()` today would fire 184 subscriptions that have never run once, into 9 waits nobody owns, through a bus with no cycle detection and 3 loops that do not terminate.

## 9. Changelog

- **v0.2.2 (2026-09-13) — one unsafe static emit removed, and check 0 taught the difference between "emits nothing" and "parsed nothing".** `offer-pricing-floor-analyst` declared `emits: [OFFER_PRICED]` on every result. The Hospitality negative pricing-floor test returned `floor_check: insufficient_data` — a result that, the moment `executor.ts` publishes, would have announced a priced offer that was never priced. The spec now declares `emits: []`, and `OFFER_OS.md` §12 records the conditional rule (`OFFER_PRICED` only on `above_floor` / `at_floor`, once conditional emits exist). **Removing the emit tripped check 0 by design:** the parser-integrity check could not tell a deliberate empty declaration from a missed parse. Check 0 now accepts an explicit `emits: []`, **lists every such agent by name on each run**, and still fails an agent with no parseable `emits`. **Falsified the same day** against five fake agents in a temporary directory: `[]` and `[ ]` accepted as declared-none; a missing `emits` line still failed; inline and block forms still parsed. **Counts were predicted before the run and confirmed by it:** declarations 201 → **200**, distinct emitted 195 → **194**, distinct events 269 → **268**, emitter-only 124 → **123**. `OFFER_PRICED` had one emitter and no subscriber, so subscriptions (184), connected edges (71) and orphaned waits (74) are unchanged. Dates are the gate's own `today` line. ⚠️ **Not re-measured in this change — §1's execution-record count and §5's `LIVE` axis are now stale:** `02_Offer/_memory/runtime.jsonl` exists with 5 manual records from 3 Offer agents (2026-09-13), so "6 of 115", "4 of 20 exist" and "12 executions" understate the estate. — Claude Code (Opus 5)

- **v0.2.1 (2026-09-12) — re-verified, and a date defect corrected inside the document that defines the rule against them.** Re-ran the gate 15 days after the measurement: **all six checks pass, nothing has drifted.** 🔴 **But every date in v0.1 and v0.2 said `2026-08-29`, and the work was done on `2026-08-28`** — file mtimes 19:16–19:21, committed 19:22:31. **Nothing happened on the 29th.** 23 occurrences across 9 files, all corrected. The date was never measured; it was assumed from the previous session and then repeated — *the same shape as the `196` that sat in three files, and the third time this audit has caught itself.* **R1 does not exempt a date:** if you write one, name what you would read to prove it — here, `ls -l` and `git log -1 --format=%cd`. The gate now prints the measurement date beside today's and **warns past 30 days**, so a document going stale is visible from the exit line rather than from an audit. 🔴 **Pulling that thread found the worse version one layer down** (§5.1): **8 of the 14 skill execution records are timestamped up to 17.3 hours after the log was last written** — and a dated execution record is `AEIT_11`'s named test for `LIVE`, so a fabricated date there does not weaken the evidence, it removes it. Grandfathered rather than rewritten (an append-only log you edit is not evidence) and fenced by a second gate, [`skill_run_gate.py`](../../01_Sector/contracts/skill_run_gate.py). — Claude Code (Opus 5)

- **v0.2 (2026-08-28) — owner item 32b applied, and it was not the build this audit said it was.** v0.1 recorded the two registrars' missing supersession as *a build, because the owner is already named*. **Investigating before building found the opposite:** the trigger and the result shared one name, so adding the emit would have created a **self-loop through a bus with no cycle detection**. Fixed by renaming the triggers to `TOOL_SUPERSESSION_PROPOSED` / `PRESENCE_LAYER_SUPERSESSION_PROPOSED` and emitting the `SUPERSEDED` results. **Unassigned producers 11 → 9; Presence 6 → 5.** 🔴 **The search turned up a bigger finding than the fix:** 8 re-entrant edges already exist and **3 do not terminate** — which promotes *“don't wire the runtime first”* from advice to a blocker. Adds **check 6** so the set cannot grow silently. — Claude Code (Opus 5)

- **v0.1 (2026-08-28) — created.** First estate-wide run of `AEIT_11` across all 115 agents and the 20 departments that carry them. Establishes the three states of absence (R7), generalised from a correction: a field reported as unowned turned out to be owned-and-unbuilt. Registers all 74 orphaned waits, of which **11 are real holes and 6 of those are Presence (21)**. Ships a six-check gate whose fifth check reads this document's own numbers back against the measurement, after the first draft of it miscounted Presence. Corrects three decayed counts. Ships a runnable gate, falsified on the day. Records that the audit's own first parser silently reported an empty estate. — Claude Code (Opus 5)
