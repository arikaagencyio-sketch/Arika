# Hospitality — Sector Plugin #001

**Sector:** Hospitality (vertical) → **Accommodation (Hotels)** (sub-sector, `Status = Target`)
**Interface:** [`../../SECTOR_OS_ARCHITECTURE.md`](../../SECTOR_OS_ARCHITECTURE.md) §3 — the 14-slot Sector Plugin Interface
**Status:** Gate 1 (DECIDE) — **config pack only. No *rows* from this file have been written to Notion.**

> ⚠️ **Precision correction (2026-08-24).** This line previously read *"Nothing in this file has been written to Notion,"* which is not accurate. **Two of this pack's vocabularies are already live Notion option sets** on DB 16 Destination Profile — `Demand Themes` (23 options, slot **P5**) and `Asset / Property Archetypes` (10 options, slot **P2**) — each stamped `PLUGIN-SUPPLIED VOCABULARY (slot Pn)` in its own Notion field description. They arrived with the Gate 2 schema apply, because a select option set *is* schema. **No rows exist**; the vocabularies do. The distinction matters: the blanket claim read as though the plugin had had no effect on the workspace.
**Version:** v0.1 (2026-08-20)

> **What this file is.** A **doctrine/config pack**, not runtime code. The word "plugin" here is deliberately *not* the repo's runtime sense (`finos-plugin`, `bois`, which are executable) — hence the directory `sector_plugins/`, not `plugins/`. This pack supplies **values** into Universal Core fields. It **MUST NOT** create a store, a field, an agent, or an event.

> **What this file is not.** A second copy of the pilot. Work already live in Notion (signals, findings, linguistics, audience roles, decision-maker titles, the entry offer) is **referenced by its owning store**, never re-typed here. Re-typing upstream truth downstream is the duplication the architecture exists to end.

**Honesty legend:** 🟢 web-cited · 🟡 owner-curated (hypothesis) · 🔴 gated (paid/PII/Legal) · ⚫ template (needs a client system) · ⬜ unauthored · ◐ partial (some authored and cited; a named sub-layer explicitly ⬜)

**Machine-readable sidecar:** [`plugin.config.json`](plugin.config.json) carries the mechanically-read slots — **P2** (the signal→archetype rule matrix), **P5** (demand-theme vocabulary), **P6** (signal-type weighting), **P7** (activation offsets) and **P13** (compression threshold). It is **derived from this file**, which stays the source of truth; if the two disagree, the markdown wins and the JSON is regenerated. It exists because `SECTOR_OS_ARCHITECTURE.md` §4.1 steps 4 and 6 require the Resolution Engine to *read* P2 and P7, and a markdown table cannot be read by a procedure. It creates no store, field, agent or event — it is a representation change, not a new value.

---

## Slot status at a glance

| Slot | Content | State |
|---|---|---|
| P1 Ontology | ✅ authored | 🟢 loaded in DB 1/2 |
| P2 Property-type rules | ✅ authored **here** | 🟡 owner-curated — **new this pass** |
| P3 Demand model | ◐ partial | 🟢 4 findings live · demand-pattern layer ⬜ |
| P4 Geography scope | ✅ authored | 🟢 10 Geography rows live |
| P5 Destination themes | ✅ vocabulary authored **here** | 🟡 assignments are hypotheses |
| P6 Signal-type profile | ✅ authored **here** | 🟡 |
| P7 Timing rules | ✅ **migrated here** | 🟢 derived from pilot booking-window research |
| P8 Source pack | ✅ **migrated here** | 🔴 every row `candidate` — unverified |
| P9 Audience + DMs | ✅ authored | 🟢 roles/titles live · 🔴 named people gated |
| P10 Linguistics | ✅ authored | 🟢 live in DB 6 |
| P11 Offer ladder | ✅ authored | 🟡 entry offer is a Working Hypothesis seed, unpriced |
| P12 Content pillars | ◐ partial | 🟢 3 opportunities live · pillar/angle set ⬜ |
| P13 Seasonality + compression | ✅ authored **here** | 🟡 threshold inherited from core default |
| P14 KPI semantics | ✅ authored **here** | 🟡 |

