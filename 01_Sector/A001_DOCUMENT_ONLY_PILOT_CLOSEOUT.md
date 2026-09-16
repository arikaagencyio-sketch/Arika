# A001 — Document-only pilot close-out

**Department:** Sector (01) — owns this record. Offer (02) may read it, but **not as Offer evidence** (§9).
**Status:** ✅ Document-only pilot closed 2026-09-16 · ✅ Use of this evidence bounded by **D20** (mechanisms only) · 🔴 **No runtime-backed work** — blocked by D16 until the API key is rotated (AG-19).
**Version:** v0.2

> **IDs only.** A001 is a **fictional** hospitality group. Nothing here is evidence about any market, property or buyer. Read [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) §2 and §4 before using any A001 value anywhere.

---

## 1. What A001 was for

A001 is a group-level **simulated** Hospitality Sector Sandbox and pilot-company architecture specimen. Its purpose was never to learn about hospitality. It was to run the agency's own intake, fit and governance machinery against a company shaped like a real one — a group with several properties — and find out where that machinery bends, without a real client bearing the cost of the discovery.

It is **not** a real client, prospect, lead, CRM company or the item 72 real-property pilot. `PILOT-H-001` stays reserved for that.

## 2. What the group-level pilot proved

Running the group (`A001`) through S1 produced the result the architecture should produce, by design rather than by accident:

- **A group has no resolvable archetype.** The `Hospitality Group` union operator is not built (AG-4), so the group cannot be classified as a single company. The system said so instead of guessing.
- **A central brand and direct-booking team is an anti-ICP marker**, not a neutral fact. Owner Decision 71 treats it as disqualifying, and the group carries it.
- **The group sits above every size band.** No band in the current model describes it.
- **Those three flags are inherited by every unit and are never suppressed.** That is the single most important structural finding: no unit can be assessed as though it were independent, however clean its own checks are.

The group verdict was recorded as `SIMULATED_VERDICT` — outside the current offer ICP, by design.

## 3. What `A001-P07` proved as the Phase 3 slice

`A001-P07` is the only unit that passes archetype, Destination Fit and the H-band together (D18). That made it the slice, and it proved two things:

- **A unit can be fully clean and still be ineligible.** Every unit-level check passes, and the inherited group flags still place it outside the current offer ICP. The slice is a group-architecture test, never an MVP audit.
- **Intake can reach S2 entirely on documentation.** S2 was filled and applied in four passes under the document-only run mode (D15), every required S2 row was declared, and the gate passed at S2 — with no agent, skill, scheduler, event or runtime memory write. Reaching a stage is an intake milestone, **not** a classification, so no verdict line was added for it.

## 4. What the other units proved through controlled failure

The nine units were shaped so that they differ on one axis at a time. That turned the sandbox into a set of controlled comparisons rather than nine anecdotes:

| Comparison | Held constant | Varied | What it showed |
|---|---|---|---|
| `A001-P06` · `A001-P09` | archetype, destination status, band | nothing | Identically-shaped units return identical verdicts — the rules are deterministic |
| `A001-P04` · `A001-P05` | archetype, destination status | band | The size rule is independent of the geography rule |
| `A001-P01` · `A001-P08` | archetype and destination both pass | band | The MVP band is bounded at both ends — one above, one below |
| `A001-P03` · `A001-P04` | both fail destination and size | destination status | A missing profile is recoverable by authoring; an absent database row is not |
| `A001-P07` · `A001-P08` | archetype, destination, the declared link | band | The linked-unit relationship is recorded but undefined (AG-9) |
| `A001-P02` | — | two archetypes | The only test of a mixed-archetype property. Its size rule fired on the main band alone, so the unruled secondary never had to be resolved to reach a verdict — which is exactly how that gap stays invisible in a real engagement |

## 5. What the controls did

Each of these was exercised repeatedly, not merely described:

- **Key scan (`--scan`).** Every sandbox file and every repo-bound draft was scanned before it moved. It was also proved in the negative: a deliberately planted key term was caught.
- **D10 draft-first write-back.** Nothing reached the repository without being drafted in the sandbox's scan folder, scanned, and hand-checked. Every verdict line and both close-outs went through it.
- **Documentation truth gate.** Run after every repository change, and extended during the pilot with a destination-profile check after drift was found between the plugin and the database.
- **Block-per-question format (D19).** Adopted after pipe tables lost cells twice. One field per line makes a lost field visible rather than silent.
- **Staged apply.** Worksheets are validated, dry-run, then written, with the script refusing on any defect and verifying that untouched rows stayed byte-identical.
- **Relevance review.** Advisory, never an automatic failure — a human reads every flag.
- **The stage gate was read, not assumed.** `stage_reached` moved to S2 only after the gate's own rule was read in the source, re-checked by a guard, and confirmed by a passing run, with an automatic revert had it failed.

## 6. What broke, or nearly did

Recorded plainly, because the near-misses are the point of a pilot:

- **Pipe tables dropped cells during owner fill — twice.** Once a single trailing cell, once four cells across three rows in each of four units. Both were caught by a cell-count guard before anything was written; both needed authorised repairs. This is what retired the format (D19).
- **An answer was pasted into the wrong block.** One unit's answer overwrote another's, destroying the original text. The relevance check caught it; the format check could not, because the result was structurally perfect.
- **A whole tranche answered the wrong questions.** Twelve blocks were filled with a plausible general theme instead of answers to their own questions. Format and content checks passed them; only relevance caught it.
- **The validator produced false positives.** A vendor name matched inside an ordinary word, a decision reference was read as a bare number, and a place name quoted by the question's own option list was flagged as a disclosure. Each was fixed at the rule level — word boundaries, governance-token exemption, and an exemption for terms the question itself offers.
- **Stale claims outlived their truth.** Several documents asserted that work had not started after it had. Each was corrected in place, with the superseded wording kept and marked.

