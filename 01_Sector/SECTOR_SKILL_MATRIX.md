# Sector — Skill Matrix

**Department:** Sector (01) · **Version:** v0.7 (2026-08-28) · **Status:** Gate 3 — **Phases 1–2 built, Phase 3 nearly complete.** `S01`–`S06` are live at `.claude/skills/` and have executed against Notion; **S09 and the Gate F falsification test are the remaining Phase 3 work.** S07, S08, S10–S12 remain contract-only.
**Reads:** [`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) (the rules) · [`contracts/sector-databases.json`](contracts/sector-databases.json) (the field contracts) · [`SECTOR_DISCOVERY_INVENTORY.md`](SECTOR_DISCOVERY_INVENTORY.md) (why)

> **The architectural law this file implements:** *agents decide what is true; skills decide how that truth becomes a valid database state.* Five Sector agents already exist and remain in scope — none of the twelve skills below duplicates one.

---

## 1. Ownership — skill → database → field

**One writer per field.** This is `AEIT_06`'s *"one owner per entity"* applied one level down, and it mirrors `CRM_SCHEMA.md`'s "Set by" column, which is already the agency's write-permission model.

| Skill | Databases it writes | Field scope |
|---|---|---|
| **S01** `sector-finding-writer` | DB3 | all 15 fields; DB2 `Intelligence` + DB7 `Sector Intelligence` + DB16 `Related Intelligence` back-relations |
| **S02** `sector-audience-language-mapper` | DB6, DB9, DB10 | all fields except the 🔴 CRM reference fields (`CRM Lead/Person`, `CRM Person`) |
| **S03** `sector-source-registrar` | DB14 | all 28 fields; DB11 `Signal Sources` back-relation |
| **S04** `sector-signal-writer` | DB7 | all 45 fields; incidental DB11 rows when a signal cites a new place |
| **S05** `sector-place-profiler` | DB11, DB15, DB16 | all fields except `Related Entities (CRM)` (🔴) |
| **S06** `sector-state-distiller` | DB12, DB13 | all fields — **derived only**, may introduce no new fact |
| **S07** `sector-taxonomy-registrar` | DB1, DB2 | identity, classification, score, band, lifecycle. **Not** the 14 outbound relations. |
| **S08** `sector-offer-router` | DB8 | all 25 fields, including the three currently-empty relations |
| **S09** `sector-calendar-resolver` | **nothing** | reads DB7/11/12/15/16 + plugin; emits through S10 |
| **S10** `sector-handoff-packet` | Content (04) + Offer (02) relations; CRM text-ID fields | the department boundary only |
| **S11** `sector-plugin-author` | `sector_plugins/{sector}/` | the 14 slots. **No database, field, agent or event.** |
| **S12** `sector-prospect-classifier` | DB4, DB5 | all fields, as one paired write. **Scraping-gated.** |

**Unassigned fields:** none. Every field in `contracts/sector-databases.json` carries a `writer_skill`. A field that ever loses one **must not be written** until it is reassigned.

### 1.1 Where ownership crosses a boundary

| Target | Mechanism | Owner |
|---|---|---|
| Content (04) — 9 relations | native Notion relation | S10 only |
| Offer (02) — `Offers` relation + `Offer Fit` text | relation + reference | S08 routes, S10 packages |
| ClickUp CRM — 6 free-text ID fields | unvalidated string | S10 (S12 once scraping opens) |
| Sales · Marketing · Operations | **event bus only** | S10 |
| Design (19) · EE (20) · Presence (21) · Audits (14) · Client Success (07) | **nothing exists** | — |

DB16 `Visual Language` is explicitly documented as routing to Design (19) — a department that appeared in **neither** routing vocabulary. The field routed somewhere the taxonomy could not express, which was the sharpest proof of finding F2. **Resolved in contract 2026-08-24:** one canonical 21-value vocabulary, taken from `GLOBAL_OS.md` §4 rather than curated ([`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) §1.1 · [`contracts/department-vocabulary.json`](contracts/department-vocabulary.json)). The two live Notion option sets are not yet migrated.

---

## 2. The twelve skills

Each entry is the contract a `SKILL.md` must implement. Grouped by **write boundary** — the set of databases that must be written in one pass to stay consistent — not one skill per table.

---

### S01 · `sector-finding-writer`
**Writes:** DB3 Sector Intelligence · **Loops:** activation, refresh, signal-change, feedback

Turns one piece of researched market truth into one Sector Intelligence row satisfying all eight Intelligence-Object questions. The atomic write of the department — every other intelligence artifact is assembled from these rows.

