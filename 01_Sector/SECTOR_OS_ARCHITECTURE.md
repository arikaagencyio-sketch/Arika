# Sector OS — Universal Core / Sector Plugin Architecture

**Department:** Sector (01) · **Status:** Gate 1 (DECIDE) + Gate 2 (SCHEMA APPLY) complete — the model exists and is wired; **no rows, no sources promoted, no dates or contacts created**.
**Version:** v0.2 (2026-08-20) — Gate 1 (DECIDE) + **Gate 2 (SCHEMA APPLY) executed**. DB 14/15/16 are built and wired; **all three hold 0 rows.**

**Purpose.** State the boundary between what is **universal** in the Sector Operating System and what belongs to a **single sector's plugin**, so that Sector #002 can be activated by authoring a plugin rather than by re-deriving the architecture. Define the Resolution Engine that turns intelligence into a live, layered calendar.
**Authority.** Subordinate to `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md`, `GLOBAL_OS.md`, and [`SECTOR_ACTIVATION_CONTRACT.md`](SECTOR_ACTIVATION_CONTRACT.md). Authoritative for core-vs-plugin classification and for the resolution algorithm. The data model remains [`SECTOR_NOTION_SCHEMA.md`](SECTOR_NOTION_SCHEMA.md); the calendar engine remains [`CALENDAR_INTELLIGENCE.md`](CALENDAR_INTELLIGENCE.md).
**Inputs.** The 13 live Sector DBs + 3 specified-unbuilt (DB 14/15/16) · `AEIT_06/07/08` · `arika-runtime` · the live CRM (ClickUp) · Content (04)'s 8 DBs · Offer (02)'s registry.
**Outputs.** The Sector Plugin Interface (§3) · the Resolution Engine contract (§4) · the contamination migration (§5) · the generalization test (§7).

> **The governing sentence.** *The calendar is not a store of content. It is a resolved view of live external reality, computed per sector, per geography, per property archetype, per client.*

---

## 1. Audit — what already exists (2026-08-20)

The Sector Layer is **substantially built**. This architecture separates and completes it; it does not restart it.

### 1.1 Live substrate

| Store | State | Notes |
|---|---|---|
| DB 1 Sectors Master | **live** — 25 verticals, all scored (`Sector Priority Score`, `Priority Band`) | multi-vertical universe; B2B SaaS is one branch |
| DB 2 Sub-Sectors | **live** — 321 rows (52 SaaS · 88 established · 48 Growth · 133 Frontier/Deep-Future) | the hub; already relation-wired to Marketing, Content, Offer, Branding |
| DB 3 Sector Intelligence | **live** — 211 findings | Sheets 03–06 loaded; Sheet 07 pending |
| DB 4 ICP Classification · DB 5 Prospect Signal Scores | **live, empty by design** | written by agents against real companies (gated on scraping) |
| DB 6 Sector Linguistics | **live** — Accommodation 5-layer map | otherwise empty |
| DB 7 Sector Signals (SCIC) | **live** — 34 rows, 21 `Signal Type` values, 14 views | the one canonical temporal store |
| DB 8 Industry Offer Matrix | **live** — 87 rows | routes onto Offer (02)'s ascension model |
| DB 9 Audience Roles | **live** — 4 Accommodation rows | otherwise empty |
| DB 10 Decision-Maker Registry | **live** — 52 SaaS + 4 Accommodation titles | titles only; named people are 🔴 gated |
| DB 11 Geography | **live** — **11 rows, re-measured 2026-08-28** (the earlier count of 10 was never a measurement): `Global → Africa → Kenya → {Nairobi, Mombasa}` at `City` and `{Diani, Maasai Mara}` at **`Destination`**, plus European Union, United States, Germany, UK | `AEIT_06` `[CANDIDATE]` canonical entity |
| DB 12 Sector State · DB 13 Sector Forecast | **live** — Accommodation rows exist | dated, confidence-gated |
| DB 14 Signal Sources | ✅ **built 2026-08-20** — 0 rows | `13741534-…`; the registration gate is live, no source is `active` |
| DB 15 Market Routes | ✅ **built 2026-08-20** — 0 rows | `c8585c52-…`; route fields are cited-or-blank by field comment |
| DB 16 Destination Profile | ✅ **built 2026-08-20** — 0 rows | `ed957373-…`; the net-new object §3 P5 requires |

