# Live Sector Event Intelligence (LSEI) — Calendar Intelligence Spec

**Department:** Sector (01) · **Version:** v0.1 · **Created:** 2026-08-19
**Status:** **Pass 1 (spec) + Pass 2a (partially applied, 2026-08-20).** ✅ **Live:** the §8 colour/type taxonomy (`Signal Type` 16 → 21), the §6 direction model at signal level (`Signal Role`), §7 change-versioning fields, the §10 operating views, and a real Kenya-inbound pilot calendar with §5 timing offsets written. ✅ **Built 2026-08-20 (Gate 2):** **DB 14 Signal Sources** (`13741534-…`) and **DB 15 Market Routes** (`c8585c52-…`) now exist and DB 7 is wired to both (`Signal Source`, `Market Routes`). 🔲 **Still design-only because the stores are EMPTY:** the source-registry discipline (§2/§3), route-level intelligence (§6.1), ICS subscription (§3.1) and the demand-surge rule (§9) do not operate until rows exist. **No external source has been registered — every §12 candidate remains unverified, with no URL recorded.** A built table is not a followed source.
**Authority:** subordinate to `SECTOR_ACTIVATION_CONTRACT.md` (esp. §12 SCIC, §13 Kernel, §14 Cross-Loop, and the new §15 LSEI doctrine) and the Operating Constitution. Authoritative for calendar/source/route/timing design.
**Governs:** `SECTOR_NOTION_SCHEMA.md` DB 7 · DB 11 · DB 14 · DB 15 · `SECTOR_CALENDAR_REFRESH_SPEC.md` · `AEIT_08` §3.2.

---

## 0. Why this file exists

The Sector time dimension was already built as a **temporal intelligence layer** (SCIC, 2026-08-15): one canonical Sector Signals DB, 16 signal types, six lead-time activation dates, eight per-department impact fields, and a Geography relation. That architecture is correct and is **not** being replaced.

What was missing is everything that makes it *live*:

| Missing | Consequence |
|---|---|
| A registry of the **real external calendars** | `Authoritative Source` was free text. Nothing recorded feed type, refresh cadence, or supersession — so nothing could be re-followed, only re-Googled. |
| **Authority discipline in practice** | The hospitality pilot's seasonality rows were sourced to hotel-tech *marketing blogs*, not to tourism boards, federations, or organizers. The `Source Tier` field existed; the discipline did not reach the data. |
| **Origin ↔ destination** | Nothing in the repo. A signal had one Geography. But marketing Dubai to Africans and marketing Kenya to Germans are different commercial jobs against the *same* physical event. |
| **Reusable timing rules** | The six activation dates were hand-derived per signal. No per-sector clock profile existed to derive them from. |
| **Change as a first-class record** | `Change Status` is a single select. A date that moves overwrote the old one; nothing recorded what the move invalidated. |
| **A route into the agency's own calendars** | `COMPRESSION_EVENT` / `DEMAND_SHIFT` were emitted and unsubscribed. The market clock never reached Operations. |

The reference model is the **FIA/F1 calendar**: an official body publishes a structured, dated calendar; the calendar *changes*; amendments are recorded; and an ecosystem synchronizes off it. The hospitality equivalent exists — but distributed across tourism boards, city DMOs, sports federations, MICE bodies, and event-data providers rather than in one place. LSEI is the layer that registers those sources, follows them, and turns their changes into agency timing.

**One-line doctrine:** *the agency calendar is not the source of truth — it is a rendered view of live external reality, computed per market route.*

---

## 1. Architecture — what is new vs. what already exists

