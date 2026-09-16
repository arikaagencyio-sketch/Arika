# A001 — Mechanism queue triage checkpoint

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** This note classifies; it implements, approves and schedules nothing. Every item still needs its own owner decision.
**Version:** v0.1

> **Governed by D20** (sandbox record §5.1). Every classification below turns on one question: does the item change *how the system works*, or does it describe *how the market behaves*? The first is permitted, the second is barred however it is phrased.

---

## 1. Position after Batches 1 and 2

Nine of the queue's thirty items are implemented, all as documentation in [`INTAKE_OWNER_FILL_STANDARD.md`](INTAKE_OWNER_FILL_STANDARD.md). No code has been written or changed anywhere.

| Item | What it became |
|---|---|
| **F2** | §2 — block-per-question format for large owner-fill stages |
| **F3** | §3 — confirm the `question_id` before typing |
| **F4** | §4 — guidance and validator written together |
| **S2** | §9 — unprofiled is not absent, documentation only |
| **W1** | §6 — draft repo-bound lines first, then scan, then write |
| **W2** | §10 — negative-test the scan boundary |
| **W3** | §7 — apply large answer sets in stages |
| **W4** | §11 — correct stale claims with a dated note |
| **W5** | §8 — read the gate's source before forcing a stage |

**V3 and V4 are half-done by design:** §5 records the standing policy that relevance checks stay advisory, must be read and must not hard-fail. Their validator-code half is untouched and remains open.

**The owner-workflow group (W1–W5) is complete.** The intake-format group is complete apart from F1, which is addressed below.

## 2. Triage of every remaining item

Five classifications are used: **safe now** · **needs owner decision** · **later only** · **blocked by D16** · **never from A001**.

### 2.1 Intake formats

| # | Classification | Reasoning |
|---|---|---|
| **F1** | ✅ **Superseded — no action** | Its observation (pipe tables losing cells) is the evidence *for* F2, and its remedy is already recorded in D19 and implemented as standard §2. There is nothing left for F1 to change. It should be closed as superseded rather than implemented. |

### 2.2 Validators and gates

| # | Classification | Reasoning |
|---|---|---|
| **V1** | **Later only** | Fixes false-positive classes in a validator that exists only as a sandbox script, not in the repository. There is nothing in the repo to fix until such a validator is adopted — which is itself an owner decision. |
| **V2** | **Later only** | Same dependency as V1: rule-level fixes to a checker the repository does not yet hold. |
| **V3 / V4** | **Needs owner decision** (code half) | The policy half is done. Whether relevance checking is ever *enforced in code* is explicitly deferred by §5, and enforcement would change a flag into a stop — a different instrument. Needs a decision, not a build ticket. |
| **V5** | ⛔ **Never from A001** | Records that the intake gate behaved exactly as documented. A negative finding, kept so the gate is not "improved" without cause. |
| **V6** | ✅ **Done** | The truth-gate destination check was added mid-pilot and has held since. |

### 2.3 Sector schema and profiles

| # | Classification | Reasoning |
|---|---|---|
| **S1** | **Needs owner decision, then later only** | Authoring a destination profile is permitted as a mechanism fix *in principle*, but the content must come from real sources. **A001 supplies none, and simulated material may never fill one.** The decision is whether to commission the authoring at all; the work is not A001's to justify beyond naming the gap. |
| **S3** | **Needs owner decision** | A Sector rule for mixed-archetype properties. The sandbox convention (resolve on the main archetype, mark the secondary unruled) is **not** evidence that any rule is correct — it was a working expedient. The rule must come from Sector reasoning. |
| **S4** | **Later only** | Building the group union operator (AG-4) is a real build that gates Phase 4. A001 showed the system correctly refusing to guess; it does not specify the resolver. |
| **S5** | **Later only** | No Sector agent can check a hotel's company fit (AG-17). A capability gap A001 made visible and cannot fill. |

### 2.4 Offer routing and gating

| # | Classification | Reasoning |
|---|---|---|
| **O1** | ✅ **Safe now, with a drafting caution** | See §3 below. |
| **O2** | ⛔ **Never from A001** | A group run returning `reject` or `needs_more_seed_data` is the gate working. Explicitly **not** a reason to widen any band. |
| **O3** | **Needs owner decision** | Order-of-evaluation masking a gap is a genuine routing-logic finding, but the fix changes how gates are sequenced — an Offer/Sector design decision, not a documentation edit. |
| **O4** | ⛔ **Never from A001** | H-bands, MVP scope, anti-ICP, pricing gates, floors, capacity. All need market, demand, pricing or capacity evidence. Barred by D20. |

### 2.5 Runtime blockers