> **Gate 2 executed 2026-08-20.** All three previously-unbuilt databases now exist; DB 7 is wired to DB 14/15; DB 3 and DB 11 carry their extensions. Full build record + the two deviations: `SECTOR_NOTION_SCHEMA.md` §6. **Structure only — 0 rows in all three.** The state is now *"the model can hold the intelligence"*, not *"the intelligence exists."*

**Runtime.** `arika-runtime` (agent registry · executor · governance · memory-writer · 5 trigger types: `manual · schedule · event · webhook · join`). Sector agents: `sector-icp-fit` · `sector-intelligence-mapper` · `sector-readiness-analyst` · `sector-signal-refresher` · `sector-signal-scorer` — all **Class 1/2, advisory**, operating mode **manual-apply**.

**Events.** Nine canonical Sector emits. **Six reach a live subscriber** (`PROSPECT_SCORED`, `ICP_CLASSIFIED`, `SECTOR_MAPPED`, `SECTOR_READINESS_SET`, `CALENDAR_UPDATED`, `REGULATORY_CHANGE`). **Three are emitted but unsubscribed** (`DEMAND_SHIFT`, `COMPRESSION_EVENT`, `COMPETITOR_MOVE`) — documented extension points, not live dead events, because the emitter is advisory/manual.

### 1.2 Dependency map — who owns what (never duplicate)

```
                      ┌──────────────────────────────────────────┐
   EXTERNAL WORLD ───►│ DB 14 Signal Sources   (Sector, unbuilt) │
                      └────────────────────┬─────────────────────┘
                                           ▼
   AEIT_08 Source Registry ◄──mirrors── DB 7 SECTOR SIGNALS  (Sector) ──┐
   (Governance 00)                        │        │                    │
                                DB 11 Geography  DB 15 Market Routes    │
                                (Sector, shared)  (Sector, unbuilt)     │
                                          │                             │
                                DB 16 DESTINATION PROFILE ★ net-new     │
                                          │                             │
   DB 1/2/3 taxonomy + findings ──────────┼─── DB 9/10 audience ────────┤
   DB 6 linguistics ──────────────────────┤                             │
   DB 8 Industry Offer Matrix ────────────┤                             │
                                          ▼                             │
                        ══ RESOLUTION ENGINE (§4) ══                    │
                                          │                             │
        ┌─────────────────────────────────┼──────────────────┐          │
        ▼                 ▼               ▼                  ▼          │
  Content (04)       Offer (02)      Sales (05)      Operations (08)    │
  8 live DBs         registry        CRM packet      7 Cognitive        │
  DB5 opportunity    #13 seed        (ClickUp)       Calendars          │
  DB7 briefs                                         (input, never 8th) │
        │                                                               │
        ▼                                                               │
  Design (19) ──► Presence (21) ──► Marketing (03) performance ─────────┘
                                    🔴 no store exists (feedback gap)
```

**Owned elsewhere — Sector references by ID, never re-stores:** `Company / Person / Lead / Opportunity / Client / Project / Invoice / Partner` (**CRM, ClickUp**) · `Offer` (Offer 02) · `Competitor` / `Campaign` performance (Marketing 03) · `Campaign` entity + all content intelligence (Content 04) · the 7 Cognitive Calendars (Operations 08) · `Source` (`AEIT_08`) · `Platform` (Content 04, PIL).

### 1.3 Findings recorded, not silently absorbed

