# AEIT_11 — Estate Audit

**Version:** v0.1
**Measured:** 2026-08-29
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
| `emits` declarations | **199** (**193** distinct event names; 4 events have more than one emitter) |
| Event subscriptions | **184** (**145** distinct event names) |
| Distinct events in the estate | **267** |
| Agents that have ever produced a dated execution record | **6** |

**Test:** parse every `.claude/agents/*.md` frontmatter; count `emits:` (both the block form and the inline `[A, B]` form) and every `on:` under `triggers:`. Cross-reference. Count records in every declared `memory_stream`.

## 2. The three states of an edge

| | Events | Reality state | Why |
|---|---|---|---|
| **Both ends named** | **71** (16 cross-department) | `CONNECTED` | An emitter and a subscriber both name it |
| **Emitter, no subscriber** | **122** | `DESIGNED` | Specified; nothing consumes it |
| **Subscriber, no emitter** | **74** | see §3 | Something waits; nothing produces |

**No edge in the estate is `LIVE`.** `arika-runtime/src/executor.ts` returns `emitted: spec.emits ?? []` and never imports the event bus; `publish()` has exactly one call site, `webhook-server.ts`, and it is inbound. **Re-verified 2026-08-29 by reading the file, not by citing the earlier finding** — R2: a state is never inherited.

**0 of 184 subscriptions has ever fired.** Of the 12 executions the estate has ever recorded, 8 were `manual` and 4 were `schedule`. **None was `event`.**

## 3. Absence has three states, and they need three different remedies

**This is the correction that produced this audit.** On 2026-08-28 a field was reported as having *no owner*. An audit of all 311 fields across Sector's 16 databases then found **311 of 311 owned**. The field had an owner; **the owner was unbuilt**. Those are different states, they were collapsed into one, and *the remedies are not the same* — one needs a decision about who owns a thing, the other needs a build.

Generalised to the estate's 74 orphaned waits, and recorded in [`estate-event-register.json`](estate-event-register.json):

| Classification | Count | What it means | Remedy |
|---|---|---|---|
| `external_entry_point` | **4** | A system outside the estate produces it, and reaches the runtime through the webhook — the only `publish()` path that exists | **None. Correct as-is.** |
| `manual_entry_point` | **59** | A human produces it by running the agent | **None. Correct as-is — but it must be *labelled*, or a reader reads a working design as a break.** |
| `producer_unassigned` | **11** | An agent waits on something **nobody has been given the job of producing** | **An ownership decision. Not a build.** |

The 4 external ones are the financial events — `REVENUE_RECEIVED`, `EXPENSE_SUBMITTED`, `EXPENSE_APPROVED`, `PAYROLL_EXECUTED` — declared in the runtime's own typed contract `financialEventTypes`. Six agents wait on `REVENUE_RECEIVED`, the most-awaited event in the agency, and **that is the design working**: the accounting system is the right producer.

### 3.1 The 11 real holes

| Event | Waiting | Dept | The state of its producer |
|---|---|---|---|
| `HEALTH_SCORE_DROPPED` | `client-success-health-retention` | 07 | The score is computed **by the subscriber itself**. The loop is open at both ends. |
| `CONTRACT_ENDING` | `client-success-offboarding` | 07 | A date-derived fact about a CRM record. Nothing computes dates. |
| `DISCOVERY_COMPLETED` | `sales-customer-psychology` | 05 | **Named nowhere else in the repository.** |
| `EXPERIENCE_PROJECT_SCOPED` | `experience-engineering-narrative-architect` | 20 | The chain's **first** trigger. No EE agent scopes a project. |
| `TOOL_SUPERSEDED` | `techstack-inventory-registrar` | 13 | The registrar emits `TOOL_REGISTERED`. **The supersession half of its own contract has no producer.** |
| `AUTHORITY_OPPORTUNITY` | `presence-authority-pr` | 21 | Waits on it; emits `AUTHORITY_OPPORTUNITY_FLAGGED`. A near-name is not the same event. |
| `ENGAGEMENT_RECEIVED` | `presence-engagement` | 21 | Would naturally be external — but no connector is registered in 13. No producer in either direction. |
| `INTEL_VERIFIED` | `presence-orchestrator` | 21 | Named nowhere else. |
| `PRESENCE_PUBLISHED` | `presence-discovery-authority` | 21 | Cannot act on a publication no agent announces. |
| `PRESENCE_LAYER_SUPERSEDED` | `presence-layer-registrar` | 21 | Same shape as `TOOL_SUPERSEDED`: registers, never supersedes. |
| `PRESENCE_LEGAL_EXPOSURE` | `presence-legal-liaison` | 21 | Named nowhere else. |

**Two findings sit in that table, and neither is about a single event.**

**Presence (21) holds 6 of the 11** — every one of the department's orphaned waits. It is the newest department, and its event surface was written without producers — a whole department's inbound edges are `INTENDED`, not `DESIGNED`. **That is one decision to take, not six.**