```
                       EXTERNAL WORLD
   tourism boards · federations · organizers · MICE bodies · event APIs
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │  DB 14  SIGNAL SOURCES        ★ NET-NEW  │  the registry: who publishes,
        │  authority · feed type · cadence · state │  in what format, how often,
        └──────────────────────────────────────────┘  is it still true
                              │
                    ingestion (interactive CC / human — §4)
                              ▼
        ┌──────────────────────────────────────────┐
        │  DB 7   SECTOR SIGNALS          EXISTS   │  the fact + its commercial
        │  16→21 types · 6 clocks · 8 impacts      │  interpretation over time
        └──────────────────────────────────────────┘
                    │                      │
                    ▼                      ▼
   ┌────────────────────────┐  ┌──────────────────────────────────┐
   │ DB 11 GEOGRAPHY EXISTS │  │ DB 15  MARKET ROUTES  ★ NET-NEW  │
   │ Global→Region→Country  │  │ origin ⇄ destination · lead time │
   │ →City→Property         │  │ air access · visa · channels     │
   └────────────────────────┘  └──────────────────────────────────┘
                              │
                    TIMING RULES (§5 — a rule table, not a store)
                              ▼
        ┌──────────────────────────────────────────┐
        │  DB 12 SECTOR STATE · DB 13 FORECAST     │  EXISTS
        └──────────────────────────────────────────┘
                              │
              event bus (SECTOR_ACTIVATION_CONTRACT.md §8)
                              ▼
   Content (04) · Sales (05) · Marketing (03) · Offer (02) · Operations (08)
                              ▼
              THE 7 COGNITIVE CALENDARS  (an input — never an 8th)
```

**Net-new: 2 databases.** Everything else extends. The proposal that seeded this work named ~17 calendar layers, a 15-folder domain, and 6 engines; per `SECTOR_ACTIVATION_CONTRACT.md` §13.4 (no parallel stores) and §13.5 (*the engines are the runtime, not new software*), the 17 layers are `Signal Type` values, the folders are this file, and the engines already exist as `sector-signal-refresher`, `sector-intelligence-mapper`, the event bus, and `arika-runtime`.

---

## 2. Source hierarchy — who gets to be believed

Maps directly onto DB 7 / DB 14's existing `Source Tier` enum. **A source's tier is a property of the publisher, not of how convenient it is.**

| Level | `Source Tier` | Who | Examples of the class |
|---|---|---|---|
| 1 — Official authority | `T1 Primary` | The body that *runs* the thing | National tourism boards · city DMOs / convention bureaus · government gazettes (holidays) · education ministries (school terms) · sporting federations · the event organizer itself · the venue |
| 2 — Institutional | `T2 Institutional` | Recognised industry bodies | Trade-show operators (WTM, ITB) · industry associations (AHLA, HSMAI, ICCA, PCMA) · aviation-route authorities |
| 3 — Structured aggregator | `T3 Commercial-intel` | Machine-readable event platforms | Event/ticketing APIs · event-data providers · trade-show directories |
| 4 — Secondary | `T4 Secondary` | Everything else | Vendor blogs · listicles · news round-ups · social posts · AI-inferred |

**Rules (enforced in Contract §15):**
- A **T4 source may discover but may not confirm.** It can surface that an event exists; the dated record must then be sourced to the T1/T2 publisher before it is `Confirmed`.
- **A lower tier never overrides a higher one.** If an aggregator and the organizer disagree, the organizer wins and the aggregator row is marked `Superseded/Delayed`.
- **T4 / unverified / stale signals cannot drive downstream execution** — pre-existing rule (Contract §6, §12), restated here because the source pack makes it newly tempting.

> 🔴 **The failure mode this hierarchy exists to catch.** A **vendor's** claim about a market is not the market authority's claim, however convenient it is to cite. Where live rows are found sourced to vendor content at `T3`, they are **re-sourced to T1 and superseded on contradiction — never deleted.** The current open instance (the Hospitality seasonality rows) is tracked in [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) slot **P8**.

---

## 3. Feed taxonomy — how a source is actually followed

Recorded on DB 14 as `Feed Type`. The distinction that matters is **snapshot vs. subscription**:

