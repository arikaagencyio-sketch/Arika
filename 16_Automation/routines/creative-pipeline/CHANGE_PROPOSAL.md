# Creative Pipeline routine — change proposal (v1 → v2)

**Status: PREPARED, NOT APPLIED.** Written 2026-10-09 under the owner's Content-unit brief ("Next unit — prepare, do not execute"). **Amended 2026-10-09** under the owner's Content correction unit (§8). Nothing on the live routine has changed.

**Awaiting:**
1. The owner's original trigger and production-route intent section.
2. Explicit approval of this proposal.
3. Separately, explicit approval of any V1 retirement.

| | |
|---|---|
| Routine | `trig_01WyyrXEkFZck1D49tm6BfKv` "Design Creative Pipeline Automation" |
| Current prompt | [`prompt-v1-original.md`](prompt-v1-original.md) (verbatim, the rollback source) |
| Proposed prompt | [`prompt-v2-proposed.md`](prompt-v2-proposed.md) (amended) |
| Decision table as code | [`disposition.py`](disposition.py) + [`test_disposition.py`](test_disposition.py): a **non-production model** for review and tests; nothing deploys or runs it |
| V1 data source | `collection://1f0ed36e-a548-4743-9947-f408f8811140` (0 rows, 2026-10-08) |
| V2 data source | `collection://761b3f94-bdbf-4b3d-8234-4cda579697ca` (2 rows, both In progress, 2026-10-09) |

## 1. Live facts this proposal rests on (read-only checks, 2026-10-09)

- Routine **enabled**, cron `7 * * * *`, `claude-sonnet-5`. Last run 2026-10-09T11:20:22Z **succeeded** ("no briefs ready"); next run 12:07Z. *Recorded by the first draft; not re-read by the correction unit.*
- **V2 trigger-read properties are byte-identical to V1's contract** (re-fetched in the correction unit):
  - `Title` (title).
  - `Script`, `Caption`, `Visual Direction`, `Canva Instructions` (text).
  - `Publishing Status` (select). Options in order, with their IDs:
    - `Not started` `e552621d…`
    - `In progress` `5d53abab…`
    - `Ready for Design` `2502a443…`
    - `Done` `e34ae6e7…`
- **The fields v2 checks were read in the correction unit** (read-only fetch):
  - DB7 `Version` is a number, returned as a float (`1.0`).
  - DB6 `Surface` options: `LinkedIn - Founder profile`, `LinkedIn - Company Page`, `Single-identity channel`, `Not yet assigned` (ASCII hyphens).
  - DB5 `Strategic DRAGON` and DB6 `Editorial DRAGON` both read `Complete`, `Partial`, `Not applicable`, `Not yet run`.
- **Duplicate protection is readable.** The routine's run log (session `cse_01NdEuXHZtyTfriVofjopxVQ`, 2026-10-08) lists `mcp__Notion__notion-get-comments` and `notion-create-comment` among its tools.
- **Rollups on V2 come back as opaque `rollupResult://` references**, even in rows mode. So v2 fetches the linked pages instead of reading rollups.

## 2. Which GitHub revision the routine reads

The routine's source is `https://github.com/arikaagencyio-sketch/Arika` with **no ref pinned**, so each run checks out the default branch (`master`) as it is at run time. The prompt reads two repository files: `.claude/agents/design-storyboard-generator.md` and `.claude/agents/design-production-engine-coordinator.md`. **Neither unit changed either file.**

⚠ **Auto-sync.** An auto-sync job commits and pushes the working tree under the owner's account. It published the first Content unit as `74feb86` (2026-10-09 15:46). Neither unit committed by hand. The routine reads none of these files. **Recommendation:** pin nothing. Record the `master` SHA at apply time and at each test run (§5).

## 3. Proposed approval-matrix amendment (text only, not applied)

This text is for the Creative Pipeline row of `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`. Another session edits that file, so the owner applies the amendment by hand when approving it.

