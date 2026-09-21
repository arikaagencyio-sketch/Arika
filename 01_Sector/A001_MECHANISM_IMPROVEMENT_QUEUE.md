# A001 — Mechanism improvement queue

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning.** **Batches 1, 2 and 3 are implemented** (2026-09-16). Batch 1's seven owner-fill items and Batch 2's two owner-workflow items (W2, W4) are in [`INTAKE_OWNER_FILL_STANDARD.md`](INTAKE_OWNER_FILL_STANDARD.md); Batch 3 closed **F1 as superseded by F2** and recorded **O1** as an evaluation-order rule in the pilot close-out §2. **No "Now" items remain.** Everything still open is a genuine owner decision, a later build, or blocked by D16 — none of it implemented, approved or scheduled, and each needs its own owner decision before any file changes.
**Version:** v0.4

> **Governed by D20** (sandbox record §5.1). Every item below is a **mechanism** finding — a missing rule, an unauthored profile, an undefined edge, an unsafe format. Nothing here uses A001 as market, demand, pricing, proof, buyer or capacity evidence, or as a claim about any real hotel. A001 output may justify changing *how the system works*; it may never describe *how the market behaves*.

---

## 1. How to read this

The document-only pilot exercised the agency's intake, fit and governance machinery against a simulated group. Where the machinery bent, that is a mechanism finding and D20 permits acting on it. Where the pilot produced anything resembling a fact about hospitality, it is barred and does not appear here.

**Risk** is the risk of making the change, not of leaving it. **When** is a recommendation to the owner, never a decision:

- **Now** — safe, self-contained, no runtime, no Tier-1 dependency.
- **Later** — needs a prior decision, a Tier-1 ratification, or D16 to be closed first.
- **Never (as an A001 consequence)** — the observation is real, but A001 is not a valid reason to act. Listed so it is not quietly re-proposed later.

Every item traces to the pilot close-out or the sandbox record. Nothing is invented here.

## 2. Intake format improvements

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| F1 | Pipe-table owner fill silently dropped cells twice — one trailing cell, then four cells across three rows in each of four units. Both were caught only by a cell-count guard. | An unsafe input format is a mechanism finding. It says nothing about hospitality. | None — the remedy already exists in D19 and `INTAKE_OWNER_FILL_STANDARD.md` §2 | Low | ✅ **Superseded 2026-09-16 by F2** — the format decision is recorded in D19 and implemented as standard §2. Closed with no file change; restating it elsewhere would only duplicate §2 |
| F2 | The block-per-question format (D19) held: one field per line, so a lost field is visible rather than silent. It exists only as a generated sandbox artifact, not as a documented repo standard. | Promoting a proven-safe format to a documented standard is workflow design. | `INTAKE_OWNER_FILL_STANDARD.md` §2 | Low | ✅ **Implemented 2026-09-16** |
| F3 | An answer was pasted into the wrong block, destroying the original. The format could not catch it — the result was structurally perfect. | A format that cannot detect misplacement is a format gap. A per-block `question_id` confirmation step is a mechanism fix. | `INTAKE_OWNER_FILL_STANDARD.md` §3 | Low | ✅ **Implemented 2026-09-16** |
| F4 | Owner guidance and the validator contradicted each other once: the guidance said "use the list in the question", and the validator then flagged a term that list offered. | An internally inconsistent instruction set is a mechanism defect. | `INTAKE_OWNER_FILL_STANDARD.md` §4 | Low | ✅ **Implemented 2026-09-16** |