| | |
|---|---|
| **Triggers** | A research pass on a `Target` sub-sector · a signal needing interpretation (co-run with S04) · a `sector_map` proposal |
| **Context required** | `sub_sector_id` mandatory; `geography_ids` only when the finding is place-bound |
| **Reads** | Web research (cited) · plugin **P3** · `sector-intelligence-mapper` output · the xlsx corpus · existing DB3 rows for duplicate detection |
| **Refuses** | No `Recommended Action` · no source · no consuming department · confidence exceeding evidence · sub-sector unresolved |
| **Co-run** | **S02** — findings and language come from one research effort; they share a `research_run_id` |
| **Hands off** | `Routed To` → Content Opportunities relation → `SECTOR_MAPPED` |

**Agent seam:** `sector-intelligence-mapper.sector_map[]` is `{section, finding}` — a flat pair. The 11 sections are prose instruction, **not enum-constrained**, so S01 maps `section` onto DB3's 12-value `Category` itself and rejects anything that does not map.

---

### S02 · `sector-audience-language-mapper`
**Writes:** DB6 Linguistics · DB9 Audience Roles · DB10 DM Registry · **Loops:** activation, refresh

Writes the language map, the four audience roles and the buyer titles for one sub-sector **in a single coordinated pass** — they come from one research effort and are meaningless apart. Words without a role lens are decoration; a role without its incentives is a job title.

| | |
|---|---|
| **Triggers** | A sub-sector flipped to `Status = Target` · activation **Gate E** · a role lens missing its language map |
| **Context required** | `sub_sector_id`; plugin **P9** + **P10** if a plugin exists |
| **Reads** | Web research per target · plugin P9/P10 · existing DM rows for the SaaS branch |
| **Refuses** | **Any named individual** · a `Role Lens` with no matching DB9 `Role` · vocabulary not grounded in the research run |
| **Co-run** | **S01**, same `research_run_id` |
| **Hands off** | Content overlays and translations inherit the vocabulary **by rollup — never retyped downstream** |

**Two constraints unique to this skill:**

- **It cannot wrap the agent.** `sector-intelligence-mapper` emits `audience_roles: string[]` and `linguistic_notes: string[]` against schemas needing 14 and 13 fields. S02 carries the full field contract itself (F6).
- **It writes into three schemas that cannot hold provenance.** DB6 has `Confidence` only; DB9 and DB10 have none. Per the write contract §1.1, S02 records source and verification date **in the page body** and does not pretend the fields exist (F14).

**Cross-database coherence, checked before any commit:** role coherence (DB9 `Role` ↔ DB6 `Role Lens` ↔ DB10 titles) · one sub-sector across all three · one evidence set · vocabulary that matches the audience, not generic industry language · zero named people.

**Transaction reality:** the Notion API offers no cross-database transaction. S02 writes in dependency order (DB9 → DB6 → DB10), verifies, and on partial failure **records the run incomplete with the written record IDs** rather than pretending atomicity exists.

---

### S03 · `sector-source-registrar`
**Writes:** DB14 Signal Sources · **Loops:** activation, refresh

Registers an external publisher so a signal can be **re-followed**, not merely re-Googled. Holds the registration gate.

| | |
|---|---|
| **Triggers** | Plugin slot **P8** authored · a signal citing an unregistered source · a verification cadence falling due · activation **Gate D** |
| **Reads** | The plugin's candidate source pack · **a live fetch of the endpoint** · `AEIT_08` §3.2 |
| **Refuses** | `active` without a live verification call · a `Feed URL` that does not genuinely exist · a `scrape` source with `Legal Posture = Not assessed` · a source with no named `Consumers` |
| **Hands off** | Legal (10) for scrape posture · Tech Stack (13) for `metered`/`subscription` cost |

**Must also verify the `Consumers` declaration against the actual relations** — it is a hand-maintained shadow that omits Sub-Sectors, Audience Roles and the DM Registry, and can drift silently (F10).

**Status 2026-08-28 (re-measured).** No longer *"zero sources active"* — S03's first pass registered **4 sources, 2 `active`** (`src_ktb_mkte`, `src_ke_public_holidays`), so tier inheritance is now possible for the first time. **But no signal uses it yet: the `Signals` relation on DB 14 is empty across all 34 DB 7 rows.** Registering a source and inheriting from it are two different steps, and only the first has happened.

---

### S04 · `sector-signal-writer`
**Writes:** DB7 Sector Signals (+ incidental DB11) · **Loops:** signal-change, refresh, calendar recomputation

