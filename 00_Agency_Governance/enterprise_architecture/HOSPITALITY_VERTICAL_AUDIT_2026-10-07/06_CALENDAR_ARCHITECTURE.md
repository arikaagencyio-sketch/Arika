# 06 — Calendar Architecture and Destination Intelligence

**Protocol §11:** *"Do not assume there is only a content calendar"* — test fifteen calendar types, local + regional + international seasonality, and mismatched source-market seasons. **§12:** the destination chain *property → destination → city/county/region → country → East Africa → Africa → source market*.

---

## 1. What already exists — and the rule that governs it

The repository has a mature, explicit calendar doctrine. Its load-bearing rules:

- *"The calendar is not a store of content. It is a resolved view of live external reality, computed per sector, per geography, per property archetype, per client."* (`SECTOR_OS_ARCHITECTURE.md`, governing sentence)
- *"Never build a calendar per layer, per view, per sector, or per direction."* (`SECTOR_ACTIVATION_CONTRACT.md` §15; restated `CALENDAR_INTELLIGENCE.md` §13)
- *"The market clock is an input to the existing seven calendars. It is never an eighth."* (`08_Operations/OPERATIONS_OS.md:186`)
- The seeding proposal for this layer named **~17 calendar layers, a 15-folder domain and 6 engines**; it was reconciled down to **2 new databases and one specification** (`CALENDAR_INTELLIGENCE.md` §1). *The protocol's fifteen calendars should be read against that precedent.*

| Calendar system | Owner | Store / mechanism | Reality |
|---|---|---|---|
| **DB 7 Sector Signals** — the market clock: 21 `Signal Type`s, `Signal Role` (destination / origin / both), six activation dates, change versioning | Sector (01) | Notion DB 7 (34 rows at the 2026-08-20 count) | `LIVE` |
| **Resolution Engine layers** — Sector · Regional · Property-Type (views) · Client (resolution step) · Execution (Content DB 7) | Sector (01) | `SECTOR_OS_ARCHITECTURE.md` §4.2; skill S09 | `LIVE` (6 of 8 steps) |
| **Timing rules** — six offsets per Signal Type × Role (Strategic · Marketing · Sales · Offer · Revenue Watch · Action Deadline) | Sector plugin P7 | `plugin.config.json` | `BUILT`; Sports, Mega-Event, Cruise/Port, Aviation rows ⬜ unauthored |
| **The 7 Cognitive Calendars** — Revenue · Pipeline Probability · Operational · Cash Flow · Capacity · Opportunity · Strategic | Operations (08) | reasoned by `operations-calendar-orchestrator`; no store | `BUILT`; **never fired** (scheduler unapproved) |
| **Intelligence Calendar** — refresh, decay, revalidation rhythm | IntOS / Operations | `AEIT_08` §4 | `DESIGNED` |
| **Sector operating cadence** — daily · weekly · monthly · quarterly · yearly | Sector (01) | `SECTOR_CADENCE.md` | `DESIGNED` |
| **Editorial view** — `Target Publish Date` on Content DB 7 Briefs | Content (04) | Notion view | `BUILT`, empty |
| **Sales follow-up cadence** — Day 0/2/5/9/14/21/30 from the actual first send | Sales (05) | `PROSPECTING_CYCLE.md` step 7 | `DESIGNED`; 0 sends |
| **External follow layer** — ICS subscriptions via Google Calendar → Notion Calendar | Sector / Tech Stack | `CALENDAR_INTELLIGENCE.md` §3.1 | `DESIGNED` — *no registered publisher offers a feed* |

## 2. The protocol's fifteen calendars — mapped