1. **No Destination Intelligence exists.** DB 11 Geography is a lean *place-tree* deliberately kept shareable (`AEIT_06` `[CANDIDATE]`). Nothing in the repo can express that Nairobi is a corporate/MICE market, Mombasa a beach/family market, and Maasai Mara a migration-led international-leisure market. **This is the one genuinely new object.**
2. **The Entity Registry already exists — in ClickUp.** Properties, groups, parents and subsidiaries are `Company` (`AEIT_06` Party domain: *"Prospect/Client/Partner/Competitor are roles, not types"*). A Sector-side property store would be a parallel contact/company store, banned by `SECTOR_ACTIVATION_CONTRACT.md` §14.4.
3. **No performance store exists anywhere.** Marketing (03) owns performance; it holds no live campaign or performance database. The `INTELLIGENCE ← FEEDBACK` return edge is therefore **doctrine only** (`runtime.jsonl` + IntOS Learning). Flagged in §6; **not built here**.
4. **A stale row count.** `CONTENT_INTELLIGENCE_SCHEMA.md` §6 records Content DB 5 as `0 — seeded by an agent run`, but `SECTOR_OS.md` §15 (2026-08-19, ADDENDUM 4 G2) records **3 real Accommodation Content Opportunities** created there. The schema's count is stale. Flagged in that file; the live count should be re-read before any bulk work on DB 5.
5. **Hospitality rules are inside universal files.** See §5.
6. **Documented ≠ applied** *(found at Gate 2, 2026-08-20)*. Two changelog claims did not match the live workspace: DB 3's `Category` was missing the `Tool-Stack Chaos` option that ADDENDUM 3 records as added on 2026-08-19, and Geography holds **11** rows where the schema recorded 10. Both are now closed. **The lesson is architectural, not clerical:** a changelog entry is a record of intent, not proof of state — so every gate from here reads the live system before it writes, and verifies by query after. This is the same discipline Tech Stack (13) invented after finding 4 of its 30 inventory rows false.
7. ~~**Two mis-levelled places.**~~ — ✅ **RESOLVED 2026-08-28 by skill S05.** Maasai Mara and Diani carried `Level = City`; neither is a city, and the `Destination` level had existed for exactly them since Gate 2 without ever being applied. Both are now `Destination`, verified live. **It mattered because §4.1 step 1 filters by geography and a wrong level returns a wrong signal set with no error** — and it was corrected before S09 existed, so no resolution had ever run against the wrong tree.

---

## 2. The three tiers

```
┌─ TIER 1 · UNIVERSAL CORE ────────────────────────────────────────────┐
│  Schema (DB 1–16 field definitions) · the Resolution Engine (§4)      │
│  · doctrine (SECTOR_ACTIVATION_CONTRACT.md) · arika-runtime + the     │
│  event bus · AEIT_06 conformance · the Intelligence-Object Contract   │
│  Changes ONLY when the architecture changes — never per sector.       │
└──────────────────────────┬───────────────────────────────────────────┘
                           │ supplies values into core fields
┌─ TIER 2 · SECTOR PLUGIN ─┴───────────────────────────────────────────┐
│  One pack per sector, filling the 14 interface slots (§3).            │
│  Hospitality = Sector #001. Config and rule VALUES only.              │
│  MUST NOT create a store, an agent, an event, or a field.             │
└──────────────────────────┬───────────────────────────────────────────┘
                           │ resolved against a real engagement
┌─ TIER 3 · CLIENT INSTANCE ┴──────────────────────────────────────────┐
│  Not a store. The OUTPUT of §4 for one client: their calendar,        │
│  opportunities, briefs. Lands in Content DB 7 + the ClickUp CRM.      │
└──────────────────────────────────────────────────────────────────────┘
```

**The load-bearing rule.** *A plugin supplies values into core fields. It never adds a store, a field, an agent, or an event.* If a sector appears to need a new store, that is an architecture change (Tier 1) requiring owner ratification and an `AEIT_06` entry — not a plugin edit.

**The corollary.** *A universal file MUST NOT carry a sector's rule values.* A timing offset, a source list, a demand vocabulary, or a property typology is plugin content wherever it currently sits.

---

## 3. The Sector Plugin Interface

The fixed contract every sector pack MUST fill. Each slot names the universal field its values land in. A slot with no research basis is left **empty**, never plausible — an empty slot is a research task, not a defect.