---

## P1 — Ontology

| Level | Value | Where it lives |
|---|---|---|
| Vertical | **Hospitality** — `Atlas Layer = Established`, `Industry Type = A (Marketing-driven)`, `Priority Tier = T1`, `Sector Priority Score = 78` (**P1 Pursue now**) | DB 1 Sectors Master |
| Sub-sector (pilot) | **Accommodation (Hotels)** — `Status = Target`, the repo's first `Target` sub-sector | DB 2 Sub-Sectors |
| Business models | Independent property · group/chain-affiliated · owner-operated · management-contract · franchise | DB 2 `Business Model` |
| Company archetype (pilot) | 30–100 room independent property | DB 2 `Company Archetype` |
| Tool-stack chaos | 🔴 **Extreme**, `Fragmentation Type = Integration`; characteristic stack: PMS · CRS · channel manager · RMS · CRM · POS · booking engine | DB 2 tool-stack field group |

**Second sub-sector** in the established atlas (`Hospitality` carries 2 division-level industries) is **not** authored — depth-first rule: it gets plugin rows when its cross-loop is authored.

---

## P2 — Entity/asset typology + property-type rules ★ new this pass

**The Entity Registry is the ClickUp CRM `Company` object.** A property, a group, a parent and a subsidiary are all `Company` with roles and relationships (`AEIT_06`: *"Prospect/Client/Partner/Competitor are roles, not types"*). This plugin does **not** create a property store; it supplies the **archetype vocabulary** and the **rule that says which signals move which archetype's demand** — the property-type calendar layer (`SECTOR_OS_ARCHITECTURE.md` §4.1 step 4).

