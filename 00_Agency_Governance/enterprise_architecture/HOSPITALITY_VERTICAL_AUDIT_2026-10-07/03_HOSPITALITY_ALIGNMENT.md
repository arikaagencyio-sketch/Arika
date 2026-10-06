# 03 — Hospitality Alignment: where the vertical belongs

**Protocol §1:** *"Where does the Hospitality vertical belong inside the existing Agency OS, and what must exist for it to operate correctly without breaking or duplicating the existing system?"*
**Protocol §6–§7:** property types, revenue centres, and the experience model — *"audited as a vertical, not as a content category."*

---

## 1. The answer

> **Hospitality already has an architectural home, and it is not a new operating system. It is a *sector configuration* (Tier 2 plugin) over the Sector Universal Core, a *sector-specific offer family* inside Offer (02), an *overlay* on the universal client intake, and a *company-structure profile* in the CRM — with each client's reality computed as a Tier 3 *client instance*, never stored as a parallel system.**
>
> **What is missing is not a place to put Hospitality. It is the half of Hospitality that faces the guest.** The existing configuration models the agency's sale *to* hotels (Plane A) deeply and the hotel's sale *to its guests, companies and intermediaries* (Plane B) thinly. Closing that gap belongs inside the existing extension points — chiefly plugin slot **P3 (demand model)**, which is already defined for exactly this and is the plugin's one substantive unauthored slot — plus, at most, one new canonical entity after owner ratification.

**Evidence (`CONFIRMED`):**

- `E: 01_Sector/SECTOR_OS_ARCHITECTURE.md §2 → three tiers → "A plugin supplies values into core fields. It never adds a store, a field, an agent, or an event." → the ratified mechanism by which any vertical enters → Hospitality = Sector #001.`
- `E: 01_Sector/sector_plugins/hospitality/HOSPITALITY_PLUGIN.md → 14 slots authored, P3 demand-pattern layer "⬜ Unauthored … who travels · why · from where · … what creates repeat/group/corporate/school/wedding/international demand" → the Plane B model has a reserved, empty slot.`
- `E: 02_Offer/OFFER_OS.md §3 → "Engineered entry offer (seed) — Hospitality Revenue Content OS" → registry #13 candidate, held out of the priced table → the commercial model lives in Offer (02).`
- `E: 02_Offer/…Pilot Intake Overlay.md §1 → "Universal core + one sector overlay … A new sector gets a new overlay, not a new intake" → the client-intake model.`
- `E: 00_Agency_Governance/CRM_SCHEMA.md "Company / Organization Level" → structure_type SGL/MBR/GRP/HLD/OUT, parent/child levels, Pilot Engagement → the client-type configuration.`

## 2. The protocol's candidate categories — tested

| Candidate | Verdict | Why (evidence) |
|---|---|---|
| A separate operating system / department | ❌ **No** | The generalization test forbids it: *"Remove the Hospitality plugin. The Universal Core MUST still load… If it breaks, this is a hospitality system wearing a sector-OS label"* (`SECTOR_OS_ARCHITECTURE.md` §7). `SECTOR_WRITE_CONTRACT.md:126`: *"Never default to Hospitality… a context that falls back to it is a system that has silently become a hospitality tool."* |
| Vertical module | ◐ Partly — as a *configuration pack*, not a code module | The plugin is explicitly "a doctrine/config pack, not runtime code" (`HOSPITALITY_PLUGIN.md` header) |
| Sector operating model | ✅ Yes — the 14-slot plugin **is** the sector operating model | P1–P14 cover ontology → KPI semantics |
| Domain configuration | ✅ Yes — `plugin.config.json` + controlled vocabularies (P2 archetypes, P5 themes, P6 weights, P7 offsets) | Ratified as a compiled sidecar (item 31c) |
| Sector intelligence layer | ✅ Yes — the plugin's values drive DB 7 / DB 15 / DB 16 and the Resolution Engine | Gate F passed three times on Hospitality places |
| Commercial model | ✅ Yes, *separately owned* — Offer (02) | Plugin P11: *"Owned by Offer (02); routed by Sector DB 8. Do not re-own the offer."* |
| Client-type configuration | ✅ Yes — CRM `Company` structure + intake overlay | `CRM_SCHEMA.md`, overlay §1–§3 |
| **A combination** | ✅ **This is the answer** | Each component above has exactly one owner, as `AEIT_06` §1 requires |

