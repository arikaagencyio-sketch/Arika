---
name: content-approval-prep
description: Skill C06 of Content (04). Assembles the G2 packet for ONE exact brief revision — copy, claim-review verdict, both DRAGON passes, surface, sources and open risks — and may set G2 Decision to Not submitted or Submitted for review only. The human reviewer sets Approved, Rejected or Changes requested, the reviewer, the date and the approved revision. Use after content-claim-review passes and a human G1 is recorded for the current Version (both paths), and for design work only once the finished artifact exists (text-only: once the final copy exists). Never approves, publishes or schedules.
---

# C06 · Content Approval Prep

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) §7–§8 first.**

> **The one rule that defines this skill: you prepare the decision; you never make it.** An approval belongs to a named human, to one `Version`, and to the **exact finished artifact**.

**When you may submit (contract §8, corrected 2026-10-09, hardened the same day).**
- **Both paths: a human G1 is on record for this brief at its current Version.** It names the brief ID, the revision and the path.
- **Design work:** only after Design has delivered the finished artifact for the current Version. Each asset needs:
  - a valid asset ID (a registry token, never a URL);
  - a whole-number version;
  - provenance naming this brief and revision;
  - known rights.

  A storyboard is not a finished artifact.
- **Text-only work** (text-capable format; `Visual Direction` and `Canva Instructions` empty or `text-only`; no assets; G1 path `text_only`): as soon as the final copy exists.
- **The packet must belong to the page you write.** The write carries `target` (the brief page ID). The target is read back (`state.prior`, **including its page ID**) at the packet's Version. `target`, `state.prior.id` and the packet's brief ID must be three non-blank, unpadded page IDs that are **exactly equal**. Use the same form for all three: a dashed and an undashed ID of one page do not match (R24, tightened 2026-10-10).
- **How the gate checks it.** `validate_write` refuses `Submitted for review` without a `g2_submission` context. It runs `validate_g2_submission`, which refuses on R12, R20, R22, R24 and R25. Dry-run it with `python 04_Content/contracts/content_write_gate.py submission <snapshot>.json`.

## Step 0 · The write path

| | |
|---|---|
| DB7 *(write `G2 Decision` = Not submitted / Submitted for review only)* | `collection://761b3f94-bdbf-4b3d-8234-4cda579697ca` |

## The G2 packet (appended to the brief page body)

1. Brief ID, **Version**, surface (exact Notion name), platform, and whether the brief is design work or text-only. Quote the G1 line: brief, revision, path, reviewer, date.
2. The copy exactly as it will publish. For design work, also the **asset set**: asset ID, version, and provenance (`brief_id`, `brief_revision` = this Version). The publication record must reproduce this list, because no Notion property holds it yet.
3. C05's verdict and claim table.
4. Strategic and Editorial DRAGON statuses with notes.
5. `content-publishing-gate`'s advisory verdict (6 alignments, 8 filters, 3 never-publish rules).
6. Open risks: unassigned surface, missing Offer (no commercial claims), stale timing words, Legal Class C items.
7. The question for the reviewer: approve **this Version**, request changes, or reject.

## Permitted writes

`G2 Decision` → `Not submitted` or `Submitted for review`. Nothing else on DB7.

## Refusals

R01 any of `Approved`, `Rejected`, `Changes requested`; any write to `G2 Reviewer`, `G2 Decided At`, `G2 Approved Revision` · R18 `Packet State` · R22 submitting before C05 passed this Version, before the finished artifact (design) or the final copy (text-only), or with an artifact of unknown rights · R09 submitting while `Surface = Not yet assigned`, or with a surface outside the vocabulary · R12 submitting a revision other than the current `Version`, or an artifact made for an older one · R20 a missing or invalid revision · R22 no G1 for this Version (either path), or a G1 path the brief no longer matches · R24 a G1, claim review or asset provenance for another brief, or a packet for a page other than the write target · R25 an invalid asset ID or version, or an asset listed twice.

## After the human decides

Read back the four G2 fields. `Approved` with `G2 Approved Revision = Version` is the only state that admits publication (R11, R12). Any later copy change makes it stale; `Approval Integrity` turns red.

## Execution record

`04_Content/_memory/skill_runs.jsonl`, `skill: content-approval-prep`.