| # | Classification |
|---|---|
| **R1** | 🔴 **Blocked by D16** — and is itself the blocker: the API key rotation (AG-19) |
| **R2** | 🔴 **Blocked by D16** — sandbox memory stream, or shared stream with markers. Tier-1 (T1-5), deferred under D6 |
| **R3** | 🔴 **Blocked by D16** — sandbox marker field in skill execution records. Tier-1 (T1-4), deferred under D6 |
| **R4** | 🔴 **Blocked by D16** — entity model: `Company`, its parent edge and property-unit meaning. Tier-1 (T1-1), deferred under D6 |
| **R5** | 🔴 **Blocked by D16** — test-fixture trust value on knowledge objects. Tier-1 (T1-3), deferred under D6 |
| **R6** | 🔴 **Blocked by D16** — intake-gate builds: group/child answer files and a test-fixture label mode. Deferred under D7, with a manual workaround that held throughout the pilot |

**None may be started on A001's account while D16 is open.**

## 3. F1 and O1 examined closely

### F1 — already satisfied, recommend closing as superseded

**What it would change:** the intake overlay and the worksheet-generation convention, to stop using pipe tables for owner fill.

**Whether D20 permits it:** yes — an unsafe input format is a mechanism finding, and the item says nothing about hospitality.

**Why no action is recommended anyway:** the change already exists. D19 records the format decision, and standard §2 states the rule. Implementing F1 separately would either duplicate §2 or edit the Governance-owned intake profile (item 73, under review) and the Offer-owned overlay to say what §2 already says. **Recommend marking F1 superseded by F2, with no file change.**

**Risk of touching barred ground:** none. Format only.

### O1 — safe now, but the wording carries the only real D20 risk in this batch

**What it would change:** a short documentation note recording that group flags are inherited by every unit and never suppressed, so a unit passing every unit-level check can still be correctly ineligible.

**Whether D20 permits it:** yes. This is **routing logic behaving as designed**, and recording that it holds is documentation. It describes how the system evaluates, not how any market behaves.

**Where it would go:** `OFFER_OS.md` has **no routing-notes section**. Its §8 Decision Log would be wrong — Offer makes no decision here — and §10 is a doctrine list. The honest home is **Sector-side**, in the A001 close-out or the standard, with a pointer from `OFFER_OS.md` §15 if Offer needs visibility. This matters: creating a new Offer section for an A001-derived note would overstate the finding's standing.

**Risk of touching market, buyer, pricing, capacity, proof, ICP or Offer claims:** **low but real, and entirely in the drafting.** The permitted sentence is *"inherited group flags are not suppressed at unit level, so unit-level passes do not imply eligibility."* The same observation becomes barred the moment it is extended — *"therefore the ICP should treat groups as…"* or *"this shows group-owned properties are poor fits"* would be an ICP or market claim built on simulated data. The finding licenses a statement about **evaluation order**, nothing about **who is a good client**.

**Recommendation:** implement as a single sentence in Sector-owned documentation, with no change to any Offer rule, band, gate or the ICP.

## 4. Recommended next batch

**Batch 3 — close out the intake-format group. Two items, both documentation, both low risk.**

| Item | Action |
|---|---|
| **F1** | Mark **superseded by F2**. No file change beyond the queue row. |
| **O1** | Add the inherited-flags note to Sector-owned documentation, worded strictly as an evaluation-order statement, with an optional `OFFER_OS.md` §15 pointer. |

That batch leaves the queue with **no "Now" items outstanding**, which is a clean stopping point: everything remaining is a genuine owner decision, a later build, or blocked by D16.

**Not recommended next:** V3/V4's code half, S1, S3 and O3. Each needs an owner decision first, and each is a place where a mechanism fix could quietly become a market claim if drafted loosely.

## 5. What this note does not do

It implements nothing, approves nothing and schedules nothing. It changes no queue row — the queue remains the record of state, and this note is a reading of it at a point in time. No H-band, ICP, pricing, capacity, proof, buyer or market claim is touched, and no destination profile is authored or requested.

## 6. Cross-references

- [`A001_MECHANISM_IMPROVEMENT_QUEUE.md`](A001_MECHANISM_IMPROVEMENT_QUEUE.md) — the queue itself, and the authoritative record of item state.
- [`INTAKE_OWNER_FILL_STANDARD.md`](INTAKE_OWNER_FILL_STANDARD.md) — where Batches 1 and 2 landed.
- [`A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md`](A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md) — the pilot the findings came from.
- [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) — D16 (runtime block), D19 (block format), D20 (limits on simulated evidence), §5.1.

## 7. Changelog

- **v0.1 — 2026-09-16** — Triage checkpoint after Batches 1 and 2. Classifies every remaining queue item into safe now, needs owner decision, later only, blocked by D16, or never from A001; examines F1 and O1 in detail; and recommends a two-item Batch 3 that would leave no "Now" items outstanding. Planning only — nothing implemented, approved or scheduled, and no queue row changed. — Claude Code (Opus 5)
