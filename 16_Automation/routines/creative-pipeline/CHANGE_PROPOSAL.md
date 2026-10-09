# Creative Pipeline routine — change proposal (v1 → v2)

**Status: PREPARED, NOT APPLIED.** Written 2026-10-09 under the owner's Content-unit brief ("Next unit — prepare, do not execute"). Nothing on the live routine has changed. **Awaiting:** (1) the owner's original trigger and production-route intent section; (2) explicit approval of this proposal; (3) separately, explicit approval of any V1 retirement.

| | |
|---|---|
| Routine | `trig_01WyyrXEkFZck1D49tm6BfKv` "Design Creative Pipeline Automation" |
| Current prompt | [`prompt-v1-original.md`](prompt-v1-original.md) (verbatim, the rollback source) |
| Proposed prompt | [`prompt-v2-proposed.md`](prompt-v2-proposed.md) |
| V1 data source | `collection://1f0ed36e-a548-4743-9947-f408f8811140` (0 rows, 2026-10-08) |
| V2 data source | `collection://761b3f94-bdbf-4b3d-8234-4cda579697ca` (2 rows, both In progress, 2026-10-09) |

## 1. Live facts this proposal rests on (read-only checks, 2026-10-09)

- Routine **enabled**, cron `7 * * * *`, `claude-sonnet-5`, last run 2026-10-09T11:20:22Z **succeeded** ("no briefs ready"), next run 12:07Z.
- V2 trigger-read properties are byte-identical to V1's contract: `Title` (title), `Script`, `Caption`, `Visual Direction`, `Canva Instructions` (text), `Publishing Status` (select: Not started, In progress, Ready for Design, Done, in that order; option IDs unchanged after the 2026-10-09 schema additions).
- **Duplicate protection is readable.** The routine's own run log (session `cse_01NdEuXHZtyTfriVofjopxVQ`, 2026-10-08) lists `mcp__Notion__notion-get-comments` and `notion-create-comment` among its tools. v2 reads comments before posting.
- Rollups on V2 return as opaque `rollupResult://` references even in rows mode (checked 2026-10-09). v2 therefore fetches the linked Opportunity, Translation, Narrative and Campaign pages.

## 2. Which GitHub revision the routine reads

The routine's source is `https://github.com/arikaagencyio-sketch/Arika` with **no ref pinned**, so each run checks out the default branch (`master`) as it is at run time. `origin/master` was `b8f2311` at the start of this unit. The prompt reads two repository files: `.claude/agents/design-storyboard-generator.md` and `.claude/agents/design-production-engine-coordinator.md`. **This unit changed neither.**

⚠ **Auto-sync.** This repository has an auto-sync job (`chore(auto-sync)` commits by the owner's account) that commits and pushes working-tree changes on its own schedule. This unit did not commit or push. The job may publish this unit's files to `master`; none of them is read by the routine. **Recommendation:** when v2 is applied, pin nothing, but record the `master` SHA at apply time and at each test run in the evidence table (§5).

## 3. Proposed approval-matrix amendment (text only, not applied)

To `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`, the Creative Pipeline row. Another session is editing this file, so the amendment is applied by hand when the owner approves.

> **Creative Pipeline Automation (Design 19), prompt v2 (2026-10-09 proposal; applied <date>).** Trigger source: Content Briefs **v2** (`collection://761b3f94-bdbf-4b3d-8234-4cda579697ca`), `Publishing Status = Ready for Design`, set by a human only. Reads linked Opportunity, Translation, Narrative and Campaign by relation. **Duplicate protection:** one comment per brief per revision, keyed by the marker `[creative-pipeline v2 | brief=<id> | rev=<Version>]`, checked by reading the page's comments before posting; unreadable comments mean no post. **Errors are not empties:** a failed query ends the run with `RESULT: ERROR`. Side effects: Notion comments only; no property writes, no generation, no commits. Risk class 2, with a human gate before credit spend (unchanged). **Rollback:** restore `16_Automation/routines/creative-pipeline/prompt-v1-original.md` with `RemoteTrigger update`. **Detection:** the run summary's `RESULT:` line; `automation-reliability-monitor` is not yet scheduled, so detection is manual (read `list_runs`). Test evidence: §5 of `CHANGE_PROPOSAL.md`.

## 4. Concurrency and other limitations (disclosed, not solved)

1. **Race between overlapping runs.** Two runs that overlap could both read "no marker" before either posts. Scheduled runs are an hour apart, and a run takes under a minute. A **forced run within ~2 minutes of :07 can race the scheduled one.** Mitigation: never force a run between :05 and :10.
2. **Copy edited without a Version bump** is not re-processed, because the marker matches. The Content contract requires C04 to bump `Version` on any copy change (R12 depends on it too).
3. **Comment readability depends on the connector.** If comments can't be read, v2 skips the brief, which is fail-closed, and says so in the summary. A brief can then sit unprocessed; the summary's `skipped-unverifiable` count is the signal.
4. **The marker is a convention, not a lock.** A human pasting the marker into a comment would suppress processing for that revision.
5. **Workspace query quota.** The routine's query shares the workspace's Query Data Source allowance. Hourly polling uses ~24 queries a day. On exhaustion, v2 reports `RESULT: ERROR` rather than "none ready".

## 5. Test protocol (later, after approval; nothing here has been run)

| # | Step | Pass condition | Evidence to record |
|---|---|---|---|
| T0 | Re-verify V2 trigger properties (fetch schema) | Names, types and option order unchanged | Fetch time; option IDs |
| T1 | Apply v2 with `RemoteTrigger update`; `get` it back | Prompt text equals `prompt-v2-proposed.md`; routine still enabled | `updated_at`; diff |
| T2 | **Human** sets the OTA Tax brief (`3c121e15eb9381f48574dfe6e1f43828`) to `Ready for Design` | Set by a person in the Notion UI | Who, when |
| T3 | Wait for the **scheduled** run at :07 | Exactly one comment beginning with the v2 marker for `rev=1`; summary `posted 1` | Session ID, `fired_at`, comment ID, `master` SHA |
| T4 | Wait for the **next scheduled** run | No second comment; summary `skipped-duplicate 1` | Session ID, comment count unchanged |
| T5 | Human returns the brief to `In progress` (or leaves it, by the owner's choice) | No further comments | — |

**Forced-run proof is not scheduled-run proof.** A `RemoteTrigger run` proves the prompt works when invoked. Only T3 and T4 on the cron prove the schedule. Record which kind each piece of evidence is. **Clean-up:** the storyboard comment is a real artifact on a real brief and is kept. No disposable test data is created.

## 6. V1 retirement (separate approval, destructive)

Only after T0–T4 pass, and only with **separate** owner approval of the destructive step:

1. Fresh `SELECT COUNT(*)` on V1 returns 0. A failed count blocks retirement; it is not zero.
2. Reference check: `grep -r 1f0ed36e-a548-4743-9947-f408f8811140` returns only history and decision-log lines plus `prompt-v1-original.md` (kept as the rollback source).
3. **Archive (move to Notion trash), not permanent deletion.** Trash is restorable from the Notion UI for a limited period; permanent deletion (emptying trash) is irreversible and is a human action, never an agent's.
4. Record the archive date and who did it in `16_Automation/AUTOMATION_OS.md` and `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` §10.

## 7. Rollback

`RemoteTrigger update` with the prompt in `prompt-v1-original.md`. The routine then reads V1 again, which is empty, so it returns to "no briefs ready" with no side effects. No Notion data is changed by v1 or v2 except comments, which remain as history.
