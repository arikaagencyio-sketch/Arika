# Content unit — rollback proposal (prepared, not executed)

**Department:** Content (04) · **Prepared:** 2026-10-09 (correction unit) · **Status:** **PROPOSAL ONLY. No rollback has been executed.** Each option below needs its own explicit owner approval. A Notion rollback also needs a separate approval, because it writes to the live workspace.

## 1. What is committed, and where

| Change set | Commit | Files | Live effect |
|---|---|---|---|
| **Content unit** (2026-10-09) | `74feb86` (auto-sync, 15:46:32; on `origin/master`) | **25 files, all from this unit.** The commit holds no unrelated file: `git show --stat 74feb86`, checked in the correction unit | None. The routine reads neither these files nor V2. The runtime loads the six edited agents |
| **Correction unit** (2026-10-09) | Not committed by this session. If auto-sync publishes it, find the SHA with `git log --format=%H -1 -- 16_Automation/routines/creative-pipeline/disposition.py` (a file only this unit adds) | Edits to 19 of the 25 files above (`git status`, checked in the correction unit), plus 3 new: `disposition.py`, `test_disposition.py`, this file | None |
| *Correction unit, as published* | **`ce310c6`** (auto-sync, 2026-10-09 19:07:30; on `origin/master`). Exactly the 22 files above, no unrelated file (`git show --stat ce310c6`, checked in the hardening unit) | — | None |
| **Hardening unit** (2026-10-09) | Not committed by this session. If auto-sync publishes it, find the SHA with `git log --format=%H -1 -- 04_Content/APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md` (a file only this unit adds) | Edits to files from both earlier units, plus that one new file | None |
| *Hardening unit, as published* | **`9124997`** (auto-sync, 2026-10-09 19:39:26; on `origin/master`). Exactly its 17 files (`git show --stat 9124997`, checked 2026-10-10) | — | None |
| **Follow-up unit** (2026-10-10) | Not committed by this session. It adds no file, so find its auto-sync commit as the first commit after `9124997` that touches `04_Content/contracts/content_write_gate.py`, and check `git show --stat` | Edits only | None |
| **Notion, Content unit** (2026-10-09) | Not in git. Recorded in `CONTENT_OS.md` §8 and `CONTENT_INTELLIGENCE_SCHEMA.md` §10 | — | Additive properties and options on DB2, DB5, DB6 and DB7; row edits on DB2, DB5, DB6 and DB7 |
| **Notion, correction unit** | None. Only read-only schema fetches were made | — | — |
| *Follow-up unit, as published* | **`6731006`** (auto-sync, 2026-10-10 14:38:38; on `origin/master`). Exactly its 8 files (`git show --stat 6731006`, checked in the storage unit) | — | None |
| **Storage unit** (2026-10-10) | Not committed by this session. Find its auto-sync commit as the first commit after `6731006` that touches `04_Content/contracts/content-databases.json`, and check `git show --stat` | Edits only | Gate, tests, contract, skills and agents now require the six DB7 properties |
| **Notion, storage unit** (2026-10-10) | Not in git. Recorded in `CONTENT_INTELLIGENCE_SCHEMA.md` §10 (2026-10-10) and §6 below | — | DB7 +6 properties (49 → 55); Approval Integrity formula extended. No row written |

## 2. Dependency map (what breaks if you remove one layer and keep another)

```
contracts/content-databases.json ◄── content_write_gate.py ◄── test_content_write_gate.py
        ▲   ▲                             │ C2 checks every SKILL.md exists
        │   └── 16_Automation/.../disposition.py ◄── test_disposition.py (reads vocabularies, revision rule)
        │
   .claude/skills/content-* (7) ── reference the contract, the gate and each other
        ▲
   .claude/agents/content-* (6) ── point at vocabularies; loaded by arika-runtime (npm test, arika list)
        ▲
   CONTENT_WRITE_CONTRACT.md · CONTENT_SKILL_MATRIX.md · CONTENT_RECONCILIATION_LEDGER.md · _memory/README.md
        ▲
   CONTENT_OS.md §6/§8/§10/§15 · CONTENT_INTELLIGENCE_SCHEMA.md §10/§11  ← dated history: never reverted, only appended to
```

