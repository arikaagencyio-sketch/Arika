# Live Sector Event Intelligence (LSEI) — Calendar Intelligence Spec

**Department:** Sector (01) · **Version:** v0.1 · **Created:** 2026-08-19
**Status:** **Specification only (Pass 1 — DECIDE).** Defines the model, the rules, and the candidate source pack. Builds nothing: DB 14/15 do not exist yet, no source has been verified, no Notion row has been written. Pass 2 applies it.
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

> 🔴 **Standing correction this file exists to fix.** The four Hospitality rows currently in DB 7 (Peak / Shoulder / Low season + Independent Hotel Show Miami) are sourced to hotel-tech marketing blogs at `T3` — a *vendor's* seasonality claim, not a destination authority's. They are **not deleted**: Pass 2 re-sources them to T1 and supersedes any claim the T1 source contradicts.

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

### 5.2 The rule table (seed — Hospitality)

Offsets are **derived planning offsets, never external facts** (Contract §12). They are configurable sector rules, not hardcoded assumptions, and are re-tuned as real outcomes accumulate in `01_Sector/_memory/runtime.jsonl`.

| Sector · Signal Type · Role | Strategic | Marketing | Sales | Offer | Revenue Watch | Action Deadline |
|---|---|---|---|---|---|---|
| Hospitality · `Event/Compression` · destination-side | T-180 | T-120 | T-90 | T-60 | T-30 | T-7 |
| Hospitality · `Seasonality` · destination-side | T-270 | T-180 | T-120 | T-90 | T-45 | T-14 |
| Hospitality · `Sales/MICE` · destination-side | T-365 | T-240 | T-180 | T-120 | T-60 | T-30 |
| Hospitality · `Holiday/School-Holiday` · **origin-side** | T-240 | T-150 | T-120 | T-90 | T-45 | T-21 |
| Hospitality · `Travel-Trade` (Arika's own attendance) | T-120 | T-90 | T-60 | T-45 | — | T-14 |
| Any sector · `Regulatory` | T-365 | T-180 | T-270 | T-180 | T-90 | T-30 |

**Two rules govern the table:**
- **Origin-side signals run on longer clocks than destination-side ones** — a German school holiday drives a booking decision months before the trip; a destination event compresses inventory closer in.
- **A row without a real research basis is left empty, not filled with a plausible number.** The Hospitality rows above derive from the pilot's booking-window research; the `Regulatory` row derives from the FSMA/CSRD worked examples. Other sectors get rows when their cross-loop is authored — **not before.**

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

**Current scope (owner decision, 2026-08-19): Kenya-inbound.** Pass 2 seeds `Germany → Kenya`, `UK → Kenya`, `US → Kenya`, and `Regional Africa → Kenya`. Outbound and Gulf routes are built when a real engagement requires them — not pre-populated as a world atlas.

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

> When a signal's date moves, the change MUST name the downstream work it invalidates: affected **Market Routes**, **Content Opportunities**, **campaign windows**, derived **activation dates**, and any **agency-calendar** entry computed from it.

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

---

## 12. Candidate source pack — Hospitality, Kenya-inbound

**Every row below is `state = candidate`.** Per `AEIT_08` §5, *a source enters `active` only after a live verification call proves it answers.* The material that seeded this file names many sources and specific claims (feed capabilities, event counts, revised dates); **none of it is transcribed here as fact.** Pass 2 verifies each against the live publisher, records the real `Feed Type` and ICS URL if one exists, and only then promotes it. The registry rows live in `AEIT_08` §3.2.

| Class | Candidates | Why |
|---|---|---|
| **T1 · Kenya destination authority** | Kenya Tourism Board / Magical Kenya events · Kenya public-holiday source (government gazette) · Kenya school-terms calendar (Ministry of Education) · KICC + Nairobi/Mombasa/Diani venue calendars | The destination-side spine. Public holidays and school terms are date-certain and directly move domestic + regional demand. |
| **T1 · Origin-market authority** | Germany public-holiday + **state-level** school-holiday calendars · UK equivalents · US federal holidays · regional-Africa holiday sources | The origin-side clock. German state school holidays are staggered by Land and are the single highest-value inbound-planning driver for a Kenya-inbound route. |
| **T1/T2 · Travel trade & MICE** | WTM Africa · Africa's Travel Indaba · AviaDev Africa · ITB · WTM London · HSMAI · ICCA · Cvent · AHLA | Where the *trade* meets — Arika's own attendance calendar and the client's MICE-demand calendar. Two different uses, one registry. |
| **T1 · Federations (the literal F1 model)** | FIA championship calendars · Safari Rally · World Athletics · major marathons | The reference case: an official body publishing a structured, amendable calendar. Verify per event — never assume a series' dates. |
| **T3 · Aggregators / event APIs** | Event-data providers · ticketing discovery APIs · trade-show directories | Breadth and machine-readability. **Registered candidate, paid/keyed, cost-gated** — same posture as the Tier-2 people-data set (`AEIT_08` §3.1). Discovery only; they never outrank the organizer (§2). |

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

`SECTOR_ACTIVATION_CONTRACT.md` §12 (SCIC) · §13 (Kernel) · §14 (Cross-Loop) · **§15 (LSEI doctrine)** · `SECTOR_NOTION_SCHEMA.md` DB 7 / 11 / 12 / 13 / **14 / 15** · `SECTOR_CALENDAR_REFRESH_SPEC.md` (cadence + escalation ladder) · `AEIT_08` §1 (Source entity) · §3.2 (the candidate pack) · §4 (Intelligence Calendar) · §5 (registration gate) · `13_Tech_Stack/TECHSTACK_OS.md` §3 (Google Calendar + Notion Calendar) · `08_Operations/OPERATIONS_OS.md` (the market-clock bridge into the 7 Cognitive Calendars) · `.claude/agents/sector-signal-refresher.md` (extended in Pass 2).

## 15. Changelog

- **v0.1 (2026-08-19):** Created (Pass 1 — DECIDE). Specifies the source hierarchy, feed taxonomy + Google/Notion Calendar sync architecture, the Timing Rule table, the Market Direction doctrine, change-versioning, colour semantics, the demand-surge rule, the Control Tower read-view contract, sector generalization, and the Kenya-inbound candidate source pack. Reconciles the seeding proposal's ~17 calendars / 15 folders / 6 engines down to **2 net-new databases and this file**. Builds nothing — DB 14/15 and all source verification are Pass 2. — Claude Code (Opus 5)
