# AEIT_08 — Agency Global Source Registry & Intelligence Calendar (Blueprint)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** `GLOBAL_OS.md` §11 item 1 — *Agency Global Source Registry (source IDs, active/superseded/
archive state, owners, cadence)* — the longest-standing **Open** gap.
**Status:** **Specification only.** Defines the registry schema + the refresh discipline. Does **not**
populate sources (that arrives with IntOS activation). Illustrative rows are labelled as examples.

> The repo already has a **tool/connector inventory** (Tech Stack 13) and a **CRM object model**
> (Governance). What it lacks is a registry of *where intelligence comes from* — the inputs to IntOS.
> This is that registry's design.

---

## 1. Source entity schema

Every source is one row keyed by a stable `source_id`. Fields (extends the `Source` entity in
`AEIT_06`):

| Field | Type | Meaning |
|---|---|---|
| `source_id` | id | stable, never reused |
| `name` | text | human name |
| `category` | enum | see §2 |
| `access_method` | enum | official-API / public-API / registry / scrape / RSS / MCP / manual / AI-assisted |
| `trust` | 1–5 | how much we trust its claims (drives IntOS trust score) |
| `coverage` | text | what entities/topics it covers |
| `latency` | enum | realtime / daily / weekly / on-demand |
| `freshness` | date | **last verified** (not "added" — per `TECHSTACK_OS.md:152` discipline) |
| `legal` | enum + note | ToS/robots/PII posture → Legal (10) sign-off flag |
| `auth` | enum | none / key / oauth / account |
| `rate_limits` | text | calls/window |
| `cost` | text | free / metered / subscription (runway in units) |
| `fallback` | source_id | what to use if this fails |
| `consumers` | dept[] | who relies on it |
| `cadence` | cron-ish | how often it is collected/revalidated (→ §4) |
| `owner` | dept | single owning department |
| `state` | enum | **active / superseded / archived** (with supersession chain) |

---

## 2. Source categories (coverage of the input universe)

Official APIs · Public APIs · Public/government registries · Research platforms · Social networks ·
Search engines · Company websites · RSS · Forums · Communities · Directories · News · Technical
documentation · Public repositories · Knowledge bases · Browser automation · Scraping platforms ·
Search platforms · Manual collection · AI-assisted collection.

Each registered source declares its category; the category informs default `trust`, `legal`, and
`access_method`.

---

## 3. Illustrative rows (EXAMPLES — not a populated registry)

Drawn only from what the repo already confirms exists, to show the schema in use. Real population is
deferred.

| source_id | name | category | access | trust | state | owner |
|---|---|---|---|---|---|---|
| `src_sector_xlsx` | Owner-curated SaaS taxonomy (xlsx) | Knowledge base | manual | 5 | active | Sector (01) |
| `src_clickup_crm` | Agency CRM (ClickUp) | Official API | account | 5 | active | Governance (00) |
| `src_zoho_books` | Zoho Books (invoicing) | Official API | account | 4 | active* | Finance (09) |

\* `src_zoho_books` illustrates two live findings: it is **missing from the DPA sub-processor
register** and its **trial expired** (`AEIT_04 §D1`) — exactly the kind of drift the registry's
`legal` + `freshness` fields exist to catch.

---

## 3.1 Registered intelligence sources — Sector Commercial Activation MCP stack *(added 2026-08-19)*

First **real** (non-illustrative) registration, driven by Sector (01)'s commercial-activation phase
(plan ADDENDUM 4). Split by PII/Legal exposure — the honest line between what runs now and what is
gated. Every row names its **`consumers`** (destination DB) per the decision-purpose gate
(`SECTOR_ACTIVATION_CONTRACT.md` §13.3): **no source without a downstream home.**

**Tier 1 — Market / web intelligence (non-PII; lower Legal risk).** *For the single-sector pilot the
"web researcher" is the interactive Claude Code session itself — `WebSearch`/`WebFetch` are already
available and sufficient. The scraping MCPs below are registered for when we generalize across many
sub-sectors/companies, not for the pilot.*