- **Removing skills while keeping the gate:** the gate fails check C2 (SKILL.md missing). Remove the skills and the gate together.
- **Removing the contract JSON while keeping the gate, tests or `disposition.py`:** all three fail to import or load. They go together.
- **Reverting the agents to their pre-unit text** (`74feb86^`): the runtime is unaffected. The pre-unit specs loaded and passed 80/80 before the unit. The skills and contract would then describe V2 fields the agents no longer emit, which is a documentation mismatch, not a failure.
- **Reverting the repository while keeping the Notion additions:** the DB5/DB6/DB7 fields lose their recorded owner. They are documented only in the history entries, which stay. Harmless to the routine: its six trigger-read properties were never changed.
- **Reverting Notion while keeping the repository:** the field contract would describe properties that no longer exist (counts 361 → fewer), and the routine proposal's readiness checks would read empty fields. **Edit the contract in the same change as any Notion rollback.**
- **Reverting `74feb86` before the correction unit:** this conflicts, because the correction unit edits 19 of the same files. **Order: correction unit first, then `74feb86`.**
- **Full order (updated 2026-10-10):** follow-up unit → `9124997` (hardening) → `ce310c6` → `74feb86`. *(As first written, 2026-10-09: hardening unit → `ce310c6` → `74feb86`.)* Each edits files the next one introduced. Reverting the hardening unit alone (R0 below) leaves `ce310c6` intact. That reinstates the evidence-binding and asset failures and text-only G2 without G1, all reproduced against `ce310c6` on 2026-10-09.

## 3. Options

**Option R0: undo the hardening unit only.** Not recommended, for the same reason as R1. Revert its auto-sync commit, or restore its paths from the parent commit and delete `APPROVAL_EVIDENCE_STORAGE_PROPOSAL.md`. Append the history entry; do not delete it.

**Option R1: undo the correction unit only.** *(After the hardening unit is committed, R0 must come first.)* This returns to `74feb86`. **Not recommended**: it reinstates the seven defects the owner's review found (each reproduced against `74feb86` on 2026-10-09).
`git revert <correction-sha>` if its auto-sync commit holds only this unit's files. Otherwise restore by path:
`git checkout <correction-sha>^ -- <the 19 modified paths>`, delete the three new files, then commit.

**Option R2: undo the agent edits only.** Use this if the V2-shaped agent outputs cause trouble.
`git checkout 74feb86^ -- .claude/agents/content-brief-builder.md .claude/agents/content-intelligence-hub.md .claude/agents/content-multiplication-engine.md .claude/agents/content-narrative-architect.md .claude/agents/content-opportunity-mapper.md .claude/agents/content-publishing-gate.md`
Verify with `npx tsc --noEmit -p .`, `npm test` and `npx arika list` (expect 115) in `arika-runtime/`. The contract, skills and gate stay; record the mismatch in `CONTENT_OS.md` §8.

**Option R3: undo the whole repository layer.** Keep the history entries and the Notion state.
1. R1, then `git revert 74feb86`, or the path-scoped equivalent.
2. **Restore the history**: re-apply the `CONTENT_OS.md` §8/§15 and `CONTENT_INTELLIGENCE_SCHEMA.md` §10/§11 entries the revert removed. Append a dated "rolled back on <date> by <who>, reason" entry. A revert must not erase the record of what was done.
3. Notion stays as it is, and the history entries describe it.
4. Verify: runtime as in R2; Sector tests 228/228 (unaffected); `git status`.

**Option R4: Notion rollback.** This needs a separate approval and a live session.
1. **Order: rows before properties**, so no value is orphaned mid-way.
2. Restore DB6 `Audience Role` on the two translations from `General Manager / Owner` to `CEO`. The prior value is in each page body.
3. Set DB2 `nar-terminology-dragon` back to `Active`, and archive `nar-terminology-dragon-v2` (to trash, never a permanent delete).
4. Clear DB5's OTA `Narrative Position` link.
5. Remove the properties added on 2026-10-09:
   - DB5 `Strategic DRAGON` and `Strategic DRAGON Notes`
   - DB6 `Editorial DRAGON`, `Editorial DRAGON Notes` and `Surface`
   - DB7 `G2 Decision`, `G2 Reviewer`, `G2 Decided At`, `G2 Approved Revision` and `Approval Integrity`
6. Remove the added options: DB6 `Audience Role` hospitality options (only once no row uses them) and DB2 `DRAGON Reading` two-pass.
7. **Never touch the six trigger-read DB7 properties** (R17).
8. Read every change back.
9. Update `content-databases.json` in the same change (see §2).

