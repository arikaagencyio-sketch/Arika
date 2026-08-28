---
name: sector-calendar-resolver
description: Skill S09 of Sector (01). Runs the eight-step Resolution Engine to produce a calendar for a sector × geography × property archetype × client. Writes nothing — the resolution is computed on demand, never stored. Use for a client engagement, a planning window, after any material signal change, or to run the Gate F falsification test. Runs after S04, S05 and S06.
---

# S09 · Sector Calendar Resolver

You are performing the **apply** step of Sector's write layer — except this skill has no write.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** The algorithm: [`01_Sector/SECTOR_OS_ARCHITECTURE.md`](../../../01_Sector/SECTOR_OS_ARCHITECTURE.md) §4.1. Field truth: [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json). Contract row: `SECTOR_SKILL_MATRIX.md` §2.

> **This skill writes nothing, and that is a design decision, not a limitation.**
>
> A 365-day calendar is `resolve(sector, geography, property_type, null, 365d)` — **an output**, recomputed on change. Authoring it as 365 rows is the exact failure the architecture exists to prevent: a beautiful hospitality database that cannot generalise. The standing law (`SECTOR_ACTIVATION_CONTRACT.md` §15): *never build a calendar per layer, per view, per sector, or per direction.*
>
> If a resolution should become durable, it leaves through **S10**, as Content Opportunities in Content (04)'s store. It never becomes rows here.

---

## Step 0 · The read path — all reads, no writes

| | Data source |
|---|---|
| DB7 Signals | `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` |
| DB11 Geography | `collection://e095c661-86cd-4f45-9149-eca1c7195e71` |
| DB15 Market Routes | `collection://c8585c52-6b77-4dab-8ba1-dc228e1c5424` |
| DB16 Destination Profile | `collection://ed957373-e916-4a01-9f44-354d5e037a6a` |
| DB12 Sector State | `collection://4a9b8ca5-f042-4938-85af-e0706ee9e1ff` |
| DB1 Sectors Master | `collection://68a5d070-58de-4b4d-8293-0fab0849a4b9` |
| Plugin P2 / P7 | [`sector_plugins/hospitality/plugin.config.json`](../../../01_Sector/sector_plugins/hospitality/plugin.config.json) — per sector |

**If the sector has no `plugin.config.json`, steps 4 and 6 cannot run.** Say so and produce the unfiltered, undated resolution, labelled as such. Do not substitute another sector's plugin. A hospitality offset applied to a SaaS signal is a fabricated date.

## Step 1 · SELECT — and the scope is the ancestor chain, not just the subtree

```
SELECT signals FROM DB7
 WHERE sub_sector ∈ sector
   AND geography ∈ (ancestor chain of the place  ∪  subtree below it)
   AND (signal_date ∨ any activation_date) ∈ window
   AND source_tier ≠ T4
   AND refresh_status ∉ {Needs verification, Superseded/Delayed}
```

> ⚠️ **The scope clause is `ancestors ∪ subtree`, and this correction matters more than it looks.** A place at `Destination` level is a **leaf** — it has no subtree. Resolving `Maasai Mara` against descendants alone returns **zero signals**, because every Kenyan signal is tagged to *Kenya*, one level up. A Kenyan public holiday obviously reaches a Kenyan lodge; the model has to say so. **Signals are inherited downward.** A `Global` seasonality row reaches every place; a `Kenya` holiday reaches Nairobi, Mombasa, Diani and Maasai Mara; a `Nairobi` trade expo reaches Nairobi and nothing else — *a sibling is not an ancestor.*

**The T4/stale gate is the point of the SELECT, not a detail.** `Needs verification` and `Superseded/Delayed` rows are excluded **by status, before any scoring**. An unverified signal must not reach a client-facing calendar, and this is where that rule is enforced.

**A signal with no `Geography` is unreachable.** It cannot be placed, so it falls out of every place-scoped resolution — silently, and regardless of its tier. Report those rows by name; do not let a `T1 · Confirmed` signal disappear because nobody tagged it.

## Step 2 · SCOPE by Signal Role × Market Route direction

Destination-side signals **compress inventory at the place**. Origin-side signals **release demand from the client's source markets**.

The mapping from origin market to destination lives in **DB 15**. **With DB 15 empty, step 2 degrades to its domestic case** — origin-side signals can only be read against the place's own country. Say that in the output rather than presenting a domestic resolution as a full one.

## Step 3 · ENRICH from DB 16 Destination Profile

Demand themes · primary/secondary audiences · travel motivations · content angles · visual language · booking triggers.

**With DB 16 empty, step 3 is a no-op** and the resolution loses the layer that most distinguishes one destination from another. Record it as a no-op. A resolution that skipped three of its eight steps is not the same artifact as one that ran them.

## Step 4 · FILTER by the plugin's property-type rule (P2)

*"Does this signal move THIS archetype's demand?"*

Three outcomes, and the third is the one that gets mishandled:

| P2 says | Treat as |
|---|---|
| in `moves_demand` | passes the filter |
| in `does_not_move` | filtered out |
| **in neither list** | **UNRULED — unknown, not false** |

**An unruled signal is not a rejected signal.** Carry it through, marked, and count the unruled rate. If an archetype rules on none of the signal types actually present, step 4 did nothing for that archetype — which is a finding about the plugin, not about the market.