| source_id | name | category | access | trust | cost | consumers | state |
|---|---|---|---|---|---|---|---|
| `src_web_builtin` | Interactive WebSearch/WebFetch | Search/Browser | MCP/AI-assisted | 3 | free | Sector Signals · Intelligence · Linguistics · DM-titles · Tool-Stack | **active** (verified in session) |
| `src_firecrawl` | Firecrawl (scrape-first; keyless tier) | Scraping platform | MCP | 3 | free tier / metered | Sector Intelligence · company-website reads · DM-title pages | registered — stand up at generalization |
| `src_tavily` | Tavily (ranked web search) | Search platform | MCP | 3 | free tier / metered | Sector Signals · Intelligence | registered — stand up at generalization |
| `src_exa` | Exa (semantic search) | Search platform | MCP | 3 | metered | Sector Signals · Intelligence | registered (alt to Tavily) |
| `src_perplexity` | Perplexity (cited synthesis) | Research platform | MCP | 3 | metered | Sector State / Forecast summaries | registered — optional |
| `src_fetch` | Fetch (URL fallback) | Browser automation | MCP | 2 | free | any | registered — fallback |

**Tier 2 — People / contact data (PII; paid; Legal-gated; DEFERRED).** Provides real decision-maker
names/emails/dials → CRM. **Not connected.** Enters `active` only after a Legal (10) posture note
(ToS/robots/PII/GDPR) + a live verification call + cost governance + an Approval-Matrix row
(`AEIT_07`/`AEIT_10`; §5 below).

| source_id | name | category | access | trust | cost | consumers | state |
|---|---|---|---|---|---|---|---|
| `src_apollo` | Apollo.io (contact DB + enrichment + sequences) | Directory/API | MCP | 4 | paid | CRM `Lead` · Decision-Maker Registry (named people) | **registered — GATED (Legal + cost)** |
| `src_clay` | Clay (waterfall enrichment, 150+ providers) | Data platform | MCP | 4 | paid | CRM `Lead` enrichment | **registered — GATED (Legal + cost)** |
| `src_cognism` | Cognism (EU verified dials/emails) | Directory/API | MCP | 4 | paid | CRM `Lead` (EU/GDPR region) | **registered — GATED (Legal/GDPR)** |

**Honesty (carried from `SECTOR_ACTIVATION_CONTRACT.md` §14.5):** cloud routines have **no web** —
collection is interactive/human or a gated runtime; **no unattended scraper daemon**. Tier-1 sources
read public, non-PII pages; Tier-2 sources touch personal data and stay gated until Legal signs the
posture. The paid people-data MCP is authorized by the owner **after** the Hospitality pilot proves
the loop.

---

## 3.2 Event-calendar source pack — Hospitality, Kenya-inbound *(added 2026-08-19 · LSEI Pass 1)*

The **live external calendars** the Sector Signals layer follows — the layer that was missing when
`Authoritative Source` was free text on a Notion row. Design: `01_Sector/CALENDAR_INTELLIGENCE.md`;
doctrine: `SECTOR_ACTIVATION_CONTRACT.md` §15. These rows will be **mirrored into the Sector-owned
`Signal Sources` DB (DB 14)** — which conforms to the §1 schema above rather than rivalling it.

> 🔴 **Every row below is `state = candidate`.** Per §5, *a source enters `active` only after a live
> verification call proves it answers.* The owner's seeding material named many publishers and made
> specific claims about them (ICS availability, API capabilities, event counts, revised dates).
> **None of it is transcribed here as fact, and no URLs are recorded yet** — a URL written from
> memory is exactly the fabrication this registry exists to prevent. Pass 2 locates and verifies each
> publisher's real calendar, records the actual `Feed Type` (and ICS/API endpoint **only if one
> genuinely exists**), then promotes the row.

**Scope discipline.** The pack is **Hospitality → Accommodation, Kenya-inbound only** (owner decision
2026-08-19). Other destinations, outbound routes, and other sectors get source rows when their
cross-loop is authored — never pre-populated (`SECTOR_ACTIVATION_CONTRACT.md` §14.1).

