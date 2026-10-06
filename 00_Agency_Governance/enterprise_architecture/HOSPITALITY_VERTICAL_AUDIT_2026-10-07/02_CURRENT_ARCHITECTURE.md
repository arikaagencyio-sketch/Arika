# 02 — Current Architecture (evidence-based)

**Protocol §3:** build the layer map — *constitution → governance → OS → intelligence → strategy → commercial → marketing ops → creative → production → distribution → sales → delivery → measurement → learning → intelligence* — **"but do not assume these layers exist."**

---

## 1. What the Agency OS actually is

**A documentation-first operating system for one owner-operator, with a progressively-wired agent layer, whose deepest built component is a sector-intelligence engine.**

- **Root:** `GLOBAL_OS.md` is the single entry point and anti-hallucination contract (§2); the constitution is supreme (§3); each department's `{DEPT}_OS.md` is locally authoritative (*"Plugin = Department"*, §7).
- **Registries are sections, not systems:** eleven curated registries live as standard sections inside every department file (`GLOBAL_OS.md` §6); thirty further registries are deliberately unbuilt (`REGISTRY_TAXONOMY_REFERENCE.md`).
- **Agents are advisory:** 115 specs on one runtime; every agent recommends and logs, none performs a state change; Class 3+ always needs a human (`arika-runtime/src/governance.ts`, memory `arika-runtime-is-the-agent-substrate`).
- **Truth discipline is the distinguishing feature:** no silent invention (Constitution §3); `INTENDED → LIVE` reality states with named tests (`AEIT_11`); provenance labels and honesty states on every sector value; authorisation registers for any state-changing run; *decide ≠ apply*.
- **Operating reality:** pre-revenue, zero clients, solo owner. `AEIT_01` §5 and the 2026-10-03 readiness assessment both conclude that **the machinery is far ahead of the reality it runs on** (agency-wide mechanism 53.0 %, real-pilot 16.5 %, client-facing 2.3 %).

## 2. The protocol's layer stack — tested layer by layer