The pattern worth carrying: **structural checks catch structural defects, and nothing else.** Meaning needs a reader.

## 7. Governance decisions now in force

Nineteen owner decisions, D1–D19, are recorded in the sandbox record §5.1 — sandbox root and key custody, package custody, run mode, deferred Tier-1 changes, intake tooling, answer labelling, the S2 stage cap, write-back, answer sourcing and granularity, unit archetypes, geography policy, and the five Phase 3 entry decisions. Ruling G1 re-scoped the phase gates.

Two of them define the current boundary:

- **D9 — S3–S5 stay `BLOCKED`.** The sandbox has no client system. S2 is the end of the intake road for A001 as scoped; going further means revisiting D9, not filling more rows.
- **D16 — runtime-backed work is blocked** until the API key is rotated (AG-19). Document-only work never needed the key; anything beyond it does.

## 8. Current hard stop

**D16.** Document-only work may continue. Anything runtime-backed — any agent, skill, scheduler, event or runtime memory write — waits on the API key rotation. That is the only remaining Phase 3 entry blocker; run mode (D15), ratification (D17) and slice scope (D18) are decided.

## 9. What this document is not

- **Not an Offer verdict.** A001 amends nothing in Offer (02): not the H-band model, not the MVP scope, not the anti-ICP definition, not the pricing gates.
- **Not CRM or Sector-store evidence.** A001 may not enter the Offer runtime, the Sector store, the CRM or any shared store (D17).
- **Not pricing.** Pricing was skipped for every unit and every phase.
- **Not a claim about any real client, market, property or buyer.** Every value is simulated. A `SIMULATED_VERDICT` shows only that a gate ran (sandbox record §4 rule 4).

Simulated evidence can show that a **mechanism** behaves as documented. It cannot show what a real property would answer.

**This is now binding as D20** (sandbox record §5.1, owner decision 2026-09-16): A001 output may be used to improve **mechanisms only** — schemas, gates, intake formats, validators, routing logic, documentation and safe workflow design — and may **never** be used as market, demand, pricing, proof, buyer or capacity evidence, or as any claim about real hotels. The test is whether the change is to *how the system works* or to *how the market behaves*. It applies in every department, permanently.

## 10. Before a real pilot

| # | Do this first | Why |
|---|---|---|
| 1 | **Rotate the API key** (AG-19 · D16) | The hard stop. No runtime-backed work until it is done and recorded |
| 2 | **Decide the real client folder, storage and legal path** | A real engagement carries real data. The storage location, retention and the legal review path are undecided — the legal path is tracked separately as item 59 |
| 3 | **Do not use pipe-table owner fill for larger stages** | It lost cells twice at the smaller stage. Use the block-per-question format, or something equally loss-evident |
| 4 | **Keep public research off unless explicitly approved** | A001 ran with public research disabled throughout. For a real property this is a per-engagement permission, recorded before anyone looks at a page |
| 5 | ~~Decide how simulated evidence may inform Offer and Sector changes~~ ✅ **Decided 2026-09-16 — D20** | A001 evidence may improve **mechanisms only**: schemas, gates, intake formats, validators, routing logic, documentation, safe workflow design. It may **not** serve as market, demand, pricing, proof, buyer or capacity evidence, or as any claim about real hotels. Recorded in the sandbox record §5.1 |

## 11. Cross-references

- [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) — the sandbox record: decisions (§5.1), child register and verdicts (§6), gap register (§7), run plan and Phase 3 progress (§9).
- [`Hospitality Revenue Content OS - Full Push Readiness Packet.md`](../02_Offer/Hospitality%20Revenue%20Content%20OS%20-%20Full%20Push%20Readiness%20Packet.md) — the **real** single-property push. A001 does not satisfy it; `PILOT-H-001` stays reserved.
- [`OFFER_OS.md`](../02_Offer/OFFER_OS.md) §3 Hospitality entry offer and §8 Decision Log — what A001 leaves untouched.
- [`OWNER_INPUT_NEEDED.md`](../00_Agency_Governance/OWNER_INPUT_NEEDED.md) item 74 — the open owner decisions, of which API key rotation is the last blocker for runtime-backed work.

## 12. Changelog

- **v0.2 — 2026-09-16** — **D20 recorded, closing the open decision this document raised.** "Before a real pilot" item 5 is marked decided, and §9 now states the binding rule: A001 evidence may improve **mechanisms only** — schemas, gates, intake formats, validators, routing logic, documentation, safe workflow design — and may never serve as market, demand, pricing, proof, buyer or capacity evidence, or as a claim about real hotels. The canonical wording lives in the sandbox record §5.1 as D20; this document points to it rather than restating it as a second source. — Claude Code (Opus 5)
- **v0.1 — 2026-09-16** — Close-out written at the end of the document-only pilot: purpose, what the group and `A001-P07` proved, the controlled failure patterns across the other units, which controls worked, what broke or nearly broke, the D1–D19 governance position, the D16 hard stop, the limits on how this may be used, and a five-point list to settle before a real pilot. IDs and stage labels only. — Claude Code (Opus 5)