> ✅ **The Sector-owned mirror now exists** *(2026-08-20).* **DB 14 Signal Sources** was built live in Notion (`collection://13741534-e31d-4ff8-bebf-dd50133e20af`) conforming to the §1 Source entity schema — `Authority Level`, `Feed Type`, `Cadence`, `State`, `Legal Posture`, `Auth`/`Cost`, `Consumers`, and a `Supersedes`/`Superseded By` chain. **It held 0 rows until 2026-08-24; it now holds 4** — the first sources ever registered in this agency, written by Sector skill `sector-source-registrar` (S03). **The §5 registration gate has now been exercised, and it bit.** Of four Kenya destination-authority sources called live: **2 promoted to `active`** — Kenya Tourism Board / MKTE (`src_ktb_mkte`) and Kenya Law / Public Holidays Act Cap. 110 (`src_ke_public_holidays`), each verified from the publisher's own site — and **2 held at `candidate`** because `www.education.go.ke`, `education.go.ke` and `www.interior.go.ke` all returned **`certificate has expired`**. Both are unimpeachably T1 publishers and neither could be promoted, which is the gate working as designed: **`Authority Level` describes the publisher, `State` describes whether we can actually follow it, and they are different axes.** **`Feed URL (ICS/API)` is blank on all four** — not one publishes an ICS or an API, and none was invented. A table that can hold sources is not a registry of sources; four rows is a start, not a registry either.

> 📌 **Ownership of the *selection*** *(added 2026-08-20).* This registry is the canonical home of the
> **source rows** — that is `AEIT_08`'s job, agency-wide. But **which** sources a sector needs, and
> **why** each class matters for its demand model, is **sector plugin content**: slot **P8** of the
> 14-slot Sector Plugin Interface (`01_Sector/SECTOR_OS_ARCHITECTURE.md` §3), authored in
> `01_Sector/sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`. The rows below stay here; the
> reasoning that selects them lives in the plugin, so a second sector adds a pack rather than editing
> this file's rationale. Doctrine: `SECTOR_ACTIVATION_CONTRACT.md` §16.

**Tier 1 — Destination authority (Kenya).** The destination-side spine.

> **Registration pass 1 — 2026-08-24.** Four rows written; **2 active, 2 candidate**. Two refinements this pass made to the plan above, both worth carrying. **(1) `src_ke_public_holidays` was split in two.** The *statute* (Cap. 110) fixes the recurring dates and is reachable; only a *Gazette notice* can add or move a holiday in a given year, and that is a different publisher on a different cadence (`event-driven`, not `annual`). One source row could not honestly carry both. **(2) `src_ke_tourism_events` was NOT satisfied by `src_ktb_mkte`.** KTB's own expo is one event; the tourism authority's full events calendar is a broader source still unlocated. Registering the narrow one does not close the broad one — kept as two rows so the gap stays visible.

| source_id | Publisher (the body that owns it) | category | consumers | state |
|---|---|---|---|---|
| `src_ke_tourism_events` | Kenya's national tourism authority — official **events calendar** (the full calendar, still unlocated) | Tourism board/DMO | Sector Signals · Sector State | **candidate** |
| `src_ktb_mkte` | **Kenya Tourism Board — Magical Kenya Travel Expo** *(added 2026-08-24)* | Tourism board/DMO | Sector Signals | ✅ **active 2026-08-24** |
| `src_ke_public_holidays` | **Kenya Law (National Council for Law Reporting)** — Public Holidays Act Cap. 110 | Government registry | Sector Signals (`Holiday/Cultural`) · Market Routes | ✅ **active 2026-08-24** |
| `src_ke_gazette` | **Ministry of Interior** — Kenya Gazette holiday declarations *(split out 2026-08-24)* | Government registry | Sector Signals | **candidate** — TLS cert expired |
| `src_ke_school_terms` | Kenya Ministry of Education — school term dates | Education ministry | Sector Signals (`School-Holiday`) · Market Routes | **candidate** — TLS cert expired |
| `src_ke_venues` | Nairobi/Mombasa/Diani conference + venue calendars (KICC and peers) | Venue | Sector Signals (`Sales/MICE`) | **candidate** |

**Tier 1 — Origin-market authority (the source markets for Kenya inbound).** The **origin-side**
clock — the half the previous model had no way to express. German school holidays are staggered by
*Land* and are the highest-value inbound-planning driver on this route set.