**Option R4b: storage-unit Notion rollback (2026-10-10).** This needs a separate approval and a live session. **Dependency: revert the storage unit's repository changes in the same change.** The gate, the contract (55 / 367 fields) and the C06 submission path require these properties; with them removed, every submission and publication check refuses.
1. Restore the formula first, so it never references a dropped property: `ALTER COLUMN "Approval Integrity" SET FORMULA('<prior expression, §6>') COMMENT '<prior description, §6>'`.
2. Only if no row uses them, drop `G1 Decision`, `G1 Reviewer`, `G1 Decided At`, `G1 Revision`, `G2 Packet Manifest` and `G2 Submitted Fingerprint`. Today no row does, because no backfill was made. Once any G1 or G2 evidence exists, dropping it destroys approval history: export it into the brief's page body first.
3. Read back: 49 properties, the trigger-read six unchanged.

**Option R5: the routine.** Nothing to roll back. v2 has never been applied. If it is applied later, its rollback is `CHANGE_PROPOSAL.md` §7 (restore `prompt-v1-original.md`).

## 4. Never

- No `git reset --hard`, no force push, no history rewrite. Both commits are on `origin/master`.
- No permanent deletion of any Notion page.
- No rollback that also reverts unrelated work. Auto-sync commits can bundle other sessions' files, so check `git show --stat <sha>` before any whole-commit revert.

## 5. Changelog

- **2026-10-10 (storage unit)** — Changes:
  - Recorded the follow-up unit's commit (`6731006`).
  - Added rows for the storage unit and its Notion changes.
  - Added option R4b.
  - Kept the exact formula expressions in §6.
  - Nothing executed. — Claude Code (Opus 5.5)
- **2026-10-10 (follow-up unit)** — Records the hardening unit's commit (`9124997`, 17 files, no unrelated work) and adds the follow-up unit and the full revert order. Nothing executed. — Claude Code (Opus 5.5)
- **2026-10-09 (hardening unit)** — Updates:
  - The correction unit's commit is recorded (`ce310c6`, 22 files, no unrelated work).
  - A row and option R0 are added for the hardening unit.
  - The full revert order is stated.
  - Nothing executed. — Claude Code (Opus 5.5)
- **2026-10-09** — Prepared under the owner's correction-unit brief ("prepare a current, dependency-aware rollback proposal for the committed changes; execute no rollback"). — Claude Code (Opus 5.5)

## 6. Approval Integrity: exact expressions (rollback source)

**Prior** (created 2026-10-09; in force until 2026-10-10), with description `GOV - red cell when the packet lifecycle is ahead of G2, or when the approval was given to a different revision than the current Version. Computed; never written.`:

```
ifs(and(or(format(prop("Packet State")) == "approved", format(prop("Packet State")) == "scheduled", format(prop("Packet State")) == "published", format(prop("Packet State")) == "measured"), format(prop("G2 Decision")) != "Approved"), "🔴 lifecycle ahead of G2 approval", and(format(prop("G2 Decision")) == "Approved", prop("G2 Approved Revision") != prop("Version")), "🔴 approval is for a different revision", format(prop("G2 Decision")) == "Approved", "✅ G2 approved - current revision", format(prop("G2 Decision")) == "", "- G2 not recorded", format(prop("G2 Decision")))
```

**Current** (applied 2026-10-10, storage unit), with description `GOV - red when the packet lifecycle is ahead of G2, an approval or G1 covers another revision, or Ready for Design lacks a design G1. Shows only: it prevents no edit and authenticates no reviewer.`:

```
ifs(and(or(format(prop("Packet State")) == "approved", format(prop("Packet State")) == "scheduled", format(prop("Packet State")) == "published", format(prop("Packet State")) == "measured"), format(prop("G2 Decision")) != "Approved"), "🔴 lifecycle ahead of G2 approval", and(format(prop("G2 Decision")) == "Approved", prop("G2 Approved Revision") != prop("Version")), "🔴 approval is for a different revision", and(format(prop("Publishing Status")) == "Ready for Design", format(prop("G1 Decision")) != "Passed (design)"), "🔴 Ready for Design without a design G1", and(or(format(prop("Publishing Status")) == "Ready for Design", format(prop("Publishing Status")) == "Done"), prop("G1 Revision") != prop("Version")), "🔴 G1 is for a different revision", and(format(prop("G2 Decision")) == "Approved", prop("G2 Approved Revision") != prop("G1 Revision")), "RED - G2 and G1 cover different revisions", format(prop("G2 Decision")) == "Approved", "✅ G2 approved - current revision", format(prop("G2 Decision")) == "", "- G2 not recorded", format(prop("G2 Decision")))
```

The connector cannot read a formula's expression back. These are the strings that were sent and accepted. A UI edit made after them would not show here.