## 3. Validator and gate improvements

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| V1 | Substring matching produced false positives: a vendor name matched inside an ordinary word, and a decision reference was read as a bare number. Fixed in the sandbox validator only. | Validator precision is a mechanism concern. | A repo-side validator, if one is ever adopted; the sandbox script is not repo-tracked | Low | **Later** — only if the validator is promoted into the repo |
| V2 | Word-boundary matching, a governance-token exemption for digits, and an exemption for terms quoted by the question itself each removed a class of false positive. | Rule-level fixes to a checker are mechanism fixes. | Same as V1 | Low | **Later** |
| V3 | Structural checks passed a whole tranche that answered the wrong questions, and passed a wrong-block paste. Only a relevance read caught either. | The finding is about what a class of check can and cannot detect. | `INTAKE_OWNER_FILL_STANDARD.md` §5 (policy); validator code unchanged | Medium — a relevance heuristic over-flags and must stay advisory | ◐ **Policy documented 2026-09-16**; code half still **Later** |
| V4 | The relevance heuristic produced more false positives than genuine catches, and under-scored answers that demonstrate rather than restate. It earned its place only as an advisory flag a human reads. | Calibration of a check is a mechanism concern. | `INTAKE_OWNER_FILL_STANDARD.md` §5 (policy); validator code unchanged | Medium | ◐ **Policy documented 2026-09-16**; code half still **Later** |
| V5 | `intake_gate.py --answers` behaved exactly as documented at every stage, and its stage rule was readable in source. No change proposed. | Recorded as a negative finding so it is not "improved" without cause. | None | — | **Never (as an A001 consequence)** |
| V6 | `sector_truth_gate.py` check 6 was added mid-pilot after real drift between the plugin and the database, and has held since. | Already implemented; recorded for completeness. | None — done | — | Done |

## 4. Sector schema and profile gaps

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| S1 | A destination present in the geography database but with no profile blocks Destination Fit. The sandbox recorded the status rather than authoring a profile (D14). | A missing profile is a mechanism gap. **Authoring one is a separate Sector decision requiring real sources — A001 supplies none.** | Sector destination schema and profile set | Medium — must not be filled from simulated data | **Later**, and only from real sources. *Not implemented: no profile has been authored. Only the status distinction is documented, under S2.* |
| S2 | Destinations absent from the geography database cannot be profiled at all without first commissioning the destination. | The distinction between "unprofiled" and "absent" is a structural one the pilot made visible. | `INTAKE_OWNER_FILL_STANDARD.md` §9 | Low | ✅ **Implemented 2026-09-16** — documentation note only; no profile authored, no geography commissioned |
| S3 | No Sector rule covers a property mixing two archetypes (AG-5). The sandbox used a convention — resolve on the main archetype, mark the secondary unruled — explicitly **not** a Sector rule. | An unruled case is a mechanism gap. The sandbox convention is not evidence that any rule is correct. | Hospitality plugin archetype rules | Medium — the rule must come from Sector reasoning, not from A001 | **Later** |
| S4 | A group has no resolvable archetype while the union operator is unbuilt (AG-4). | A missing resolver is a mechanism gap, and the pilot showed the system correctly refusing to guess. | S09 / union-operator build | High — a build, and it gates Phase 4 | **Later** |
| S5 | No Sector agent can check a hotel's company fit; the existing classifiers are B2B SaaS-only (AG-17). Fit was checked by hand throughout. | A missing capability is a mechanism gap. | Sector agent roster | High | **Later** |

## 5. Offer routing and gating implications

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| O1 | Group flags are inherited by every unit and are never suppressed, so a unit that passes every unit-level check can still be correctly ineligible. | This is routing logic behaving as designed. Recording that it holds is documentation. | `A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` §2 (Sector-owned); `OFFER_OS.md` §15 pointer only | Low | ✅ **Implemented 2026-09-16** — recorded as an **evaluation-order rule only**, with an explicit bar on extending it into an ICP, demand, buyer, pricing or capacity claim. No Offer decision, doctrine or ICP change |
| O2 | An `A001` group run would be expected to return `reject` or `needs_more_seed_data` (AG-7), which is the correct outcome, not a defect. | Confirms a gate's intended behaviour. | None | — | **Never (as an A001 consequence)** — and explicitly not a reason to widen any band |
| O3 | A mixed-archetype unit reached a verdict without its unruled secondary ever being resolved, because another rule fired first. A real property could hide the same gap. | Order-of-evaluation masking a gap is a routing-logic finding. | Offer/Sector gate ordering notes | Medium | **Later** |
| O4 | Anything touching the H-bands, the MVP scope, the anti-ICP definition, pricing gates, floors or capacity. | **Barred by D20.** These need market, demand, pricing or capacity evidence, which A001 cannot supply. | None | — | **Never (as an A001 consequence)** |