| source_id | Publisher | category | consumers | state |
|---|---|---|---|---|
| `src_de_holidays_school` | Germany — federal public holidays + **state-level** school-holiday calendars | Government registry | Sector Signals · Market Routes (`Germany → Kenya`) | **candidate** |
| `src_uk_holidays_school` | UK — bank holidays + school term dates | Government registry | Sector Signals · Market Routes (`UK → Kenya`) | **candidate** |
| `src_us_holidays` | US — federal holidays | Government registry | Sector Signals · Market Routes (`US → Kenya`) | **candidate** |
| `src_africa_regional_holidays` | Regional-Africa public-holiday sources (per country, as routes are added) | Government registry | Sector Signals · Market Routes (`Regional Africa → Kenya`) | **candidate** |

**Tier 1/2 — Travel trade & MICE.** Two distinct uses, one registry: Arika's **own** attendance
calendar, and the client's **MICE-demand** calendar. `Signal Role` separates them.

| source_id | Publisher | category | consumers | state |
|---|---|---|---|---|
| `src_wtm_africa` · `src_indaba` · `src_aviadev` | African travel-trade show operators | Trade body | Sector Signals (`Travel-Trade`) | **candidate** |
| `src_itb` · `src_wtm_london` | Global travel-trade show operators | Trade body | Sector Signals (`Travel-Trade`) | **candidate** |
| `src_hsmai` · `src_icca` · `src_ahla` · `src_cvent` | Hospitality-industry + business-events associations | Trade body | Sector Signals (`Sales/MICE`) · Offer (02) | **candidate** |

**Tier 1 — Federations (the literal F1 model).** The reference case for this whole design: an
official body publishing a structured, **amendable** calendar that an ecosystem synchronizes off.

| source_id | Publisher | category | consumers | state |
|---|---|---|---|---|
| `src_fia_calendars` | FIA — championship calendars (the pattern-setter; amendments are published) | Federation | Sector Signals (`Sports`) | **candidate** |
| `src_ke_motorsport` · `src_athletics` | The bodies running the events that actually compress the Kenyan/regional market (rally, athletics, major marathons) | Federation | Sector Signals (`Sports` · `Event/Compression`) | **candidate** |

⚠️ **Verify per event, never per series.** A championship calendar is the *publisher's* current
statement, not a guarantee; the FIA's own calendars carry in-season amendments. That is precisely why
`Previous Signal Date` + `Change Reason` exist (`SECTOR_CALENDAR_REFRESH_SPEC.md` §2b).

**Tier 3 — Aggregators / event APIs.** Breadth and machine-readability. Same posture as the §3.1
Tier-2 people-data set: **registered, not connected.**

| source_id | Publisher | category | consumers | state |
|---|---|---|---|---|
| `src_event_api_predicthq` · `src_event_api_ticketmaster` | Event-data / ticketing discovery APIs | Event API | Sector Signals (discovery only) | **candidate — GATED (cost + key + capability unverified)** |
| `src_tradeshow_directories` | Trade-show / event directories | Aggregator | Sector Signals (discovery only) | **candidate — GATED** |

🔒 **Discovery only.** A T3 aggregator may surface that an event exists; the dated record must then
be sourced to the T1/T2 publisher before it is `Confirmed`, and an aggregator **never outranks the
organizer** (`CALENDAR_INTELLIGENCE.md` §2). Their claimed capabilities — ICS/API coverage, event
counts, demand-surge scoring — are **unverified** and must be proven with a live call before any
spend is approved (`techstack-cost-guardian` + an Approval-Matrix row).

**Standing correction this pack exists to fix.** The Hospitality signals currently in the live DB are
sourced to hotel-technology **marketing blogs** at `T3` — a vendor's seasonality claim, not a
destination authority's — and `Source Tier` is null on 20 of the 28 rows. Pass 2 re-sources them to
T1 and supersedes any claim a T1 publisher contradicts. **Nothing is deleted.**

---

## 4. The Intelligence Calendar (refresh / decay / revalidation)

