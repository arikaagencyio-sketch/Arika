# Intake owner-fill standard

**Department:** Sector (01) — owns this record. Applies to any intake work where an owner types answers into a worksheet.
**Status:** ✅ **The current Sector working standard for owner fill**, adopted 2026-09-16. It stands as written **pending any later intake-profile ratification** — Governance (00) owns the universal intake profile (item 73), and if that ratification absorbs or supersedes these rules, this record defers to it.
**Version:** v0.3

> **Origin and limits.** Every rule here comes from the A001 document-only pilot and is adopted under **D20** (sandbox record §5.1): simulated evidence may improve **mechanisms only** — schemas, gates, intake formats, validators, routing logic, documentation and safe workflow design. Nothing here rests on a claim about demand, guests, prices, competitors or any real property, and nothing here changes the H-bands, the ICP, pricing, capacity or any destination profile.

---

## 1. Why this exists

Owner fill is the point where a human types free text into a structured file that a gate will later parse. The A001 pilot ran that loop repeatedly and found that the failures cluster in two kinds: **structural** (a field is lost or displaced) and **semantic** (a well-formed answer answers the wrong question). Different mechanisms catch each, and one will never catch the other. These rules are the cheapest form of each.

Governance (00) owns the universal intake profile. This is **the current Sector working standard** for owner fill and applies now; it is ready to fold into that profile's ratification (item 73), and defers to it if that ratification absorbs or supersedes these rules.

## 2. Use the block-per-question format for large owner-fill stages

**Rule.** For any large owner-fill stage — S2 and any stage of comparable size — the worksheet must present **one block per question with one field per line**. Pipe-table rows must not be used for owner-typed answers at those stages.

**Why.** In a pipe table every field of an answer shares one line, so a single deleted `|` silently shifts each remaining cell's meaning: a value slides into the state column and still looks plausible. In a block, each field is its own `key: value` line, so damage removes or malforms a **named** line — visible on sight and unambiguous to a parser.

**Evidence.** Pipe-table owner fill lost cells twice during the pilot: once a trailing cell, then several cells across three rows in each of four units. Both were caught only by a cell-count guard in the apply script, and both required authorised repairs before anything could be written.

**Small stages.** A short worksheet may still use a table, because a defect in a handful of rows is visible on inspection. The risk scales with the number of rows, not the format alone.

## 3. Confirm the `question_id` before typing

**Rule.** Every block carries its own `question_id` line, and the person filling it **confirms that line before typing into the block**. Any tool that applies a filled worksheet must verify that each block's `question_id`, question text and requirement flag still match the question bank, and must refuse the apply if any of them was altered.

**Why.** Structural checks cannot detect a well-formed answer placed in the wrong block. The result is perfectly shaped and simply wrong.

**Evidence.** During the pilot an answer was pasted into a neighbouring block and overwrote the original, which was then unrecoverable from the file. Every format check passed. Only a read of the answer against its own question found it.

## 4. Guidance and validator must agree

**Rule.** Worksheet guidance and the validator's rules are written and changed **together**. When guidance invites a specific form of answer, the validator must accept that form. When the validator bars something, the guidance must say so in the block where it applies.

**Why.** An instruction set that contradicts its own checker wastes the filler's effort and, worse, trains them to ignore flags.

**Evidence.** A block's guidance said to answer using the option list in the question; the validator then flagged a term that list itself offered. The guidance was right and the rule was wrong. The fix belonged in the rule: **a term quoted by the block's own question is not a disclosure.**

## 5. Relevance checks are advisory, and must be read

**Rule.** A relevance or similarity check on an answer is **advisory**. It never fails an apply on its own. Every flag it raises **must be read by a person**, and the decision recorded — accepted, or sent back for repair.

**Why.** These checks are heuristics. They under-score answers that *demonstrate* rather than *restate* — an answer giving a decision chain in order without echoing the words "steps" or "decide" scores badly and is correct. Treating that as a hard failure would train people to pad answers with the question's vocabulary.

**Evidence.** Across the pilot the relevance heuristic produced more false positives than genuine catches. It also produced the only two catches that mattered: a whole tranche that answered the wrong questions, and the wrong-block paste. Both had passed every structural check. **Advisory but mandatory reading** is what makes it worth keeping.

**Standing policy (queue items V3 and V4, recorded 2026-09-16).**

1. **Relevance checks stay advisory.** They must be read; they must **not hard-fail** an apply.
2. **This does not change without a separate owner decision.** Until one is taken, a relevance flag is information for a person, never a stop.
3. **Code enforcement, if any, is a later decision.** No validator code has been written or changed for this, and none is proposed here. The rule today is procedural: nothing in the repository enforces it, and that is deliberate.

If enforcement is ever built, it must preserve the advisory default. A flag that stops work is a different instrument with different failure modes, and the pilot's evidence — more false positives than catches — does not support one.