| `Feed Type` | Follow mode | Notes |
|---|---|---|
| `ICS` | **Subscription** | The one true "keep following" format. A subscribed ICS URL reflects the publisher's later additions and changes. This is what the F1-calendar model actually runs on. |
| `API` | Subscription-ish | Queryable, often supports "records updated since". Usually keyed/paid → cost-gated. |
| `RSS` / `JSON` | Subscription-ish | Polled on cadence. |
| `HTML` / `sitemap` | **Snapshot** | Read on cadence; every read is a fresh diff. |
| `scrape` | Snapshot | Requires a Legal (10) posture note before `active` (`AEIT_08` §5). |
| `manual` | Snapshot | A human reads a PDF/page and transcribes. Legitimate — many tourism boards publish only this way. |

**Downloading an `.ics` file is a snapshot. Subscribing to an `.ics` URL is a follow.** DB 14 records which one a source supports, because it determines whether the calendar can stay current on its own or needs a scheduled human/CC read.

### 3.1 The sync architecture (owner decision, 2026-08-19)

```
external ICS URL  (federation · tourism board · organizer)
        │  subscribe — the publisher's changes flow in
        ▼
   Google Calendar        ← the follow layer (the only free layer that
        │                   can subscribe to an external ICS URL)
        │  account sync
        ▼
   Notion Calendar        ← the unified agency view
        ▲
        │  database views
   Notion Sector Signals  ← the interpreted layer (DB 7)
```

Both tools are registered in `13_Tech_Stack/TECHSTACK_OS.md` §3, closing that file's own standing gap (*"A calendar is arguably the most-used tool in any advisory business and §3 does not name one"*).

**The critical separation:** a subscribed external calendar shows the agency *what the world published*. It is **not** the intelligence layer. Only a signal that has been through the DB 7 lifecycle — verified, geo-scoped, route-scoped, impact-rated, timing-derived — is a thing the agency acts on. The Google Calendar layer is an **input and a cross-check**, never a system of record.

---

## 4. Ingestion — the honest constraint

Restated from Contract §13.4, because this is the rule people most want to forget when they see the word "live":

- **A claude.ai cloud routine has no web access.** Verified 2026-08-11 against the account's one healthy routine. Its tools are `Bash/Read/Write/Edit/Glob/Grep` plus a Notion connector.
- Therefore **there is no unattended scraper daemon and no self-writing calendar.** Ingestion and verification are done by **interactive Claude Code (which has web tools) or a human**, on a cadence.
- The honest unattended form is the **comment-posting staleness watchdog** already specified in `SECTOR_CALENDAR_REFRESH_SPEC.md` §5a: it reads the DB, finds what is due, and posts a Notion comment saying *which* signals are stale and *where* to re-verify each. It writes comments, never dates.
- **"Real-time" means a freshness cadence, not a live stream.** The Google Calendar ICS subscriptions are the one genuinely self-updating surface — and they update a *view*, not the intelligence layer.

---

## 5. Timing Intelligence — the clocks

The proposal asked for a standalone Timing Engine with multiple clocks. It reconciles to a **rule table**, read by `sector-signal-refresher` and written into DB 7's **existing** six activation date fields. No new store.

### 5.1 The five questions every signal must answer

1. When is it? → `Signal Date`
2. When does demand begin? → the booking/decision lead time (route-dependent, §6)
3. When should we market? → `Marketing Activation Date`
4. When should sales act? → `Sales Activation Date`
5. When does the opportunity close? → `Action Deadline` / `Execution Deadline`

### 5.2 The rule table — schema here, values in the sector plugin

> 📦 **Moved 2026-08-20.** The **Hospitality** rows that used to sit in this section are **sector rule values**, not universal engine content, and now live in [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) **slot P7** — moved verbatim, nothing lost (`SECTOR_ACTIVATION_CONTRACT.md` §16). This section keeps the **schema** and the **rules that govern any sector's table**.

**The schema.** One row per `(Signal Type × Signal Role)`, six offsets, written into DB 7's six existing activation date fields:

| Sector · Signal Type · Role | Strategic | Marketing | Sales | Offer | Revenue Watch | Action Deadline |
|---|---|---|---|---|---|---|
| *(supplied by the active sector plugin, slot P7)* | T-n | T-n | T-n | T-n | T-n | T-n |
| **Any sector · `Regulatory`** | T-365 | T-180 | T-270 | T-180 | T-90 | T-30 |

The `Regulatory` row is **genuinely universal** — it derives from the FSMA/CSRD worked examples and holds across sectors, so it stays here rather than being copied into every plugin.

Offsets are **derived planning offsets, never external facts** (Contract §12). They are configurable sector rules, not hardcoded assumptions, and are re-tuned as real outcomes accumulate in `01_Sector/_memory/runtime.jsonl`.

**Two rules govern any sector's table:**
- **Origin-side signals run on longer clocks than destination-side ones** — a German school holiday drives a booking decision months before the trip; a destination event compresses inventory closer in.
- **A row without a real research basis is left empty, not filled with a plausible number.** A sector gets rows when its cross-loop is authored — **not before.**

### 5.3 What is *not* modelled
The proposal named nine parallel clocks (event / demand / booking / marketing / content / sales / production / travel / recovery). Six activation dates already exist and are unfilled on 25 of 28 live rows. **Fill the six before inventing three more.** Post-event retention is carried in `Recommended Action` until a real engagement proves a dedicated field is needed.

---

## 6. Market Direction — the origin ⇄ destination doctrine

**The core claim:** the commercial meaning of a physical event is not a property of the event. It is a property of the **route** — who you are moving, from where, to where.

```
                    ONE PHYSICAL EVENT
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  Germany → Kenya      UK → Kenya      Regional Africa → Kenya
  long booking lead    mid lead        short lead
  seasonal, planned    seasonal        opportunistic
  school-holiday-led   school-led      event-led
  ≠                    ≠               ≠
        └───────── different campaign windows ─────────┘
```

And the reverse is a **different route object entirely**: `Kenya → Dubai` is not `Dubai → Kenya`. Same two places, different audience, different seasonality overlap, different visa friction, different message, different clock.

### 6.1 How it is modelled

| Concept | Where it lives |
|---|---|
| The place | **DB 11 Geography** (exists) — `Global → Region → Country → City → Property` |
| The pair | **DB 15 Market Routes** (net-new) — one row per directed pair |
| Which side of a route a signal sits on | **DB 7 `Signal Role`** (net-new field) — `Destination-side` · `Origin-side` · `Both` |
| Which routes a signal affects | **DB 7 `Market Routes`** relation (net-new) — one signal ↦ many routes |

`Signal Role` is what makes the two-sided model work with one signal store:
- A Kenyan coastal festival is `Destination-side` — it compresses inventory *at* the destination.
- A German state school holiday is `Origin-side` — it releases demand *from* the origin.
- Ramadan is `Both`, and means opposite things on each side.

### 6.2 The client-direction rule

Which direction Arika is working in is a property of the **client engagement**, not of the calendar. A Kenyan lodge selling to German travellers and a Dubai hotel selling to African travellers consume the *same* signal store through *different* routes. The calendar therefore never assumes a direction — it stores both sides and lets the route resolve it.

**Scope is plugin content, not engine content** *(clarified 2026-08-20)*. Which routes a sector actually builds is slot **P4** of its plugin — the active Hospitality scope (Kenya-inbound, owner decision 2026-08-19) lives in [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md). The universal rule: **routes are built when a real engagement requires them — never pre-populated as a world atlas.**

*(The place names used throughout §6 are illustrations of the direction mechanic, not scope decisions.)*

### 6.3 Honesty
Route fields — booking lead time, air connectivity, visa friction, currency context — are **web-cited per route or left blank**. They are never estimated to make a row look complete. A blank route field is a research task, not a defect.

---

## 7. Change as a first-class record