| Slot | What the plugin supplies | Lands in (Universal Core) |
|---|---|---|
| **P1** | **Ontology** — vertical → industries → business models → company archetypes | DB 1 · DB 2 (`Industry`, `Business Model`, `Company Archetype`) |
| **P2** | **Entity/asset typology + property-type rules** — the archetypes a client can be, and which signal types move each one's demand | DB 2 `Company Archetype` · CRM `Company` (reference) · the §4 step-4 filter |
| **P3** | **Demand model** — who buys/travels, why, when, from where, what triggers it, what cancels it, what makes it repeat | DB 3 `Category = Demand Pattern` · DB 9 · DB 15 |
| **P4** | **Geography scope + destination set** | DB 11 (incl. the `Destination` level) |
| **P5** | **Destination demand-theme vocabulary** — the controlled option set for destination profiles | DB 16 `Demand Themes` |
| **P6** | **Signal-type profile** — which of the 21 `Signal Type` values dominate this sector, and their relative weight | DB 7 + its views |
| **P7** | **Timing rule table** — activation offsets per `Signal Type` × `Signal Role` | DB 7's six activation date fields |
| **P8** | **Source pack** — the T1/T2 publishers per side (destination-side and origin-side) | DB 14 (mirroring `AEIT_08` §3.2) |
| **P9** | **Audience roles + decision-maker titles** | DB 9 · DB 10 |
| **P10** | **Linguistics** — the 5 layers, words to use / avoid, decision-language patterns | DB 6 |
| **P11** | **Offer ladder + outreach angle** — Entry → Expansion → Transformation, or `GAP — needs OEOS` | DB 8 → Offer (02) |
| **P12** | **Content pillars / angles / platform bias** | Content (04) DB 2 · DB 3 · DB 5 |
| **P13** | **Seasonality model + compression threshold** — the sector's season shape and its own `≥ N signals in a rolling window` value | DB 7 · the `CALENDAR_INTELLIGENCE.md` §9 rule, made configurable |
| **P14** | **KPI semantics** — what DB 12's sector-appropriate fields mean here (`ADR / Price Pressure`, `Connectivity / Access`) | DB 12 · Marketing (03) |

