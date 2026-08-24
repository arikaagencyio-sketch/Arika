---
name: sector-finding-writer
description: Skill S01 of Sector (01). Turns one piece of researched market truth into one Sector Intelligence row (DB 3) that answers all eight Intelligence-Object questions. Use on a research pass over a Target sub-sector, when a signal needs interpretation, or to apply a sector-intelligence-mapper proposal. The atomic intelligence write of the department; co-runs with sector-audience-language-mapper.
---

# S01 · Sector Finding Writer

You are performing the **apply** step of Sector's write layer. An agent proposes what is true; this skill decides whether that truth may become a database state, and in what mutation mode.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) before doing anything else.** Field-level truth lives in [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB3. Your own row in the library is `SECTOR_SKILL_MATRIX.md` §2.

**This is the atomic write of the department.** Every other intelligence artifact — Sector State, Forecast, Destination Profile, the Opportunity Map, Content's whole chain — is assembled from these rows. A weak row here is not a weak row; it is a weak foundation under five databases.

> **One finding per row.** Not a paragraph, not a summary, not a research note. If it takes two sentences to say what changed, it is probably two findings.

---

## Step 0 · Establish the write path

Notion MCP, in this interactive session. You are the apply step.

| | Data source |
|---|---|
| DB3 Sector Intelligence | `collection://72f90a0f-e34e-4c54-9fcd-9af2e108527e` |
| DB2 Sub-Sectors (the hub) | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |
| DB11 Geography | `collection://e095c661-86cd-4f45-9149-eca1c7195e71` |

## Step 1 · Resolve the Sector Execution Context

Per write contract §2: `record → Sub-Sector → Parent Sector → plugin`. Through the graph, never by name-matching.

`sub_sector_id` is **mandatory** — a finding that resolves to no sub-sector is noise, and the field contract says so. `geography_ids` only when the finding is genuinely place-bound; a finding true everywhere in the sector must not be pinned to a place to look precise.

**Never default to Hospitality.** If a plugin exists, read slot **P3** (demand model) as research input — noting it is `◐ partial` for Sector #001.

## Step 2 · Duplicate detection — before researching anything

Query DB3 filtered to the resolved sub-sector. 215 rows exist today, and the natural key is **title + sub-sector**.

Then choose the mutation mode explicitly (§5) — `CREATE` · `UPDATE` · `VERSION` · `SUPERSEDE` · `NO_OP` · `REJECT` · `ESCALATE`. Never implied by what happened.

`VERSION` when the claim itself changed; `SUPERSEDE` when a better-sourced row replaces this one — **both records survive and the chain stays auditable**. DB3 has no `Previous Value` field, so per write contract §5.1 the prior value goes in the **page body** as a dated line: *what changed · when · which source · what tier*.

**Step 4 of that rule is the one that matters and the one always skipped: name what this invalidates.** A superseded finding may have been the basis of a Sector State, a forecast, an opportunity-map row, or a live content brief. List them. This is the difference between a database row edit and operating-system behaviour.

## Step 3 · The eight questions are the row

A record missing any one is not a finding; it is a note. Each maps to a field:

| # | Question | DB3 field | |
|---|---|---|---|
| 1 | what | `Finding` (title) | required |
| 2 | source | `Evidence` + `Source` | required — **no evidence, no row** |
| 3 | when-observed | `Freshness` | required |
| 4 | reliability | `Confidence` | required |
| 5 | which sector | `Sub-Sector` (relation) | required |
| 6 | which decision | `Strategic Implication` | required |
| 7 | which system consumes it | `Routed To` | required |
| 8 | what action | `Recommended Action` | required |

Plus `Category` (required), `Impact` (optional, derived), `Geography` (optional relation).

### `Category` — preserve all twelve facets

**Structure · Economics · Value Chain · Buying Psychology · Decision Dynamics · Trust · Governance/Power · Infrastructure · Risk/Fragility · Strategic Node · Tool-Stack Chaos · Demand Pattern**

Do not collapse these into a generic bucket. The twelve facets are the analytical resolution of the department; a row filed as the nearest easy category loses it silently.

### `Source` — the four provenance kinds

`xlsx` · `chat` · `agent run` · `research`. This is *where the claim reached us*; `Evidence` is *what backs it*. Both are required and they are not the same field.

### `Strategic Implication` and `Recommended Action` — the two that make it intelligence

`Strategic Implication` is the **so what**. A raw observation is not a finding.

`Recommended Action` is the **decision-purpose gate** made concrete: *an observation with no available action is not intelligence.* If you cannot name an action, the correct outcome is `REJECT` — not a row with a hopeful sentence in it.

### `Routed To` — the canonical 21-value vocabulary

Validate against the **live** option set fetched now. The vocabulary is `GLOBAL_OS.md` §4 itself, not a Sector-curated subset ([`contracts/department-vocabulary.json`](../../../01_Sector/contracts/department-vocabulary.json)). It must be non-empty — a finding no department consumes fails Q7.