## 6. Draft repo-bound lines first, then scan, then write

**Rule.** Any line destined for a repository file that originates in a client or sandbox folder is **drafted in a scan folder first**, scanned against the engagement's key file, checked by hand for what a scan cannot see — numbers, place names, name variants, labels — and only then written into the repository.

**Why.** A repository with an auto-commit hook makes every write permanent within minutes. The draft step is the last point at which a mistake is cheap.

**Evidence.** In A001 this is D10. Every verdict line, close-out and checkpoint passed through it, and the hand-check caught content the scan could not — coincidental numbers that matched source data, and a stale claim that had outlived its truth.

## 7. Apply large answer sets in stages

**Rule.** Applying a filled worksheet to an answers file runs in this order: **validate → dry run → write → verify**. The apply tool must refuse the whole batch on any defect rather than write part of it, and must confirm after writing that every row outside the target set is byte-identical and that header fields are unchanged.

**Why.** A partial write to an answers file is worse than no write: the file looks applied and is not, and the difference is invisible without a diff.

**Evidence.** The staged apply refused every defective batch during the pilot — unfilled placeholders, malformed rows, altered question text — before any file was touched. The byte-identical check is what made "S1 answers unchanged" a verified statement rather than an assertion.

## 8. Read the gate's source before forcing a stage

**Rule.** Before setting or advancing a stage marker, **read the gate's own rule in its source** and confirm the file satisfies it. Never infer a gate's behaviour from the fact that earlier runs passed. If a stage is set, the gate runs immediately afterwards, and the change reverts automatically if it fails.

**Why.** A stage marker is a claim that a file has reached a level of completeness. Setting it on an assumption puts a false claim into a governed record.

**Evidence.** In the pilot the rule was read directly — a required row at or below the stage may not be left unasked — and it settled two decisions that guesswork would have got wrong: an earlier stage move was correctly refused while one required row was outstanding, and the later move was made only after a guard re-checked the rule and a gate run confirmed it.

## 9. Destination status: unprofiled is not absent

**Documentation note only. This authors no destination profile and commissions no geography.**

Two different states block a destination-fit check, and they are not interchangeable:

| Status | Meaning | What would clear it |
|---|---|---|
| `in_DB11_not_profiled` | The destination exists in the geography database but has no profile authored | Authoring a profile, from **real sources**, as a separate Sector decision |
| `not_in_DB11` | The destination is absent from the geography database entirely | Commissioning the destination first; no profile can exist until then |

**Why the distinction matters.** They look identical at the point of failure — both read as "destination fit blocked" — but one is an authoring gap inside existing scope and the other needs a prior decision to bring the place into scope at all. Recording only "blocked" loses that, and the two need different owners and different work.

**What this note does not do.** It does not author, request or imply any profile, and it does not assert anything about any destination. A profile must be written from real sources; simulated material may never fill one (D20).

## 10. Negative-test the scan boundary

**Rule.** Where a key scan protects the repository from a client or sandbox folder, **prove the scan in the negative before relying on it**, and re-prove it whenever either side changes. A scan that has never failed is indistinguishable from a scan that *cannot* fail, and both look like a clean pass.

**When a negative test is required.**

- Before the first repository-bound write of an engagement.
- After any change to the key file.
- After any change to the scanning tool or its rules.
- After any change to what the scan is asked to cover.

**How to run it without exposing a key value.**

1. Build the test file **by script, reading from the key file**, into the engagement's scan area outside every git tree. The planted term is never typed by hand, never pasted into a conversation and never displayed.
2. Run the scan against that file and read **only the exit status and the pass/fail word**. Do not echo the tool's finding lines — they quote the matched term.
3. Confirm the result is a **failure**. A pass here means the boundary is not working.
4. Delete the test file.

**Where to record that it passed.** A dated line in the engagement's admin record — its decisions or setup-status file — naming the test, the date and the outcome. **Record the outcome only.** The planted term, the key value and the tool's finding lines never enter that record, the repository, or a commit message.

**Why.** Every later scan that passes is only as meaningful as the one demonstration that the scan can fail. Without it, "PASS" is an untested assumption wearing the clothes of a control.

**Evidence.** In the pilot the boundary was proved this way once, against a planted term that was never printed, and the result recorded as a dated pass line in the sandbox admin record. Every subsequent pass meant something because of that one deliberate failure.

## 11. Correct stale claims with a dated note, not a silent rewrite

**Rule.** When text that describes the present has become false, **correct it in place and keep the superseded wording as a marked note**. When text is dated history, leave it exactly as written.

**Live drift versus dated history.**

| Kind | Where it appears | What to do |
|---|---|---|
| **Live text** — describes the present | Status lines, gate cells, register rows, section bodies, a tracker's open-item rows | Correct it. It is drift the moment it stops being true |
| **Dated history** — records a moment | Changelog entries, decision-log entries, anything a reader enters through a date, and "earlier the same day" chains | Leave as written. Rewriting it destroys the record |

