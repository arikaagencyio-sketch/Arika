---
name: sector-place-profiler
description: Skill S05 of Sector (01). Writes the place layer — the DB 11 geography tree at the correct level, DB 15 directed origin-to-destination routes, and DB 16 destination profiles. Use when plugin slot P4/P5 is authored, at activation Gate E, or to correct a mis-levelled geography row. Holds an open architectural question: DB 15 and DB 16 may not be universal.
---

# S05 · Sector Place Profiler

You are performing the **apply** step of Sector's write layer.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** Field truth: [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB11, DB15, DB16. Contract row: `SECTOR_SKILL_MATRIX.md` §2.

---

## ⚠️ Read this before writing anything to DB 15 or DB 16

**Whether Market Routes and Destination Profile are genuinely universal is an open architectural question, and it is not yours to close.**

Both are `[CANDIDATE]` in `AEIT_06` and neither is canonised. `SECTOR_ACTIVATION_PROTOCOL.md` §4 rates plugin slot **P5 confidence LOW**, in its own words: *"Is a destination profile universal at all? For B2B SaaS, geography may carry no demand-theme meaning."* They may belong to a **travel-shaped family of sectors** rather than the Universal Core.

**Gate I must rule** — it is owner item **31b** and it has not run.

| | |
|---|---|
| **DB 11 Geography** | Universal. Every sector has places. **Write freely.** |
| **DB 15 / DB 16** | Contested. For a **travel-shaped** sector, write. For a **non-travel** sector, **record what you could not fill rather than forcing values in** — an empty DB 16 for a SaaS sub-sector is evidence for Gate I, not a gap to close. |

Forcing a destination profile onto a sector where geography carries no demand meaning would manufacture exactly the false universality Gate I exists to detect.

---

## Step 0 · The write path

| | Data source |
|---|---|
| DB11 Geography | `collection://e095c661-86cd-4f45-9149-eca1c7195e71` |
| DB15 Market Routes | `collection://c8585c52-6b77-4dab-8ba1-dc228e1c5424` |
| DB16 Destination Profile | `collection://ed957373-e916-4a01-9f44-354d5e037a6a` |

## Step 1 · The geography tree — level is load-bearing, not cosmetic

`Level`: **Global · Region · Country · City · Destination · Property**. `Parent` is self-referential and forms the subtree spine.

> **Why a wrong level is a silent corruption.** Resolution Engine step 1 filters by geography **subtree**. A row at the wrong level returns a **wrong signal set with no error** — the resolution looks like it worked. This is the failure mode that makes `Level` the highest-consequence select in the department.

**`Destination` is not a smaller `City`.** A city is an administrative place; a destination is a place people travel *to* for a reason. A reserve, a beach strip or a resort area is a `Destination` even when it has no municipal status — and it is where demand-theme meaning attaches.

**The `Property` level is plugin-supplied (P14), not universal.** Without a plugin it is readable but semantically empty. Say so rather than inventing a house meaning.

**Before writing a level, check the subtree it implies.** Re-levelling a row silently changes which signals resolve under it — name that in the run record.

## Step 2 · Routes — directed, with their own clock

A route is **origin → destination**, and the direction matters: `Germany → Kenya` is not `Kenya → Germany`. The origin side carries its own calendar — German school holidays are staggered by *Land*, and that staggering is itself the demand signal.

Route facts must be **web-cited**. In particular:

- **Never estimate a booking lead time to make a row look complete.** A lead time you did not source is the single most damaging invention here, because every activation date downstream is computed from it.
- A derived campaign window is a **planning offset**, never an external fact. Label it.

## Step 3 · Destination profiles — the commercial read of a place

`Destination Profile` requires a `Geography` relation. **A profile with no place is not a profile.**

Demand themes come from plugin **P5**. Where P5 is unauthored, the profile records which themes it could not source — it does not borrow a neighbouring destination's.

**Never write a destination's demand or booking numbers.** Those are ⚫ never-fill: they come from a connected external system, and no such system is connected. A plausible occupancy figure is a constitutional breach, not a helpful placeholder.

## Step 4 · Fields — yours and not yours

**DB 11 — yours:** `Name` · `Level` · `ISO / Code` · `Parent` · `Notes` · `Destination Profile` · `Routes (as Origin)` · `Routes (as Destination)`.
**Not yours:** `Signal Sources` (S03).

**DB 15 and DB 16 — yours**, except `Related Entities (CRM)` (🔴 scraping-gated, S12).

## Step 5 · Verify, log, hand off

Read each write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S05"`. On any re-levelling, `writes[].invalidates` must name **what now resolves differently**.

Hands off: content angles → Content (04) · visual language → Design (19) · preferred channels → Marketing (03) — all **through S10**, never directly.

Loops: `activation`, `refresh`.

---

## Refuse

- An estimated booking lead time, written to make a row look complete.
- A destination's demand or occupancy numbers.
- A derived campaign window presented as an external fact.
- A `Destination Profile` with no `Geography` relation.
- Populating DB 15 or DB 16 for a non-travel sector **to avoid an empty table**. Empty is the finding.
- Any field whose `writer_skill` is not S05.

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-28.** DB 11 held 11 rows — `Global > Africa > Kenya > {Nairobi, Mombasa, Diani, Maasai Mara}`, plus Germany and the UK as origin markets. **Two rows were mis-levelled `City` (F3)**: a reserve and a beach strip, both of which are `Destination` by the definition above, and the `Destination` level was added at Gate 2 for exactly them.

DB 15 and DB 16 both held **0 rows**, with their universality still unruled by Gate I.