Writes one market signal with its full commercial interpretation — the 21-value type, geography, six lead-time activation dates, eight per-function impact ratings, and the routing set. Owns the change discipline.

| | |
|---|---|
| **Triggers** | `sector-signal-refresher` proposals · a verification cadence · a newly registered source · plugin **P6/P7/P13** |
| **Reads** | Registered sources (S03) · the plugin timing table via [`plugin.config.json`](sector_plugins/hospitality/plugin.config.json) · DB11 subtree |
| **Refuses** | An invented date · an activation date presented as external fact · a property's live figures · a signal out-ranking its publisher's tier |
| **Co-run** | S03 (tier inheritance) · S01 (the interpreted finding) |
| **Hands off** | `CALENDAR_UPDATED` · `REGULATORY_CHANGE` — **both intra-department only today** (see §5) |

**Consumes the existing proposal shape directly.** `sector-signal-refresher.output_schema.proposed_updates[]` is already `{signal, field, current, proposed, source, source_tier, confidence}` — a field-level diff with provenance. S04 takes exactly this and does not invent a second format.

**On the scope axis:** write `Sub-Sector` (the relation) as the canonical scope. The `Sector` select is a deprecated overloaded axis with **no Hospitality option at all** (F1) — populate it only for continuity with existing rows, never rely on it for filtering.