> **Creative Pipeline Automation (Design 19), prompt v2 (2026-10-09 proposal, amended; applied <date>).**
> - **Trigger source:** Content Briefs **v2** (`collection://761b3f94-bdbf-4b3d-8234-4cda579697ca`), `Publishing Status = Ready for Design`. A human sets it, only after the Content readiness check (G1) passes for the brief's current Version.
> - **Context read:** the linked Opportunity, Translation and Narrative Position (required), and the Campaign (optional), by relation.
> - **Per-brief outcomes:** COMPLETED, SKIPPED-DUPLICATE, BLOCKED or FAILED.
>   - BLOCKED means one of: missing required context, an invalid revision, an unassigned or unknown surface, or an unrun DRAGON pass. It posts at most one notice per reason set and never writes the completed marker.
>   - FAILED means an unreadable page, unreadable comments, or an unverified post. It posts nothing and the next run retries.
> - **Duplicate protection:** one COMPLETED comment per brief per revision, keyed by `[creative-pipeline v2 | completed | brief=<id> | rev=<Version>]` and checked by reading the page's comments before posting. Unreadable comments mean no post.
> - **Errors are not empties:** a failed query ends the run with `RESULT: ERROR`.
> - **Side effects:** Notion comments only. No property writes, no generation, no commits.
> - **Risk class:** 2, with a human spend approval before any credit use (unchanged).
> - **Rollback:** restore `16_Automation/routines/creative-pipeline/prompt-v1-original.md` with `RemoteTrigger update`.
> - **Detection:** the run summary's `RESULT:` line. `automation-reliability-monitor` is not yet scheduled, so detection is manual (read `list_runs`).
> - **Test evidence:** §5 of `CHANGE_PROPOSAL.md`.

## 4. Concurrency and other limitations (disclosed, not solved)

1. **Overlapping runs can race.** Two overlapping runs could both read "no marker" before either posts, for a COMPLETED comment or a BLOCKED notice. Scheduled runs are an hour apart and take under a minute. **A forced run within about 2 minutes of :07 can race the scheduled one.** Mitigation: never force a run between :05 and :10.
2. **Copy edited without a Version bump is not re-processed.** The marker still matches. Content's gate now refuses such an edit when it goes through a skill (R21). **A person editing the brief directly in Notion bypasses the gate**, and the routine cannot see it. Nothing here claims complete protection (`04_Content/CONTENT_WRITE_CONTRACT.md` §0.2).
3. **Comment readability depends on the connector.** If comments can't be read, the brief is FAILED and nothing is posted; the next run retries. A brief that keeps failing appears in every run's `failed` count.
4. **The marker is a convention, not a lock.** A human pasting the COMPLETED marker into a comment would suppress processing for that revision.
5. **Workspace query quota.** The routine's query shares the workspace's Query Data Source allowance. Hourly polling uses about 24 queries a day. When the allowance is exhausted, v2 reports `RESULT: ERROR`, not "none ready".
6. **BLOCKED notices are a design choice.** They make a stuck brief visible on its own page. If the owner prefers silence, delete the "post ONE comment" sentence in step f; the summary still reports `blocked`.
7. **The readiness check (G1) is a human checkpoint, not a routine check.** v2 checks what it can read: revision, required context, surface and both DRAGON passes. No Notion property records G1 yet (contract §8). So the human step T2a below is what prevents a brief reaching Design without G1. The minimal G1 and approved-asset storage that would let a later version read G1 is proposed, not built, in `04_Content/APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md`. The COMPLETED marker already names `brief=<id>` and `rev=<N>`. Content's gate uses it as the storyboard evidence for that exact brief and Version before any spend approval.

## 5. Test protocol (later, after approval; nothing here has been run)

