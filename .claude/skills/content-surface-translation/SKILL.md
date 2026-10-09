---
name: content-surface-translation
description: Skill C03 of Content (04). Translates one narrative family onto one platform and one publishing identity — writes the Sector x Platform overlay (DB3), the Content Translation (DB6) with its Surface (founder profile, Company Page, or single-identity channel) and the Editorial DRAGON pass, and maintains platform behaviour in the Platform Registry (DB1). Use after C01 has recorded the Strategic pass and C02 has confirmed the narrative. Blocks duplicate-disguised-as-repurposing.
---

# C03 · Content Surface Translation

You are performing the **apply** step of Content's write layer.

**Read [`04_Content/CONTENT_WRITE_CONTRACT.md`](../../../04_Content/CONTENT_WRITE_CONTRACT.md) first** (§4 DRAGON order, §7 surfaces). Field truth: DB1, DB3, DB6 in [`content-databases.json`](../../../04_Content/contracts/content-databases.json).

> **The one rule that defines this skill: one family, many native expressions, never one expression copied across surfaces.** `Translation Family ID` equals the source narrative's `Position ID` verbatim, and each surface gets its own row.

## Step 0 · The write path

| | Data source |
|---|---|
| DB6 Content Translation *(write)* | `collection://9abf586d-d3bd-4401-b416-d5e0af1f3162` |
| DB3 Sector x Platform *(write)* | `collection://bb21b3fc-b14f-4237-b5cd-9affd08b98fc` |
| DB1 Platform Registry *(write: behaviour fields only)* | `collection://3fe9685e-6cb0-4a62-9a12-a3db999dc88e` |
| DB5 / DB2 *(read)* · Sector DB9/DB10/Linguistics *(read)* | contract §3 |

## Surfaces

| Surface | Voice | Publishing |
|---|---|---|
| `LinkedIn - Founder profile` | First person, opinion, building in the open. Never a fabricated history | Manual, by the founder, always |
| `LinkedIn - Company Page` | Institutional. **No first person singular** (R15) | Manual during warm-up; engine later, gated (R13) |
| `Single-identity channel` | Newsletter, website: one sending identity | Per channel |
| `Not yet assigned` | Declared state | Blocks a LinkedIn Ready-for-Design recommendation (R09) |

Choosing the surface for a new piece is an owner editorial call. Record it, don't infer it.

## Permitted writes

DB6 and DB3 fields whose writer is `C03`, including `Surface`, `Editorial DRAGON` and its notes, and `Audience Role` (hospitality options came from Sector DB9 on 2026-10-09; never rename an option). DB1 behaviour fields only. **Never** DB1 `Account Status` (Presence 21), `Launch Priority` (owner), or DB6 `Approved By` (human).

## Refusals

R03 no Opportunity, Platform, or source · R06 family ≠ Source Truth Position ID · R07 blank Editorial status on CREATE · **R08 Editorial pass recorded while the Opportunity's Strategic pass is `Not yet run`** · R09 a non-LinkedIn surface on a LinkedIn row · R10 an existing family + platform + surface + format · R05 T4-only buyer-behaviour claims (`Presence Reality` stays `Unverified` without a cited source).

## Procedure

1. Read the Opportunity's `Strategic DRAGON`. Not set → stop and hand back to C01.
2. Run the **Editorial pass**: D (the question that invites a real answer), R (the pain felt this week), A (only substantiated, first-hand claims), G (what the reader can use today), O (the defensible argument), N (the one reader it is written for). Record the status and per-letter notes.
3. Match the natural key on DB6. Query failed → stop, incomplete.
4. Apply; append the change line. On an UPDATE that replaces a value, preserve the prior value in the line.

## Verification

Query or fetch the row. Confirm `Translation Family ID`, `Surface`, `Editorial DRAGON` and `Audience Role` read back. `Family Integrity` and `Publishable Here` are formulas the API returns as opaque references: check them in the Notion UI, and say so in the record.

## Handoff

To C04 (brief). Multiplication across further surfaces repeats this skill per surface; see contract §10.1 for the event-ordering mismatch.

## Execution record

`04_Content/_memory/skill_runs.jsonl`, `skill: content-surface-translation`.
