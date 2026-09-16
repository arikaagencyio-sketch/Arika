# A001 — Owner decision menu

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** This menu presents choices. It decides nothing, approves nothing and schedules nothing.
**Version:** v0.2

> **Governed by D20** (sandbox record §5.1). For every decision below, the "D20 permits A001 evidence?" column answers one narrow question: may the A001 pilot be *cited as support* for this change? A "no" never means the change is forbidden — it means A001 is not a valid reason for it, and the justification must come from somewhere else.

---

## 1. Where A001 has stopped

A001 is at a clean, deliberate stopping point. Nothing is mid-flight.

| Dimension | State |
|---|---|
| Group and unit intake | Complete. Group S1 and all nine unit S1 verdicts recorded; Phase 2 exit gate met |
| Phase 3 slice | `A001-P07` reached **S2**, document-only, gate passing at S2 |
| Phase 3 mode | **Document-only** (D15). No agent, skill, scheduler, event or runtime memory write has occurred |
| Runtime-backed work | 🔴 **Blocked by D16** until the API key is rotated (AG-19) |
| S3–S5 | `BLOCKED` under D9 — the sandbox has no client system |
| Governance | D1–D20 in force; A001 ratified as an internal simulation sandbox only (D17) |
| Mechanism queue | 10 implemented, 1 superseded, 2 policy-half, 3 never-from-A001, 1 done, 13 later/open. **No "Now" items remain** |

**Nothing is waiting on Claude.** Every remaining move needs an owner decision first.

## 2. Group A — D16 and runtime-backed work

| | |
|---|---|
| **Decision** | Rotate the API key (AG-19 · D16), and record the rotation |
| **Unlocks** | Every runtime-backed item at once: R1–R6, any `arika run` on A001, any agent or skill execution, and the runtime half of Phase 3 |
| **Risks** | The rotation itself is routine. The real risk is what it opens: every run appends its full input to a git-tracked, auto-synced memory stream, and skill records still have no sandbox marker (R3). Rotating without deciding R2/R3 first means the first A001 run writes simulated data into a shared, permanent stream |
| **D20 permits A001 evidence?** | Not applicable — this is an operational security action, not a change A001 evidence is cited for |
| **Recommended default** | **Rotate when you next intend runtime work, not before.** A rotated key with no runtime plan is an unused credential; a rotated key plus an unresolved R2/R3 is a live footgun. Pair the rotation with a decision on R2 and R3 |
| **First safe next prompt** | *"A001: plan the D16 API key rotation — record the rotation in the sandbox admin file and item 74, and state what remains blocked by R2/R3 afterwards. Planning only; do not rotate, do not run anything."* |

**R2–R6** are each individually Tier-1 or owner-gated and stay deferred under D6 and D7. None may be started on A001's account while D16 is open, and closing D16 does not by itself approve any of them.

## 3. Group B — validator code (V3 / V4)

| | |
|---|---|
| **Decision** | Whether relevance checking is ever enforced in validator code, and if so, whether a flag may ever block an apply |
| **Unlocks** | A repo-side validator with relevance checking; consistency between what the standard says and what any tool does |
| **Risks** | Enforcement converts a flag into a stop. The pilot's heuristic produced **more false positives than genuine catches**, and it systematically under-scores answers that demonstrate rather than restate. A hard-failing version would train people to pad answers with the question's own vocabulary — worse inputs, not better |
| **D20 permits A001 evidence?** | ✅ **Yes.** Validator behaviour is explicitly a mechanism. The pilot's false-positive record is legitimate evidence about the checker |
| **Recommended default** | **Leave as policy, do not enforce.** Standard §5 already fixes the rule: advisory, must be read, must not hard-fail. Nothing in the repo enforces it, and that is recorded as deliberate. Revisit only if flags start being ignored in practice |
| **First safe next prompt** | *"A001 V3/V4: draft, planning only, what a repo-side relevance check would need to guarantee before it could ever block an apply. Do not write validator code."* |