## Step 5 · FILTER by client context

Inventory · positioning · blackout dates · owned offers · capacity.

**No client calendar exists until a real client does** (`SECTOR_OS_ARCHITECTURE.md` §4.2). With no client, this step is correctly skipped and the output is the **default** resolution. Structure may be empty; it may not be guessed.

## Step 6 · DERIVE activation dates from the plugin timing table (P7)

Six derived dates per signal: Strategic Planning · Marketing Activation · Sales Activation · Offer Activation · Revenue Watch · Action Deadline.

> **LABEL EVERY DERIVED DATE AS A PLANNING OFFSET, NEVER AN EXTERNAL FACT** (`SECTOR_ACTIVATION_CONTRACT.md` §12). *"Marketing activation: 2026-07-08"* is a number this system computed. It is not something a publisher announced, and a reader who confuses the two will cite it as evidence.

**A `null` offset is unavailable, not zero, and never a neighbour's.** Where P7 marks a signal type `unauthored`, report the offsets as unavailable and name the signal type. Where a single offset is genuinely absent in the source (P7's `Travel-Trade · revenue_watch`), report it absent. **Substituting a plausible number here is the highest-value fabrication in the department**, because a derived date looks exactly like a researched one.

## Step 7 · SCORE, then the three gates

**Order matters.** Content DB 5's five additive dimensions run **unchanged** — S09 does not re-score and does not touch `content-opportunity-mapper`'s published `output_schema`. Then three pass/fail gates:

| Gate | Asks |
|---|---|
| **Timeliness** | Is today inside the activation window — i.e. before the Action Deadline? |
| **Destination Fit** | **Does a DB 16 Destination Profile resolve?** |
| **Client Fit** | Does the property-type rule match? |

> **The gates are conditions of applicability, not magnitudes of value.** *A piece is not slightly out of season.* They sit **upstream** of Content's score and are deliberately not added to its five dimensions (owner decision 2026-08-20, `CONTENT_INTELLIGENCE_SCHEMA.md`). **Running them as score dimensions is a refusal.**

> **`Destination Fit` was ruled by the owner on 2026-08-28 (item 31h): it asks whether a DB 16 **Destination Profile** resolves** — *not* merely whether the signal's `Geography` relation resolves. The rejected reading passes for essentially every geography-tagged signal, and **a gate that never fails is not a gate**. Under the ruling, a place with **no** Destination Profile blocks its opportunities until one is written. **That is the gate working**: it reports where the model is thin rather than waving it through. As of 2026-08-28 that means Nairobi, Diani and Maasai Mara pass and **Mombasa does not**.

**A failed Timeliness gate is a live finding, not a filter.** A signal whose Action Deadline has already passed means the window was missed — surface it by name.

## Step 8 · EMIT

Content Opportunities → Content Briefs, **through S10**. S09 produces the packet; it does not route it and it does not write it.

## The falsification run (Gate F)

`SECTOR_ACTIVATION_PROTOCOL.md` §3: **the outputs must be structurally different per validation place. If identical, the model is wrong — stop.**

Resolve for **each** validation place, then compare on **structure, not volume**: which signals survived step 1, which the archetype rule moved, which offset clock governs. *Two places returning five signals each is not sameness if the five differ.*

Report **which steps actually did work**. A pass produced by 4 of 8 steps is a real pass and a weak one — say both. Gate F is the gate that can falsify the architecture, so an overstated pass here is worse than a fail.

## Verify, log

Nothing is written, so verification is that the inputs were live. Record the row counts you read and the date. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S09"`, `decision: "NO_OP"`, and an empty `writes` array — **a resolution is an execution with no mutation, and it still gets a record.**

Loop: `calendar_recomputation`.

---

## Refuse

- **Writing any row.** A resolution is an output. If it must persist, it leaves through S10.
- Treating a derived activation date as an external fact.
- Substituting an offset for an `unauthored` P7 row, or borrowing a neighbouring signal type's.
- Running the three gates as score dimensions instead of pass/fail conditions.
- Passing `Destination Fit` on a signal whose geography merely resolves. **The ruling is that a Destination Profile must resolve** (31h).
- Re-scoring Content DB 5's five dimensions.
- Including a `Needs verification` or `Superseded/Delayed` signal in a client-facing calendar.
- Reporting a resolution as complete when DB 15 or DB 16 is empty — say which steps were no-ops.
- Reading one sector's plugin for another sector's resolution.

## Appendix · A dated snapshot — re-measure it, do not trust it

**Re-measured 2026-08-28, end of day.** DB 7 held 34 signals, 11 of them hospitality; **8 survived the status/tier gate**. DB 11 held **13** places. **DB 15 held 5 routes and DB 16 held 3 profiles**, so **steps 2 and 3 both run** and Gate F reached **6 of the 8 steps** — up from 4 on the first run.

Only **step 5** (needs a real client) and **step 8** (hands to S10) are unexercised, and neither is a gap.

**What to weigh before quoting a resolution:** DB 16 holds three profiles and DB 15 five routes. The engine now produces structurally different calendars *for the three places that have them* — and `Destination Fit` (31h) correctly **blocks** any place that does not, which today means Mombasa.