## 6. Owner workflow improvements

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| W1 | Draft-first write-back (D10) — draft in a scan folder, scan, hand-check, then edit — caught content before it reached the repository every time it ran. | Safe workflow design, named explicitly in D20. | `INTAKE_OWNER_FILL_STANDARD.md` §6 | Low | ✅ **Implemented 2026-09-16** |
| W2 | The key scan was proved in the negative on a planted term, not merely assumed to work. | Testing a control negatively is workflow design. | `INTAKE_OWNER_FILL_STANDARD.md` §10 | Low | ✅ **Implemented 2026-09-16** (Batch 2) |
| W3 | Staged apply — validate, dry-run, write, verify untouched rows byte-identical — refused every defective batch before any write. | Workflow design. | `INTAKE_OWNER_FILL_STANDARD.md` §7 | Low | ✅ **Implemented 2026-09-16** |
| W4 | Stale status claims outlived their truth in several documents, each asserting work had not started after it had. | Documentation drift is a mechanism problem. A "correct the claim, keep the superseded wording marked" convention was used throughout and could be stated once. | `INTAKE_OWNER_FILL_STANDARD.md` §11 | Low | ✅ **Implemented 2026-09-16** (Batch 2) |
| W5 | A gate's rule was read in its source before being relied on, rather than inferred from past runs. | Workflow design. | `INTAKE_OWNER_FILL_STANDARD.md` §8 | Low | ✅ **Implemented 2026-09-16** |

## 7. Runtime blockers — do not touch until D16 is closed

| # | Item | Status | When |
|---|---|---|---|
| R1 | API key rotation (AG-19 · D16) | The single hard stop before any runtime-backed work | **Later** — owner action, and a precondition for everything else in this section |
| R2 | Sandbox memory stream, or shared stream with markers (AG-12 · T1-5) | Tier-1, deferred under D6 | **Later** |
| R3 | Sandbox marker field in skill execution records (AG-13 · T1-4) | Tier-1, deferred under D6 | **Later** |
| R4 | Entity model: `Company`, its parent edge and property-unit meaning (AG-9, AG-10 · T1-1) | Tier-1, deferred under D6 | **Later** |
| R5 | Test-fixture trust value on knowledge objects (AG-11 · T1-3) | Tier-1, deferred under D6 | **Later** |
| R6 | Intake-gate builds: group/child answer files and a test-fixture label mode (AG-1, AG-3) | Deferred under D7 with a documented manual workaround that worked throughout | **Later** |

**Nothing in this section may be started on A001's account while D16 is open.** Each is Tier-1 or owner-gated in its own right.

## 8. Explicitly excluded under D20

The pilot produced material that looks like evidence and is not. None of the following may be drawn from A001, in any department, however phrased:

- Any statement about demand, seasonality, guest mix, origin markets or booking behaviour.
- Any statement about prices, rates, margins, channel costs or commissions.
- Any statement about competitors, comparison sets or market position.
- Any statement about capacity, staffing, hours or delivery effort.
- Any performance figure, conversion claim or proof point.
- Any claim about a real hotel, group or destination, including "a property like this would…".

The simulated answers were written to exercise the machinery. They were never sourced from a market, and no volume of them becomes evidence.

## 9. What happens next

This queue decides nothing. Each item needs an owner decision before any file is touched, and the **Now** items are recommendations, not approvals. The queue is deliberately separate from the close-out so that lessons stay stable while proposals change.

## 10. Cross-references

- [`A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md`](A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md) — what the pilot proved, which controls held, what broke.
- [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) — D20 (§5.1), the gap register (§7), Tier-1 changes (§8), the run plan (§9).
- [`OWNER_INPUT_NEEDED.md`](../00_Agency_Governance/OWNER_INPUT_NEEDED.md) item 74 — open owner decisions, of which API key rotation is the last runtime blocker.
- [`OFFER_OS.md`](../02_Offer/OFFER_OS.md) §15 — the D20 boundary as it applies to Offer.

