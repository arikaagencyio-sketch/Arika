---
name: content-opportunity-intake
description: Skill C01 of Content (04). Writes one Content Opportunity (DB5) from a real Sector finding or an existing narrative position, runs and records the Strategic DRAGON pass (Diagnosis, Revenue Logic, Architecture, Growth Systems, Operational Intelligence, Navigation), and links or creates the campaign record (DB4) only on a recorded owner direction. Use when content-opportunity-mapper has proposed an opportunity, or when the owner names a new idea to evaluate. Runs before any translation or brief.
---

# C01 · Content Opportunity Intake

You are performing the **apply** step of Content's write layer.

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) first.** Field truth: [`04_Content/contracts/content-databases.json`](../../../04_Content/contracts/content-databases.json) — every DB5 and DB4 field whose writer is `C01`.

> **The one rule that defines this skill: an opportunity is never the starting point of truth.** It points at a Sector finding or an existing narrative position, and it records what proof *would* be required when none exists.

## Step 0 · The write path

| | Data source |
|---|---|
| DB5 Content Opportunity *(write)* | `collection://b9cd2f53-1e6a-4765-aaf4-4742d7d12520` |
| DB4 Campaign Intelligence *(write, owner direction only for CREATE)* | `collection://6f1f092b-2b26-4bef-94e6-b87e00ba9fb6` |
| Sector DB3 findings *(read)* | `collection://72f90a0f-e34e-4c54-9fcd-9af2e108527e` |
| Sector DB7 signals *(read)* | `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` |
| Sector DB9 audience roles *(read)* | `collection://e0513cc9-682f-4dd4-965c-e0292abe86e4` |
| DB2 Narrative *(read)* | `collection://e76c2bec-8077-4b84-9db3-f1f819000745` |

## Inputs

A `content-opportunity-mapper` recommendation (or an owner-named idea) carrying: `opportunity_id`, the atomic unit (problem · insight · solution · proof · action), pillar, house, five impact scores, the Sector finding ID(s) or narrative Position ID, and the proposed `dragon.strategic` block.

## Permitted writes

DB5: every field whose writer is `C01`, including `Strategic DRAGON` and `Strategic DRAGON Notes`. `Decision = Promoted to Brief` only with a recorded owner decision (quote + date). DB4: fields whose writer is `C01`; a new campaign only on a recorded owner direction. **Never** `Revenue Target` (human only) or `Design Folder` (Design writes it).

## Refusals (run `validate_write` first)

R03 no Source, or neither a Sector finding nor a narrative position · R04/R05 a fact without a dated, non-T4 source · R07 a blank or unreasoned Strategic pass · R10 an `Opportunity ID` that already exists · R16 any price or offer term · R19 `Promoted to Brief` without an owner quote. **Never default the Sub-Sector to Hospitality**; leave it empty for agency-wide ideas.

## Procedure

1. **Resolve the source.** Fetch the Sector finding by ID. Carry its tier into `Source Tier` and map its confidence across the boundary (High → Confirmed, Medium → Working Hypothesis, Low → Experimental).
2. **Run the Strategic pass.** For each letter write one line in `Strategic DRAGON Notes`: D (the actual constraint), R (the commercial mechanism), A (the systems producing it), G (the capability that improves it), O (what decision or workflow it changes), N (the next action). Set `Strategic DRAGON` to `Complete`, `Partial` (with which letters are missing and why) or `Not applicable` (with why). Never leave it blank.
3. **Score honestly.** `Total Score` and `Tier` are formulas. A total below 20 has no tier. Leave it below threshold rather than inflating a dimension.
4. **Proof.** If no proof exists, set `Proof Status = Proof required — named` and write what proof would be required.
5. **Match the natural key.** Query DB5 for the `Opportunity ID`. Found → UPDATE or VERSION. Not found → CREATE. If the query fails, stop: the result is incomplete, not empty. Hand the gate the lookup as `{status, checked_at, records}`; only `status: complete` admits a CREATE (R10_LOOKUP_UNVERIFIED).
6. **Apply**, then append the change line to the page body.

## Verification (read-after-write)

Fetch the page by ID. Confirm every written property reads back, and that `Strategic DRAGON` and its notes are present. A mismatch is a partial failure: record it, don't retry blind.

## Handoff

To `content-narrative-review` (C02) for the narrative check, then `content-surface-translation` (C03). The event `CONTENT_OPPORTUNITY_MAPPED` is not published by the runtime; the handoff is manual (contract §10).

## Execution record

Append one line to `04_Content/_memory/skill_runs.jsonl` (Sector envelope, `skill: content-opportunity-intake`). Fixture runs never write there.