Information is dynamic; **nothing is assumed permanently correct.** This is an operational rhythm
that sits alongside the existing 7 Cognitive Calendars (it is the intelligence-specific 8th rhythm,
owned jointly by IntOS and Operations' calendar-orchestrator).

| Mechanism | Rule |
|---|---|
| **Scheduled refresh** | Each source's `cadence` drives routine re-collection. |
| **Event-based refresh** | A `Signal/Event` (`AEIT_06`) about an entity forces re-collection of related knowledge. |
| **Risk-based refresh** | Higher-risk-class decisions demand fresher, higher-trust knowledge before acting. |
| **Confidence decay** | Confidence declines with age; below a threshold, the Knowledge Object returns to **Revalidate** (SM4). |
| **Staleness detection** | `freshness` older than the source's max-age flags the object stale. |
| **Change detection** | Diff against last snapshot; a change emits a `Signal`. |
| **Revalidation** | Re-run verification; update trust/confidence; log to Learning memory. |
| **Learning loop** | Sources whose claims proved wrong lose trust; the registry self-corrects. |

**Anchor discipline:** every knowledge claim carries a **last-verified date**, generalizing the
convention Tech Stack adopted after its inventory rotted undetected (`TECHSTACK_OS.md:152`) and
Automation adopted after the 11-day outage (`AUTOMATION_OS.md:152`).

---

## 5. Governance of the registry

- **Registration gate:** a source enters `active` only after a **live verification call** proves it
  answers — mirroring `techstack-inventory-registrar`'s "verify, don't assume" rule. No source is
  registered on faith.
- **Legal boundary:** any `scrape`/`browser-automation` source requires a Legal (10) posture note
  (ToS/robots/PII) before `active`. This is a Class-2+ gate.
- **Supersession, not deletion:** replaced sources move to `superseded` with a pointer to their
  successor; the chain stays auditable (the repo's existing supersession pattern).

---

## 6. What is deferred
- **Population.** No real sources are catalogued here beyond the three illustrative rows.
- **Collector code.** Connectors are built in the IntOS Collection layer post-activation (`AEIT_10`).

## 7. Decision Log
- **2026-07-22 — Source Registry + Intelligence Calendar specified.** Closes the design of
  `GLOBAL_OS.md` §11 item 1; schema includes active/superseded/archived state + last-verified
  freshness + legal boundary gate. — Claude Code (Opus 4.8)
- **2026-08-19 — First real sources registered (§3.1), driven by Sector commercial activation
  (ADDENDUM 4).** The registry moves from spec-only to holding a live Tier-1 source (`src_web_builtin`,
  verified active) + a registered-but-not-connected web-research MCP stack (Firecrawl/Tavily/Exa/
  Perplexity/Fetch) + a **gated** Tier-2 people-data set (Apollo/Clay/Cognism, Legal+cost gate). Every
  source names its `consumers` DB (decision-purpose gate). Population is still narrow (Sector's stack);
  other departments' sources remain deferred. — Claude Code (Opus 4.8)

- **2026-08-19 — Event-calendar source pack registered as candidates (§3.2), driven by Sector's LSEI
  Pass 1.** The first sources registered for *following an external calendar* rather than for
  research or enrichment. Covers Kenya destination authority, the origin-market holiday/school
  calendars that drive Kenya-inbound demand, travel-trade + MICE bodies, sports federations (the
  FIA-calendar pattern this design is modelled on), and gated event APIs. **Every row is
  `candidate`; no URLs recorded and no capability claimed** — the §5 registration gate is the whole
  point, and the seeding material's claims are unverified. Also confirms this registry's §1 schema
  is the parent of the Sector-owned `Signal Sources` DB (DB 14), not a rival to it. — Claude Code (Opus 5)

## 8. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
- **v0.2 (2026-08-19):** Added §3.1 — the Sector Commercial Activation MCP stack (Tier-1 market/web
  now; Tier-2 people-data gated). First non-illustrative rows. — Claude Code (Opus 4.8)
- **v0.3 (2026-08-19):** Added §3.2 — the Hospitality/Kenya-inbound event-calendar source pack, all
  `candidate`. Extends the registry from *how we research* to *which calendars we follow*. — Claude Code (Opus 5)