## Step 4 · Confidence must match the evidence

`Low` · `Medium` · `High` — and all three are legal outcomes.

- **`High`** — owner-adopted, or a T1/T2 publisher stating it directly.
- **`Medium`** — ordinary research: several credible sources agree, no primary confirmation.
- **`Low`** — a single weak or T3/T4 source, or a claim the evidence only gestures at. **A `Low` finding is a real row**, not a failed one — it records what is suspected and how thinly. It simply may not drive execution until it is raised.

Weak evidence plus `High` confidence is a **constitutional breach**, not a rounding error. Downgrading to `Low` is always available and always preferable to inflating.

`Impact` (`Low` · `Medium` · `High`) is **derived, not researched** — it is your read of what the finding does to Arika's decisions, not a fact about the market. Leave it empty rather than guessing.

A record may never out-rank its publisher. A **T4 source may discover but may not confirm** — a T4, unverified or stale finding must not drive a downstream event, a department action or an execution. Where an aggregator and the primary body disagree, **the primary body wins**.

`Freshness` is `Fresh` · `Aging` · `Stale` — and it is operational, not decorative. A `Stale` finding is barred from driving execution until revalidated.

## Step 5 · Write only your fields

**Yours:** `Finding` · `Sub-Sector` · `Category` · `Evidence` · `Source` · `Confidence` · `Freshness` · `Impact` · `Strategic Implication` · `Recommended Action` · `Routed To` · `Geography`, plus the back-relations on DB2 `Intelligence`, DB7 `Sector Intelligence` and DB16 `Related Intelligence`.

**Not yours:** `Destination Profiles` (S05) · `Content Opportunities` (S10) · `Translations` (S10, cross-department into Content 04 — and an undocumented live relation, finding F8).

Before writing any relation, confirm the target record exists. A relation to nothing is worse than an empty one: it looks resolved.

## Step 6 · Co-run with S02

Findings and language come from one research effort and share one `research_run_id` with `sector-audience-language-mapper`. Splitting them produces a language map with no evidence behind it.

## Step 7 · Verify, log, and record the event honestly

Read the write back and confirm it. *Documented is not applied.*

Append one line to `01_Sector/_memory/skill_runs.jsonl` conforming to [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json), with `skill: "sector-finding-writer"`, `skill_id: "S01"`, the shared `research_run_id`, every gate result, the explicit mutation mode, `writes[].invalidates` where anything was versioned or superseded, and `post_write_verification`.

**`SECTOR_MAPPED`** is this skill's event — subscribers **Content (04)** and **Offer (02)**, both live. Record it with `subscriber_check: "has_subscribers"`.

**Record the event you *would* emit; never claim a publish happened.** `emits` is declarative metadata in this repo — `arika-runtime/src/executor.ts` never calls `eventBus.publish()`. Check [`contracts/event-catalog.json`](../../../01_Sector/contracts/event-catalog.json) for the live subscriber list before recording any other event; routing into one with zero subscribers is a `HANDOFF_FAILURE`, recorded as such and **not silently discarded**.

Loops: `activation`, `refresh`, `signal_change`, `feedback` — with the standing caveat that **the feedback loop cannot close**. No performance store exists anywhere in the agency, so a feedback finding only enters here when a human observed an outcome and cites it. Never infer performance from activity.

---

## Refuse

- No `Recommended Action` → no row. The decision-purpose gate is not advisory.
- No source → no row. Not a low-confidence row: **no row.**
- No consuming department in `Routed To`.
- Confidence exceeding the evidence.
- An unresolved or ambiguous sub-sector. Ambiguity is not a tie to break.
- A fabricated number, date, price, contact or property figure. When source material is missing, **say so** — that is the whole job.
- Writing any field whose `writer_skill` is not S01.

## The agent seam

`sector-intelligence-mapper` emits `sector_map[]` as `{section, finding}` — a flat pair. Its 11 sections are **prose instruction, not an enum**, and they are not DB3's 12 categories.

**S01 performs the mapping itself**, and rejects any section that does not map onto a category rather than forcing it into the nearest one. Where a proposal genuinely needs a thirteenth category, that is an `ESCALATE` — a Tier-1 schema question for the owner, not a field this skill widens.

---

## Appendix · A dated snapshot — re-measure it, do not trust it

> **This section is an observation with an expiry date, not part of the procedure.** Step 2 is authoritative: query current state before every run.

**Measured 2026-08-24.** DB3 held 215 rows, all on the SaaS branch; the 88 established non-SaaS industries had zero findings; exactly one sub-sector was `Status = Target`, which is where the co-run with S02 applied.

**Why this paragraph is written to distrust itself.** The Gate 0 inventory took its row counts from department changelogs rather than queries, and three of the six later measured were wrong (finding F19). **A population claim in a changelog is not a row count.** If this appendix disagrees with a live `COUNT(*)`, the query wins and this appendix is stale — say so and update it.