**The test.** Ask what a reader would do if they believed the sentence today. If they would *act on it*, it is live text and must be true now. If they would *understand what was true then*, it is history and must stay as written.

**When a `Was:` note is warranted.**

- The superseded wording was **true when written** and has since been overtaken.
- The change touches a gate, a status, or a claim about what has or has not happened.
- The same claim appears in more than one place, and a reader may meet a stale copy first.

**When it is not.** Wording that was **never** true — a typo, a miscount, a wrong reference — is simply fixed, and the fix noted in the changelog. Do not preserve a false statement as though it once had standing.

**Form.** *Was: "&lt;superseded wording&gt;" — true only until &lt;what changed&gt;.*

**Evidence.** The pilot produced repeated stale claims: several documents asserted that work had not started after it had. Each live occurrence was corrected in place with the superseded wording marked, while the dated changelog entries recording the earlier state were deliberately left untouched. A later audit found surviving occurrences of one such phrase and confirmed each was legitimate — some in dated entries, one in a header's history chain, one inside a `Was:` quotation. Without the distinction, that audit would have read as drift and "fixed" the record.

## 12. What this standard does not cover

- It changes **no runtime code**, no agent, no skill and no gate implementation.
- It changes **no H-band, ICP, pricing, capacity, proof, buyer or market position**, and authors **no destination profile**.
- It is not evidence about any sector, property or buyer. It is a set of working rules for how a human and a gate exchange a file.

## 13. Cross-references

- [`A001_MECHANISM_IMPROVEMENT_QUEUE.md`](A001_MECHANISM_IMPROVEMENT_QUEUE.md) — the full queue; this standard implements its Batch 1.
- [`A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md`](A001_DOCUMENT_ONLY_PILOT_CLOSEOUT.md) — the pilot these rules came from.
- [`A001_HOSPITALITY_SECTOR_SANDBOX.md`](A001_HOSPITALITY_SECTOR_SANDBOX.md) — D10 (write-back), D19 (block format) and D20 (limits on simulated evidence), §5.1.
- [`CLIENT_INTAKE_PROFILE.md`](../00_Agency_Governance/CLIENT_INTAKE_PROFILE.md) — the universal intake profile, Governance-owned and awaiting ratification under item 73. This standard is ready to fold into it.

## 14. Changelog

- **v0.3 — 2026-09-16** — **Batch 2 adopted: the two remaining owner-workflow standards.** Two new sections, drawn from the A001 pilot under D20.
  - **§10 Negative-test the scan boundary (W2).** A key scan must be proved in the negative before it is relied on, and re-proved when the key file, the tool or the scan's coverage changes. It sets how to run the test without exposing a key value — build the file by script from the key, read only the exit status and pass/fail word, confirm a *failure*, delete the file — and where to record it: a dated outcome-only line in the engagement's admin record, never the term.
  - **§11 Correct stale claims with a dated note (W4).** Live text must be corrected when it goes false; dated history is never rewritten. Includes the test for telling them apart, when a `Was:` note is warranted, and when wording that was never true should simply be fixed instead.
  - Trailing sections renumbered: "What this standard does not cover" §10 → §12, "Cross-references" §11 → §13, "Changelog" §12 → §14. Sections §2–§9 are unchanged, so every reference to them still resolves.

  Documentation only: no code written or changed, no runtime, gate, agent or skill touched, and no H-band, ICP, pricing, capacity, proof, buyer, market claim or destination profile affected. — Claude Code (Opus 5)
- **v0.2 — 2026-09-16** — **Adoption status and the V3/V4 standing policy recorded.** The status line now states that this is **the current Sector working standard for owner fill**, standing as written pending any later intake-profile ratification (Governance item 73), to which it defers. §5 gains the standing policy in three clauses: relevance checks stay **advisory and must not hard-fail**; that does not change without a **separate owner decision**; and **code enforcement, if any, is a later decision** — none is written, changed or proposed, and the rule is deliberately procedural. Documentation only: no validator code, no runtime code, no gate, agent or skill touched, and no H-band, ICP, pricing, capacity, proof, buyer, market claim or destination profile affected. — Claude Code (Opus 5)
- **v0.1 — 2026-09-16** — Adopted from the A001 document-only pilot under D20, implementing queue Batch 1: the block-per-question format for large stages (F2), the `question_id` confirmation rule (F3), guidance and validator written together (F4), relevance checks advisory but mandatory reading (documentation half of V3/V4), draft-first write-back (W1), staged apply (W3), and reading the gate source before forcing a stage (W5). Adds the unprofiled-versus-absent destination distinction as a documentation note only (S2). No runtime change, no destination profile, no Offer or ICP change. — Claude Code (Opus 5)
