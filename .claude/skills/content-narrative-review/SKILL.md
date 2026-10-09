---
name: content-narrative-review
description: Skill C02 of Content (04). Reviews a piece against the agency narrative and the two-pass DRAGON order (Strategic before Editorial), and is the only writer of the Narrative Intelligence Registry (DB2) — new positions, versions and supersessions. Use when content-narrative-architect returns a verdict, before a translation is approved, or when a narrative position must change. Never rewrites a superseded position.
---

# C02 · Content Narrative Review

You are performing the **apply** step of Content's write layer.

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) first** (§4 two-pass DRAGON). Field truth: DB2 in [`content-databases.json`](../../../04_Content/contracts/content-databases.json).

> **The one rule that defines this skill: a narrative position is versioned, never edited into something else.** A changed belief gets a new `Position ID` and the old record is `Superseded`, with its history intact.

## Step 0 · The write path

| | Data source |
|---|---|
| DB2 Narrative *(write)* | `collection://e76c2bec-8077-4b84-9db3-f1f819000745` |
| DB5 / DB6 / DB7 *(read: the passes and the copy under review)* | see the contract §3 |

## Two jobs

**1. Review (writes nothing).** Given an opportunity, translation or brief:
- Confirm the Strategic pass on DB5 is set and that the Editorial pass on DB6 was recorded **after** it (R08).
- Check the piece against the core narrative, the enemy (fragmentation), the misconception it challenges, and Story Architecture (Problem → Insight → Demonstration → Framework → Proof → Action).
- Return `on_narrative` / `needs_adjustment` / `off_narrative` with the `position_id` it serves and drift flags. The verdict goes to C03 or C04. It is not stored on DB2.

**2. Registry writes (DB2).** Create a new position, or VERSION or SUPERSEDE an existing one.

## Permitted writes

DB2 fields whose writer is `C02`. `Status = Active` and `Authority Level = Agency doctrine` only with a recorded owner decision (R19), because Active means agents may assert it.

## Refusals

R10 a reused `Position ID` (a new version gets a new ID, e.g. `-v2`) · R19 Active or Agency doctrine without an owner quote · R04 a belief presented as fact with no evidence · editing `Conflict — unresolved` or other historical `DRAGON Reading` values on an existing row (supersede instead).

## Procedure (registry write)

1. Query DB2 for the `Position ID`. Query failed → stop, incomplete.
2. **SUPERSEDE**: create the successor (new ID, `Version` +1, Status per owner decision), then set the predecessor's `Status = Superseded` and append a change line to **both** pages naming the other. Do not change the predecessor's content fields.
3. **CREATE**: Status starts `Draft` or `Validating`. New terminology rows use `DRAGON Reading = Two-pass — Strategic then Editorial`; other rows use `Not applicable`, never blank.

## Verification

Fetch both pages after a supersession. Confirm successor Active (if decided), predecessor Superseded, both change lines present, and the predecessor's original fields unchanged.

## Handoff

Verdict → C03 (translation) or C04 (brief). New Position IDs become Translation Family IDs downstream (C03).

## Execution record

`04_Content/_memory/skill_runs.jsonl`, `skill: content-narrative-review`.