**V1 and V2** (false-positive fixes) depend on this: there is no repo-side validator to fix until one is adopted. They stay **later only**.

## 4. Group C — schema and routing (S1 / S3 / O3)

| # | Decision | Unlocks | Risks | D20 permits A001 evidence? | Recommended default |
|---|---|---|---|---|---|
| **S1** | Commission authoring of a destination profile for a place that is in the geography database but unprofiled | Destination Fit can pass for that place; unblocks any real engagement there | **The content must come from real sources.** Filling it from simulated material would look like a mechanism fix and be a fabricated market claim | ◐ **Partly.** A001 may name the *gap*. It may supply **none** of the profile's content | **Defer** until a real engagement needs that destination. Authoring on spec spends real research effort on a hypothetical |
| **S3** | A Sector rule for properties mixing two archetypes | Consistent resolution for mixed properties instead of a per-case convention | The sandbox convention (resolve on main, mark secondary unruled) was an **expedient, not a validated rule**. Promoting it because it "worked" in simulation would give a convenience the standing of reasoning | ◐ **Partly.** A001 may show the gap exists and that it stayed invisible. It may **not** justify the specific rule | **Decide when a real mixed property appears.** The rule should come from Sector reasoning about real cases |
| **O3** | Whether gate evaluation order should change, so an earlier-firing rule cannot mask an unresolved gap behind it | Gaps surface even when another rule already blocks | Changing evaluation order touches live routing logic and could change outcomes for real companies. Higher blast radius than anything else in this menu | ✅ **Yes.** Order-of-evaluation masking is routing logic, squarely a mechanism finding | **Take it up, but scope it as a diagnostic first** — report every rule that *would* have fired, without changing which one blocks |

## 5. Group D — later-only builds

| # | What | Why it waits |
|---|---|---|
| **S4** | Group union operator (AG-4) | A real build that gates Phase 4. A001 showed the system correctly refusing to guess; it does not specify the resolver |
| **S5** | A Sector agent that can check a hotel's company fit (AG-17) | A capability gap A001 made visible and cannot fill. Fit was checked by hand throughout |
| **V1 / V2** | Validator false-positive fixes | Nothing to fix until a repo-side validator exists (Group B) |

**D20 permits A001 evidence for all four** — each is a mechanism gap the pilot made visible. None is urgent, and none is blocked by D16.

## 6. Group E — never from A001

These are real observations that A001 may **never** be cited to support. Listed so they are not quietly re-proposed.

| # | Observation | Why it is barred |
|---|---|---|
| **V5** | The intake gate behaved exactly as documented | A negative finding, recorded so the gate is not "improved" without cause |
| **O2** | A group run returning `reject` or `needs_more_seed_data` is correct | The gate working as intended. **Explicitly not a reason to widen any band** |
| **O4** | Anything touching H-bands, MVP scope, anti-ICP, pricing gates, floors or capacity | Needs market, demand, pricing or capacity evidence. A001 has none and can have none |

If any of these is ever revisited, the justification must come from real engagements — not from this pilot, however many times it ran.

## 7. Group F — the real pilot path

A001 was never the real pilot. These decisions sit outside the mechanism queue and are tracked separately.