| # | Layer | Exists? | Where | Implementation | Governing doc | Reality | Missing pieces |
|---|---|---|---|---|---|---|---|
| 1 | **Agency constitution** | ✅ Yes | `00_Agency_Governance/AGENCY_OPERATING_CONSTITUTION.md` | Non-negotiables, decision rights, Risk Class 0–4, amendment process | itself; summarised `GLOBAL_OS.md` §3 | `BUILT`; class model enforced in code (`governance.ts`) | Still `v0.1-draft` dated 2026-06-30; decision rights all resolve to one person; contact line says website "not yet live" |
| 2 | **Governance** | ✅ Yes | `00_Agency_Governance/` + `enterprise_architecture/` | RACI, KPI dictionary, approval matrix, CRM schema, AEIT_00–11, runnable gates, authorisation registers | Constitution | `BUILT`; gates `LIVE` (run 2026-10-06) | RACI frozen 2026-06-30 (Sector, Design, Experience Engineering and Presence are never Responsible or Accountable for any function); **truth gate red on master** (`HV-01`); ratified R1/R3 unenacted (`HV-21`) |
| 3 | **Agency operating system** | ✅ Yes | `GLOBAL_OS.md`, department OS files, `arika-runtime/` | Department plugins + runtime executor | `GLOBAL_OS.md` | `BUILT`; runtime `LIVE` for manual runs only | Scheduler unapproved; event bus never publishes |
| 4 | **Intelligence** | ✅ Strongest layer | `01_Sector/` (16 Notion DBs, 10 skills, plugin), `AEIT_07/08` (IntOS blueprint, source registry) | Sector Universal Core + Hospitality plugin + Resolution Engine (skill S09) | `SECTOR_OS_ARCHITECTURE.md`, `SECTOR_ACTIVATION_CONTRACT.md` | `LIVE` — Gate F run ×3; 33 registered sources; 3 destination profiles | Learning feedback into intelligence (no performance store); IntOS proper `DESIGNED`; Gate H/I unrun |
| 5 | **Strategy** | ✅ Yes | `AGENCY_VISION.md`, `AGENCY_COMMERCIAL_DOCTRINE.md`, OEOS phases per offer, `AEIT_10` roadmap | Doctrine documents; OEOS 12-phase engineering | — | `BUILT` (doctrine) | **Client strategy** (Draft 41 D2) never produced; strategy object not an entity |
| 6 | **Commercial / revenue** | ◐ Partial | `02_Offer/` (registry, OEOS, pricing floors), `AGENCY_REVENUE_TARGETS.md`, `finos-plugin` | Offer Engineering Registry (12 + #13 candidate) | `OFFER_OS.md` | `BUILT` design; **no sale, no price for Hospitality** | Phase 11 blocked; hotel floors absent; client-side (hotel) revenue model absent (file 07) |
| 7 | **Marketing operations** | ◐ Doctrine only | `03_Marketing/` | 9 advisory agents, no store | `MARKETING_OS.md` | `BUILT` agents, **never run**; no memory stream | No route from Sector (item 31k); no performance store; RACI placeholder |
| 8 | **Creative / content** | ✅ Yes | `04_Content/` (8 Notion DBs, ACCOS, Story Architecture), `12_Branding/` | Content Intelligence Layer; Brand Genome | `CONTENT_OS.md`, `CONTENT_INTELLIGENCE_SCHEMA.md` | Stores `LIVE`; agents never run | No client dimension on campaigns/briefs (`HV-11`); narratives are problem-led B2B (`HV-14`) |
| 9 | **Production** | ✅ Yes | `19_Design/` (production engine, asset library, Canva), `20_Experience_Engineering/` (spec system, website) | Storyboard → image → video → voice → music → upscale → Canva assembly; 6-station web spec system | `DESIGN_OS.md`, `EXPERIENCE_SPEC_SYSTEM.md` | `BUILT`; Creative Pipeline routine restored 2026-07-15; KIE client mock-tested | Canva structure agency-only; depiction rules absent (`HV-13`) |
| 10 | **Distribution** | ◐ Blueprint | `21_Presence/`, Marketing §10, Content DB 6 translation matrix | Presence Layer Registry; four directions; Postiz executor | `PRESENCE_OS.md` | `DESIGNED` — *"Presence has produced nothing"* (§16) | Hospitality channels (WhatsApp, Google Business Profile, OTAs, review sites) on an unbuilt watchlist (`HV-19`) |
| 11 | **Sales / conversion** | ✅ Partial | `05_Sales/`, `06_ClientPartner_Acquisition/` | 10 Sales agents; prospecting cycle; CRM Lead/Opportunity | `SALES_OS.md`, `CRM_SCHEMA.md` | Prospecting `LIVE` once; **0 sends** | Proposal/agreement blocked (Phase 11, Legal); no real Lead row |
| 12 | **Client delivery** | ◐ Designed | `07_Client_Success/`, `08_Operations/`, offer-level OEOS delivery models | Onboarding/retention/offboarding workflows; delivery scheduler/QA/risk agents; ClickUp Project pipeline | `CLIENTSUCCESS_OS.md`, `OPERATIONS_OS.md` | `BUILT` agents, never run | Capacity model absent; SLAs unset; no client-workspace separation |
| 13 | **Measurement** | ❌ Effectively absent | `AGENCY_KPI_DICTIONARY.md`, plugin P14, Draft 41 D7/M6, `marketing-attribution-modeling` | Formulas and semantics only | KPI dictionary | `DESIGNED` | **No performance store anywhere** (`SECTOR_OS_ARCHITECTURE.md` §1.3 finding 3); thresholds unset; no BI |
| 14 | **Learning** | ❌ Effectively absent | `AEIT_07` §3.5 (IntOS learning layer), Marketing memory flywheel, Sales `Learning_Loop_Log.md`, changelogs, memory files | Prose lessons in changelogs; 9 small memory streams | `AEIT_07` | `DESIGNED`; Sales learning log is an **empty template** | P2 cells cannot be promoted to `observed` because no outcome store exists |
| 15 | **Back to intelligence** | ❌ Loop open | `SECTOR_OS_ARCHITECTURE.md` §1.2 diagram: `Marketing (03) performance → 🔴 no store exists (feedback gap)` | — | — | `INTENDED` | The return edge is "doctrine only" (§1.3 finding 3) |

**Reading of the table (`CONFIRMED`):** the stack exists from layer 1 to layer 12 — at very different depths — and **stops at layer 13.** Measurement and learning are designed in several places and built in none, so the loop the protocol asks for (*information → decision → action → outcome → learning*) is currently **open at "outcome"**. The architecture itself names this break and deliberately refuses to fill it with a parallel store (`SECTOR_OS_ARCHITECTURE.md` §6, gap register).

## 3. The architecture as built — one diagram

```
                      AGENCY_OPERATING_CONSTITUTION  (Class 0–4 · no silent invention · decide ≠ apply)
                                     │
            GLOBAL_OS.md ── RACI · KPI dict · CRM_SCHEMA · Approval Matrix · AEIT_00–11 · gates · authorisation registers
                                     │
 ┌──────────────── INTELLIGENCE (Sector 01) ── LIVE ───────────────────────────────────────────────┐
 │ DB 1/2 taxonomy · DB 3 findings · DB 6 language · DB 9 roles · DB 10 titles                       │
 │ DB 7 signals ◄ DB 14 sources        DB 11 geography ─ DB 15 routes ─ DB 16 destinations           │
 │ Hospitality plugin (14 slots) ──► RESOLUTION ENGINE (S09) ──► S10 handoff packet                  │
 └──────────────────────────────────────────────┬──────────────────────────────────────────────────┘
          text/relation routes that DELIVER ────┤ CRM tags (verified on fixtures) · Offer inbox (offline) · Content relations
          routes that do NOT deliver ───────────┤ Sales (event-only; nothing publishes) · Marketing ✗ · Operations ✗  (item 31k)
                                                ▼
 OFFER (02) — OEOS · registry · Hospitality Revenue Content OS (unpriced, Phase 11 BLOCKED)
        │
        ├─► CONTENT (04) 8 DBs ─► DESIGN (19) production ─► EXPERIENCE ENG (20) ─► PRESENCE (21) ─► [market]   (nothing published)
        │
        └─► SALES (05) prospecting ─► CRM Lead/Opportunity (ClickUp) ─► CLIENT SUCCESS (07) ─► OPERATIONS (08) ─► FINANCE (09)
                          (drafts only, 0 sent)        (no real rows)          (agents never run)   (no clients)    (no invoices)
                                                                                                     │
                                       MEASUREMENT ✗ (no performance store) ─► LEARNING ✗ ─► back to INTELLIGENCE ✗
```

## 4. The central architectural observation — two market planes

Every hospitality question in the protocol lands on one of **two different markets**, and the repository serves them very unequally.

| | **Plane A — the agency's market** | **Plane B — the client's market** |
|---|---|---|
| Relationship | Arika → a hospitality business (B2B) | A hospitality business → guests, companies, intermediaries |
| Who is the "audience"? | GM, Owner/MD, Director of Revenue, DOSM, group commercial leaders | Leisure guests, couples, families, corporates, MICE planners, wedding parties, travel trade, diaspora… |
| Where it is modelled | DB 9 roles (Operator·Buyer·Amplifier·Enabler), DB 10 titles, DB 6 linguistics, `sector-icp-fit`, prospecting cycle, CRM Company tree, Offer ladder, intake | DB 15 routes (audience as **free text**), DB 16 destination profiles, P5 demand themes, P2 archetype × signal rules, intake H-C01…C05 (aggregate answers, outside the repo) |
| Depth | **Deep** — live rows, runnable code, tests, gates | **Shallow** — themes and calendars, no entities for guest segment, occasion, offering, revenue centre, booking or intermediary |
| Example | *"Talk to the GM / Revenue Manager, not IT; use 'the OTA tax'"* (plugin P10, Draft 41 §2.2) | *"Employee discovers a corporate tennis experience → sends to HR → HR requests a proposal"* — **no representation** |

The Hospitality offer **sells** on Plane A and **delivers** on Plane B (a revenue-year content calendar, direct-booking content, booking-journey messaging, guest nurture — Draft 41 D3–D6). The pre-experience methodology, the experience model, the revenue centres and all five relationship pathways in the protocol are Plane B. **This is the single most important structural fact for Hospitality's placement** (files 03, 04, 08).

One place where the two planes have been conflated in the data model: DB 16 Destination Profile's *Primary/Secondary Audiences* — meant to say *"who actually comes here"* — is a relation to DB 9 Audience Roles, whose only allowed values are the four Plane A buyer lenses (`contracts/sector-databases.json`, DB 9 `Role.allowed_values`, DB 16 `Primary Audiences.relation_target`). → `HV-17`.

## 5. Architectural patterns worth naming — reuse these, do not replace them

| Pattern | Where | Why it matters for Hospitality |
|---|---|---|
| **Universal Core / Sector Plugin / Client Instance** (three tiers) | `SECTOR_OS_ARCHITECTURE.md` §2 | The existing, ratified answer to "how does a vertical enter the OS" — *"A plugin supplies values into core fields. It never adds a store, a field, an agent, or an event."* |
| **Roles, not types** | `AEIT_06` §1 | A group, property, outlet and shared service are all `Company`; prospect/client/partner are roles. Prevents a parallel hotel/property registry |
| **Resolution, not storage** | `SECTOR_OS_ARCHITECTURE.md` §4 | A client calendar is computed (`resolve(sector, geography, property_type, client, window)`), never authored as rows |
| **Reality states + named tests** | `AEIT_11` | Lets a Hospitality capability say "designed" without overstating |
| **Totality rule for rule matrices** | `SECTOR_OS_ARCHITECTURE.md` §3.1 + `p2_coverage_gate.py` | Absence is a declared verdict, not a blank — the template for any new hospitality rule table |
| **Authorisation registers** (draft → approved → spent) | `crm_provisioning/provisioning-authorisations.json`, `01_Sector/delivery/delivery-authorisations.json`, `contracts/skill-fixture-authorisations.json` | The most mature approval object in the repo; the natural basis for client/creative approvals (file 13) |
| **Provenance labels** | A001 §4, Draft 41 provenance legend, intake §4 | `[TEST_FIXTURE]`, `[SECTOR]`, `CLIENT-SUPPLIED`, … — the weakest label wins |
| **Namespaces** | `CRM_SCHEMA.md` pilot activation rule | `ORG-*` · `PER-*` · `PILOT-*` · `SIM-*` keep prospects, pilots and simulations from mixing |
| **Reality gating** | `AEIT_10` §1 | New structure waits for activation, incorporation and real content — the owner's standing preference (memory `right-sized-architecture-preference`) |

## 6. Strongest and weakest points

**Strongest (`CONFIRMED`):** sector/destination/calendar intelligence; truth and provenance discipline; separation of real, pilot, fixture and simulation identities; approval-gating in code; honest self-reporting of gaps (most findings in file 14 were first found by the repo's own documents).

**Weakest (`CONFIRMED`):** everything after the sale — delivery, measurement, learning; the client's market (Plane B); public-facing coherence (website and root documents vs. live strategy); work-item and decision bookkeeping (registers drift; the decision tracker is three weeks behind); enforcement at commit time (gates exist and are not run before auto-sync pushes).