## 11. Changelog

- 2026-09-21 — **Pointer: a bounded agency-systems test plan now exists** — `01_Sector/A001_AGENCY_SYSTEMS_TEST_PLAN.md` (planning only). It turns this queue’s items into a test matrix across Sector, Offer, Content, Marketing and Sales, and records the finding that **§7’s R2/R3/R5 are what block every runtime test** — without a sandbox stream or skill marker, an A001 run would write an **unmarked** line into a shared department stream. **This queue is unchanged**; no item was started, approved or reclassified. — Claude Code (Opus 5)
- **v0.4 — 2026-09-16** — **Batch 3 implemented: the last two "Now" items closed.**
  - **F1 → superseded by F2**, with **no file change**. Its remedy already exists in D19 and `INTAKE_OWNER_FILL_STANDARD.md` §2; implementing it separately would have duplicated §2 or edited the Governance-owned intake profile (under review as item 73) and the Offer-owned overlay to restate it.
  - **O1 → implemented** as a single evaluation-order sentence in `A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md` §2, where the finding was already recorded: *inherited group flags are not suppressed at unit level, so unit-level passes do not imply eligibility.* It carries an explicit bar on extension into an ICP, demand, buyer, pricing or capacity claim. `OFFER_OS.md` received a §15 changelog pointer only — **no Offer decision, doctrine, band, gate or ICP changed**, because Offer has no routing-notes home and a new section would have overstated an A001-derived note's standing.
  - **No "Now" items remain.** Still open: V1, V2, V5 and V6 in §3; V3/V4's code half; S1, S3, S4 and S5; O2, O3 and O4; and R1–R6 behind D16.
  - **Nothing implemented in code:** no validator, runtime, gate, agent or skill change; no destination profile authored. — Claude Code (Opus 5)
- **v0.3 — 2026-09-16** — **Batch 2 implemented: the two remaining owner-workflow standards.** **W2** negative-testing the scan boundary → `INTAKE_OWNER_FILL_STANDARD.md` §10, and **W4** correcting stale claims with a dated note rather than a silent rewrite → §11. With these, **every item in §6 Owner workflow is implemented** (W1–W5).
  - **Still open elsewhere:** F1 and O1 remain "Now" and unimplemented; V3/V4 stay policy-documented with their code half open; S1 stays unimplemented, with no destination profile authored and none permitted from simulated data (D20); everything else in §3, §4, §5 and §7 is unchanged.
  - **Nothing implemented in code:** no validator, runtime, gate, agent or skill change. — Claude Code (Opus 5)
- **v0.2 — 2026-09-16** — **Batch 1 implemented: owner-fill workflow standards.** Seven items moved to implemented, all in the new [`INTAKE_OWNER_FILL_STANDARD.md`](INTAKE_OWNER_FILL_STANDARD.md): **F2** block-per-question format for large stages (§2) · **F3** `question_id` confirmation before typing (§3) · **F4** guidance and validator written together (§4) · **W1** draft-first write-back (§6) · **W3** staged apply (§7) · **W5** read the gate source before forcing a stage (§8) · **S2** the unprofiled-versus-absent destination distinction as a documentation note (§9).
  - **V3 and V4 are half-done by design:** the policy that relevance checks are advisory but must be read is now documented (§5); their validator-code half stays **Later**.
  - **S1 is explicitly not implemented.** No destination profile was authored, and none may be from simulated data (D20). Only the status distinction is documented.
  - **W2 and W4 stay open.** Both are "Now" items and were simply not in this batch.
  - **Nothing runtime changed**, and no H-band, ICP, pricing, capacity, proof, buyer or market claim was touched. — Claude Code (Opus 5)
- **v0.1 — 2026-09-16** — Queue created from the document-only pilot, under D20. Thirty items — intake formats (F1–F4), validators and gates (V1–V6), Sector schema and profile gaps (S1–S5), Offer routing implications (O1–O4), owner workflow (W1–W5) and runtime blockers (R1–R6) — plus an explicit exclusion list. Planning only: nothing implemented, approved or scheduled. — Claude Code (Opus 5)