**Two registrars supersede nothing.** `techstack-inventory-registrar` and `presence-layer-registrar` are both built to *maintain* a registry, both emit only the `REGISTERED` half, and both wait on a `SUPERSEDED` event nothing raises. **A registry that can only add is an append-only log wearing a registry's name** — and supersession is precisely the discipline both departments were built to enforce.

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

## 6. Count corrections

Three figures recorded before this audit are wrong. They were measured once and then repeated.

| Claim | Recorded | Measured 2026-08-29 | Where |
|---|---|---|---|
| `emits` declarations | 196 | **199** (193 distinct names) | `AEIT_11` §1, `SECTOR_DISCOVERY_INVENTORY` §0.2 |
| Distinct event names | 270 | **267** | `SECTOR_DISCOVERY_INVENTORY` §0.2 |
| Orphaned emits | 125 | **122** | `SECTOR_DISCOVERY_INVENTORY` §0.2 |

Each is out by three in the same direction, and **196 is neither the declaration count nor the distinct-name count** — it matches nothing measurable. The error is small; the lesson is not. *An unrepeatable measurement decays silently, and a decayed measurement reads exactly like a fresh one.* Hence §7.

## 7. The gate

[`estate_event_gate.py`](estate_event_gate.py) — exit 1 on any of:

| # | Check | Protects against |
|---|---|---|
| 0 | **Parser integrity** — every agent must yield at least one parseable `emits` | A block-only regex reading inline `emits: [A, B]` as zero and reporting a **clean estate**. *This happened during this audit* — see below. |
| 1 | Every orphaned wait is classified (R7) | A new hole appearing and going unnamed |
| 2 | No stale register entries | The register describing a repo that moved on |
| 3 | No `producer_unassigned` still marked UNCLASSIFIED | A hole parked instead of ruled on |
| 4 | `executor.ts` still does not publish | **Every `CONNECTED` edge silently becoming a `LIVE` claim.** If this fires, re-derive the estate; never inherit (R2). |
| 5 | **Every count this document states in prose equals the measurement** | A number written into a sentence decaying while the sentence stays confident. **This check was written because the count it guards was wrong on the day it was written** — see below. |

**Falsified 2026-08-29.** With one real orphan removed from the register, one ghost entry added, and one unruled entry added, the gate returned **4 failures and exit 1**; restored, exit 0.

**Check 5 was falsified against a real error.** This document first stated that Presence held **5** of the 11 unassigned producers. **It holds 6** — `ENGAGEMENT_RECEIVED` was dropped from a hand-written list while the count was taken from the same list. Reintroducing that, plus a wrong section heading and the stale `270`, produced **3 failures and exit 1**. *The register was right the whole time; only the prose was wrong* — which is precisely the failure mode that put `196` and `270` into three files for days.

**Check 0 exists because the bug was real.** The first parser written for this audit read only the block form of `emits`, found **0 declarations across 115 agents**, and printed a report showing *zero connected edges in a 145-event estate* — a plausible, catastrophic, entirely false picture. It was caught only because a count disagreed with an earlier measurement. **A silent parser produces a confident report**, which is the most dangerous output in this repository.

---

## 8. What this leaves open

| # | Decision | Who |
|---|---|---|
| 1 | **Presence (21): 6 orphaned waits** — every inbound edge the department has. Assign producers, or mark the inbound edges `INTENDED` and stop routing through them. | Owner + 21 |
| 2 | **Two registrars cannot supersede.** Add the `SUPERSEDED` emit in 13 and 21, or drop the trigger. | 13, 21 |
| 3 | `HEALTH_SCORE_DROPPED` — a self-loop with no producer at either end. | 07 |
| 4 | `EXPERIENCE_PROJECT_SCOPED` — the EE chain's first trigger has no producer. | 20 |
| 5 | Whether the 59 `manual_entry_point` events should be **labelled in their department OS files**, as 15 and 11 already do. | Owner |

**None of these is a runtime change.** Making the estate event-driven is one change to `executor.ts`, and it is a different decision from these five — **and it must not be taken first.** Wiring `publish()` today would fire 184 subscriptions that have never run once, into 11 waits nobody owns.

## 9. Changelog

- **v0.1 (2026-08-29) — created.** First estate-wide run of `AEIT_11` across all 115 agents and the 20 departments that carry them. Establishes the three states of absence (R7), generalised from a correction: a field reported as unowned turned out to be owned-and-unbuilt. Registers all 74 orphaned waits, of which **11 are real holes and 6 of those are Presence (21)**. Ships a six-check gate whose fifth check reads this document's own numbers back against the measurement, after the first draft of it miscounted Presence. Corrects three decayed counts. Ships a runnable gate, falsified on the day. Records that the audit's own first parser silently reported an empty estate. — Claude Code (Opus 5)