A calendar that overwrites a moved date has destroyed the most valuable thing it holds. The FIA publishes *amendments*; so must this.

**On a material change** (date moved · cancelled · postponed · venue changed · new edition):

1. Write the prior value to `Previous Signal Date` and the reason to `Change Reason` (new DB 7 fields).
2. Append a dated line to the signal page body: *what changed · when · which source confirmed it · what tier.*
3. Set `Change Status` and `Refresh Status` accordingly.
4. **Name what it invalidates** — the rule that makes this an operating system rather than a table:

> When a signal's date moves, the change MUST name the downstream work it invalidates: affected **Market Routes**, **Destination Profiles** *(added 2026-08-20)*, **Content Opportunities**, **campaign windows**, derived **activation dates**, and any **agency-calendar** entry computed from it.

5. Emit the appropriate event (`CALENDAR_UPDATED` · `REGULATORY_CHANGE` · `COMPRESSION_EVENT` · `DEMAND_SHIFT`).

The repo already holds two worked examples of exactly this: **FSMA 204** (Jan 2026 → Jul 2028) and **CSRD Wave 2** (→ 2028), both of which reduced near-term sector urgency that readiness scoring had leaned on. Those are the pattern.

---

## 8. Colour semantics — intelligence class, not decoration

Colour encodes **what kind of signal this is**; texture encodes **how much to trust it**. Implemented with Notion select colours and view grouping — **no new field**.

| Class | Colour | `Signal Type` values |
|---|---|---|
| Critical compression | 🔴 red | `Event/Compression` at `Commercial Priority = Critical` · `Mega-Event` |
| Sector event | 🔵 blue | `Event/Compression` · `Sports` |
| MICE / business | 🟣 purple | `Sales/MICE` · `Travel-Trade` · `Trade/Fashion` |
| Demand opportunity | 🟢 green | `Demand` · `Consumer-Behaviour` |
| Seasonal trigger | 🟡 yellow | `Seasonality` · `School-Holiday` · `Cruise/Port` |
| Cultural / consumer | 🩷 pink | `Holiday/Cultural` |
| Regulatory / government | ⚫ dark | `Regulatory` |
| Operational constraint | 🟤 brown | `Risk/Disruption` · `Supplier/Cost` · `Aviation/Connectivity` |
| Market structure | 🟠 orange | `Competitor` · `Distribution` · `Economic` · `Technology` |

**Confidence is read off two existing fields, not a new one:** `Source Tier` (T1 → trust) × `Refresh Status` (`Confirmed` / `Annual-recurring` / `Needs verification` / `Superseded/Delayed`). The proposal's solid/striped/dotted idea has no Notion equivalent; the honest implementation is a **filtered view per confidence band**, plus the existing "Unverified" view.

---

## 9. Demand surge — aggregate compression

The single most valuable read the calendar can produce is not *"an event is happening"* but *"this destination is about to be under pressure from several things at once."*

**Rule (a derived view + agent logic — no new store):**

> Where **≥ 3 signals** of `Commercial Priority` High or Critical overlap the **same Geography** within a **rolling 14-day window**, flag a **compression read** on that geography and window.

The compression read is written as a **Sector Intelligence finding** (DB 3, `Category = Strategic Node`) linked to its constituent signals, and emits `COMPRESSION_EVENT`. It is *interpretation*, so it inherits the lowest confidence among its inputs and is never presented as a forecast of occupancy or price — those numbers belong to the ⚫ client-connected template layer and are never fabricated.

---

## 10. The Control Tower — a read view

Per Contract §13.1, the Control Tower is **a read view over memory, not a new store.** It is a Notion dashboard page assembling the DB 7/12/13 views that already exist, answering:

- **What changed** — signals with `Change Status ≠ Unchanged`, last 7 days
- **What is stale** — `Needs verification` + past `Next Verification`
- **What is close** — `Action Deadline` inside 30 days (the ⏰ Activation Deadlines calendar)
- **What is compressing** — geographies triggering §9
- **What it hits** — grouped by `Departments Affected`
- **Which routes** — grouped by Market Route
- **What is unsourced** — `Source Tier` null or T4

The point: a strategist should not open two hundred tourism websites every morning. The system says *these are the changes that matter.*

---

## 11. Generalization — this is not a hospitality framework

Hospitality is the pilot because its demand is transparently event-driven, which makes the model easy to falsify. The engine is sector-agnostic:

```
SECTOR → registered sources → signals → geography → routes
       → timing rules → impact → client context → agency action
```

Every `Target` sector authors the **same links, different content** (Contract §14.2). What changes per sector is: which sources are T1, which `Signal Type` values dominate, and what the timing-rule row says.

| Sector | T1 sources look like | Dominant signal types |
|---|---|---|
| Hospitality | Tourism boards · DMOs · federations · MICE bodies | Seasonality · Event/Compression · Holiday · Sales/MICE |
| B2B SaaS | Regulators · conference organizers · fiscal calendars | Regulatory · Event/Compression · Demand |
| Professional Services | Tax/filing authorities · bar & accounting bodies | Regulatory · Seasonality · Demand |

**Rule:** a sector gets timing-rule rows and registered sources when its cross-loop is authored, never pre-emptively. Depth-first on `Target` sectors (Contract §14.1) — the discipline that stops this becoming a 321-sector data-collection project.

> 📦 **Formalized 2026-08-20.** "The same links, different content" is now a **stated interface**: the 14-slot Sector Plugin Interface in [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) §3, of which this file's §5.2 (timing) and §12 (sources) are slots **P7** and **P8**. The table above is the cross-sector *comparison* that motivates the interface; the per-sector *values* live in `sector_plugins/{sector}/`.

---

## 12. Source pack — the classes here, the sector's candidates in its plugin

> 📦 **Moved 2026-08-20.** The **Hospitality, Kenya-inbound** candidate pack that used to sit in this section is **sector content** and now lives in [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) **slot P8** — moved, nothing lost. The agency-wide registry rows remain in `AEIT_08` §3.2, which is their canonical home (`SECTOR_ACTIVATION_CONTRACT.md` §16). This section keeps the **classes** every sector's pack must cover.

**Every source row starts at `state = candidate`.** Per `AEIT_08` §5, *a source enters `active` only after a live verification call proves it answers.* Seeding material — however specific its claims about feed capabilities, event counts or revised dates — is a **lead list, not evidence**, and is never transcribed as fact.

**The classes a sector's pack MUST cover** (what changes per sector is *which publishers occupy each class*, and whether a class is even populated):

| Class | What occupies it | Why the class exists |
|---|---|---|
| **T1 · Destination-side authority** | The bodies that own the dated reality where demand lands — official calendars, government registries, venues | The destination-side spine; date-certain and directly demand-moving |
| **T1 · Origin-side authority** | The bodies that govern when the *source market* is released — holiday and institutional calendars | The origin-side clock, on longer offsets (§5.2) |
| **T1/T2 · Trade & industry bodies** | Where the trade meets. **Two distinct uses, one registry:** Arika's own attendance, and the client's demand calendar — separated by `Signal Role` | Institutional dates that move both sides |
| **T1 · Federations / governing bodies** | The reference case: an official body publishing a structured, **amendable** calendar. **Verify per event, never per series** | Amendments are why `Previous Signal Date` + `Change Reason` exist |
| **T3 · Aggregators / APIs** | Machine-readable breadth. **Registered, not connected** — paid/keyed, cost-gated (same posture as the §3.1 people-data set) | **Discovery only.** They never outrank the organizer (§2) |

Each candidate must carry a named **`consumers`** destination DB before promotion — the decision-purpose gate (Contract §13.3): *no source without a downstream home.*

---

## 13. What this file will never do