| # | Step | Pass condition | Evidence to record |
|---|---|---|---|
| T0 | Re-verify the V2 schema by fetch: trigger properties, `Version`, DB6 `Surface`, both DRAGON fields | Names, types, option order and option IDs equal §1 and `content-databases.json` | Fetch time; option IDs |
| T1 | Apply v2 with `RemoteTrigger update`; `get` it back | Prompt text equals the block in `prompt-v2-proposed.md`; routine still enabled | `updated_at`; diff; `master` SHA |
| **T2a** | **Readiness checkpoint (G1), before any status change.** Fetch the chosen brief and its linked Opportunity and Translation. Write a snapshot JSON of the live values: the brief's page ID, Version, relations, both DRAGON passes, Surface, Format, Visual Direction, Canva Instructions, and the G1 record for **this brief ID and this Version** (`brief_id`, `revision`, `path: design`, reviewer, date). Run `python 04_Content/contracts/content_write_gate.py readiness <snapshot>.json` | Exit 0 (`READINESS … PASS`). Capture **REV = the brief's live Version**; never assume it | Snapshot file; gate output; **REV** |
| T2b | **Human** sets that brief to `Ready for Design`, only after T2a passed for REV | Set by a person in the Notion UI; Version still equals REV | Who, when, Version read back |
| T3 | Wait for the **scheduled** run at :07 | Exactly one comment beginning `[creative-pipeline v2 \| completed \| brief=<id> \| rev=<REV>]`; summary `completed 1`. If Version changed between T2a and T3, the test is void: return to T2a | Session ID, `fired_at`, comment ID, `master` SHA |
| T4 | Wait for the **next scheduled** run | No second completed comment; summary `skipped-duplicate 1` | Session ID, comment count unchanged |
| T5 | Human returns the brief to `In progress` (or leaves it, by the owner's choice) | No further comments | — |
| TB *(optional, owner's choice)* | Blocked-path proof on a brief that **fails** T2a, flipped by a human for the test | One BLOCKED notice with the expected reason codes; **no completed marker**; on the next run, no second notice | Session IDs, comment IDs |

**Today, both V2 briefs would fail T2a.** Both DRAGON passes read `Not yet run`, and no G1 is recorded. The OTA LinkedIn brief's surface is also `Not yet assigned`. So T2b cannot start until the owner chooses the surface, the two passes run (C01, C03), and G1 is recorded for the brief's then-current Version.

**Forced-run proof is not scheduled-run proof.** A `RemoteTrigger run` proves the prompt works when invoked. Only T3 and T4 on the cron prove the schedule. Record which kind each piece of evidence is.

**Clean-up.** The storyboard comment is a real artifact on a real brief and is kept. No disposable test data is created.

## 6. V1 retirement (separate approval, destructive)

Only after T0–T4 pass, and only with **separate** owner approval of the destructive step:

1. A fresh `SELECT COUNT(*)` on V1 returns 0. A failed count blocks retirement; it is not zero.
2. Reference check: `grep -r 1f0ed36e-a548-4743-9947-f408f8811140` returns only history and decision-log lines, plus `prompt-v1-original.md` (kept as the rollback source).
3. **Archive (move to Notion trash), not permanent deletion.** Trash is restorable from the Notion UI for a limited period. Permanent deletion (emptying trash) is irreversible and is a human action, never an agent's.
4. Record the archive date and who did it in `16_Automation/AUTOMATION_OS.md` and `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` §10.

## 7. Rollback

Run `RemoteTrigger update` with the prompt in `prompt-v1-original.md`. The routine then reads V1 again, which is empty, so it returns to "no briefs ready" with no side effects. Neither v1 nor v2 changes any Notion data except comments, which remain as history.

## 8. Changelog

- **2026-10-09 (hardening unit)** — Changes:
  - The T2a snapshot now includes the brief page ID, and the G1 record must name that brief, the Version and `path: design`. Content's gate binds all stage evidence to brief ID + Version.
  - Limitation 7 points to the storage proposal.
  - `disposition.py` is labelled a non-production model.
  - The prompt and its decision table are unchanged.
  - Still not applied. — Claude Code (Opus 5.5)
- **2026-10-09 (correction unit)** — Amended. Changes:
  - Blocked, failed and completed outcomes are now distinct, with separate markers.
  - Invalid revision, missing or unreadable required context, unassigned or unknown surface, and unrun DRAGON passes stop the brief without a completed marker.
  - Campaign kept optional. Read-after-write added on the posted comment.
  - T2a readiness checkpoint added before the human flip.
  - REV is captured from the live Version, not hard-coded (the draft's T3 named `rev=1`).
  - Optional blocked-path test TB added.
  - Limitation 2 restated: direct Notion edits bypass the gate. Limitations 6 and 7 added.
  - The first draft is in commit `74feb86`.
- **2026-10-09** — Prepared under the Content-unit brief. — Claude Code (Opus 5.5)
