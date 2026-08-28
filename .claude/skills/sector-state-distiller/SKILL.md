---
name: sector-state-distiller
description: Skill S06 of Sector (01). Distils what is happening in a market now (DB 12 Sector State) and where it is heading (DB 13 Sector Forecast) from signals and findings that already exist. Purely derivative — it may not introduce a single new fact. Use after a research pass completes, on a quarterly cadence, or after a material signal change. Runs only after S01 and S04.
---

# S06 · Sector State Distiller

You are performing the **apply** step of Sector's write layer.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** Field truth: [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB12, DB13. Contract row: `SECTOR_SKILL_MATRIX.md` §2.

> **The one rule that defines this skill: it may not introduce a fact.**
>
> Every value you write must be **derivable from rows that already exist** in DB 3 and DB 7. If a claim is true but not yet in a finding or a signal, it does **not** go here — it goes to S01 as a finding, first. A state that quietly adds market truth is no longer a distillation; it is an unsourced claim wearing a summary's clothes.

DB 12 is the **first thing every downstream department reads** for a sector. That is exactly why it must contain nothing of its own.

---

## Step 0 · The write path

| | Data source |
|---|---|
| DB12 Sector State | `collection://4a9b8ca5-f042-4938-85af-e0706ee9e1ff` |
| DB13 Sector Forecast | `collection://920781ae-fabd-4c9f-8045-42b40abf3cda` |
| DB7 Signals *(read)* | `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` |
| DB3 Intelligence *(read)* | `collection://72f90a0f-e34e-4c54-9fcd-9af2e108527e` |
| DB1 Sectors Master | `collection://68a5d070-58de-4b4d-8293-0fab0849a4b9` |

## Step 1 · Refuse to run too early

**S06 runs after S01 and S04. Never before.** Distilling a state from an empty or thin signal set produces a confident summary of nothing, which is worse than no summary at all — downstream departments read DB 12 as settled.

Before writing, check what you are distilling *from*. If the underlying rows are too few or too weak to support a state, **say so and stop.** An absent state row is a legible signal; a speculative one is not.

## Step 2 · Every value traces to a row

Assemble the evidence set first — the DB 7 signals and DB 3 findings in scope for this sector and geography. Then derive.

**`Critical Signals` (DB 12) and `Key Drivers` (DB 13) are both REQUIRED relations.** They are not decoration; they are the audit trail that makes the row a distillation. **A state with no underlying signals is sourced only to itself** — the exact circularity this skill exists to prevent.

Inherit the *weakest* evidence, not the strongest. If the state rests on three signals and one is `T3` and unbacked, the state's `Confidence` cannot be `High`.

## Step 3 · `As-of Date` is required, and it is not decoration

**An undated state claim is not a state claim.** A market state is true *at a moment*; without the date, a reader cannot tell whether they are looking at intelligence or archaeology.

The same applies to DB 13's `As-of Date`, alongside `Horizon` (`30d` · `90d` · `12mo` · `3yr`) and a `Review Date`.

## Step 4 · The plugin supplies the meaning — and only for some fields

`Demand Direction` · `Price Pressure` · `Connectivity / Access` · `Competition` are **configurable rules** (`SECTOR_OS_ARCHITECTURE.md` §3, slot **P14**). They are core fields whose *meaning* is plugin-supplied.

**Without a plugin they are readable but semantically empty.** Say that; do not invent a house meaning. "Price Pressure = High" means nothing until the plugin says what price pressure *is* in this market.

> ⚠️ **Two DB 12 fields have no P14 mapping at all, even for Sector #001.** `Tech Disruption` and `Regulatory Risk` are not in the plugin's KPI-semantics table. They are therefore **unconfigured for every sector including the pilot** — leave them empty and record the gap, or escalate for a P14 extension. Filling them against an invented definition is the failure mode P14 exists to prevent.

## Step 5 · A forecast is probabilistic or it is wrong

**`Likely Trajectory` MUST be phrased as probability, never as fact.** Not *"ADR rises in Q4"* but *"ADR more likely than not to rise through Q4, driven by [signals]; the main way this is wrong is [driver]."*

Name what would falsify it. A forecast that cannot be wrong is not a forecast — it is a sentence.

`Key Driver Notes` carries the reasoning; `Key Drivers` carries the signal relations the reasoning rests on. Both, or neither.

## Step 6 · Fields

**DB 12 — all yours:** `State` · `Sector` · `Geography` · `As-of Date` · `Demand Direction` · `Price Pressure` · `Connectivity / Access` · `Competition` · `Tech Disruption` · `Regulatory Risk` · `Top Opportunities` · `Top Threats` · `Confidence` · `Critical Signals`.

**DB 13 — all yours:** `Forecast` · `Sector` · `Geography` · `Horizon` · `Likely Trajectory` · `Key Drivers` · `Key Driver Notes` · `Confidence` · `As-of Date` · `Review Date`.

Note both relate to **`Sector`** (DB 1), not Sub-Sector — state is read at the vertical level. Resolve it through the hub anyway; never by name.

## Step 7 · Verify, log, and the loop that cannot close

Read each write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S06"`, and record **which signals and findings the state was derived from** — the derivation is the point.

Loops: `refresh`, `signal_change`, `feedback`.

> **The feedback loop cannot close, and this skill must not imply it can.** There is no performance store anywhere in the agency (`SECTOR_OS_ARCHITECTURE.md` §1.3). A state can be refreshed from new signals; it **cannot** be corrected by outcome data, because no outcome data is collected. **Never infer performance from activity.** Until a human observes a real outcome and feeds it back through S01 as a cited finding, this loop runs one-way.

---

## Refuse

- **Introducing any fact not already in DB 3 or DB 7.** Route it to S01 instead.
- A DB 12 row with an empty `Critical Signals`, or a DB 13 row with empty `Key Drivers`.
- An undated state or forecast.
- A forecast phrased as fact.
- A confidence higher than the weakest evidence beneath it.
- Filling a P14-governed select for a sector with no plugin, or filling `Tech Disruption` / `Regulatory Risk` against an invented definition.
- Running before S01 and S04 have populated the underlying rows.

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-28.** DB 12 and DB 13 both held **0 rows**. The underlying evidence base was thin but no longer empty: DB 3 held 217 findings (6 for the one `Target` sub-sector) and DB 7 held 34 signals, of which **only 3 were backed by a registered source**.

That ratio is the thing to weigh before writing a first state row: a state distilled from 31 unbacked signals would inherit their weakness, and its `Confidence` would have to say so.
