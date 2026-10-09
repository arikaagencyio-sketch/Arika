---
name: content-approval-prep
description: Skill C06 of Content (04). Assembles the G2 packet for ONE exact brief revision — copy, claim-review verdict, both DRAGON passes, surface, sources and open risks — and may set G2 Decision to Not submitted or Submitted for review only. The human reviewer sets Approved, Rejected or Changes requested, the reviewer, the date and the approved revision. Use after content-claim-review passes. Never approves, publishes or schedules.
---

# C06 · Content Approval Prep

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) §7–§8 first.**

> **The one rule that defines this skill: you prepare the decision; you never make it.** An approval belongs to a named human and to one `Version`.

## Step 0 · The write path

| | |
|---|---|
| DB7 *(write `G2 Decision` = Not submitted / Submitted for review only)* | `collection://761b3f94-bdbf-4b3d-8234-4cda579697ca` |

## The G2 packet (appended to the brief page body)

1. Brief ID, **Version**, surface, platform.
2. The copy exactly as it will publish.
3. C05's verdict and claim table.
4. Strategic and Editorial DRAGON statuses with notes.
5. `content-publishing-gate`'s advisory verdict (6 alignments, 8 filters, 3 never-publish rules).
6. Open risks: unassigned surface, missing Offer (no commercial claims), stale timing words, Legal Class C items.
7. The question for the reviewer: approve **this Version**, request changes, or reject.

## Permitted writes

`G2 Decision` → `Not submitted` or `Submitted for review`. Nothing else on DB7.

## Refusals

R01 any of `Approved`, `Rejected`, `Changes requested`; any write to `G2 Reviewer`, `G2 Decided At`, `G2 Approved Revision` · R18 `Packet State` · submitting a revision C05 marked `reject` · submitting while `Surface = Not yet assigned` on a LinkedIn brief.

## After the human decides

Read back the four G2 fields. `Approved` with `G2 Approved Revision = Version` is the only state that admits publication (R11, R12). Any later copy change makes it stale; `Approval Integrity` turns red.

## Execution record

`04_Content/_memory/skill_runs.jsonl`, `skill: content-approval-prep`.