- Invent a date. Unverifiable → `Needs verification`, no value.
- Treat the seeding research as evidence. Every URL and claim in it is a lead until checked against the publisher.
- Present a derived timing offset as an external fact.
- Estimate a route's lead time, air capacity, or visa friction to fill a blank.
- Fabricate a property's occupancy, ADR, RevPAR, or pickup — ⚫ template until a client connects a real RMS/PMS.
- Build a calendar per layer, per view, or per sector.
- Run unattended. No web in cloud routines; no auto-write without an `AUTOMATION_APPROVAL_MATRIX.md` row.

---

## 14. Cross-references

`SECTOR_ACTIVATION_CONTRACT.md` §12 (SCIC) · §13 (Kernel) · §14 (Cross-Loop) · **§15 (LSEI doctrine)** · **§16 (Core/Plugin separation)** · [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) (Plugin Interface + Resolution Engine) · [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) (slots P7/P8) · `SECTOR_NOTION_SCHEMA.md` DB 7 / 11 / 12 / 13 / **14 / 15 / 16** · `SECTOR_CALENDAR_REFRESH_SPEC.md` (cadence + escalation ladder) · `AEIT_08` §1 (Source entity) · §3.2 (the candidate pack) · §4 (Intelligence Calendar) · §5 (registration gate) · `13_Tech_Stack/TECHSTACK_OS.md` §3 (Google Calendar + Notion Calendar) · `08_Operations/OPERATIONS_OS.md` (the market-clock bridge into the 7 Cognitive Calendars) · `.claude/agents/sector-signal-refresher.md` (extended in Pass 2).

## 15. Changelog

- **v0.3 (2026-08-20, Sector OS Architecture Gate 1):** Made this file **sector-agnostic**. §5.2 now carries the timing-rule **schema** + the genuinely-universal `Any sector · Regulatory` row; the five Hospitality rows moved verbatim to the plugin (slot **P7**). §12 now carries the **classes** of source every sector's pack must cover; the Kenya-inbound candidate pack moved to the plugin (slot **P8**) — the agency-wide registry rows stay in `AEIT_08` §3.2, their canonical home. **Nothing deleted; pointers left behind.** §7's invalidation list gains **Destination Profiles** (the new DB 16). §11 now points at the formal 14-slot Plugin Interface it had informally described. Doctrine: `SECTOR_ACTIVATION_CONTRACT.md` §16. — Claude Code (Opus 5)
- **v0.2 (2026-08-20, Pass 2a):** Applied the parts that needed no new database. `Signal Type` 16 → 21 (adds School-Holiday · Sports · Mega-Event · Trade/Fashion · Cruise/Port, per §8); `Signal Role` created and set on 32 of 34 rows (§6 direction, at signal level); `Previous Signal Date` + `Change Reason` created (§7); the operating views built (§10); the Hospitality timing rules (§5.2) written as real activation dates on the Kenya pilot signals. **Diagnosis that drove it:** the calendar had been built for coverage, not operation — one anchor per sector, and a `Target` sub-sector whose only seasonality was destination-less and vendor-blog-sourced. The generic peak-season row was found to be *directionally wrong* for Kenya (northern-summer peak vs Kenya's Dec–Jan) and is now `Superseded/Delayed` with a reason, not deleted. §12's candidate pack is still unregistered — DB 14/15 do not exist. — Claude Code (Opus 5)
- **v0.1 (2026-08-19):** Created (Pass 1 — DECIDE). Specifies the source hierarchy, feed taxonomy + Google/Notion Calendar sync architecture, the Timing Rule table, the Market Direction doctrine, change-versioning, colour semantics, the demand-surge rule, the Control Tower read-view contract, sector generalization, and the Kenya-inbound candidate source pack. Reconciles the seeding proposal's ~17 calendars / 15 folders / 6 engines down to **2 net-new databases and this file**. Builds nothing — DB 14/15 and all source verification are Pass 2. — Claude Code (Opus 5)