| # | Calendar | Existing implementation | Store or view? | Class | Gap |
|---|---|---|---|---|---|
| 1 | Market | Layer 1 *Sector Calendar* = DB 7 filtered by Sub-Sector | view | **EXISTING** | — |
| 2 | Destination | Layer 2 *Regional Calendar* = DB 7 by Geography (ancestor chain ∪ subtree) + DB 16 `Seasonal Demand` / `Events` | view | **EXISTING** | Mombasa unprofiled → Destination Fit blocks it (31h) |
| 3 | Source-market | DB 7 `Signal Role = Origin-side` + DB 15 `Holiday / School-Calendar Overlap` | view | **EXISTING** (thin) | 5 routes; `Booking Lead Time` **blank on all five** (S05 run: *"TRI does not publish it"*) |
| 4 | Audience | — | — | **EXTEND** | Signals carry no audience/segment tag; DB 15 audience is free text → author a segment vocabulary in P3 and filter by it (**a view, never a store**) |
| 5 | Tourism seasonality | DB 7 `Seasonality` (destination-side) + plugin P13 | view | **EXISTING** | See §4 — country- vs destination-level seasonality needs verification |
| 6 | Property seasonality | Layer 3 *Property-Type Calendar* (P2 filter) + step 5 client context (inventory, blackout dates, capacity) | view + resolution | **EXISTING** | Step 5 never exercised (needs a real client); seasonal closure months only via intake H-A07 |
| 7 | Revenue | **Name collision**: Operations' *Revenue Calendar* is the **agency's** $35K/day heartbeat. A **hotel's** revenue calendar (pickup, occupancy, ADR) is plugin P13's ⚫ template layer | — | **METRIC GAP** (client side) | Client revenue timing exists only in client RMS/PMS — correctly never fabricated; no defined import path |
| 8 | Occasion | DB 7 `Holiday/Cultural`, `School-Holiday`, `Event/Compression`, `Mega-Event`, `Sports`; P5 `Weddings`, `Romance/Honeymoon` | view | **EXTEND** | Personal/corporate occasions (anniversaries, year-end, offsites, AGMs) absent → P3 `occasion` vocabulary |
| 9 | Experience | — | — | **EXTEND** (client instance) | A property's own scheduled experiences (a tournament, a wine dinner, a festive programme) have **no input home** until a client exists — they are step-5 client context, captured by intake, never a store |
| 10 | Campaign | Content DB 4 `Start / End`; DB 15 `Campaign Window` (derived, *"a planning offset, not an external fact"*); P7 Marketing offsets | store field + derivation | **EXISTING** (partial) | DB 4 has no status (`HV-08`) |
| 11 | Production | Content DB 7 `Target Publish Date`; Draft 41 Phase 7 lead times; Design has no schedule | partial | **EXTEND** (view) | No production-schedule view; `Packet State` reserved but unused |
| 12 | Distribution | Presence `Packet State` (`scheduled → published`); Postiz | designed | **EXTEND** | Nothing scheduled or published; 0 channels connected |
| 13 | Sales | P7 Sales offsets; Operations *Pipeline Probability Calendar*; P13 "low season is Arika's buying window"; follow-up cadence | rules + agent | **EXISTING** | Not carried into the prospecting record (`HV-36`) |
| 14 | Client | Resolution step 5 — *"No client calendar exists until a real client does. Structure may be empty; it may not be guessed."* (`SECTOR_OS_ARCHITECTURE.md` §4.2) | resolution | **EXISTING** (by design) | — |
| 15 | Measurement | KPI dictionary cadences; Draft 41 D7 monthly; M6 seasonally comparable baseline; S5 cadence (blocked) | rules | **EXTEND** | No client measurement cadence while S5 is blocked; baseline design open (worksheet §8 #22) |

**Reading (`CONFIRMED`):** **eight of fifteen exist** as views, resolutions or rules over one canonical store; **six need extension, not new stores**; **one** (a client's revenue calendar) is a metric gap that only client systems can fill. Not one of the fifteen justifies a new calendar database. The only genuinely missing *inputs* are client-owned events and a guest-segment/occasion vocabulary — both client-instance or plugin values.

Calendars the protocol did not list but the OS already runs: the **7 Cognitive Calendars**, the **Intelligence Calendar**, the **sector cadence**, the **Presence account warm-up stages** (S0–S6), and — notably — **Arika's own travel-trade attendance clock** (plugin P7 row *"Travel-Trade (Arika's own attendance)"*, T-120 → T-14), which is a self-marketing calendar the agency already has rules for (file 09 §4).

## 3. Local + regional + international seasonality, and mismatched source markets

The protocol's example — *North American summer ≠ East African summer; European winter planning creates East African demand in a different local season* — is **the exact case this architecture was built for**, and it is the most rigorously evidenced part of the repository.

| Capability | Mechanism | Evidence | State |
|---|---|---|---|
| A signal sits on one side of a route | `Signal Role` = `Destination-side` · `Origin-side` · `Both` (Ramadan is *Both, and means opposite things on each side*) | `CALENDAR_INTELLIGENCE.md` §6.1 | `LIVE` (set on 32 of 34 rows at application) |
| Direction is a property of the engagement, not the calendar | *"A Kenyan lodge selling to German travellers and a Dubai hotel selling to African travellers consume the same signal store through different routes."* | §6.2 | doctrine |
| Origin-side signals run on longer clocks | P7: `Holiday/School-Holiday · origin-side` = T-240 strategic … T-21 deadline; destination events T-180 … T-7 | plugin P7 | `BUILT` |
| Different destinations, different source markets | Gate F run 3: **Maasai Mara and Diani draw from completely disjoint origin markets** (US/UK long-haul via the capital vs Italy/Germany, with Italy landing 72 % directly at the coast airport) | GLOBAL_OS v0.25.0; DB 15 sourced to the 2025 national tourism research report | `LIVE` |
| Hemisphere correction | A generic peak-season row asserting a northern-summer peak was found *directionally wrong for Kenya* and superseded, not deleted | plugin P8 "standing correction" | `LIVE` |
| A suppression is also a move | A Kenyan public holiday **empties** a Nairobi conference hotel while **releasing** domestic leisure | plugin P2, `City / Conference Hotel × Holiday/Cultural` | `BUILT` (owner_reasoning) |

**Verdict:** temporal intelligence for mismatched source markets is **supported in architecture and partly in data** (`CONFIRMED`). What limits it is **coverage, not design**: five routes, three profiled destinations, P7 rows unauthored for four signal types, no lead times on any route, origin-side source registration status not enumerated in the files read (`UNKNOWN` — see `HQ-06`), and Gate H (*does a moved date version and name what it invalidates?*) unrun.

## 4. ⚠️ A modelling risk worth verifying before any client calendar

Draft 41 deliverable **D3** sets as its quality standard: *"Uses destination seasonality (Plugin P8: **Kenya's peak is Dec–Jan**, not a northern-hemisphere summer)."* That statement is made at **country** level. Meanwhile plugin P2 rules `Safari Lodge × Seasonality` as *"If lodge occupancy does not track the **migration/wildlife calendar**, the sector's core seasonality model is wrong"*, and P5 assigns Maasai Mara the theme `Seasonal Migration`.

Because the Resolution Engine scopes a place by its **ancestor chain ∪ subtree** (`SECTOR_OS_ARCHITECTURE.md` §4.1, corrected 2026-08-28), *a country-level seasonality signal is inherited by every Kenyan destination*. If a country-level "peak = Dec–Jan" signal and a destination-level migration season both resolve for a safari property, the calendar either double-counts or contradicts itself, and D3's quality check would mark a correct migration-season calendar as a defect.

**Status: `UNKNOWN — HUMAN INPUT REQUIRED` / research.** This audit did not open DB 7 rows and makes no claim about Kenyan seasons. The check is: confirm against a T1 destination source whether safari-circuit seasonality differs from the coast's, and if so (a) scope seasonality signals at `Destination` rather than `Country` level and (b) restate D3's quality standard per destination. → `HQ-05`, `HV-24`.

## 5. Destination intelligence chain (protocol §12)

| Level | Representation (DB 11 `Level`) | Live rows | Gap |
|---|---|---|---|
| Property | `Property (template level)` in DB 11 **and** CRM `Company` | none | Property's home undecided (A001 AG-10, `HD-11`) |
| Destination | `Destination` (added 2026-08-20) + DB 16 profile | Maasai Mara, Diani (profiled), Nairobi (City, profiled) | Mombasa unprofiled |
| City | `City` | Nairobi, Mombasa | — |
| County | **no level** | — | Not modelled (Kenyan counties) — add only if a real engagement needs it (lean-tree rule) |
| Region / East Africa | `Region` level exists | **no East Africa row** — the live chain is `Global → Africa → Kenya` | Regional (EAC) demand and Uganda→Kenya land route have no intermediate node |
| Country | `Country` | Kenya + origin countries (Germany, UK, Italy, Uganda, US) | — |
| Africa / Global | `Region` / `Global` | Africa, Global, European Union | — |
| Source market | DB 15 route origins | 5 directed routes | Lead time blank; scope = Kenya-inbound only (owner decision 2026-08-19) |

| Association asked for | Where it lives | State |
|---|---|---|
| Travel patterns / tourism flows | DB 15 routes (arrivals by nationality and port of entry, 2025 report) | `LIVE` (5 routes) |
| Source markets | DB 15 + DB 11 origin nodes | `LIVE` |
| Languages | DB 6 = **buyer** language (Plane A); DB 15 `Preferred Channels / Messaging` text | **Guest-language / localisation absent** (German, Italian, French content for origin markets) |
| Cultural occasions | DB 7 `Holiday/Cultural` | `LIVE` |
| Holidays | Kenya public holidays from statute (Kenya Law, T1); origin holidays are P8 candidates | Kenya `LIVE`; origin registration `UNKNOWN` |
| School calendars | Kenya's Ministry of Education and Ministry of Interior hosts were both refused at registration for expired certificates (2026-08-24); *"a ministry"* was later re-tested and promoted (v0.23.0) — **which one is not stated** in the files read. German *Land* school holidays are named the *"single highest-value inbound-planning driver"* (plugin P8) | Kenya `UNKNOWN`; Germany `UNKNOWN` (`HQ-06`) |
| Climate | Seasonality + `Risk/Disruption` (weather) | Partial — no climate/rains model as such |
| Flight / connectivity | DB 15 `Air Connectivity`; `Aviation/Connectivity` signal type; KCAA + KAA registered (zero cost, v0.23.0) | Partial — P7 aviation offsets unauthored |
| Destination events | DB 7 `Event/Compression`, `Mega-Event`, `Sports`; travel-trade shows | Partial — Nairobi corporate/MICE claims **refused** without a registered commercial source (item 31j) |
| International planning windows | P7 origin-side offsets; DB 15 `Campaign Window` | `BUILT`; route lead times blank |

## 6. What not to build

- **No fifteen calendar stores.** Each new calendar the protocol names is a filter, a resolution step or a client input over DB 7 / DB 15 / DB 16 (§2).
- **No "Revenue Calendar" for clients under that name** — it collides with the agency's own Revenue Calendar; call the client-side layer by its contents (pickup, occupancy) and keep it ⚫ client-sourced.
- **No eighth agency calendar.** Reword `AEIT_08` §4's "intelligence-specific 8th rhythm" to "a refresh rhythm that feeds the seven" (`HV-23`).
- **No unattended ingestion.** Cloud routines have no web access (verified 2026-08-11); "live" means a freshness cadence (`CALENDAR_INTELLIGENCE.md` §4).