**Plugin honesty states.** Every slot carries one: 🟢 web-cited · 🟡 owner-curated · 🔴 gated (needs paid/PII data) · ⚫ template (needs a client system) · ⬜ unauthored · **◐ partial** (some of the slot is authored and cited; a named sub-layer is explicitly ⬜). *(`◐` was added to the legend 2026-08-24 — it was already in active use in the Sector #001 slot table for P3 and P12 while being defined nowhere. A state in use but undeclared is exactly the drift this legend exists to prevent.)*

**Depth-first rule (inherited, `SECTOR_ACTIVATION_CONTRACT.md` §14.1).** A sector gets plugin rows **only when its cross-loop is authored** — never pre-emptively across the 321 sub-sectors.


### 3.1 The P2 rule matrix — the totality rule

**Universal. The *mechanism* below is core and never re-authored; only the cell values are plugin.**

> **Why this section exists.** The first Gate F run (2026-08-28, `SECTOR_ACTIVATION_PROTOCOL.md` §3a) found that
> Sector #001's P2 matrix ruled on **none** of the signal types actually present for one of its three live archetypes,
> and that **`Travel-Trade` — which slot P6 classifies as *dominant* for that sector — appeared in no archetype row at all.**
> Step 4 of the Resolution Engine did nothing for that archetype. Nothing was wrong with any rule that *was* written;
> the defect was that **a sparse matrix cannot tell you what it is missing.** This section makes it able to.

**Rule 1 — the matrix is total, not sparse.** Every (`archetype` × `Signal Type`) cell resolves to one of five verdicts.
**Absence is not a verdict.**

| Verdict | Means | Step 4 does |
|---|---|---|
| `moves` | materially moves this archetype's demand | passes the filter |
| `moves_weakly` | real but secondary | passes, carrying lower weight |
| `does_not_move` | **considered and rejected** | filtered out |
| `not_applicable` | **structurally impossible for this archetype**, in any market | filtered out |
| `unruled` | **not yet considered** — a *declared* gap, with a reason and a date | carried through as **unknown, not false** |

Those are five different facts. Today a sparse matrix collapses the last three into one blank, so *"we decided this does
not move"*, *"this cannot apply"* and *"nobody has thought about it"* are indistinguishable — which is exactly how a
sector's dominant signal type went unruled without anyone noticing.

> **`moves` means *moves*, not *moves up*.** A signal that **suppresses** an archetype's demand moves it as
> surely as one that creates it. A verdict records **materiality, not direction of benefit** — a rule read as
> *"is this good for us"* will systematically miss every suppression signal in the sector.

**Rule 2 — every ruled cell carries four fields.**

| Field | Values | Why |
|---|---|---|
| `verdict` | the five above | the decision itself |
| `direction` | `destination-side` · `origin-side` · `both` | **A property of the *pair*, not of the signal.** A school holiday is origin-side for a lodge selling to Europe and both-sided for a resort selling into its own domestic market. Step 2 needs this and currently infers it from the signal alone. |
| `basis` | `observed` · `owner_reasoning` · `inherited(<archetype>)` | What kind of claim this is. |
| `falsifier` | one sentence | **What would prove this cell wrong.** |

**A cell with no `falsifier` may not hold `moves`.** *A rule that cannot be wrong is not a rule* — the same discipline
this system already applies to a forecast (`DB 13 Likely Trajectory`) and for the same reason.

**Rule 3 — `basis` governs what a cell may be used for.** `owner_reasoning` is a **planning default**, exactly like a
derived activation date: it may filter a calendar; it may **not** be cited as evidence in a client-facing claim. Only
`observed` promotes — and `observed` requires a real outcome fed back through a cited finding, because *no performance
store exists anywhere in the agency* (§1.3). Until one does, an honest plugin is mostly `owner_reasoning`, and says so.

**Rule 4 — the coverage gate, which runs BEFORE Gate F.** Mechanical, and cheap enough to run every time:

1. Every `Signal Type` that P6 marks **`dominant`** or **`secondary`** MUST be ruled (verdict not `unruled`) for **every**
   archetype in the vocabulary. `watch` and `low_relevance` types may remain `unruled`.
2. Every archetype in the live `Asset / Property Archetypes` option set MUST appear in P2.
3. Report `ruled %` per archetype **and** per signal type. A signal type at 0% across all archetypes is the
   `Travel-Trade` failure, and it is now a visible number rather than an absence.

**Gate F does not run against an archetype that fails check 1.** A falsification test on an unruled archetype cannot
falsify anything — it measures the gaps in the plugin, not the structure of the market.

**Rule 5 — authoring order, because totality is a *target*, not a first sitting.** A full matrix is
`archetypes × 21 signal types`; forcing all of it at once produces plausible guesses, and **a guess is worse than a declared
`unruled`** — the blank is honest, the guess is not. Author in tiers:

| Tier | Scope | When |
|---|---|---|
| **1 — must** | P6-`dominant` types × archetypes present in the live geography | before Gate F |
| **2** | P6-`secondary` types × the same archetypes | before the sector is quoted externally |
| **3** | everything else | on demand, when an archetype or a place actually enters scope |

**The same totality discipline applies to P7.** Its `unauthored` rows are the identical failure in the timing table:
a resolver that meets one reports the offsets **unavailable**, which is correct behaviour and still a gap. P7's rows are
already explicitly `state: unauthored` rather than absent — P2 is being brought up to that standard, not the reverse.

---

## 4. The Resolution Engine

The mechanic that makes the calendar **default but live**. It is an **algorithm plus existing views**, not a new store.

### 4.1 The algorithm

```
resolve(sector, geography, property_type, client, window) →

 1 SELECT  signals FROM DB 7
           WHERE sub_sector ∈ sector
             AND (geography ∈ (ANCESTOR CHAIN of the place ∪ its subtree)
                  OR  a DB 15 route touches it)
             AND (signal_date ∨ any activation_date) ∈ window
             AND source_tier ≠ T4
             AND refresh_status ∉ {Needs verification, Superseded/Delayed}
                                                       ← the T4/stale gate

 2 SCOPE   by Signal Role × Market Route direction
           destination-side signals compress inventory AT the place;
           origin-side signals release demand FROM the client's source markets

 3 ENRICH  with DB 16 Destination Profile
           demand themes · primary/secondary audiences · travel motivations
           · content angles · visual language · booking triggers

 4 FILTER  by property-type rule (plugin P2)     ← the property-type calendar
           "does this signal move THIS archetype's demand?"

 5 FILTER  by client context                     ← the client calendar
           inventory · positioning · blackout dates · owned offers · capacity

 6 DERIVE  activation dates from the plugin timing table (P7)
           LABEL every derived date as a planning offset, never an external fact

 7 SCORE   Content DB 5's five additive dimensions (unchanged)
           THEN pass/fail three engine gates:
             · Timeliness      — inside an activation window?
             · Destination Fit — does the destination relation resolve?
             · Client Fit      — does the property-type rule match?

 8 EMIT    Content Opportunities (Content DB 5) → Content Briefs (Content DB 7)
```

**Corrected 2026-08-28 by the first Gate F run.** Step 1 originally read *"geography ∈ DB 11 subtree"*. A place at the tree's lowest level is a **leaf** — it has no subtree — so a place-scoped resolution against descendants alone returns **zero signals** whenever the applicable signals are tagged one level up, which is exactly where broad signals belong. **Signals are inherited downward:** the scope is the place's **ancestor chain ∪ its subtree**. A country-level signal reaches every place in that country; a city-level signal reaches that city alone, because *a sibling is not an ancestor*. The clause as written produced an **empty calendar for a leaf place, with no error** — and it was invisible until something ran it.

**Why gates, not score dimensions (owner decision 2026-08-20).** Content DB 5 runs a live 5-dimension additive score with formula-enforced tier thresholds, written by `content-opportunity-mapper` against a published `output_schema`. Timeliness, Destination Fit and Client Fit are **conditions of applicability**, not magnitudes of value — a piece is not *slightly* out of season. Modelling them as gates preserves the live agent contract and expresses the intent exactly: *publish because the conditions make it commercially valuable, not because it is available.*

### 4.2 The five calendar layers — one store, no calendar-per-layer

| Layer | Implementation | Store? |
|---|---|---|
| 1 · **Sector Calendar** | DB 7 filtered by `Sub-Sector` | view |
| 2 · **Regional Calendar** | DB 7 filtered by `Geography` subtree | view |
| 3 · **Property-Type Calendar** | DB 7 filtered by the plugin P2 rule | view |
| 4 · **Client Calendar** | **step 5 of §4.1** — resolution, not rows | **none** |
| 5 · **Execution Calendar** | Content DB 7 Briefs → Design (19) → Presence (21) | existing |

This upholds the standing law (`SECTOR_ACTIVATION_CONTRACT.md` §15): *never build a calendar per layer, per view, per sector, or per direction.*

**No client calendar exists until a real client does.** Structure may be empty; it may not be guessed.

### 4.3 Live behaviour — what "default but live" actually means

The default is the resolved output for `(sector, geography, property_type)` with no client. It is **live** because a change to any input recomputes the slice:

```
signal changes (date · cancellation · new edition · venue · tier)
        │
        ├─► write Previous Signal Date + Change Reason  (version, never overwrite)
        ├─► append a dated line to the page body naming the confirming source + tier
        ├─► NAME WHAT IT INVALIDATES:
        │     affected Market Routes · Destination Profiles · Content
        │     Opportunities · campaign windows · derived activation dates ·
        │     any agency-calendar entry computed from it
        ├─► re-run §4.1 for the affected slice only
        └─► emit CALENDAR_UPDATED · REGULATORY_CHANGE · COMPRESSION_EVENT · DEMAND_SHIFT
```

*Naming what a change invalidates is the difference between a database row edit and operating-system behaviour.* Destination Profile is added to that invalidation list by this file; the rest is the existing §7 rule in `CALENDAR_INTELLIGENCE.md`.

**"Live" ≠ unattended.** Cloud routines have no web access. Ingestion and verification are interactive Claude Code or a human, on a freshness cadence. The one genuinely self-updating surface is the subscribed external `.ics` layer (Google Calendar → Notion Calendar), which updates a **view**, never the intelligence layer.

### 4.4 The 365-day calendar

A 365-day sector calendar is `resolve(sector, geography, property_type, null, 365d)` — **an output**, produced on demand and recomputed on change. It is never authored as 365 rows of content. Authoring it by hand would be the exact failure this architecture exists to prevent: a beautiful hospitality database that cannot generalize.

---

## 5. Contamination register + migration

Hospitality rule values currently sitting in universal files. **Nothing is deleted** — content moves and a pointer stays behind.

| # | Location | What | Destination | Treatment |
|---|---|---|---|---|
| 1 | `CALENDAR_INTELLIGENCE.md` §5.2 | 5 of 6 timing-rule rows are Hospitality | Plugin **P7** | **Move.** §5.2 keeps the rule *schema*, the two governing rules, and the one `Any sector · Regulatory` row (genuinely cross-sector), plus a pointer. |
| 2 | `CALENDAR_INTELLIGENCE.md` §12 | The whole Kenya-inbound candidate source pack | Plugin **P8** | **Move.** §12 becomes a pointer + the *classes* of source a plugin must name. |
| 3 | `AEIT_08` §3.2 | A second copy of that pack, in an **agency-wide governance file** | — | **Leave in place.** `AEIT_08` is the agency Source Registry; holding source rows is its job. Add one line naming the Hospitality plugin as the owner of *which* sources this sector needs and *why*. No destructive edit to a governance file. |
| 4 | `SECTOR_NOTION_SCHEMA.md` | "Worked example (depth-proof) — Hospitality"; DB 12 `ADR / Price Pressure`, `Connectivity / Access`; DB 15 `Booking Lead Time` / `Air Connectivity` / `Visa Friction`; DB 11 `Property (template level)` | — | **Leave, relabel.** These are *field definitions with sector-appropriate semantics*, which is legitimate core. Mark each as **configurable rule** (core field, plugin-supplied meaning — slot **P14**), and mark the worked example as illustrative. |

**Classification introduced by this pass:** every element of the system is **universal** (core, never re-authored), **plugin** (re-authored per sector), or **configurable rule** (core field, plugin value). §4 of `SECTOR_ACTIVATION_PROTOCOL.md` carries the full slot-by-slot classification once Hospitality is validated.

---

## 6. Gap register — what is deliberately NOT built

| Gap | Why not | Owner |
|---|---|---|
| **Performance store** | Marketing (03) owns performance and has no live store. Building one here would create a parallel store for something already owned. The `PERFORMANCE → INTELLIGENCE` return edge stays doctrine (`runtime.jsonl` + IntOS Learning) until Marketing builds it. | Marketing (03) |
| **Property/booking numbers** (occupancy, ADR, RevPAR, pickup) | ⚫ **Template.** Populated only from a client's connected RMS/PMS. Never fabricated. | client system |
| **Real Lead / contact rows** | 🔴 Gated on a paid, PII, Legal-reviewed people-data source with an Approval-Matrix row. | owner decision #4/#5 |
| **Unattended ingestion** | Cloud routines have no web access. No scraper daemon, no self-writing calendar. | architecture |
| **A client calendar store** | No real hospitality client exists. Empty structure is banned. | §4.2 |
| **A third loop** | The 14-step Cognition Runtime Loop and the 7-link Cross-Loop already exist. The Protocol sequences them; it does not add one. | §3 of the Protocol |

---

## 7. The generalization test (the falsification gate)

> **Remove the Hospitality plugin. The Universal Core MUST still load and return an empty-but-valid resolution for a sector with no plugin. If it breaks, this is a hospitality system wearing a sector-OS label.**

Operationally, at Gate 9:

1. Every reference from a Tier-1 file into `sector_plugins/hospitality/` is a **pointer**, resolvable or absent — never a dependency that changes core behaviour.
2. `resolve()` with a plugin-less sector returns: signals scoped by sub-sector and geography, **no** timing derivation (P7 absent → activation dates blank, not guessed), **no** property-type filter (P2 absent → no narrowing), **no** destination enrichment (P5 absent → themes blank). That is a *valid, honest, empty* result.
3. The mechanical check: `grep -inE "hospitality|kenya|nairobi|mombasa|\bmara\b|safari|hotel|\bota\b"`
   > ⚠️ **Word-boundary anchoring added 2026-08-28, because the original pattern was noisy enough to hide a real hit.** Unanchored, `ota` matches **total**, **totality**, **quota** and **notation**, and `mara` matches nothing useful without boundaries. A §3.1 review returned 5 hits of which **4 were the word "totality"** — a check whose false positives outnumber its findings 4:1 trains its reader to skim, which is how the one real hit gets waved through. *A test nobody reads carefully is not a test.* across the Tier-1 files returns only pointers, explicitly-labelled illustrations, and the cross-sector comparison table — **no rule values**.

**Second-sector proof.** The Protocol is not considered validated until one non-hospitality sector (Professional Services → Legal & Accounting, or B2B SaaS) has been taken through it and produced a *structurally different* calendar shape without a core edit.

---

## 8. Cross-references

[`SECTOR_ACTIVATION_CONTRACT.md`](SECTOR_ACTIVATION_CONTRACT.md) §12 (SCIC) · §13 (Kernel) · §14 (Cross-Loop) · §15 (LSEI) · **§16 (Core/Plugin separation)** · [`SECTOR_NOTION_SCHEMA.md`](SECTOR_NOTION_SCHEMA.md) §0.4 + DB 16 · [`CALENDAR_INTELLIGENCE.md`](CALENDAR_INTELLIGENCE.md) · [`SECTOR_CALENDAR_REFRESH_SPEC.md`](SECTOR_CALENDAR_REFRESH_SPEC.md) · [`SECTOR_ACTIVATION_PROTOCOL.md`](SECTOR_ACTIVATION_PROTOCOL.md) · [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) · `00_Agency_Governance/enterprise_architecture/AEIT_06` (canonical model) · `AEIT_07` (IntOS) · `AEIT_08` §3.2 (source pack) · `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md` · `08_Operations/OPERATIONS_OS.md` §12a.

## 9. Changelog

- **v0.2 (2026-08-20, Gate 2 — SCHEMA APPLY):** Built the three missing databases live in Notion — **DB 14 Signal Sources**, **DB 15 Market Routes** (both specified 2026-08-19 and unbuilt since), and **DB 16 Destination Profile**. Wired DB 7 to DB 14/15, extended DB 3 (`Geography` relation + `Demand Pattern`) and DB 11 (`Destination` level). **Verified non-destructive by query rather than assumed:** both select ALTERs preserved every option ID byte-identically; DB 3 retains 215 rows and Geography 11, with zero nulls. Two findings recorded rather than quietly fixed: a **documented-but-never-applied** DB 3 option (`Tool-Stack Chaos`, claimed 2026-08-19) and **two mis-levelled places** (Maasai Mara, Diani) whose correction is deliberately deferred to Gate 3 as plugin-scope data work. Added finding 6 — *documented ≠ applied* — as a standing verification discipline. **All three new databases hold 0 rows.** — Claude Code (Opus 5)
- **v0.2 (2026-08-28, Gate 3 — THE P2 TOTALITY RULE):** **§3.1 added: the P2 rule matrix is now total, not sparse.** The first Gate F run found that Sector #001's matrix ruled on **none** of the signal types present for one of its three live archetypes, and that **`Travel-Trade` — that sector's own P6-*dominant* type — was ruled by no archetype at all. Nothing was wrong with any rule that *was* written; the defect was that **a sparse matrix cannot tell you what it is missing.** Five verdicts replace two lists (`moves` · `moves_weakly` · `does_not_move` · `not_applicable` · `unruled`), because *"considered and rejected"*, *"structurally impossible"* and *"nobody has thought about it"* are three different facts that a blank collapses into one. Every ruled cell carries `verdict` · `direction` (**a property of the pair, not the signal**) · `basis` · **`falsifier`** — and **a cell with no falsifier may not hold `moves`**, the same discipline already applied to a forecast. `basis: owner_reasoning` is a **planning default, not evidence**: it may filter a calendar, it may not be cited to a client. A **runnable coverage gate** ([`contracts/p2_coverage_gate.py`](contracts/p2_coverage_gate.py)) reports ruled % per archetype and per signal type and **blocks Gate F** on an unruled Tier-1 archetype — *a falsification test on an unruled archetype measures gaps in the plugin, not the structure of the market*. Authoring is **tiered** (dominant × live archetypes first) because 210 cells forced at once produces guesses, and **a guess is worse than a declared gap**. **The gate proved itself during authoring**: it caught a regression in the very restructure that introduced it, when migrating the dominant types silently dropped `Mega-Event` and `Aviation/Connectivity` rulings for three archetypes. — Claude Code (Opus 5)
- **v0.1 (2026-08-20, Gate 1 — DECIDE):** Created. Audited the live Sector Layer (13 built DBs, 3 specified-unbuilt, 5 agents, 9 events / 6 wired), mapped cross-department ownership, and recorded five findings — including that **Destination Intelligence is the only genuinely new object** (Entity Registry is the ClickUp CRM; the Client Calendar is a resolution, not a store; no performance store exists anywhere; Content DB 5's documented row count is stale). Defined the three tiers, the **14-slot Sector Plugin Interface**, the **Resolution Engine** (with the three engine gates deliberately kept *out* of Content DB 5's score to protect the `content-opportunity-mapper` contract), the five calendar layers as views over one store, the live-change propagation rule, the contamination register + migration, the gap register, and the generalization/falsification test. **Nothing built; no Notion or ClickUp write; `.claude/agents/` untouched.** — Claude Code (Opus 5)
