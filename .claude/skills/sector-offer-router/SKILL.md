---
name: sector-offer-router
description: Skill S08 of Sector (01). Writes an industry's land-and-expand routing record in DB 8 Agency Opportunity Map against the twelve capability families, and records `GAP — needs OEOS` where no real offer exists rather than inventing one. Sector routes; Offer (02) owns the offers. Use when plugin slot P11 is authored, when an industry reaches Validated, or at activation Gate G. Runs after S01, S02 and S04.
---

# S08 · Sector Offer Router

You are performing the **apply** step of Sector's write layer.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) first.** Field truth: [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB8. Contract row: `SECTOR_SKILL_MATRIX.md` §2.

> **The one rule that defines this skill: Sector routes; Offer (02) owns the offers.**
>
> This database says *which capability family a sector's pain lands in* and *what the entry point is*. It does **not** create offers, price them, or name a service that is not in the Offer Engineering Registry. **An offer name absent from the registry is a refusal, not a draft** — the honest write is `GAP — needs OEOS`, which is a commission to another department, not a blank.

---

## Step 0 · The write path

| | Data source |
|---|---|
| DB8 Agency Opportunity Map | `collection://efd6319c-081e-4a6b-b930-a362ef2bc1b2` |
| DB3 Sector Intelligence *(read — the pain)* | `collection://72f90a0f-e34e-4c54-9fcd-9af2e108527e` |
| DB7 Signals *(read — the triggers)* | `collection://c14fedb3-6048-4bc5-8a40-6558cc985f57` |
| DB10 Decision-Maker Registry *(read — the who)* | `collection://5566c27c-d5db-4a22-9587-e57d0ce5fbbe` |
| DB6 Sector Linguistics *(read — the words)* | `collection://172efe6d-08b5-4c85-b24a-fa7065b3e721` |
| DB2 Sub-Sectors *(the scope axis)* | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |
| Offer Engineering Registry | `02_Offer/` — the authority for every offer name |

## Step 1 · The three empty relations are the job

DB 8 holds **87 rows with real routing text and three relations empty on every one of them**: `Pain Points` → DB 3, `Buying Triggers / Demand Signals` → DB 7, `Target Decision-Maker` → DB 10.

**That is the difference between a routing opinion and a routed record.** A row that says *"lead with an audit"* and cannot name the finding that proves the pain, the signal that makes it urgent, or the person who feels it, is an assertion. Closing these three is what makes the row defensible to Sales.

> **Do not close a relation by plausibility.** If DB 3 holds no finding for this sub-sector, the `Pain Points` relation stays empty and you say so. **An empty relation is a research task; a wrong one is a false citation** that Sales will quote in a call.

## Step 2 · Capability families are a routing vocabulary, not a service list

`Entry` · `Expansion` · `Transformation` each take from the twelve: `INT` · `STR` · `BR` · `MKT` · `CNT` · `SAL` · `ACQ` · `OPS` · `AUTO` · `AI-X` · `FIN` · `SCALE`.

These name **where the work sits**, not what is sold. The saleable thing is in `Ladder Offer Refs / OEOS Gap`, and it must resolve to the registry.

**The ladder is a sequence, not three independent picks.** `Expansion` must be reachable from `Entry` for the same client; `Transformation` from `Expansion`. A ladder whose rungs do not connect is three offers in a column.

## Step 3 · `GAP — needs OEOS` is a real value, and using it is correct

Where the routing is sound but no offer exists to serve it, write **`GAP — needs OEOS`** in `Ladder Offer Refs / OEOS Gap`. That is a commission to Offer (02), and it is more useful than a plausible service name — because a plausible name gets quoted.

**Never present a price as validated.** Pricing is Offer (02)'s, via the segmented ARR-band floor. If a number appears here at all it is labelled a hypothesis.

## Step 4 · Fields

**Yours:** `Opportunity` · `Sub-Sector` · `Primary Opportunity` · `Entry-Point Service` · `Entry Capability` · `Expansion Capability` · `Transformation Capability` · `Ladder Offer Refs / OEOS Gap` · `Offer Fit (Offer 02)` · `Outreach Angle` · `Retainer Upsell Path` · `Cross-sell / Scale Pathway` · `Scraping Fields` · `KPIs` · `Revenue Potential` · `Urgency` · `Confidence` · `Industry Type` · `Portfolio Mode` · `Priority Tier` · `Pain Points` · `Buying Triggers / Demand Signals` · `Target Decision-Maker` · `Destination Profiles` · `CRM Opportunities`.

> ⚠️ **`Scraping Fields` is a trap.** It names data a prospecting workflow would collect. **Listing a field here does not authorise collecting it.** Any actual scraping is a `scrape` under the standing constraint and goes to **Legal (10)** before anything runs. Describe; do not enable.

**`Outreach Angle` must use DB 6's words.** The linguistics layer exists so the department stops paraphrasing its market. If DB 6 has no role lens for this audience, say so rather than inventing phrasing.

## Step 5 · Confidence, and the tier it inherits

`Confidence` cannot exceed the weakest evidence beneath the row. A routing record whose `Buying Triggers` relation points at **unbacked or `Needs verification`** signals is `Low`, whatever the reasoning quality.

`Revenue Potential`, `Urgency` and `Priority Tier` are **judgements about Arika's opportunity**, not measurements of the market. Where they rest on owner reasoning rather than evidence, they are hypotheses — say so in the page body.

## Step 6 · Verify, log

Read each write back. Append to `01_Sector/_memory/skill_runs.jsonl` per [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json) with `skill_id: "S08"`, recording **which relations were closed and which were left open for want of a target**.

Loop: `activation`.

---

## Refuse

- **An offer name absent from the Offer Engineering Registry.** Write `GAP — needs OEOS`.
- A price presented as validated rather than as a hypothesis.
- Closing a relation to a plausible target rather than a correct one.
- Re-owning Sales' or Content's artifact — this database routes; it does not sell or publish.
- A ladder whose `Expansion` is not reachable from its `Entry`.
- `Confidence` above the weakest signal the row cites.
- Treating `Scraping Fields` as authorisation to collect anything.

## Appendix · A dated snapshot — re-measure it, do not trust it

**Measured 2026-08-24.** DB 8 held **87 rows**, every one with `Pain Points`, `Buying Triggers / Demand Signals` and `Target Decision-Maker` **empty**. DB 3 held 217 findings, DB 10 held 57 decision-makers, DB 6 held 4 role lenses for one sub-sector.

The shape of the gap matters: there is plenty to link *for the one `Target` sub-sector* and very little for the other 86 rows. **Closing these relations is not a bulk operation** — it is one sub-sector's worth of real linking and 86 honest blanks.