| # | Decision | Unlocks | Risks | D20 permits A001 evidence? | Recommended default |
|---|---|---|---|---|---|
| **P1** | Supply the real pilot property and its pre-run decisions (tracker item 72) | The first real Sector → Offer → downstream push; `PILOT-H-001` | A real property means real data, real names and a real reputation. Every control the pilot exercised now matters for real | ⛔ **No.** A001 does not satisfy item 72 and never did | **Do this before any further simulation.** The mechanisms have been exercised as far as simulation can take them |
| **P2** | The client folder, storage and retention path for real client data | Somewhere lawful and durable to put real intake | Undecided storage is how real data ends up somewhere provisional and stays there | ◐ **Partly.** A001 proved a *workflow* (folder outside every git tree, key-scanned boundary). It says nothing about lawful retention | **Decide alongside P3.** The workflow pattern is proven; the legal basis is not |
| **P3** | The legal review path (tracked as item 59) | Removes the standing blocker on client-data handling and on several Offer gates | Counsel is named but not engaged, and letters are unsigned. Until that closes, a real engagement carries undecided legal exposure | ⛔ **No.** Nothing in A001 bears on this | **Highest-value unblock on this page.** It gates more than A001 does |
| **P4** | Whether public research is permitted per engagement, recorded before anyone looks at a page | Public-source intake for a real property | Research permission granted loosely is how a "quick look" becomes an unrecorded data source | ✅ **Yes**, as workflow design. A001 ran with research disabled throughout and showed the discipline holds | **Default to off**, and record the permission explicitly per engagement |

### ↪ P3 update — 2026-09-16

**The scope decision is made; the engagement is not.** The owner approved narrowing or amending the counsel scope before engagement, covering the six blocking matters — recorded in [`LEGAL_OS.md`](../10_Legal/LEGAL_OS.md) §8 and [`LEGAL_REVIEW_PATH_DECISION_PACKET.md`](../10_Legal/LEGAL_REVIEW_PATH_DECISION_PACKET.md). **No counsel has been contacted, nothing has been sent or signed, no engagement is active and no document has been reviewed**, so tracker item 59 stays open and every gate P3 would unlock stays shut — Offer's G5 is **narrowed, not passed**. **P3's remaining half — revising and approving the drafted reply before any sending — is still the highest-value unblock on this page**, and needs a separate, explicit instruction. Nothing else in this menu changed.

## 8. If you want a single recommendation

**Take P3, the legal review path.** It is the only item on this page that blocks work beyond A001, it needs no code, no runtime and no key, and it is not waiting on anything else. D16 can wait until you actually intend a run; the mechanism queue is at a natural resting point; and the simulation has taught what simulation can teach.

## 9. What this menu does not do

It decides nothing and changes no queue row, no decision record and no tracker item. It cites tracker item 59 by number only, and deliberately carries none of its detail into this file. No H-band, ICP, pricing, capacity, proof, buyer or market claim is touched, and no destination profile is authored or requested.

## 10. Cross-references

- [`A001_MECHANISM_IMPROVEMENT_QUEUE.md`](A001_MECHANISM_IMPROVEMENT_QUEUE.md) — the authoritative record of item state.
- [`A001_MECHANISM_QUEUE_TRIAGE.md`](A001_MECHANISM_QUEUE_TRIAGE.md) — the classification this menu builds on.
- [`A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md`](A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md) — what the pilot proved, and its "Before a real pilot" list.
- [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) — D9, D15–D20, the gap register and the run plan.
- [`OWNER_INPUT_NEEDED.md`](../00_Agency_Governance/OWNER_INPUT_NEEDED.md) — items 74, 72, 59 and 57.

## 11. Changelog

- **v0.2 — 2026-09-16** — **P3's scope decision recorded** (§7): the counsel scope is to be narrowed or amended before engagement, neither unsigned letter accepted as-is, and the path not deferred while a real hospitality pilot is still intended. **The engagement is still not active** — nothing contacted, sent, signed or reviewed — so item 59 stays open and P3's second half remains the top unblock. Canonical record: `10_Legal/LEGAL_OS.md` §8. No other menu row, queue row, decision record or tracker item changed here. — Claude Code (Opus 5)
- **v0.1 — 2026-09-16** — Menu created after Batch 3 closed the last "Now" queue items. Groups every remaining decision into D16/runtime, validator code, schema and routing, later-only builds, never-from-A001, and the real pilot path; gives each what it unlocks, what it risks, whether D20 permits A001 evidence to support it, a recommended default and a first safe next prompt. Planning only — nothing decided, implemented or scheduled, and no other file changed. — Claude Code (Opus 5)