## 3. Placement map — every Hospitality component, its home, its state

| Component | Home (owner) | Reality | Class | Priority | Note |
|---|---|---|---|---|---|
| Vertical definition, archetypes, rules, timing, sources, KPI semantics | Sector (01) — plugin P1–P14 | `BUILT`; Tier-1 P2 cells 18/18 ruled | EXISTING | — | Keep |
| Destination / route / seasonality intelligence | Sector (01) — DB 7, 11, 14, 15, 16 | `LIVE` (3 destinations, 5 routes, 33 sources) | EXISTING | — | Conditional "travel-family" objects (item 31b) |
| Client calendar | Sector (01) — Resolution Engine step 5 | `DESIGNED` (*"no client calendar exists until a real client does"*) | EXISTING | — | Correct by design |
| Guest-side demand model (segments, occasions, pathways, revenue centres) | Sector (01) — **plugin P3** | ⬜ unauthored | **EXTEND** | P2 (P1 if the group pilot spans outlets) | `HV-12`, `HV-16` |
| Commercial offer + gateway audit | Offer (02) — Draft 41, worksheet | `DESIGNED`; Phase 11 BLOCKED | EXISTING | P1 to unblock | `HV-27` |
| Group / portfolio offer | Offer (02) | **absent** (A001 AG-7) | **NEW** (OEOS run) or decision to defer | **P0 decision** | `HV-03` |
| Organisation structure (group → property → outlet) | Governance (00) — CRM `Company` | `DESIGNED`, not verified live | **EXTEND** | P1 | `HV-05`, `HV-06` |
| Pilot engagement record | Governance (00) — CRM `Pilot Engagement` (`PILOT-H-*`) | `DESIGNED` | **EXTEND** | P1 | `HV-05` |
| Client intake | Governance (00) core + Offer (02) overlay | `DESIGNED`, unratified (item 73) | EXISTING | P1 to ratify | — |
| Prospecting | Sales (05) — prospecting cycle | `LIVE` once (drafts only) | EXISTING | P1 to release | `HV-36` |
| Content for hotel buyers (Plane A) | Content (04) DB 5 | 3 opportunities | EXISTING | — | — |
| Content *for the hotel's guests* (Plane B, delivery) | Content (04) — but no client dimension | **absent** | **EXTEND** | P1 before delivery | `HV-11`, `HV-14` |
| Creative production for a hotel | Design (19) / EE (20) | `BUILT` (engine), agency-only structure | **EXTEND** | P1 before delivery | `HV-11` |
| Pre-Experience methodology | Content (04) + Design (19) + EE (20) + Offer (02) | **absent** | **NEW** (methodology) on EXTENDED components | P2 / P1 for the prototype | file 11 |
| Measurement of hotel outcomes | Marketing (03) (measurement truth) + client systems | **absent** | **METRIC GAP** | P2 (P1: per-client baseline in M6) | `HV-18` |
| Agency self-marketing into Hospitality | Presence (21) + Marketing (03) + EE (20) | website/LinkedIn **contradict** | **GOVERNANCE GAP** | **P0** (truth) / P1 (plan) | `HV-02`, `HV-29` |

## 4. Property types (protocol §6)

The live vocabulary is plugin P2's ten archetypes (`HOSPITALITY_PLUGIN.md` P2; live as the DB 16 `Asset / Property Archetypes` option set) plus four CRM organisation levels used by the pilot. `p2_coverage_gate.py` (run 2026-10-06) reports ruled coverage per archetype against the 12 dominant + secondary signal types.

