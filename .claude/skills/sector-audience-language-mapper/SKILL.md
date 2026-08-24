---
name: sector-audience-language-mapper
description: Skill S02 of Sector (01). Writes the audience roles (DB 9), the 5-layer language map (DB 6) and the buyer titles (DB 10) for ONE sub-sector as a single coordinated pass. Use when a sub-sector flips to Status = Target, at activation Gate C, or when a role lens is missing its language map. Co-runs with sector-finding-writer on one shared research_run_id.
---

# S02 · Sector Audience & Language Mapper

You are performing the **apply** step of Sector's write layer. An agent proposes what is true; this skill decides whether that truth may become a database state, and in what mutation mode.

**Read [`01_Sector/SECTOR_WRITE_CONTRACT.md`](../../../01_Sector/SECTOR_WRITE_CONTRACT.md) before doing anything else.** It is the governing contract and this skill does not restate it. Field-level truth lives in [`01_Sector/contracts/sector-databases.json`](../../../01_Sector/contracts/sector-databases.json) — DB6, DB9, DB10. Your own row in the library is `SECTOR_SKILL_MATRIX.md` §2.

**Why the three databases are one skill.** Words without a role lens are decoration; a role without its incentives is a job title. They come from one research effort and are meaningless apart — so they are written together or not at all.

---

## Step 0 · Establish the write path

Notion MCP, in this interactive session. There is no other path — `arika-runtime` has no Notion client. You are the apply step; act like it.

| | Data source |
|---|---|
| DB2 Sub-Sectors (the hub) | `collection://dbe10a8b-5c67-4602-9108-12feb540995c` |
| DB9 Audience Roles | `collection://e0513cc9-682f-4dd4-965c-e0292abe86e4` |
| DB6 Sector Linguistics | `collection://172efe6d-08b5-4c85-b24a-fa7065b3e721` |
| DB10 Decision-Maker Registry | `collection://5566c27c-d5db-4a22-9587-e57d0ce5fbbe` |

## Step 1 · Resolve the Sector Execution Context

Per write contract §2: `record → Sub-Sector → Parent Sector → plugin`. Resolve through the graph — never by string-matching a name, never by a hard-coded branch.

**Stop conditions are stop conditions.** Unresolvable sub-sector, ambiguous match, or a hub row with no `Parent Sector` → record `resolution_failure` and write nothing. **Never default to Hospitality.** It is Sector #001, not the system default.

If a plugin exists, read slots **P9** (audience roles + DM titles) and **P10** (linguistics). If either is unauthored, record it in `plugin_slots_unavailable` and report the dependency as unmet — do not substitute a neighbouring sector's values. A sector with no plugin at all is legal: proceed and produce an empty-but-valid result.

## Step 2 · Read what already exists — before researching anything

This is the step that prevents the most common failure: re-writing a row that is already there, or writing a fifth role into a set of four.

Query all three databases filtered to the resolved sub-sector. Then determine, per record, the mutation mode (§5):

- No equivalent row → `CREATE`
- Row exists, better values, no contradiction of a prior claim → `UPDATE`
- The claim **changed** → `VERSION`, and run the 5-step change-history rule
- Nothing material changed → `NO_OP` — still a real result, still logged

**Match on the natural key** — `Sub-Sector` + `Role` for DB9, `Sub-Sector` + `Role Lens` for DB6, `Sub-Sector` + `Buyer Title` for DB10. Never create a duplicate because a run was retried.

**Coverage is per role lens, not per database.** A sub-sector with four DB9 roles and one DB6 language map is 25% complete, not complete. Report coverage as the `4 × role` grid.

## Step 3 · One research run

You and `sector-finding-writer` (S01) share a single `research_run_id`. Splitting the research produces a language map with no evidence behind it — that is why the co-run is non-negotiable.

Research the sub-sector's **buying population**: how the four role lenses actually talk, what each is measured on, what each fears, and which words mark an outsider. Cite every source. If a plugin authored P9/P10, treat it as the starting vocabulary, not the answer.

## Step 4 · Build the records — in dependency order

Write DB9 first: the roles are the lens everything else is expressed through.

### DB9 Audience Roles — one row per role lens

`Audience Profile` (title) · `Sub-Sector` (relation) · `Role` — the canonical four: **Operator · Buyer · Amplifier · Enabler** · `Wants` · `Fears` · `Beliefs` · `Rejects` · `Access Paths` · `Content Persona` (derived) · `Primary Signal Type` — **Authority · Market · Conversion**.

`Access Paths` means **channels and venues** — conferences, communities, publications, peer networks. It does not mean contact details. A named person, an email or a phone number in this field is a contract breach.

**Never write** `CRM Lead/Person` (🔴 gated, S12), `Content Opportunities` (S10), `Destination Profiles (Primary)` and `Destination Profiles (Secondary)` (S05).

### DB6 Sector Linguistics — one row per role lens

`Language Map` (title) · `Sub-Sector` · `Role Lens` (same four values) · the five layers, in order:

1. **Surface (terms/jargon)** — the vocabulary itself
2. **Functional (role language)** — the phrases they use to describe their own job
3. **Cognitive (how they think)** — the mental model the words sit inside
4. **Incentive (what they optimize)** — what they are actually paid and judged on
5. **Cultural (tone/identity)** — how they see themselves, and what tone is disqualifying

Then `Words to use` · `Words to avoid` · `Confidence` (Low/Medium/High).

The five layers are a ladder, not five synonyms for "their words." A row where all five say the same thing has one layer filled and four padded — reject it and research again.

`Words to avoid` is rolled up by Content's Platform Matrix. **It must not be retyped downstream** — Content inherits it by rollup.

**Never write** `Platform Overlays` or `Narrative Positions` (both S10, cross-department into Content 04).

### DB10 Decision-Maker Registry — one row per buyer title

`Buyer Title` (title) · `Sub-Sector` · `KPIs` · `Incentives` · `Fears` · `Buying-Trigger Signals` · `Outreach Intelligence` (derived).

**`Buyer Title` is a TITLE.** "Director of Revenue" is a row. A person's name is a contract breach — people resolve to the CRM under Legal gating, never here.

**Never write** `CRM Person` (🔴 gated, S12) or `Platform Overlays` (S10).

## Step 5 · Coherence — checked before any commit, across all three

| Check | Fails when |
|---|---|
| **Role coherence** | a DB6 `Role Lens` has no matching DB9 `Role` for the same sub-sector |
| **One sub-sector** | any of the three records points somewhere else |
| **One evidence set** | a claim in DB10 has no basis in the research run behind DB6/DB9 |
| **Audience language** | the vocabulary is generic industry language, not this audience's |
| **Zero named people** | any field in any of the three carries a person |

A DB6 row whose `Role Lens` has no DB9 counterpart is the specific failure this check exists for. Write the DB9 role first, or do not write the language map.

## Step 6 · Run the gates (write contract §4)

Decision-purpose · evidence · **confidence-matches-evidence** · vocabulary validated against the **live** option set fetched now (not remembered) · relation targets confirmed to exist.

`Confidence` must match the evidence: research → `Medium`; owner-adopted or T1/T2-sourced → `High`. Weak evidence plus `High` is a constitutional breach, not a rounding error.

## Step 7 · Provenance goes in the page body

**These three schemas cannot hold it.** DB6 has `Confidence` only; DB9 and DB10 have no provenance fields at all (finding F14). Per write contract §1.2, record source and verification date as a dated line in the **page body**:

```
Source · Tier · Verified YYYY-MM-DD · research_run_id
```

Do not invent the fields. Do not write a row that cannot answer the eight Intelligence-Object questions and stay silent about it. Adding the fields is a ratified schema change, not something this skill does.

## Step 8 · Write, verify, log

**There is no cross-database transaction.** The Notion API does not offer one, so do not pretend atomicity exists.

Write **DB9 → DB6 → DB10**. Read each write back and confirm it. On partial failure, **record the run incomplete with the record IDs that were written** — a half-written pass that reports success is worse than a failed one.

Append one line to `01_Sector/_memory/skill_runs.jsonl` conforming to [`contracts/skill-execution-record.schema.json`](../../../01_Sector/contracts/skill-execution-record.schema.json), with `skill: "sector-audience-language-mapper"`, `skill_id: "S02"`, the shared `research_run_id`, every gate result (a skipped gate is recorded as skipped, never omitted), the explicit mutation mode, and `post_write_verification`.

Loops: `activation`, `refresh`.

---

## Refuse

- **Any named individual**, in any field, in any of the three databases.
- A `Role Lens` with no matching DB9 `Role` for the same sub-sector.
- Vocabulary not grounded in the research run — including plausible industry jargon you already know.
- A row written to fill a blank. An empty field is a legitimate state; a plausible guess is a constitutional breach.
- Writing any field whose `writer_skill` in `sector-databases.json` is not S02.

## This skill cannot wrap the agent

`sector-intelligence-mapper` emits `audience_roles: string[]` and `linguistic_notes: string[]` — flat string arrays against schemas needing 14 and 13 structured fields (finding F6). **S02 carries the full field contract itself.** Use the agent's output as research input; never as the record.

---

## Appendix · A dated snapshot — re-measure it, do not trust it

> **This section is an observation with an expiry date, not part of the procedure.** Step 2 is authoritative: measure current state before every run. The snapshot is here only so the first operator knows roughly what they are walking into.

**Measured 2026-08-24.** One sub-sector was `Status = Target`. Against it, DB9 held all four role lenses, DB6 held one (`Buyer`), DB10 held four titles. So the unblocking work was **three missing DB6 role lenses — Operator, Amplifier, Enabler** — not a bulk load.

**Why this paragraph is written to distrust itself.** The Gate 0 inventory recorded DB6 and DB9 as empty. Both claims were wrong (finding F19); the counts came from a changelog rather than a query. **A population claim in a changelog is not a row count.** If this appendix disagrees with a live `COUNT(*)`, the query wins and this appendix is stale — say so and update it.