**Unauthored plugin offsets** (`Sports`, `Mega-Event`, `Cruise/Port`, `Aviation/Connectivity` for Sector #001) are `null` in the sidecar. S04 **reports the offset as unavailable**; it never substitutes a neighbouring row's value.

> 🔴 **Scope correction, measured 2026-08-28 — S04 is bigger than the Hospitality slice.** DB 7 holds **34 rows, none with a null tier**: **25 `T1 Primary`, 7 `T3`, 2 `T4`** — and **zero linked to a registered source**. So all 25 T1 claims are hand-assignments with nothing behind them. Only **1** of those 25 is Hospitality (MKTE); the other **24 are the SaaS branch**, which the Kenya-inbound P8 source pack never covered and which nobody has questioned.
>
> **The Hospitality slice is the honest one** — its 9 non-MKTE rows sit at T3/T4 and say so in their own source fields (*"gazette notice not directly read"*). **An unexamined T1 is more dangerous than an admitted T3**, because only the first passes the tier gate silently. S04 must re-tier against registered sources across **all 34 rows**, and should expect the 24 SaaS-branch T1s to be the larger problem, not the 9 flagged Hospitality ones.

---

### S05 · `sector-place-profiler`
**Writes:** DB11 Geography · DB15 Market Routes · DB16 Destination Profile · **Loops:** activation, refresh

Writes the place layer: the geography tree at the right level, directed origin→destination routes with their own clock, and the commercial reading of a destination.

| | |
|---|---|
| **Triggers** | Plugin **P4/P5** authored · activation **Gate E** |
| **Reads** | Plugin geography scope + demand-theme vocabulary · origin-side sources · web-cited route facts |
| **Refuses** | An estimated booking lead time "to make a row look complete" · a destination's demand numbers · a derived campaign window labelled as external fact · a `Destination Profile` with no `Geography` |
| **Hands off** | Content angles → Content (04) · visual language → Design (19) · preferred channels → Marketing (03) |

**Fixed 2026-08-28 (F3 closed).** Maasai Mara and Diani were `Level = City`; both are now `Destination` — the level created for exactly them at Gate 2 and never applied. Resolution Engine step 1 filters by geography **subtree**, so the wrong level was returning a wrong signal set silently. Corrected *before* S09 exists, which is the cheap moment.

> ⚠️ **Architectural caveat this skill must state aloud.** Whether DB15 and DB16 are genuinely universal or belong to a **travel-shaped family of sectors** is an *open question*. Both are `[CANDIDATE]` in `AEIT_06`; neither is canonised; `SECTOR_ACTIVATION_PROTOCOL.md` §4 rates P5 confidence **low** — *"For B2B SaaS, geography may carry no demand-theme meaning."* **Gate I must rule.** For a non-travel sector, S05 records what it could not fill rather than forcing values in.

---

### S06 · `sector-state-distiller`
**Writes:** DB12 Sector State · DB13 Sector Forecast · **Loops:** refresh, signal-change, feedback

Distils "what is happening now" and "where this is heading" from signals and findings that already exist. **Purely derivative — may not introduce a fact.**

| | |
|---|---|
| **Triggers** | A research pass completing · a quarterly cadence · a material signal change |
| **Reads** | DB7 · DB3 · plugin **P14** for what the sector-appropriate fields mean here |
| **Refuses** | A state with no `Critical Signals` relation · a forecast phrased as fact · anything sourced only to itself · an undated state |
| **Runs after** | **S01 and S04.** Never before. |

**P14 is why the fields are meaningful.** `Price Pressure`, `Connectivity / Access`, `Demand Direction` and `Competition` are **configurable rules** — core fields whose *meaning* is plugin-supplied. Without a plugin they are readable but semantically empty, and S06 says so rather than guessing a house meaning.

---

### S07 · `sector-taxonomy-registrar`
**Writes:** DB1 Sectors Master · DB2 Sub-Sectors · **Loops:** activation

The only sanctioned way to add or re-classify a vertical or an industry. DB2 is a 37-field hub carrying 14 relations — a careless write propagates everywhere, so this runs the tightest gate in the library.

| | |
|---|---|
| **Triggers** | A new market entering the universe · activation **Gates A/B** · a lifecycle promotion |
| **Reads** | Plugin **P1** · `sector-readiness-analyst` score and state proposals |
| **Refuses** | A lifecycle promotion without the underlying rows (**no self-promotion**) · a `Sector Priority Score` without its 8-dimension rationale (**no black-box number**) · a vertical filed as a category · a Sub-Sector with no `Parent Sector` |
| **Runs** | **First.** Everything else needs its sub-sector to exist. |
| **Hands off** | `SECTOR_READINESS_SET` → Marketing (03) |

**Why it is placed late in the build order despite running first logically:** the taxonomy is already loaded (25 + 321 rows). S07 governs *future* writes; it does not unblock the pilot.

---

### S08 · `sector-offer-router`
**Writes:** DB8 Agency Opportunity Map · **Loops:** activation

Writes an industry's land-and-expand routing record against the twelve capability families — and records `GAP — needs OEOS` where no real offer exists rather than inventing one. **Sector routes; Offer (02) owns the offers.**

| | |
|---|---|
| **Triggers** | Plugin **P11** authored · a new industry reaching `Validated` · activation **Gate G** |
| **Reads** | The Offer Engineering Registry · DB3 (pain) · DB7 (triggers) · DB10 (who) · DB6 (the words) |
| **Refuses** | An offer name absent from the registry · a price presented as validated rather than hypothesis · re-owning Sales' or Content's artifact |
| **Runs after** | S01, S02, S04 |

**Its concrete job on existing data:** close the three relations — `Pain Points`, `Buying Triggers / Demand Signals`, `Target Decision-Maker` — that are **empty across all 87 rows**.

---

### S09 · `sector-calendar-resolver`
**Writes:** *nothing* · **Loops:** calendar recomputation

Runs the eight-step Resolution Engine to produce a calendar for a sector × geography × property archetype × client. Produces an **output**, never rows.

| | |
|---|---|
| **Triggers** | A client engagement · a planning window · any material signal change |
| **Reads** | DB7 (T4/stale-gated) · DB11 subtree · DB15 · DB16 · DB12 · plugin **P2/P7** via the sidecar |
| **Refuses** | Treating a derived resolution as external fact · running the three gates as score dimensions instead of pass/fail conditions |
| **Runs after** | S04, S05, S06 |
| **Hands off** | Content Opportunities → Content Briefs, **through S10** |

**The eight steps** (`SECTOR_OS_ARCHITECTURE.md` §4.1): SELECT (tier/stale-gated) → SCOPE by role × route direction → ENRICH from DB16 → FILTER by property archetype (plugin P2) → FILTER by client context → DERIVE activation dates (plugin P7) → SCORE via Content DB5's five additive dimensions **then** three pass/fail gates (Timeliness · Destination Fit · Client Fit) → EMIT.

**The three gates are conditions of applicability, not magnitudes of value** — *a piece is not slightly out of season.* They sit **upstream** of Content's scoring and are deliberately not added to its five dimensions.

**Supersedes a planned agent.** `SECTOR_OS.md` §5 planned a sixth agent for this at Gate 5. Owner decision (2026-08-24): **build the skill, close the agent.** The resolution is deterministic given the tables; it needs a disciplined procedure, not a reasoning model.

**Blocked on the sidecar.** Steps 4 and 6 read plugin P2 and P7, which existed only as markdown tables. [`plugin.config.json`](sector_plugins/hospitality/plugin.config.json) resolves this for Sector #001.

---

### S10 · `sector-handoff-packet`
**Writes:** cross-boundary relations, CRM ID fields, events · **Loops:** activation, feedback

The only sanctioned exit from the department. Assembles the packet — findings, language, audience, offer match, timing, CRM tags — and routes it by the **correct mechanism per destination**, which differs.

| | |
|---|---|
| **Triggers** | A sector reaching `Offer-Ready` · activation **Gate G** · a resolver run producing opportunities |
| **Reads** | Every Sector table + the **live** subscriber list |
| **Refuses** | A fabricated contact · writing a script or proposal · **a handoff into an event with no subscriber** |
| **Runs** | **Last**, after every write skill for that sector |

**Mechanism per destination:**

| Destination | How |
|---|---|
| Content (04) | native relation — 9 available |
| Offer (02) | relation + text reference |
| ClickUp CRM | free-text ID tags on `Lead`: `sector`, `sub_sector`, `icp_tier`, `offer_id` |
| Sales · Marketing · Operations | **event only** |

**Must check before routing.** `DEMAND_SHIFT`, `COMPRESSION_EVENT` and `COMPETITOR_MOVE` have **zero subscribers**; `CALENDAR_UPDATED` and `REGULATORY_CHANGE` reach only Sector's own agents. S10 reports a handoff into any of these as `HANDOFF_FAILURE` — it does not perform it silently, and does not discard the packet.

**Boundary law (Contract §14.3):** Sector emits timing + pain + language + who + offer-match + outreach **angle**. It does **not** write the final email, proposal or script — that is Sales (05) enablement and Content (04).

---

### S11 · `sector-plugin-author`
**Writes:** `sector_plugins/{sector}/` · **Loops:** activation

Authors a new market as a **plugin pack of values**, never as new structure. Guards the rule separating a sector-agnostic OS from a single-sector system with others bolted on.

| | |
|---|---|
| **Triggers** | Activating sector #002 onward, after **Gate B** sets one sub-sector to `Target` · activation **Gate C** |
| **Reads** | The 14-slot interface · the validated Sector #001 pack **as pattern, never as template to copy** |
| **Refuses** | Creating a database, field, agent or event → **ESCALATE** as Tier-1 · filling an unresearched slot with a plausible value |
| **Runs after** | Sector #001 has proved which slots are genuinely universal (**Gate I**) |

**Slot honesty states:** 🟢 web-cited · 🟡 owner-curated · 🔴 gated · ⚫ template · ⬜ unauthored · **◐ partial**. An unauthored slot stays visibly empty — a research task, not a defect papered over.

**Must also emit the sidecar.** Any plugin whose P2/P5/P6/P7/P13 slots are authored generates a `plugin.config.json` alongside the markdown, so the resolver can read it.

---

### S12 · `sector-prospect-classifier`
**Writes:** DB4 ICP Classification + DB5 Prospect Signal Scores, **as one paired transaction** · **Loops:** refresh

Writes the tier classification and the 90-point score for a real company. Deliberately last: both databases are empty by design and stay that way until real companies exist.

| | |
|---|---|
| **Triggers** | A real company entering the CRM — **never a research pass** |
| **Reads** | `sector-icp-fit` and `sector-signal-scorer` proposals against real firmographics |
| **Refuses** | A score for a company not in the CRM · a tier without rationale · **a seeded example row** |
| **Blocked until** | API key + cost governance + Legal posture + an Approval-Matrix row |
| **Hands off** | `PROSPECT_SCORED` · `ICP_CLASSIFIED` → Sales (05) — **both live, 2 subscribers each** |

**Two schema defects block it:** DB4 and DB5 carry **no relation to each other** (F4), and `Total Score` is a plain number rather than a formula over its six components (F5). Both must be fixed before S12 can honour its paired-write contract.

---

## 3. Dependency graph

```
S07 taxonomy ──► S11 plugin ──► ┌─ S01 findings ─┐
                                └─ S02 aud/lang ─┘  (co-run, one research_run_id)
                                         │
                                         ▼
                                  S03 sources ──► S04 signals
                                                      │
                                    ┌─────────────────┼─────────────┐
                                    ▼                 ▼             ▼
                              S05 place          S06 state    (S01 re-entry)
                                    └────────┬────────┘
                                             ▼
                                     S09 calendar (writes nothing)
                                             │
                                             ▼
                                     S08 offer routing
                                             ▼
                                     S10 handoff  ──► department boundary
                                             ⋮
                                     S12 prospects (scraping-gated)
```

| Skill | Must co-run with | Must run after | Cross-references |
|---|---|---|---|
| S07 | — | — *(first)* | readiness-analyst proposals |
| S11 | — | S07 | feeds P-slots to S01–S08 |
| S01 | **S02** | S07, S11 | signals needing interpretation |
| S02 | **S01** | S07, S11 | existing DM rows |
| S03 | — | S11 (P8) | agency Source Registry |
| S04 | S03 *(tier inheritance)* | S03 | routes, destinations, geography |
| S05 | — | S03 | signals by direction |
| S06 | — | S01, S04 | **introduces no fact** |
| S09 | — | S04, S05, S06 | reads all, writes none |
| S08 | — | S01, S02, S04 | Offer Engineering Registry |
| S10 | — | all of the above | **live subscriber list** |
| S12 | **its own pair (DB4+DB5)** | scraping gate | ClickUp CRM |

**Two co-run pairs are non-negotiable.** **S01 + S02** — splitting them produces a language map with no evidence behind it. **S12's own pair** — a tier and a score written separately are two unlinked opinions about the same company.

---

## 4. Gate mapping

Two gate vocabularies are in active use and **were mapped to each other nowhere** (finding F18). This is the mapping.

**Letter gates A–I** = the *per-sector activation* sequence (`SECTOR_ACTIVATION_PROTOCOL.md`), repeated for every new sector.
**Numbered gates 1–9** = the *Hospitality build programme* (`SECTOR_OS.md` §15, `FIELD_POPULATION_PLAN.md` §6.5), run once to build the Universal Core.

| Letter | Name | Lifecycle State | Skills | Numbered equivalent |
|---|---|---|---|---|
| **A** | Qualify | `Discovered` | S07 | *(within Gate 1)* |
| **B** | Scope | `Mapped` | S07 | *(within Gate 1)* |
| **C** | Author the plugin | `Intelligence-Rich` | S11 | **Gate 1 DECIDE** ✅ done |
| — | *(Universal Core schema)* | — | — | **Gate 2 SCHEMA APPLY** ✅ done — **no letter equivalent; not per-sector work** |
| **D** | Register sources | — | S03 | **Gate 3** (first half) |
| **E** | Load | `Validated` | S01, S02, S04, S05 | **Gate 3** (second half) |
| **F** | **Resolve — falsification** | `Offer-Ready` | S09 | **Gate 6** validation run · needs **Gate 5** |
| **G** | Route | `Content-Ready` / `Acquisition-Ready` | S08, S10 | — |
| **H** | Live-loop | `Campaign-Ready` | S04 (version a real change) | — |
| **I** | **Generalize — falsification** | — | S11 | **Gate 9** protocol completion |

**Gates F and I are the falsification gates.** *Everything else can succeed while the architecture is still wrong; those two cannot.*

**Honest gaps in the numbered sequence:** Gates **4, 7 and 8 are not defined anywhere** in the files read at Gate 0. Gate 5 was "write the resolver agent" — now superseded by S09 as a skill. The numbered vocabulary is incomplete, and this table does not invent the missing entries.

---

## 5. Event contract

Ground truth: [`SECTOR_EVENT_CATALOG.md`](SECTOR_EVENT_CATALOG.md) · [`contracts/event-catalog.json`](contracts/event-catalog.json).

| Event | Emitting skill | Subscribers | State |
|---|---|---|---|
| `SECTOR_MAPPED` | S01 | Content (04), Offer (02) | ✅ live |
| `SECTOR_READINESS_SET` | S07 | Marketing (03) | ✅ live |
| `ICP_CLASSIFIED` | S12 | Sales (05), ClientPartner (06) | ✅ live |
| `PROSPECT_SCORED` | S12 | Sales (05), Operations (08) | ✅ live |
| `CALENDAR_UPDATED` | S04 | Sector (01) only | ⚠️ intra-department |
| `REGULATORY_CHANGE` | S04 | Sector (01) only | ⚠️ intra-department |
| `DEMAND_SHIFT` | S04 | — | 🔴 dead |
| `COMPRESSION_EVENT` | S04 | — | 🔴 dead |
| `COMPETITOR_MOVE` | S04 | — | 🔴 dead |

**Runtime caveat.** `emits` is declarative metadata — `arika-runtime/src/executor.ts` never calls `eventBus.publish()`. A skill records the event it *would* emit and whether that event has a subscriber. It never asserts a publish happened.

---

## 6. Build order

Sequenced by what is actually blocked, not by skill number.

| Phase | Skills | Unblocks |
|---|---|---|
| **1 · Unblock** ✅ **authored 2026-08-24** | S02, S01 | [`.claude/skills/sector-audience-language-mapper/`](../.claude/skills/sector-audience-language-mapper/SKILL.md) · [`.claude/skills/sector-finding-writer/`](../.claude/skills/sector-finding-writer/SKILL.md). **Scope corrected by live measurement (F19):** DB9 is not empty — all four role lenses exist for the one `Target` sub-sector — and DB6 holds one of four. The unblocking work is **three missing DB6 role lenses (Operator, Amplifier, Enabler)**, not a bulk load. |
| **2 · Make it honest** ✅ **S03 + S04 built and run** | S03, S04 | [`.claude/skills/sector-source-registrar/`](../.claude/skills/sector-source-registrar/SKILL.md). DB 14 went 0 → 4 rows (2 `active`, 2 blocked by expired TLS certs on `.go.ke`). **Three DB 7 signals can now inherit a registered T1 tier; the other seven still cannot.** S04 is the remaining half — it re-tiers the signals against what S03 registered. |
| **3 · Prove it** ◐ **S05 + S06 built; F3 fixed** | S05, S06, S09 | Gates E/F. Fix the two mis-levelled Geography rows first. **Run the falsification test before loading more data.** |
| **4 · Commercialise** | S08, S10, S07 | Closes the three empty relations on 87 rows; opens the boundary. |
| **5 · Generalise & gate** | S11, S12 | S11 after Sector #001 proves universality; S12 after the scraping gate opens. |

---

## 7. Cross-references

[`SECTOR_WRITE_CONTRACT.md`](SECTOR_WRITE_CONTRACT.md) · [`SECTOR_DISCOVERY_INVENTORY.md`](SECTOR_DISCOVERY_INVENTORY.md) · [`SECTOR_EVENT_CATALOG.md`](SECTOR_EVENT_CATALOG.md) · [`SECTOR_ACTIVATION_PROTOCOL.md`](SECTOR_ACTIVATION_PROTOCOL.md) · [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) §3 §4 · [`SECTOR_OS.md`](SECTOR_OS.md) §5 §6 · `02_Offer/OFFER_OS.md` §3 · `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` §7 §8 · `00_Agency_Governance/CRM_SCHEMA.md`

## 8. Changelog

- **v0.7 (2026-08-28, Gate 3 — STATE LAYER LIVE):** **S06 `sector-state-distiller` authored and run.** DB 12 has its first row — Hospitality/Kenya — and **the notable result is what it does not contain: all six state selects are empty.** None is derivable from existing rows, and each blank carries its reason in the page body. `Demand Direction` has no demand data (the Kenya signals are **calendar events**, not demand measurements); `Price Pressure` has no ADR source (the OTA finding is about *commission*, a different thing); **`Connectivity / Access` has no aviation source in DB 14 at all** — a source-pack gap, not a research gap; `Competition` needs STR/CoStar-class comp-set data nobody has registered. `Confidence = Low`, because only **3 of 34** DB 7 signals are source-backed and all three are calendar events — *three date-certain events do not describe a market's condition*. **The no-new-facts rule held**: every clause traces to an existing DB 3 finding, including its tier caveat — the OTA commission figure is carried forward **with** its *"T3, not quotable"* warning rather than laundered into a clean number. **DB 13 left empty by decision, not omission.** — Claude Code (Opus 5)
- **v0.6 (2026-08-28, Gate 3 — PHASE 3 BEGUN):** **S05 `sector-place-profiler` authored; finding F3 closed.** Maasai Mara and Diani re-levelled `City` → `Destination` in DB 11 — the level created for exactly those two rows at Gate 2 and then never applied. Resolution Engine step 1 filters by geography **subtree**, so the wrong level was returning a wrong signal set *with no error*; it was corrected **before S09 exists**, so nothing downstream was stale. The Maasai Mara note had justified `City` as *"the model's lowest non-property tier"* — a rationale that expired when `Destination` was created, and it is replaced rather than left to mislead. **DB 15 and DB 16 deliberately NOT written:** their universality is unruled (owner item 31b, Gate I), and populating them to avoid empty tables would manufacture exactly the false universality Gate I exists to detect. **This closes one of the five queued Notion changes in owner item 31e** — actioned without a separate ruling because the build order names it Phase 3's prerequisite, the correct value is unambiguous, and a select on two rows is trivially reversible. **The other four 31e items involve real choices and remain open.** — Claude Code (Opus 5)
- **v0.5 (2026-08-28, Gate 3 — PHASE 2 BUILT):** **S04 `sector-signal-writer` authored and run — the first signals whose tier is inherited rather than asserted.** Three DB 7 rows linked to registered DB 14 sources: **Jamhuri Day and Mashujaa Day moved `T4 Secondary` → `T1 Primary`** on the Public Holidays Act's own Schedule (both previously cited Wikipedia, both admitting *"gazette notice not directly read"*), and **MKTE** gained the relation its already-correct T1 had been missing. **Mutation mode `UPDATE`, not `VERSION`, and `Change Status = Unchanged` on all three** — no date moved and no prior claim was contradicted; what changed is that three tiers stopped being assertions. DB 7 now has **no `T4` rows at all**, and the two holiday rows are released from the T4 bar on driving downstream execution. `Next Verification` recomputed from the proximity ladder, tightening two of the three to weekly. **Plugin P7 was deliberately not consulted** — no derived activation dates were written, and the unused dependency is recorded rather than silently defaulted. **3 of 34 signals are now backed; 24 unbacked `T1` claims remain**, all SaaS branch. — Claude Code (Opus 5)
- **v0.4 (2026-08-24, Gate 3 — PHASE 2 BEGUN):** **S03 `sector-source-registrar` authored and run — DB 14 has rows for the first time.** Four Kenya destination-authority sources registered: **2 `active`** (Kenya Tourism Board / MKTE; Kenya Law / Public Holidays Act Cap. 110), **2 `candidate`** (Ministry of Education; Ministry of Interior gazette) — both held back because all three `.go.ke` hosts tried returned **`certificate has expired`**. **The registration gate did the job it was built for: two unimpeachably T1 publishers were refused promotion, because authority is not reachability.** That forced a distinction the schema implied but never stated — `Authority Level` describes the publisher, `State` describes whether we can follow it — and a clarification that `Last Verified` means *last successful* verification, so it stays **blank** on a failed attempt. Two plan refinements recorded in `AEIT_08` §3.2: the holidays source **split in two** (statute fixes recurring dates; only a Gazette notice can move one), and registering MKTE **did not** close the broader `src_ke_tourism_events` gap. `Feed URL` blank on all four — none of these publishers offers an ICS or API. — Claude Code (Opus 5)
- **v0.3 (2026-08-24, Gate 3 — PHASE 1 RUN):** **The skill layer executed for the first time.** S02 created the three missing DB 6 role lenses (Operator, Amplifier, Enabler) for the `Target` sub-sector, taking it to 4/4; S01 co-ran on the same `research_run_id` and created 2 DB 3 findings. DB 9 and DB 10 were **`NO_OP`** — already complete, verified before research — which is the duplicate-detection step working rather than a skill finding nothing to do. Both runs logged to `01_Sector/_memory/skill_runs.jsonl` and **validated against the execution-record schema**, the first time that schema met real data. **Defect found by running it: S02's §2 trigger said activation `Gate C`, but §4 maps S02 to `Gate E` — `Gate C` is S11's (author the plugin).** Every other skill's gate reference was checked and is consistent; S02 was the single outlier. Corrected to `Gate E`. This is exactly what the first run was meant to surface: a contract inconsistency invisible on the page and obvious the moment something had to act on it. — Claude Code (Opus 5)
- **v0.2 (2026-08-24, Gate 3 — PHASE 1 AUTHORED):** **The department's first two skills exist.** `sector-audience-language-mapper` (S02) and `sector-finding-writer` (S01) authored at `.claude/skills/`, following the Experience Engineering precedent — two frontmatter keys, prose procedure, pointers into the write contract rather than a restatement of it. Both implement their §2 contract: context resolution and stop conditions, duplicate detection before research, explicit mutation mode, the eligibility gates, page-body provenance for the three schemas that cannot hold it, per-field write boundaries, and an execution record. **Row counts were measured live for the first time and three of six were wrong (F19)** — DB6 `0→1`, DB9 `0→4`, DB10 `52→57`. Phase 1's premise was therefore restated: DB9 is complete for the one `Target` sub-sector, and the real gap is three DB6 role lenses. **Nothing written to Notion in this pass** — the skills exist; running them is the next unit of work. — Claude Code (Opus 5)
- **v0.1 (2026-08-24, Gate 1 — CONTRACT):** Created. Twelve skills specified by **write boundary**, each with trigger, context requirement, read contract, field scope, refusals, co-run rules and loops. Skill→database→**field** ownership assigned for every field in `contracts/sector-databases.json`; no field left unassigned. Dependency graph and the two non-negotiable co-run pairs recorded. **The letter-gate A–I ↔ numbered-gate 1–9 mapping is authored here for the first time**, including the honest note that numbered Gates 4, 7 and 8 are defined nowhere. S09 recorded as superseding the planned Gate-5 resolver agent per owner decision. **No `SKILL.md` authored.** — Claude Code (Opus 5)