| Protocol property type | Existing representation | Rule coverage (gate) | Class | Note |
|---|---|---|---|---|
| Urban hotels | `City / Conference Hotel` | 7/12 · Tier 1 | **EXISTING** | — |
| Business hotels | `Business Hotel` | 5/12 · old two-list Tier 3 | **EXTEND** | Not yet on the totality format |
| Resorts | `Beach Resort` only | 7/12 · Tier 1 | **EXTEND** | No non-beach resort (lake, golf, mountain) |
| Safari lodges | `Safari Lodge` | 7/12 · Tier 1 | **EXISTING** | — |
| Camps | `Tented Camp` — `inherited(Safari Lodge)` | 7/12 | **EXISTING** | — |
| Glamping | none | — | **EXTEND** (vocabulary) | `UNKNOWN — HUMAN INPUT REQUIRED`: distinct archetype, or a Tented Camp variant? |
| Beach properties | `Beach Resort` | 7/12 | **EXISTING** (partial) | Non-resort beach hotels fold into it |
| Private villas | `Villa` | 5/12 · Tier 3 | **EXTEND** | — |
| Clubs (members', country, golf) | none | — | **NEW** vocabulary | Membership revenue is absent too |
| Restaurants | CRM level `Restaurant / Bar Outlet`; F&B is a **separate industry** in DB 2 (Type A) | — | **EXTEND** | Standalone restaurants are a different sub-sector, unauthored (plugin P1: *"Hospitality carries 2 division-level industries… second… is not authored"*) |
| Spas | CRM level `Spa / Wellness Outlet`; outlet may carry a Wellness tag | — | **EXTEND** | Same pattern as restaurants |
| Conference venues | CRM level `MICE / Conference Unit`; archetype `City / Conference Hotel` | — | **EXTEND** | A venue with no rooms has no archetype |
| Wedding venues | none — `Weddings` is a P5 *destination demand theme*, not an archetype | — | **EXTEND** | — |
| Destination properties | `Destination Property` — **live option, never defined** | **0/12 — declared `unruled`** | **DATA GAP** | Owner must define it (`HOSPITALITY_PLUGIN.md` "Declared unruled") |
| Mixed-use hospitality | no mixed-archetype rule (A001 AG-5); sandbox workaround `secondary_unruled` | — | **DATA GAP** | — |
| Groups | `Hospitality Group` — a parent, *"not a bookable unit"* | **0/12 by design** — resolves by union of sourced children | **EXTEND** | The union operator is **not built** (A001 AG-4) → `HV-03` |
| Other hospitality experiences | none | — | **UNKNOWN** | Needs the owner's scope |

**Reading (`CONFIRMED`):** archetypes that dominate *accommodation demand* are well represented. Archetypes whose identity is a *non-room revenue centre* (clubs, restaurants, spas, standalone venues, wedding venues) are represented only as CRM organisation units, with no market rules and no demand model.

## 5. Revenue centres (protocol §6)

| Protocol revenue centre | Representable today? | How | Class |
|---|---|---|---|
| Rooms · suites · villas | ✅ as economics | P14 KPI semantics (ADR, RevPAR, **net RevPAR**, direct-booking share, effective OTA commission); intake H-A04 room types; MD1/MD2 room-nights and revenue by channel | **EXISTING** (template layer ⚫ — client systems only) |
| Food & beverage · restaurants · bars | ◐ as an org unit only | CRM outlet level; intake H-A05 (optional, public observation) | **EXTEND** |
| Spa · wellness | ◐ as an org unit only | CRM outlet level | **EXTEND** |
| MICE · conferences · meetings | ◐ as org unit + market signal | CRM `MICE / Conference Unit`; DB 7 `Sales/MICE` signal type; P5 `Conferences/MICE`; intake H-C05 | **EXTEND** |
| Corporate retreats · team building | ◐ as a destination theme only | P5 `Corporate Retreat` | **EXTEND** |
| Tournaments | ◐ as a market event only | DB 7 `Sports` / `Mega-Event` signal types | **EXTEND** |
| Weddings · celebrations | ◐ as a destination theme only | P5 `Weddings`, `Romance/Honeymoon`; intake H-C05 | **EXTEND** |
| Activities · tours · excursions · destination experiences | ❌ | — | **NEW** |
| Day passes · memberships | ❌ | — | **NEW** |
| Packages · ancillary revenue | ❌ | — | **NEW** |

**What is structurally missing:** the repository can name a *place* where revenue happens (an outlet `Company`) and a *market reason* demand exists (a theme or signal), but it has **no object for what the client sells** — a package, a day pass, a membership, a wedding, a corporate tennis experience — and **no revenue measure beyond rooms**. → `HV-12`.

*Nearest existing shape:* the synthetic property schema approved for fixture `SYNCO-01-P01` on 2026-09-29 (unit categories, venue count and capacities, wellness dimensions and hours, a club window; the F&B outlet count left open). It is held in a private sandbox as **mechanism evidence only** (D20 extended) and was not read by this audit. Its **field shape** is a reasonable starting point for the P3/intake vocabulary below; its values are not reusable.

**Minimum sufficient fix (proposal, not applied):** author plugin **P3** with a controlled `revenue_centre` vocabulary and an `occasion` vocabulary (values only — no store), and capture each client's actual offerings in the client folder through intake rows (outside the repository, as intake §5 requires). Create a canonical `Client Offering` entity **only** when a second department must reference a client's offerings by ID — the `AEIT_00` §5 checklist test. See `HD-08`.

## 6. The Hospitality Experience Model (protocol §7)

`PROPERTY → ASSET → EXPERIENCE → OCCASION → AUDIENCE → DESIRE → PROPOSITION → STORY → CAMPAIGN → DISTRIBUTION → LEAD → SALES → BOOKING → EXPERIENCE DELIVERY → SOCIAL PROOF → RETENTION → REFERRAL`

| Object | Existing equivalent | Location / schema | Workflow | Owner | Depends on | Gap | Class |
|---|---|---|---|---|---|---|---|
| **Property** | CRM `Company` (`entity_level = property/branch`) + plugin P2 archetype; DB 11 also has a `Property (template level)` | `CRM_SCHEMA.md`; `SECTOR_NOTION_SCHEMA.md` DB 11 | Prospecting cycle; intake S1 | Governance (identity), Sector (market data) | ORG namespace, Geography | Not live in ClickUp; **property = Company, Geography place, or both is undecided** (A001 AG-10, T1-1) | **EXTEND** |
| **Asset** | Two different things share the word: *creative asset* (`AEIT_06` `Creative Asset`, Design asset library) and *physical facility* (intake H-A05, optional) | `DESIGN_OS.md`; overlay H-A05 | — | Design (creative); none (facility) | — | No facility inventory (court, ballroom, spa room, pool) — the input a Pre-Experience build needs | **EXTEND** (intake rows) |
| **Experience** | **None in the hospitality sense.** `AEIT_06` `Experience` = an interactive web build owned by EE (20) | `AEIT_06` §2 | — | — | — | Naming collision: a second `Experience` entity would fork the model → `HV-39` | **NEW** (under another name) |
| **Occasion** | Market occasions: DB 7 `Holiday/Cultural`, `School-Holiday`, `Event/Compression`, `Sports`, `Mega-Event`; themes `Weddings`, `Romance/Honeymoon` | DB 7, P5 | Resolution Engine | Sector | DB 14 sources | Personal and corporate occasions (anniversary, birthday, year-end, offsite, AGM) absent | **EXTEND** (P3 vocabulary) |
| **Audience** | Plane A: DB 9 roles, DB 10 titles. Plane B: DB 15 `Primary/Secondary Audience` (free text), DB 16 audiences (relation to DB 9), P5 themes, intake H-C01 | `SECTOR_NOTION_SCHEMA.md` | S02, S05 | Sector | — | **Plane B has no structured segment model**; DB 16 points at Plane A rows (`HV-17`) | **EXTEND / REFACTOR** |
| **Desire** | DB 9 Wants/Fears/Beliefs/Rejects (Plane A); DB 16 `Travel / Purchase Motivations` (Plane B, text); Content DB 7 `Desire` rollup | Sector, Content | S02, S05 | Sector, Content | DB 5 | Plane B desire is unstructured text | **EXISTING** (thin) |
| **Proposition** | Agency's: Offer registry, Content DB 2 Narrative Positions. Client's: Draft 41 deliverable D2 (offer/narrative strategy) | `OFFER_OS.md`; `CONTENT_INTELLIGENCE_SCHEMA.md` DB 2 | OEOS; ACCOS | Offer, Content | Audit verdict (QG1) | No store for a client's propositions (correctly outside the repo — but no named home) | **EXTEND** |
| **Story** | Content Story Architecture; DB 6 translations; EE Narrative Arc; Branding narrative stack | `CONTENT_OS.md` §10 | ACCOS stages 6–9 | Content | Narrative Position | All arcs are problem-led B2B (`HV-14`) | **EXTEND** |
| **Campaign** | Content DB 4 Campaign Intelligence (owner ratified 2026-08-16) | `CONTENT_INTELLIGENCE_SCHEMA.md` DB 4 | content-brief-builder → Design | Content (entity), Marketing (strategy) | Offer, Platform, Narrative | **No client field and no lifecycle status** (`HV-08`, `HV-11`) | **EXTEND** |
| **Distribution** | Presence (21) layer registry; Marketing §10; Content DB 6 `Distribution Objective/Wave`; PIL | `PRESENCE_OS.md`; PIL | Presence engine (Postiz) | Presence (coordination), Marketing (channels) | Accounts | Hospitality channels unprofiled (`HV-19`); nothing published | **EXTEND** |
| **Lead** | CRM `Lead` — Arika's leads only | `CRM_SCHEMA.md` | Prospecting; LEAD_CREATED | Sales | Company | A *hotel's* leads (wedding enquiries, corporate RFPs) live in the client's systems | **EXISTING** (Plane A) · `EXTERNAL-BY-DESIGN` (Plane B) |
| **Sales** | CRM `Opportunity` — Arika's | `CRM_SCHEMA.md` | Sales agents | Sales | Offer price (blocked) | Hotel's group/MICE sales process unmodelled | **EXISTING** (A) · `EXTERNAL-BY-DESIGN` (B) |
| **Booking** | None; measured only through client data (MD1 room-nights by channel) | Worksheet §1.4 | Audit | client systems | PMS/CRS/booking engine | No defined data path from a client's booking data to measurement | `EXTERNAL-BY-DESIGN` + **METRIC GAP** |
| **Experience delivery** | The hotel's own operations — outside the agency's scope | — | — | the client | — | Correctly external; nothing to build | `EXTERNAL-BY-DESIGN` |
| **Social proof** | Arika's: Client Success advocacy (Class C claims **banned** until real results). Hotel's: reviews/UGC — PIL watchlist only | `CLAIMS_SUBSTANTIATION_POLICY.md` §3; PIL §4.3 | client-success-advocacy | CS, Presence | Consent | Guest reviews as signal or proof unmodelled | **EXTEND** (P2) |
| **Retention** | Arika's: CS retention cadence. Hotel's: guest CRM/retention = plugin P11 Expansion 2 (unengineered); nurture D6 deferred from MVP | `CLIENTSUCCESS_OS.md` §4; Draft 41 | — | CS; Offer | Consent (QG4) | Guest retention model absent | **EXTEND** (P2) |
| **Referral** | Arika's: `Lead.source = referral`, ClientPartner. Guest-to-guest (B2C2C) absent | `CRM_SCHEMA.md` | — | ClientPartner, CS | — | No pathway model (`HV-16`) | **NEW** (P2) |

**Reading (`CONFIRMED`):** of seventeen objects, **eleven have an equivalent** — almost all on Plane A — **four are external by design** (the hotel's own lead, sales, booking and delivery processes, which the agency measures but does not run), and **two are genuinely new**: *Experience* (as a guest product, needing a different name) and *guest Referral*. Nothing here justifies a parallel hospitality data store.

## 7. What must NOT change

1. **The three-tier separation and the plugin rule** — Hospitality stays configuration; core files carry no hospitality values (`SECTOR_ACTIVATION_CONTRACT.md` §16; the `grep` test in `SECTOR_OS_ARCHITECTURE.md` §7).
2. **The CRM `Company` as the only organisation registry** — no Sector-side, Content-side or Finance-side property store (`SECTOR_ACTIVATION_CONTRACT.md` §14.4; `AEIT_06` §1).
3. **The diagnostic gate** — audit first; leakage class (a)–(d); redirect is a valid outcome (Draft 41 §3, QG1).
4. **No fabricated hotel metrics** — occupancy, ADR, RevPAR, pickup stay ⚫ template until a client system supplies them (plugin P13/P14, QG6).
5. **Identity separation** — `ORG-* / PER-* / PILOT-* / SIM-*`; real names outside the repository; A001 never becomes a pilot record (`CRM_SCHEMA.md` pilot activation rule; A001 D17/D20).
6. **Advisory-first agents and Class 3 human sign-off** — Hospitality adds no autonomous outreach, publishing or generation (`governance.ts`; Constitution §5).
7. **One store per concept, views for layers** — no calendar per layer, per audience or per direction (`SECTOR_ACTIVATION_CONTRACT.md` §15; `CALENDAR_INTELLIGENCE.md` §13).