**Archetype vocabulary** (🟡 owner-curated, from the owner's sector brief):

`City / Conference Hotel` · `Business Hotel` · `Beach Resort` · `Safari Lodge` · `Tented Camp` · `Boutique Property` · `Serviced Apartment` · `Villa` · `Destination Property` · `Hospitality Group` (a parent, not a bookable unit)

**The property-type rule** — which `Signal Type` values materially move each archetype's demand. This is the filter, not a description:

| Archetype | Signals that move it | Signals that largely do not |
|---|---|---|
| City / Conference Hotel | `Sales/MICE` · `Event/Compression` · `Trade/Fashion` · `Mega-Event` · `Regulatory` (corporate travel policy) | `School-Holiday` (origin-side leisure) · `Cruise/Port` |
| Business Hotel | `Sales/MICE` · `Aviation/Connectivity` · `Economic` · `Event/Compression` | `Seasonality` (leisure) · `Sports` |
| Beach Resort | `Seasonality` · `School-Holiday` (origin **and** destination) · `Holiday/Cultural` · `Cruise/Port` · `Mega-Event` | `Sales/MICE` (secondary) · `Trade/Fashion` |
| Safari Lodge / Tented Camp | `Seasonality` (wildlife/migration) · `School-Holiday` (**origin-side**, long lead) · `Aviation/Connectivity` · `Risk/Disruption` | `Sales/MICE` · `Cruise/Port` · `Trade/Fashion` |
| Boutique Property | `Event/Compression` · `Consumer-Behaviour` · `Holiday/Cultural` | `Sales/MICE` |
| Serviced Apartment | `Sales/MICE` (extended stay) · `Economic` · `Regulatory` | `Seasonality` (leisure) · `Sports` |
| Villa | `School-Holiday` · `Holiday/Cultural` · `Seasonality` | `Sales/MICE` · `Distribution` |
| Hospitality Group | inherits the union of its properties' archetypes | — |

🟡 **Honesty:** this table is a structured statement of the owner's sector reasoning, not measured data. It is a **falsifiable default** — the Gate 6 validation run exists to break it. Where a real client's performance contradicts a row, the row changes.

---

## P3 — Demand model

**Live in DB 3 Sector Intelligence** (4 Accommodation findings, `Confidence = Medium`, web-cited 2026-08-19 — read them there, they are not re-typed here):

1. OTA commission leakage — 15–30% effective rate
2. Direct-booking share gap against a 35–45% benchmark
3. Extreme, Integration-type tool-stack chaos
4. The time-poor GM + Revenue Manager buyer dyad

⬜ **Unauthored — the demand-pattern layer.** The brief's demand questions (who travels · why · from where · for how long · what triggers the trip · what influences the booking · what causes cancellation · what creates repeat/group/corporate/school/wedding/international demand) have **no rows yet**. They land in DB 3 under the new `Category = Demand Pattern` and in DB 15 Market Routes.

**These are research tasks, not blanks to fill.** Each requires a web-cited source before it becomes a row. Queued for Gate 3.

---

## P4 — Geography scope

**Live in DB 11** (10 rows): `Global → Africa → Kenya → {Nairobi, Mombasa, Diani, Maasai Mara}`, plus `Germany` and `UK` as origin markets.

**Scope decision (owner, 2026-08-19): Kenya-inbound.** Outbound and Gulf routes are built when a real engagement requires them — never pre-populated as a world atlas.

**Requires the new `Destination` level** on DB 11 (specified in `SECTOR_NOTION_SCHEMA.md`) so Maasai Mara — a tourism destination, not a city — sits at the right level.

**Validation destinations (Gate 6):** Nairobi · Mombasa · Maasai Mara — chosen because each demonstrates a *different* destination-demand-content relationship. If they resolve to the same calendar shape, the model is wrong.

---

## P5 — Destination demand-theme vocabulary ★ new this pass

The controlled option set for **DB 16 Destination Profile** `Demand Themes`:

`Corporate` · `Business Travel` · `Conferences/MICE` · `Diplomacy` · `Urban Leisure` · `Dining` · `Staycation` · `Transit/Gateway` · `Beach` · `Luxury` · `Family` · `School Groups` · `Weddings` · `Romance/Honeymoon` · `Cultural` · `Domestic Tourism` · `International Tourism` · `Corporate Retreat` · `Safari/Wildlife` · `Conservation` · `Photography` · `Adventure` · `Seasonal Migration`

**Proposed per-destination assignments** — 🟡 **owner hypotheses, NOT verified.** They are recorded so Gate 4 has something to falsify, and **must be web-verified before they become DB 16 rows**:

| Destination | Proposed primary themes | Proposed shape |
|---|---|---|
| **Nairobi** | Corporate · Business Travel · Conferences/MICE · Diplomacy · Urban Leisure · Dining · Staycation · Transit/Gateway | short-lead, destination-side, weekday-weighted, event- and MICE-led |
| **Mombasa** | Beach · Luxury · Family · School Groups · Weddings · Romance/Honeymoon · Cultural · Domestic + International Tourism · Corporate Retreat | mixed origin/destination-side, festive-peak compression, holiday-calendar-led |
| **Maasai Mara** | Safari/Wildlife · Conservation · Luxury · Family · Photography · Adventure · Seasonal Migration · International Tourism | long-lead, **origin-side dominant**, wildlife-season-led |
| **Diani** | ⬜ unauthored — in Geography, no profile proposed | — |

---

## P6 — Signal-type profile

Which of the core's 21 `Signal Type` values carry weight for this sector:

**Dominant:** `Seasonality` · `Event/Compression` · `Holiday/Cultural` · `School-Holiday` · `Sales/MICE` · `Travel-Trade`
**Secondary:** `Aviation/Connectivity` · `Demand` · `Sports` · `Mega-Event` · `Consumer-Behaviour` · `Distribution`
**Watch:** `Regulatory` · `Economic` · `Risk/Disruption` · `Supplier/Cost` · `Competitor`
**Low relevance here:** `Technology` · `Trade/Fashion` · `Cruise/Port` (Mombasa only) · `Industry-Knowledge`

**Cross-sector contrast** (why this slot exists): B2B SaaS is dominated by `Regulatory` · `Event/Compression` · `Demand`; Professional Services by `Regulatory` · `Seasonality` (tax/filing) · `Demand`. Same 21 values, different weight.

---

## P7 — Timing rule table *(migrated verbatim from `CALENDAR_INTELLIGENCE.md` §5.2, 2026-08-20)*

Offsets are **derived planning offsets, never external facts** (`SECTOR_ACTIVATION_CONTRACT.md` §12). They are configurable sector rules and are re-tuned as real outcomes accumulate in `01_Sector/_memory/runtime.jsonl`.

| Signal Type · Role | Strategic | Marketing | Sales | Offer | Revenue Watch | Action Deadline |
|---|---|---|---|---|---|---|
| `Event/Compression` · destination-side | T-180 | T-120 | T-90 | T-60 | T-30 | T-7 |
| `Seasonality` · destination-side | T-270 | T-180 | T-120 | T-90 | T-45 | T-14 |
| `Sales/MICE` · destination-side | T-365 | T-240 | T-180 | T-120 | T-60 | T-30 |
| `Holiday/School-Holiday` · **origin-side** | T-240 | T-150 | T-120 | T-90 | T-45 | T-21 |
| `Travel-Trade` (Arika's own attendance) | T-120 | T-90 | T-60 | T-45 | — | T-14 |

**The two governing rules** (universal — they stay in the core spec, restated here for use):
- **Origin-side signals run on longer clocks than destination-side ones.** A German school holiday drives a booking decision months before the trip; a destination event compresses inventory closer in.
- **A row without a real research basis is left empty, not filled with a plausible number.** These rows derive from the pilot's booking-window research.

⬜ **Not authored:** `Sports` · `Mega-Event` · `Cruise/Port` · `Aviation/Connectivity` offsets. Blank until researched.

> The `Any sector · Regulatory` row is **universal** and remains in `CALENDAR_INTELLIGENCE.md` §5.2.

---

## P8 — Source pack *(migrated from `CALENDAR_INTELLIGENCE.md` §12, 2026-08-20)*

> 🔴 **Every row is `state = candidate`.** Per `AEIT_08` §5, *a source enters `active` only after a live verification call proves it answers.* **No URLs are recorded** — a URL written from memory is exactly the fabrication the registry exists to prevent. Gate 3 locates and verifies each publisher, records the real `Feed Type` (and an ICS/API endpoint **only if one genuinely exists**), then promotes the row.

| Class | Candidates | Why |
|---|---|---|
| **T1 · Kenya destination authority** | Kenya Tourism Board / Magical Kenya events · Kenya public-holiday source (government gazette) · Kenya school-terms calendar (Ministry of Education) · KICC + Nairobi/Mombasa/Diani venue calendars | The destination-side spine. Public holidays and school terms are date-certain and directly move domestic + regional demand. |
| **T1 · Origin-market authority** | Germany public-holiday + **state-level** school-holiday calendars · UK equivalents · US federal holidays · regional-Africa holiday sources | The origin-side clock. German state school holidays are staggered by *Land* and are the single highest-value inbound-planning driver for a Kenya-inbound route. |
| **T1/T2 · Travel trade & MICE** | WTM Africa · Africa's Travel Indaba · AviaDev Africa · ITB · WTM London · HSMAI · ICCA · Cvent · AHLA | Where the *trade* meets — Arika's own attendance calendar and the client's MICE-demand calendar. Two different uses, one registry. |
| **T1 · Federations** | FIA championship calendars · Safari Rally · World Athletics · major marathons | The reference case: an official body publishing a structured, amendable calendar. **Verify per event, never per series.** |
| **T3 · Aggregators / event APIs** | Event-data providers · ticketing discovery APIs · trade-show directories | Breadth and machine-readability. **Registered candidate, paid/keyed, cost-gated.** Discovery only; they never outrank the organizer. |

Each candidate must carry a named **`consumers`** destination DB before promotion — the decision-purpose gate. The registry rows are mirrored from `AEIT_08` §3.2.

**🔴 Standing correction this pack must fix.** The Hospitality slice of DB 7 recorded at LSEI Pass 1 was **four rows — three seasonality rows sourced to hotel-technology *marketing blogs* at `T3`** (a vendor's seasonality claim, not a destination authority's) **plus one trade show**. Of the three, the generic peak-season row was found **directionally wrong for Kenya** (it asserted a northern-hemisphere summer peak; Kenya's peak is Dec–Jan) and is now `Superseded/Delayed` with a `Change Reason`; the shoulder row was downgraded; the low-season row was **kept** — it carries a real thesis and drives live content — but flagged that its Nov–Feb dates are Kenyan *peak*, not low. Gate 3 re-sources the survivors to T1 and supersedes any claim a T1 publisher contradicts. **Nothing is deleted.**

---

## P9 — Audience roles + decision-maker titles

**Live — read them in their stores, not here.**

- **DB 9 Audience Roles** — 4 Accommodation profiles across the canonical `Operator · Buyer · Amplifier · Enabler` lenses.
- **DB 10 Decision-Maker Registry** — 4 titles with triggers, KPIs and outreach intelligence: **General Manager · Owner/MD · Director of Revenue · DOSM**.

🔴 **Named people, emails and dials remain gated** — paid, PII, Legal-reviewed people-data only, behind an Approval-Matrix row. **No fabricated contact, ever.**

---

## P10 — Linguistics

**Live in DB 6 Sector Linguistics** — a 5-layer map for the Buyer lens. Its operative content (recorded in `SECTOR_OS.md` §15, 2026-08-19):

- **Use:** *net RevPAR* · *the OTA tax* · *direct-booking share*
- **Avoid:** *more bookings* · *awareness*

The full surface / functional / cognitive / incentive / cultural layers live in DB 6.

---

## P11 — Offer ladder + outreach angle

**Owned by Offer (02); routed by Sector DB 8.** Do not re-own the offer.

| Rung | Content |
|---|---|
| **Gateway** | *OTA Leakage & Direct-Booking Audit* — a paid diagnostic that converts Arika's Medium-confidence market view into High confidence **via the client's own numbers** |
| **Entry** | *Hospitality Revenue Content OS · "Direct Booking Engine"* — an outsourced hospitality **revenue-content department**. The enemy is *the OTA tax*. **`GAP — needs OEOS`; Working Hypothesis; no price.** |
| **Expansion 1** | Guest acquisition + booking-engine optimization (`SAL`/`ACQ`) |
| **Expansion 2** | Guest CRM + retention, WhatsApp/email (`AUTO`) |
| **Transformation** | Hospitality Revenue Intelligence + RMS-connected operating layer + Stack Rationalization (`AI-X`/`OPS`) — where the tool-stack-chaos finding is finally solved |

Full engineering: `02_Offer/OFFER_OS.md` §3. 🟡 **Not quotable** until `offer-oeos-engineer` (12 phases) and `offer-pricing-floor-analyst` have run.

---

## P12 — Content pillars, angles, platform bias

**Live in Content (04) DB 5** — 3 real Accommodation Content Opportunities created 2026-08-19, each resolving to a real Sector Intelligence finding + Sector Signal + Audience Role:

1. *The OTA Tax* — Insights / Revenue Intelligence / Awareness
2. *Are you an OTA tenant? — the direct-booking benchmark* — Education / Consideration
3. *Low season is your growth season* — Frameworks / Revenue Signals, timing-led

All carry `Confidence = Working Hypothesis` and `Proof Status = Proof required — named` — **no invented Arika case study.**

⬜ **Unauthored:** the sector's pillar/angle set and platform bias (which platforms carry hospitality authority, and why). Blocked on Content DB 3 (Sector × Platform Matrix), which needs a named sub-sector — now available.

---

## P13 — Seasonality model + compression threshold

**The commercial rhythm** — 4 live DB 7 signals (`Peak` · `Shoulder` · `Low-season buying window` · a trade show), each with booking-window lead-time dates, plus one DB 12 Sector State and one DB 13 Forecast row.

**The rhythm insight that reframes the sector** (owner's "closing season"):

> **Low season is Arika's *buying* window, not a dead period** — occupancy pain is visible and the GM/Revenue Manager finally has capacity to engage. The client's low season is the agency's high season.

**Compression threshold:** inherits the core default — *≥ 3 signals at `Commercial Priority` High or Critical overlapping the same Geography within a rolling 14-day window* → flag a compression read (a DB 3 `Strategic Node` finding + `COMPRESSION_EVENT`). 🟡 Not yet tuned for hospitality; retune once real destination density exists.

⚫ **The live forecast layer** (pickup, occupancy, ADR, RevPAR, comp-set) stays **template** — populated only from a client's connected RMS/PMS. **Never fabricated.**

---

## P14 — KPI semantics

What DB 12 Sector State's sector-appropriate fields mean here:

| Core field | Hospitality meaning |
|---|---|
| `ADR / Price Pressure` | Average Daily Rate direction + rate-parity/discounting pressure |
| `Connectivity / Access` | **Aviation** — route capacity, carrier changes, visa friction on the active market routes |
| `Demand Direction` | by segment: leisure · corporate · group/MICE · domestic · international |
| `Competition` | comp-set density and new-supply entry at the destination |

**Commercial KPI focus:** net RevPAR · direct-booking share · effective OTA commission rate. ⚫ All client-system-sourced; never estimated.

---

## Honesty ledger

- No fabricated event date, season, contact, price, or property number appears in this file.
- The property-type rules (P2) and destination theme assignments (P5) are **owner-curated hypotheses**, explicitly falsifiable at Gate 6.
- Every P8 source is `candidate` with **no URL recorded** until verified against the live publisher.
- Derived timing offsets (P7) are planning offsets, never presented as external facts.
- Live pilot content is **referenced in its owning store**, not copied here — so this file cannot drift from Notion.

## Cross-references

[`../../SECTOR_OS_ARCHITECTURE.md`](../../SECTOR_OS_ARCHITECTURE.md) (the interface) · [`../../SECTOR_ACTIVATION_CONTRACT.md`](../../SECTOR_ACTIVATION_CONTRACT.md) §14 (cross-loop) §15 (LSEI) §16 (separation) · [`../../SECTOR_NOTION_SCHEMA.md`](../../SECTOR_NOTION_SCHEMA.md) §0.3, DB 16 · [`../../CALENDAR_INTELLIGENCE.md`](../../CALENDAR_INTELLIGENCE.md) §5.2, §12 · `00_Agency_Governance/enterprise_architecture/AEIT_08` §3.2 · `02_Offer/OFFER_OS.md` §3 · `04_Content/CONTENT_INTELLIGENCE_SCHEMA.md`.

## Changelog

- **v0.1 (2026-08-20, Gate 1 — DECIDE):** Created as Sector Plugin #001. **Migrated** the Hospitality timing-rule table out of `CALENDAR_INTELLIGENCE.md` §5.2 (P7) and the Kenya-inbound candidate source pack out of §12 (P8) — moved, not rewritten, with pointers left behind. **Authored new:** the property-type typology and the signal-to-archetype rule that makes the property-type calendar layer possible (P2), the destination demand-theme vocabulary for DB 16 with proposed Nairobi/Mombasa/Maasai Mara assignments marked as falsifiable hypotheses (P5), the signal-type weighting profile (P6), the seasonality/compression configuration (P13), and the KPI semantics for DB 12's sector-appropriate fields (P14). **Referenced, never re-typed:** the live pilot content in DB 3/6/9/10, DB 7's commercial rhythm, Content DB 5's 3 opportunities, and Offer (02)'s entry-offer seed. Two slots left honestly unauthored (P3 demand-pattern layer, P12 pillar/angle set). **Nothing written to Notion.** — Claude Code (Opus 5)
