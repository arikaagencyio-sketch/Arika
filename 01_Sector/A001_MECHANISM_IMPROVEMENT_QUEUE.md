# A001 — Mechanism improvement queue

**Department:** Sector (01) — owns this record.
**Status:** 🟡 **Planning only.** Nothing here is implemented, approved or scheduled. Each item needs its own owner decision before any file changes.
**Version:** v0.1

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
| F1 | Pipe-table owner fill silently dropped cells twice — one trailing cell, then four cells across three rows in each of four units. Both were caught only by a cell-count guard. | An unsafe input format is a mechanism finding. It says nothing about hospitality. | The intake overlay and worksheet-generation convention; D19 already records the replacement | Low | **Now** |
| F2 | The block-per-question format (D19) held: one field per line, so a lost field is visible rather than silent. It exists only as a generated sandbox artifact, not as a documented repo standard. | Promoting a proven-safe format to a documented standard is workflow design. | A format note in the intake profile or overlay | Low | **Now** |
| F3 | An answer was pasted into the wrong block, destroying the original. The format could not catch it — the result was structurally perfect. | A format that cannot detect misplacement is a format gap. A per-block `question_id` confirmation step is a mechanism fix. | Worksheet template and its fill instructions | Low | **Now** |
| F4 | Owner guidance and the validator contradicted each other once: the guidance said "use the list in the question", and the validator then flagged a term that list offered. | An internally inconsistent instruction set is a mechanism defect. | Worksheet guidance text and validator rules, together | Low | **Now** |

## 3. Validator and gate improvements

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| V1 | Substring matching produced false positives: a vendor name matched inside an ordinary word, and a decision reference was read as a bare number. Fixed in the sandbox validator only. | Validator precision is a mechanism concern. | A repo-side validator, if one is ever adopted; the sandbox script is not repo-tracked | Low | **Later** — only if the validator is promoted into the repo |
| V2 | Word-boundary matching, a governance-token exemption for digits, and an exemption for terms quoted by the question itself each removed a class of false positive. | Rule-level fixes to a checker are mechanism fixes. | Same as V1 | Low | **Later** |
| V3 | Structural checks passed a whole tranche that answered the wrong questions, and passed a wrong-block paste. Only a relevance read caught either. | The finding is about what a class of check can and cannot detect. | Validator design notes; the review workflow | Medium — a relevance heuristic over-flags and must stay advisory | **Later** |
| V4 | The relevance heuristic produced more false positives than genuine catches, and under-scored answers that demonstrate rather than restate. It earned its place only as an advisory flag a human reads. | Calibration of a check is a mechanism concern. | Validator design notes | Medium | **Later** |
| V5 | `intake_gate.py --answers` behaved exactly as documented at every stage, and its stage rule was readable in source. No change proposed. | Recorded as a negative finding so it is not "improved" without cause. | None | — | **Never (as an A001 consequence)** |
| V6 | `sector_truth_gate.py` check 6 was added mid-pilot after real drift between the plugin and the database, and has held since. | Already implemented; recorded for completeness. | None — done | — | Done |

## 4. Sector schema and profile gaps

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| S1 | A destination present in the geography database but with no profile blocks Destination Fit. The sandbox recorded the status rather than authoring a profile (D14). | A missing profile is a mechanism gap. **Authoring one is a separate Sector decision requiring real sources — A001 supplies none.** | Sector destination schema and profile set | Medium — must not be filled from simulated data | **Later**, and only from real sources |
| S2 | Destinations absent from the geography database cannot be profiled at all without first commissioning the destination. | The distinction between "unprofiled" and "absent" is a structural one the pilot made visible. | Geography schema documentation | Low | **Now** — documenting the distinction only |
| S3 | No Sector rule covers a property mixing two archetypes (AG-5). The sandbox used a convention — resolve on the main archetype, mark the secondary unruled — explicitly **not** a Sector rule. | An unruled case is a mechanism gap. The sandbox convention is not evidence that any rule is correct. | Hospitality plugin archetype rules | Medium — the rule must come from Sector reasoning, not from A001 | **Later** |
| S4 | A group has no resolvable archetype while the union operator is unbuilt (AG-4). | A missing resolver is a mechanism gap, and the pilot showed the system correctly refusing to guess. | S09 / union-operator build | High — a build, and it gates Phase 4 | **Later** |
| S5 | No Sector agent can check a hotel's company fit; the existing classifiers are B2B SaaS-only (AG-17). Fit was checked by hand throughout. | A missing capability is a mechanism gap. | Sector agent roster | High | **Later** |

## 5. Offer routing and gating implications

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| O1 | Group flags are inherited by every unit and are never suppressed, so a unit that passes every unit-level check can still be correctly ineligible. | This is routing logic behaving as designed. Recording that it holds is documentation. | Offer routing notes | Low | **Now** — documentation only |
| O2 | An `A001` group run would be expected to return `reject` or `needs_more_seed_data` (AG-7), which is the correct outcome, not a defect. | Confirms a gate's intended behaviour. | None | — | **Never (as an A001 consequence)** — and explicitly not a reason to widen any band |
| O3 | A mixed-archetype unit reached a verdict without its unruled secondary ever being resolved, because another rule fired first. A real property could hide the same gap. | Order-of-evaluation masking a gap is a routing-logic finding. | Offer/Sector gate ordering notes | Medium | **Later** |
| O4 | Anything touching the H-bands, the MVP scope, the anti-ICP definition, pricing gates, floors or capacity. | **Barred by D20.** These need market, demand, pricing or capacity evidence, which A001 cannot supply. | None | — | **Never (as an A001 consequence)** |

## 6. Owner workflow improvements

| # | Source observation from A001 | Why D20 allows it | Files likely affected | Risk | When |
|---|---|---|---|---|---|
| W1 | Draft-first write-back (D10) — draft in a scan folder, scan, hand-check, then edit — caught content before it reached the repository every time it ran. | Safe workflow design, named explicitly in D20. | Governance workflow notes | Low | **Now** |
| W2 | The key scan was proved in the negative on a planted term, not merely assumed to work. | Testing a control negatively is workflow design. | Governance workflow notes | Low | **Now** |
| W3 | Staged apply — validate, dry-run, write, verify untouched rows byte-identical — refused every defective batch before any write. | Workflow design. | Apply-workflow notes | Low | **Now** |
| W4 | Stale status claims outlived their truth in several documents, each asserting work had not started after it had. | Documentation drift is a mechanism problem. A "correct the claim, keep the superseded wording marked" convention was used throughout and could be stated once. | Governance documentation conventions | Low | **Now** |
| W5 | A gate's rule was read in its source before being relied on, rather than inferred from past runs. | Workflow design. | Governance workflow notes | Low | **Now** |

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

- **v0.1 — 2026-09-16** — Queue created from the document-only pilot, under D20. Thirty items — intake formats (F1–F4), validators and gates (V1–V6), Sector schema and profile gaps (S1–S5), Offer routing implications (O1–O4), owner workflow (W1–W5) and runtime blockers (R1–R6) — plus an explicit exclusion list. Planning only: nothing implemented, approved or scheduled. — Claude Code (Opus 5)
