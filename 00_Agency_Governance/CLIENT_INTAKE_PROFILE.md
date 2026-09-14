# Client Intake Profile — Universal Core

**Status:** v0.1-draft — **Claude-synthesized, owner review required.** Built 2026-09-14 from the repository's own schemas, agent input/output contracts and department rules. It invents no client fact, price or legal term.
**Owner:** Mary Thuo (Agency Governance, 00) · consumed by every department listed in §6
**Sector overlay (pilot):** [`02_Offer/Hospitality Revenue Content OS - Pilot Intake Overlay.md`](../02_Offer/Hospitality%20Revenue%20Content%20OS%20-%20Pilot%20Intake%20Overlay.md)
**Runnable gate:** [`intake/intake_gate.py`](intake/intake_gate.py)

> **Why this exists.** `07_Client_Success/CLIENTSUCCESS_OS.md` §10 records that *"concrete intake forms … remain entirely theory-only"*. Meanwhile the first real pilot (`OWNER_INPUT_NEEDED.md` item 72) needs more than a URL: every department downstream reads a different slice of the same company. Without one intake, each department re-asks the client — or worse, guesses. This file is the single question bank. Departments **consume** it; they do not re-author their own.

> **What this file is not.** It is not a client record (no client data lives in this repository), not a contract, not a price sheet, and not permission to contact anyone. It changes no CRM field, agent spec or registry.

---

## 1. How to use it

1. **Universal core (this file) + one sector overlay.** Same pattern as `01_Sector/SECTOR_ACTIVATION_CONTRACT.md` §16: the core never carries a sector's values; the overlay supplies them (room counts, archetypes, booking channels, sector data windows). A new sector gets a new overlay, not a new intake.
2. **Stage by stage.** Ask only what the current stage allows (§2). A question above the current stage is recorded `NOT_ASKED` or `BLOCKED` — never silently skipped.
3. **The fast version = Stage S1 + S2 `R` rows.** The full profile is every row. Filter, don't rewrite.
4. **Every answer carries a label** (§4) and **every question carries a declared state** (§3). A blank is a defect; `UNKNOWN` is an answer.
5. **Answers live in the client folder**, never in this repository (§5). Generate the blank answers file with `python 00_Agency_Governance/intake/intake_gate.py --template <overlay> --out <CLIENT>/intake_answers.json` (the gate refuses a path inside this repository). Validate it at each stage with `--answers <CLIENT>/intake_answers.json` after setting `stage_reached`.
6. **Before any `arika run`**, scan the repo-bound input: `python 00_Agency_Governance/intake/intake_gate.py --scan <CLIENT>/R4_seed_brief.json --key <CLIENT>/pilot_key.json`. Every run's `--input` becomes permanent, auto-synced git history (`Full Push Readiness Packet` §3.3).

---

## 2. Stages — what may be asked, and what gates each one

| Stage | Name | How it is filled | Journey stage (`Draft 41` §6) | Allowed today? | Gate that opens it |
|---|---|---|---|---|---|
| **S1** | **Public desk profile** | Agency only — website, public listings, public media. **No contact with the company.** Manual viewing; no scraping, no account creation, no test booking | 1 Discovery (prep) | ✅ **Yes** | Owner supplies the company (item 72, OI1) |
| **S2** | **Discovery conversation** | A conversation with the company's decision-maker. **No price, quote, proposal or guarantee** — the offer is Not Quotable | 1 Discovery · 2 Qualification | ⛔ **Not in the current push** — the push stops before contacting the property (packet §6) | Owner decision to approach · S1 fit verdict `in scope` |
| **S3** | **Audit data set** | The company's own exports and assets, per the sector overlay's minimum data set | 3 Audit | ⛔ **Blocked** | A signed engagement · a legal review path for audit-data terms (Worksheet G5; LQ1–LQ3) · NDA question answered |
| **S4** | **Onboarding & asset collection** | Contract, billing, contacts, rights, access, operating terms | 6 Agreement · 7 Onboarding · 8 Asset Collection | ⛔ **Blocked** | Proposal/Agreement unblocked (`Draft 41` Phase 11) · Legal-reviewed contract |
| **S5** | **Ongoing measurement** | Recurring client-system data on the §7 cadence | 13 Reporting · 15 Retention | ⛔ **Blocked** (retainer deferred for the MVP) | Onboarding complete · reporting access agreed (O07) |

**Requirement codes used in §8:** `R` required at that stage · `O` optional · `C` conditional (condition stated in the row).

---

## 3. Answer states — absence is declared, never blank

Every question in the answers file holds exactly one state. The gate fails on any question with no state.

| State | Meaning | Must also record |
|---|---|---|
| `ANSWERED` | A value exists | The value **and** its label (§4) |
| `UNKNOWN` | Asked or researched; nobody knows | Who was asked / what was checked |
| `WITHHELD` | The company declined to say | Date declined |
| `NOT_APPLICABLE` | Does not apply to this company | Why |
| `NOT_ASKED` | The stage has not been reached | — |
| `BLOCKED` | A gate forbids asking now | Which gate (e.g. `G5`, `QG5`, `Phase 11`) |

**Rule:** a question marked `R` for a stage the company has *passed* may not be `NOT_ASKED`. It must be answered, `UNKNOWN`, `WITHHELD`, `NOT_APPLICABLE` or `BLOCKED`.

---

## 4. Labels — where every value came from

Carried from `Full Push Readiness Packet` §3.1 and `Draft 41` §2, extended for stages S2–S5.

| Label | Source | May be used as |
|---|---|---|
| `[PUBLIC · url · date]` | Public page viewed by a person | An observation — never a measured figure |
| `[PUBLIC-OTA · url · date]` | Third-party listing, **only if the overlay permits inspection** | Presence/absence facts only — never reviews or reviewer names |
| `[OWNER-SUPPLIED · date]` | Mary Thuo's own knowledge | Context — unverified by definition |
| `[CLIENT-SUPPLIED · title · date]` | Said or written by the company | The company's view or estimate — **never a measured figure** |
| `[CLIENT-SYSTEM · export · period]` | An export from the company's own system | The only label that can support a KPI, verdict or baseline (`Draft 41` QG6) |
| `[SECTOR · confidence]` | Sector (01) intelligence | A benchmark — **never a claim about this company** (QG3) |
| `[INFERENCE]` | Reviewer reasoning | A hypothesis to test — never a finding |

**One-way rule:** a company's answer never becomes a Sector finding, a Content claim, or a case study. Client-supplied data can *prompt* Sector research; it cannot *be* the research (`SECTOR_ACTIVATION_CONTRACT.md` §16 honesty law; IP terms §7).

---

## 5. Where answers live — and what may never be captured

| Location | Holds |
|---|---|
| **Client folder** (outside every git working tree — packet RD2) | `intake_answers.json` · the name ↔ pilot-ID key (`pilot_key.json`) · observation notes · media links · interview notes · every export · every draft |
| **This repository** | The pilot ID, stage verdicts, gate results and changelog lines — **nothing else about the company** |
| **Agent `--input`** | Pilot ID + labelled, non-personal descriptors, **after** `intake_gate.py --scan` passes and the owner approves the exact text (packet PG2) |

**Never captured, at any stage:**
- ❌ Personal data of the company's customers or guests — names, contacts, booking records, identifiable reviews or photos.
- ❌ Named individuals' contact details in the repository or an agent input. Titles only; names and contacts live in the client folder from S4, with consent.
- ❌ Passwords, API keys, logins. Access is **granted** by the company to Arika's accounts (S4, J04); credentials are never collected in an intake.
- ❌ Arika's own prices, fees, bands or discounts (`Draft 41` QG5). The company's *own* published prices are allowed (§8 D).
- ❌ Guarantees or outcome promises written into any answer (MSA §8.3; `Draft 41` "Unrealistic" archetype).

---

## 6. Department coverage — who reads which answers

Every department in `GLOBAL_OS.md` §4 was checked (18 is a reference archive, not a department). "Consumer" names the real schema field or agent contract the answers feed. **Pilot status** is the state for the first Hospitality pilot as of 2026-09-14.

| # | Department | What it needs from the intake | Sections | Consumer (schema / agent) | Pilot status |
|---|---|---|---|---|---|
| 00 | Agency Governance | Labels, declared absence, risk class, no invention | all | Constitution §3, §5 · `OWNER_INPUT_NEEDED.md` | ✅ applies now |
| 01 | Sector | Sector and company fit — business model, geography, size, anti-ICP, buyer titles | A, B01, overlay | Packet R2 fit record · S10 hand-off packet · DB 2 / 4 / 10 / 11 / 16 *read-only reference* | ✅ S1 — manual fit check (RD4) |
| 02 | Offer | Seed brief: what they sell, pricing model, problem, constraints; overlay data set | A, C, D, L, overlay | `offer-orchestrator.seed_brief` · `offer-oeos-engineer` · `Draft 41` §3 diagnostic gate | ✅ S1 → R4–R6 |
| 03 | Marketing | Channels, funnel, discoverability, paid media | H, I | `marketing-market-intelligence.context` · `marketing-funnel-architect` · `marketing-seo-aeo-geo` | ◐ hand-off note only (RD6) |
| 04 | Content | Offers, audience, brand language, media, campaign history | C, E, F, G | `content-intelligence-hub` source `client` — **a client insight never becomes Arika content without consent (O06) and a proof method (QG2, blocked)** | ◐ held at PG5 |
| 05 | Sales | Fit, pain, authority, timing, decision chain | B, E, L | `sales-lead-qualification` (needs a CRM `lead_id` — none in the push) · `sales-customer-psychology.decision_chain` | ◐ hand-off note only |
| 06 | ClientPartner Acquisition | The 12-input acquisition intake | A03, C01–C05, E01, G, H, I, L01, M01 | `clientpartner-acquisition-diagnostic.intake_completeness` (0–12) — mapping in §8 note | — not in the MVP scope |
| 07 | Client Success | Onboarding's 5 layers, success metrics, segmentation inputs | B04, L01–L02, O, P | `client-success-onboarding` (6-check diagnostic, `success_metrics`, `scope_summary`) · `client-success-segmentation` | ⛔ S4 blocked |
| 08 | Operations | Required inputs, delay risks, approval turnaround, kickoff | J04, M03, P05 | `operations-delivery-scheduler.required_inputs` / `delay_risks` · `operations-capacity-planner` (one client at a time, Worksheet §6.1) | ⛔ S4 blocked |
| 09 | Finance | Billing identity, segment, acquisition channel | A10–A13, B08 | Zoho Books contact + invoice · `finos.clients` (`name`, `segment`, `acquisition_channel`) · CRM `Invoice` | ⛔ S4 blocked · Zoho Books trial expired (`CRM_SCHEMA.md`) |
| 10 | Legal | Legal identity, personal-data processing, NDA, asset rights, publicity consent | A10–A11, G04, G08, N, O | `SOW_TEMPLATE.md` §5, §9, §10 · `DPA.md` Annex A · IP terms §7–§8 · `legal-counsel-router` | ⛔ G5 — templates unreviewed |
| 11 | HR / People Ops | Only if a `team` diagnosis is ever scoped | M01 | `hr-engagement-classifier` | — not in the MVP |
| 12 | Branding | Brand evidence: positioning, voice, visuals, competitors | C04–C05, E01, F | BOIS `client_object` → `branding-brand-definition` | ⛔ **blocked by gap §9 G-1** (workspace inside the repo) |
| 13 | Tech Stack | The company's systems and the access pattern | J | Verify-don't-assume discipline — **client tools are not Arika inventory** | ◐ S2 questions only |
| 14 | Audits & Diagnostics | Data availability and quantification depth | J03, K | `audits-data-access-gate` (`access_state`, `quantification_depth`) — see §9 G-4 | ⛔ S3 blocked |
| 15 | Consulting & Advisory | Nothing new — reuse audit findings on ascension | — | `consulting-advisory-prep.data_available` | — not in the MVP |
| 16 | Automation | Processes, systems, messaging tools, consent | J, M04, N | `automation-process-architect.processes` · `automation-approval-gate` (QG8) | — nurture deferred |
| 17 | AI Enablement | Data quality, AI literacy, process maturity | J05, K01, M04 | `ai-enablement-readiness-assessor` | — not in the MVP |
| 19 | Design | Brand kit, media inventory, asset rights | F02, G | `design-asset-librarian` · `design-brand-environment-consistency-checker` | — no production in the MVP |
| 20 | Experience Engineering | Website facts, CMS, sections, media | C, G, H07–H08 | `creative-direction` skill brief (purpose, audience, feeling, sections, constraints) | — no implementation in the MVP |
| 21 | Presence | The company's own presence layers and reputation surfaces | F05–F06, H | Presence Layer Registry pattern, applied to the client | — not in the MVP |

**ClientPartner 12-input mapping** (`clientpartner-acquisition-diagnostic`): 1 business model → A03 · 2 what they sell → C01–C02, D02 · 3 ideal client → E01–E02 · 4 transformation → C05 · 5 proof/assets → F05, G01–G03 · 6 acquisition situation → I01–I02 · 7 clients wanted most → E01 (S2) · 8 partners wanted → I05 · 9 channels used → H01–H06 · 10 capacity → M01–M02 · 11 revenue target + timeframe → L01 · 12 acquisition system wanted → L03 (S2).

---

## 7. Data cadence — one-time, weekly, monthly, quarterly, yearly

**Only client-system data can fill a recurring row** (`Draft 41` QG6). Nothing below is estimated to fill a gap.

**Stage S5 has no question rows, by design** — the gate reports `S5 0 0 0`. Recurring data is not a new question; it is the S3 data set repeated on the cadence below, agreed at onboarding through U-P06 (success measures and baseline) and U-O07 (outcome-data sharing). Rows are added to S5 only if a retainer is engineered.

| Cadence | What is collected | Why | Owner / consumer | Status |
|---|---|---|---|---|
| **One-time snapshot** | Every §8 question, stage by stage | The profile itself | All departments (§6) | S1 now; S2–S4 gated |
| **Audit window** | The overlay's minimum data set (hospitality: last **3 months** by channel, MD1–MD3) | Diagnosis | Offer (02) · Audits (14) | ✅ owner-approved (Worksheet §1.4); S3 blocked |
| **Seasonal baseline** | The **same months last year**, or **12–24 months by month**, *if available* | A 3-month window is not a seasonal baseline; a 6-month result can be caused by the season, not the work (`Draft 41` Phase 7) | Offer (02) — M6 measurement plan | ⏳ **Ask as optional.** Whether it is required is **open** (Worksheet §8 #22) |
| **Weekly** | **Nothing required** by any approved decision. Daily/weekly exports are useful only for event-week analysis (plugin P13 compression) | — | Sector (01) | Optional; do not request by default |
| **Monthly** | Reporting pack: direct share, commission cost per room-night, need-date occupancy, net RevPAR (hospitality `Draft 41` D7) · Client Success health review | Measurement against baseline · retention | Offer (02) · Client Success (07) | ⛔ retainer deferred for the MVP |
| **Quarterly** | QBR · strategic review · re-check of goals (L01) and archetype signals | Renewal, expansion, risk | Client Success (07) · Sales (05) | ⛔ post-onboarding |
| **Yearly** | Revenue-year content calendar (12 months ahead; plugin P7 offsets reach T-365) · year-on-year comparison · refresh of S1 public profile | Planning ahead of need-dates | Content (04) · Sector (01) | ⛔ post-onboarding |
| **Event-driven** | Material change at the company (ownership, system, brand) · contract end 60–90 days out · health drop | Re-scope, offboarding | Client Success (07) | ⛔ post-onboarding |

---

## 8. Question bank — universal core

**Format (machine-read by `intake/intake_gate.py`):** `| ID | Question | Stage | Req | Label | Feeds | If missing |`. `Stage` is the **earliest** stage at which the row is due; a row asked publicly in S1 and confirmed in S2 is listed at S1. Cross-references elsewhere drop the `U-` prefix (A03 = U-A03). The sector overlay adds `H-` rows and may mark a core row `NOT_APPLICABLE` — it may not delete one.

### A — Company identity & structure

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-A01 | Trading / brand name of the company | S1 | R | PUBLIC | Client-folder key → pilot ID · BOIS `company_name` · later CRM company / `finos.clients.name` | **Stop — nothing to profile** |
| U-A02 | Website URL | S1 | R | PUBLIC | MD4-type path review · Presence owned-website layer · overlay anti-ICP rule | Record `NONE`; the overlay decides whether that stops |
| U-A03 | Business model — independent · group-affiliated · owner-operated · management contract · franchise · other (say what) | S1 | R | PUBLIC | DB 2 `Business Model` vocabulary · 06 intake #1 | `UNKNOWN`; confirm in S2 |
| U-A04 | Parent group, brand or chain affiliation, if any | S1 | R | PUBLIC | AEIT_06 `Company` roles · overlay anti-ICP | `UNKNOWN` |
| U-A05 | Is there a central marketing or direct-sales team above this business that controls its website and campaigns? | S1 | R | PUBLIC | Anti-ICP (hospitality: Decision 71 H3 condition) | `UNKNOWN` at S1 → must be answered at S2 |
| U-A06 | Number of locations / properties / units in scope | S1 | R | PUBLIC | Size band · Offer scope · `finos.entities.parent_entity_id` | `UNKNOWN` |
| U-A07 | Location of each unit — country, town, destination | S1 | R | PUBLIC | DB 11 Geography · DB 16 Destination Profile · Legal jurisdiction | **Stop** — geography scope cannot be checked |
| U-A08 | Size indicator in the overlay's unit (e.g. rooms, seats, staff, ARR) | S1 | O | PUBLIC | Overlay size band · ICP fit | `UNKNOWN` — **never estimate** |
| U-A09 | Operating since (year) | S1 | O | PUBLIC | BOIS `narrative_memory` · proof context | `NOT_ASKED` acceptable |
| U-A10 | Registered legal name | S4 | R | CLIENT-SUPPLIED | SOW / MSA client party · Zoho Books contact · `finos.entities.legal_name` | Cannot contract or invoice |
| U-A11 | Legal person type and jurisdiction of registration | S4 | R | CLIENT-SUPPLIED | Client Legal Identity checkpoint (Client Success Draft 11) · Legal (10) | Legal cannot assess |
| U-A12 | Tax registration identifier the company requires on invoices — *Condition: the company or the accountant says invoices must carry one; requirement not assessed here* | S4 | C | CLIENT-SUPPLIED | Zoho Books contact · Finance compliance | Finance (09) decides |
| U-A13 | Billing contact title, billing address, purchase-order or supplier-registration requirements | S4 | R | CLIENT-SUPPLIED | Zoho Books invoice · SOW §6 | Invoice cannot be issued |

### B — People, decision rights & relationship

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-B01 | Which decision-maker **roles** exist — owner/MD, general manager, commercial/revenue lead, sales & marketing lead, other? **Titles only** | S1 | R | PUBLIC | DB 10 Decision-Maker titles · `sales-customer-psychology.decision_chain` | `UNKNOWN` |
| U-B02 | How does Arika know this company — cold · known contact · referral · partner introduction · inbound enquiry · event | S1 | R | OWNER-SUPPLIED | CRM `Lead.source` · `Partner.sourced_opportunity_ids` · packet OI9 | Record `cold` only if true; otherwise `UNKNOWN` |
| U-B03 | Any past approach or conversation — date, channel, outcome | S1 | O | OWNER-SUPPLIED | `sales-follow-up-recovery` · OI9 | None assumed |
| U-B04 | Who holds final spend authority? (title) | S2 | R | CLIENT-SUPPLIED | Sales qualification — authority · `Draft 41` §2.2 | `needs_more_discovery` |
| U-B05 | Who holds the operational data and can export it? (title) | S2 | R | CLIENT-SUPPLIED | `Draft 41` Phase 8 data-access owner · `audits-data-access-gate` | S3 cannot open |
| U-B06 | Who approves deliverables and public messaging? (title) | S2 | R | CLIENT-SUPPLIED | Onboarding diagnostic check 5 (control structure) · Phase 8 approver | Onboarding check 5 fails |
| U-B07 | How is a purchase like this decided — steps, who is consulted, sign-off order, usual time to decide | S2 | R | CLIENT-SUPPLIED | `decision_chain` · CRM `Opportunity.close_date_target` | `needs_more_discovery` |
| U-B08 | How many people will be involved in approvals? | S2 | O | CLIENT-SUPPLIED | Size-band buying process · Worksheet communication effort | `UNKNOWN` |
| U-B09 | Named contacts — name, title, email, phone — **client folder only**, collected with consent | S4 | R | CLIENT-SUPPLIED | CRM `Lead.contact_name` / `contact_email` · SOW §9 contacts | Onboarding check 1 fails |

### C — What they sell: products, services & descriptions

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-C01 | List of products / services / packages, in the company's own words | S1 | R | PUBLIC | BOIS `products` / `services` · 06 intake #2 · Content `client` source | `UNKNOWN` |
| U-C02 | For each: one-line description, who it is for, one-time or recurring | S1 | O | PUBLIC | `clientpartner-acquisition-diagnostic.current_state.offers` | Complete at S2 |
| U-C03 | Which offer matters most commercially — flagship, highest volume, highest margin — **as the company states it** | S2 | R | CLIENT-SUPPLIED | Offer mapping · recommendation focus | `UNKNOWN` — never inferred from the website |
| U-C04 | Why customers choose them over alternatives (their stated reasons) | S1 | R | PUBLIC | BOIS `market_position` · positioning formula · QG7 | Complete at S2 |
| U-C05 | The change or outcome the customer gets | S2 | R | CLIENT-SUPPLIED | 06 intake #4 · BOIS `emotional_positioning` | `UNKNOWN` |
| U-C06 | Offers, packages or promotions currently live, with dates | S1 | O | PUBLIC | Campaign history · Sector signal timing | `NONE FOUND` with date checked |
| U-C07 | What they deliberately do **not** sell or do | S2 | O | CLIENT-SUPPLIED | Avoids recommending the wrong thing | — |

### D — The company's own pricing *(theirs — never Arika's)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-D01 | Publicly published prices or "from" prices, per offer, with the date viewed | S1 | O | PUBLIC | Context for the seed brief · BOIS `pricing_model` | `NOT PUBLISHED` with date checked |
| U-D02 | Pricing model — fixed · per unit · per package · seasonal · dynamic · negotiated/contracted | S2 | R | CLIENT-SUPPLIED | BOIS `pricing_model` · early signal for a pricing-cause redirect (`Draft 41` class c) | `UNKNOWN` |
| U-D03 | Is there a reason to buy direct rather than through a third party (benefit, offer, guarantee)? | S1 | R | PUBLIC | Direct-channel messaging diagnosis (`Draft 41` class b-messaging) · M3 | `NONE FOUND` with date checked |
| U-D04 | Who sets prices, with which tool or process | S2 | R | CLIENT-SUPPLIED | Redirect detection · J systems | `UNKNOWN` |
| U-D05 | Channel price position / parity policy — **from client systems only**, never from public observation | S3 | C | CLIENT-SYSTEM | `Draft 41` class (c) evidence · redirect P4a. *Condition: only if pricing is suspected (MD8)* | Recorded `UNKNOWN` |

> **QG5 applies to the whole intake.** No Arika price, fee, band, discount or credit appears in any answer, note or seed brief while the offer is Not Quotable. `intake_gate.py --scan` checks for currency and price language.

### E — Customers & markets *(aggregates only — no personal data)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-E01 | Main customer segments, in the company's words — and which segments they want more of | S2 | R | CLIENT-SUPPLIED | BOIS `audience` · `content-intelligence-hub.audience_map` · 06 intake #3, #7 | `UNKNOWN` |
| U-E02 | Where customers come from — regions/countries, domestic vs international — with shares only if measured | S2 | R | CLIENT-SUPPLIED | Relevance of DB 15 Market Routes · content calendar focus | Shares `UNKNOWN`; never estimated |
| U-E03 | Why customers buy — the purposes behind a purchase | S2 | R | CLIENT-SUPPLIED | Overlay demand vocabulary (as the company's belief) · BOIS `psychographics` | `UNKNOWN` |
| U-E04 | What triggers a purchase, what influences the choice, what makes customers cancel or leave | S2 | O | CLIENT-SUPPLIED | `sales-customer-psychology.pain_architecture` | `UNKNOWN` |
| U-E05 | Busiest and quietest months, as the company experiences them | S2 | R | CLIENT-SUPPLIED | Seasonality check against Sector signals · delivery timing (approvals slow in peak) · Worksheet Q8 | `UNKNOWN` |
| U-E06 | Repeat-customer share — measured figure or "not measured" | S3 | O | CLIENT-SYSTEM | Retention narrative · future nurture case | `NOT MEASURED` |
| U-E07 | Languages customers are served in | S2 | O | CLIENT-SUPPLIED | Content translation · website build | `UNKNOWN` |

### F — Positioning, brand & competitors

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-F01 | How the company describes itself in one sentence (verbatim, with source) | S1 | R | PUBLIC | BOIS `market_position` | Ask at S2 |
| U-F02 | Which brand assets exist — logo files, colours, fonts, guidelines — format and owner | S2 | R | CLIENT-SUPPLIED | BOIS `color_preferences` / `typography_preferences` / `visual_preferences` · Design consistency checker | `branding-brand-definition` would emit `BRAND_EVIDENCE_INCOMPLETE` |
| U-F03 | Tone of voice — words they use and words they avoid | S2 | O | CLIENT-SUPPLIED | BOIS `communication_style` · Content avoid-terminology | `UNKNOWN` |
| U-F04 | Competitors or comparison set the company names | S2 | R | CLIENT-SUPPLIED | BOIS `competitors` · AEIT_06 `Competitor` role | `UNKNOWN` — never inferred |
| U-F05 | Awards, certifications, memberships, press coverage | S1 | O | PUBLIC | Presence authority layer · client-owned proof | `NONE FOUND` with date checked |
| U-F06 | Public review platforms and headline rating — **score and count only; never review text or reviewer names** | S1 | O | PUBLIC | Presence reputation layer · proof context | `NOT CHECKED` |
| U-F07 | Brand and legal approval rules — who must sign off before anything public | S2 | R | CLIENT-SUPPLIED | Hospitality MD8 · Content publishing gate · Phase 8 | `UNKNOWN` — assume sign-off needed |

### G — Media & content inventory

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-G01 | Public media found — photo galleries, videos, virtual tours, brochures — each with URL and date viewed | S1 | O | PUBLIC | Design asset reuse check · website build · Presence video layer | `NONE FOUND` with date checked |
| U-G02 | Photography library — does one exist, roughly how large, how recent, which subjects | S2 | R | CLIENT-SUPPLIED | `design-asset-librarian` (client scope) · Content formats | `UNKNOWN` |
| U-G03 | Video — brand films, tours, reels, drone footage, testimonials — list what exists | S2 | R | CLIENT-SUPPLIED | Design Production Engine · Content native formats | `UNKNOWN` |
| U-G04 | Other assets — brochures, menus, fact sheets, press kit, floor plans, presentations | S2 | O | CLIENT-SUPPLIED | Sales enablement · Design · website build | `UNKNOWN` |
| U-G05 | Recent campaigns (last 12 months) — channel, date, goal, and outcome **only if measured** | S2 | O | CLIENT-SUPPLIED | BOIS `campaign_history` · hospitality MD6 | `NONE` / `UNKNOWN` |
| U-G06 | Content produced in-house vs by agencies or freelancers, and how often | S2 | O | CLIENT-SUPPLIED | 06 intake #10 capacity · Worksheet content effort | `UNKNOWN` |
| U-G07 | **Rights, per asset set** — who created it; does the company own it or hold a licence; does the licence cover web, social and paid use; releases for identifiable people | S4 | R | CLIENT-SUPPLIED | IP terms §3.5, §8.1, §8.4 (*"the client sent it" is not a licence*) · Legal (10) | **Asset may not be used** |
| U-G08 | Where assets are stored and how access is granted (shared link, drive, asset system) | S4 | R | CLIENT-SUPPLIED | Client folder · Tech Stack verify-live | Assets unavailable |
| U-G09 | Consent held to feature identifiable customers, guests or staff in existing media | S4 | C | CLIENT-SUPPLIED | IP terms §7 · claims policy · QG2. *Condition: any asset shows identifiable people* | **Do not use those assets** |

### H — Digital presence & channels

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-H01 | Social accounts, per platform — URL, active or dormant, date of last post | S1 | R | PUBLIC | Presence layer map (client) · Content DB 3 platform overlay · `marketing-demand-generation` | `NONE FOUND` per platform checked |
| U-H02 | Search and map listings — business profile, maps, directories | S1 | O | PUBLIC | `marketing-seo-aeo-geo` · Presence discovery layer | `NOT CHECKED` |
| U-H03 | Primary call-to-action on the website | S1 | R | PUBLIC | Hospitality MD4 · journey blueprint | `NONE FOUND` |
| U-H04 | Third-party marketplaces, aggregators or listings the company says it uses — *Arika's own inspection is governed by the overlay's permission rule* | S2 | R | CLIENT-SUPPLIED | Distribution mix · audit context | `UNKNOWN` |
| U-H05 | Who runs social media and the website today — in-house role, agency or nobody | S2 | R | CLIENT-SUPPLIED | Capacity · hand-off risk | `UNKNOWN` |
| U-H06 | Email newsletter or customer list tool — exists? which platform? | S2 | O | CLIENT-SUPPLIED | `marketing-lifecycle` · nurture (deferred) · QG4 | `UNKNOWN` |
| U-H07 | Messaging channels used with customers (e.g. WhatsApp Business) | S2 | O | CLIENT-SUPPLIED | `Draft 41` Phase 8 · nurture (deferred) | `UNKNOWN` |
| U-H08 | Website platform/CMS, who can edit it, and whether analytics is installed (which tool) | S2 | R | CLIENT-SUPPLIED | Experience Engineering technical assessment · M6 measurement | `UNKNOWN` — measurement plan limited |
| U-H09 | Paid advertising — channels active, yes/no (spend only at S3, client-supplied) | S2 | O | CLIENT-SUPPLIED | `marketing-attribution-modeling` | `UNKNOWN` |

### I — How customers buy: sales & distribution

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-I01 | Every direct purchase path visible publicly — website, phone, email, messaging, walk-in — with the steps up to the public boundary | S1 | R | PUBLIC | Hospitality MD4 · `marketing-funnel-architect` · class (b) diagnosis | Overlay decides whether this stops |
| U-I02 | Intermediaries — agents, resellers, operators, marketplaces, corporate or contracted accounts | S2 | R | CLIENT-SUPPLIED | 06 intake #6 · channel mix · the company's partner landscape | `UNKNOWN` |
| U-I03 | What happens after an enquiry — who responds, through which tool, how fast | S2 | O | CLIENT-SUPPLIED | 06 control points: speed-to-lead, follow-up | `UNKNOWN` |
| U-I04 | Where the company believes sales are lost | S2 | O | CLIENT-SUPPLIED | 06 friction diagnosis · audit hypothesis (never a verdict) | `UNKNOWN` |
| U-I05 | Partners or introducers the company wants more of | S2 | O | CLIENT-SUPPLIED | 06 intake #8 | `UNKNOWN` |

### J — Systems & tech stack

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-J01 | Systems in use, per the overlay's categories — vendor name and who administers each | S2 | R | CLIENT-SUPPLIED | `automation-process-architect` · `ai-enablement-readiness-assessor.data_quality` · class (d) diagnosis | `UNKNOWN` per category |
| U-J02 | Known integration or sync problems between systems | S2 | O | CLIENT-SUPPLIED | Class (d) redirect signal · Stack Rationalization gap | `UNKNOWN` |
| U-J03 | Which systems can export reports, in what format, covering how many months | S2 | R | CLIENT-SUPPLIED | `audits-data-access-gate.access_state` · feasibility of the overlay data set · analytics effort band | `UNKNOWN` — S3 scope unknown |
| U-J04 | Access Arika would need, read-only by default, and who grants it — **never share passwords; access is granted to Arika's own accounts** | S4 | R | CLIENT-SUPPLIED | Tech Stack verify-live · SOW §5 dependencies · DPA sub-processing | Work cannot start |
| U-J05 | Current AI tool use and any AI-use policy the company has | S2 | O | CLIENT-SUPPLIED | Legal LQ4 · `team_ai_literacy` | `UNKNOWN` |

### K — Performance data: availability, then the data

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-K01 | Which performance measures are tracked today, where, and by whom | S2 | R | CLIENT-SUPPLIED | `audits-data-access-gate.quantification_depth` · QG6 | `UNKNOWN` |
| U-K02 | Months of history available per data source | S2 | R | CLIENT-SUPPLIED | Seasonal baseline (§7; Worksheet §8 #22) | `UNKNOWN` |
| U-K03 | The overlay's minimum data set, as exports | S3 | R | CLIENT-SYSTEM | Diagnosis — hospitality MD1–MD3 | Overlay sufficiency rule applies |
| U-K04 | Seasonally comparable period — same months last year or 12–24 months by month, *if available* | S3 | O | CLIENT-SYSTEM | M6 baseline | State the limitation in the measurement plan |
| U-K05 | Cost of third-party channels — actual figure from systems, or the company's own estimate, labelled as such | S3 | R | CLIENT-SYSTEM | Hospitality MD3 · QG6 | Recorded `UNKNOWN` — **never invented** |

> **Verbal figures are estimates.** Any number the company states in conversation is recorded `[CLIENT-SUPPLIED]` and can never support a verdict, a baseline or a claim.

### L — Goals, problems, what's been tried, constraints

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-L01 | Top goal for the next 12 months, stated measurably by the company — with its timeframe | S2 | R | CLIENT-SUPPLIED | `client-success-onboarding.clarity_scan` · 06 intake #11 · Sales pain/urgency | `needs_more_discovery` |
| U-L02 | What success would look like at 30, 60 and 90 days — **in the company's words; Arika promises nothing** | S2 | R | CLIENT-SUPPLIED | Onboarding form (Client Success Draft 16) · `Draft 41` "Unrealistic" archetype prevention | `UNKNOWN` |
| U-L03 | The problem the company believes it has, and how it knows | S2 | R | CLIENT-SUPPLIED | Sales pain · audit hypothesis · 06 intake #12 | `UNKNOWN` |
| U-L04 | What has been tried, with whom, and what happened | S2 | R | CLIENT-SUPPLIED | Onboarding form · risk of repeating a failed approach | `UNKNOWN` |
| U-L05 | Why now — the trigger, deadline or season | S2 | R | CLIENT-SUPPLIED | Sales timing · Sector signal timing | `UNKNOWN` |
| U-L06 | Constraints — tool access, approvals, brand or legal review, internal politics, budget process | S2 | R | CLIENT-SUPPLIED | Hospitality MD8 · SOW §5, §11 | `UNKNOWN` |
| U-L07 | Causes the company suspects lie outside messaging — pricing, technology, staffing | S2 | O | CLIENT-SUPPLIED | Early redirect signal (`Draft 41` §3) | `UNKNOWN` |
| U-L08 | Past agency or consultant experiences — what went wrong | S2 | O | CLIENT-SUPPLIED | `sales-customer-psychology.trust_gaps` · client risk archetypes | `UNKNOWN` |

### M — The company's own operations & capacity

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-M01 | Team size and structure around sales and marketing | S2 | R | CLIENT-SUPPLIED | 06 intake #10 · `automation-process-architect.org_shape` | `UNKNOWN` |
| U-M02 | Time the decision-maker and data owner can give an engagement | S2 | R | CLIENT-SUPPLIED | `Draft 41` Ghost/Quitter risk · Operations delay risks | `UNKNOWN` — flag as risk |
| U-M03 | Usual approval turnaround, and periods when the team cannot engage | S2 | R | CLIENT-SUPPLIED | `operations-delivery-scheduler.delay_risks` · `Draft 41` Phase 7 | `UNKNOWN` |
| U-M04 | Documented sales/marketing processes — exist? where? | S2 | O | CLIENT-SUPPLIED | `automation-process-architect.processes` · `process_maturity` | `UNKNOWN` |
| U-M05 | Working language, time zone and working hours | S4 | R | CLIENT-SUPPLIED | Phase 8 communication charter · SOW §9 | Default to agency norms, noted |

### N — Customer communication & consent

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-N01 | Public privacy notice on the website — yes/no, link | S1 | O | PUBLIC | `legal-exposure-register` context · LQ1 | `NONE FOUND` |
| U-N02 | Automated customer messages that exist — confirmation, pre-arrival or onboarding, follow-up — **templates or redacted samples only** | S3 | O | CLIENT-SUPPLIED | Hospitality MD5 · messaging diagnosis | `NONE` / `UNKNOWN` |
| U-N03 | Customer contact lists — exist? approximate size? consent basis recorded per list? | S4 | C | CLIENT-SUPPLIED | QG4 (blocked) · Legal LQ1 · `marketing-lifecycle`. *Condition: any messaging work is scoped* | Nurture stays blocked |
| U-N04 | Customers located outside Kenya (e.g. EU, UK) in those lists | S4 | C | CLIENT-SUPPLIED | LQ1 — which data regime applies · DPA. *Condition: N03 answered yes* | Treat as unresolved legal question |

### O — Commercial & legal readiness

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-O01 | Is an NDA needed before any data is shared? | S3 | R | CLIENT-SUPPLIED | LQ3 · `NDA.md` (unreviewed) | `BLOCKED` (G5) until counsel answers |
| U-O02 | Does the engagement involve Arika processing personal data? — **answered with counsel, not by the intake** | S4 | R | CLIENT-SUPPLIED | SOW §10.1 · DPA Annex A | `BLOCKED` (G5) |
| U-O03 | Authorised signatory — title (name in client folder) | S4 | R | CLIENT-SUPPLIED | SOW signature block · Legal Identity "Authority" | Cannot sign |
| U-O04 | Supplier documents the company requires from Arika | S4 | O | CLIENT-SUPPLIED | `[ARIKA LEGAL ENTITY]` placeholder (Legal §1) · Finance | `UNKNOWN` |
| U-O05 | At the end of the engagement: return or delete the company's data? | S4 | R | CLIENT-SUPPLIED | DPA Annex A §7 · Client Success offboarding step 5 | Default per DPA: delete |
| U-O06 | Publicity consent — may Arika name the company, use its logo, publish a case study? **Three separate consents** | S4 | R | CLIENT-SUPPLIED | IP terms §7.1–§7.4 · `client-success-advocacy` · QG2 | **Default: no** |
| U-O07 | Will the company share outcome data after delivery, so results can be measured? | S4 | R | CLIENT-SUPPLIED | `Draft 41` "Result Ghoster" prevention · proof method (blocked) | Results recorded as unmeasured |

### P — Engagement operating terms *(the onboarding control layer)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| U-P01 | Single point of contact on each side | S4 | R | CLIENT-SUPPLIED | Onboarding check 1 (confirmation) · Phase 8 | Check 1 fails |
| U-P02 | Channels agreed — decisions in writing by email; messaging for coordination only; video for reviews | S4 | R | CLIENT-SUPPLIED | Onboarding check 5 · Phase 8 | Check 5 fails |
| U-P03 | Approval window and response expectations — *durations are OPEN in `Draft 41` Phase 8; the intake records the company's need, it does not set an SLA* | S4 | R | CLIENT-SUPPLIED | Phase 8 · SOW §8 | `OPEN` |
| U-P04 | Revision rule acknowledged — one included round per output (**internal MVP policy, not contract language until Legal reviews**) | S4 | R | CLIENT-SUPPLIED | Worksheet §1.3 · SOW §8 | Check 3 fails |
| U-P05 | Kickoff date and first visible milestone | S4 | R | CLIENT-SUPPLIED | Onboarding check 6 (momentum) · `operations-delivery-scheduler` | Check 6 fails |
| U-P06 | Success measures and baseline period agreed | S4 | R | CLIENT-SUPPLIED | `client-success-onboarding.success_metrics` · M6 | Check 2 fails |

**Onboarding diagnostic mapping** (Client Success Draft 16, 6 checks, 5–6 pass = proceed): 1 Confirmation → P01, B09 · 2 Outcome clarity → L01, L02, P06 · 3 Scope control → P04 + the SOW §3 exclusions · 4 Input readiness → G07, G08, J04, K03 · 5 Control structure → B06, P02, P03 · 6 Momentum → P05.

---

## 9. Gaps surfaced while building this — reported, not worked around

| # | Gap | Evidence | Effect on the pilot | Class of fix |
|---|---|---|---|---|
| **G-1** | **Branding writes client workspaces inside this repository.** `create_client_workspace()` builds `12_Branding/bois/clients/<slug>/memory/client.json`, and every change in this repo is auto-committed and pushed. The MVP rule puts client data **only** in a client folder outside every git tree (Worksheet §5.2) | `12_Branding/bois/core/client_workspace.py:28-34` | `branding-brand-definition` cannot run on the pilot's brand evidence (section F) without putting client data in git history | Make the BOIS workspace root configurable to the client folder — a code change, owner decision (§10 ID2) |
| **G-2** | **No `Company` object exists in the CRM.** `CRM_SCHEMA.md` defines Lead, Opportunity, Client, Engagement/Project, Invoice, Partner; ClickUp has those five lists. Sector's contracts and `AEIT_06` §2 treat a property as a CRM `Company` row, but `Company` is a **[NEW] blueprint entity**, not built | `CRM_SCHEMA.md` Core Objects; `AEIT_06` §2 Party domain; `SECTOR_NOTION_SCHEMA.md` §3 | A prospect has no CRM home before it becomes a Lead. **Not a push blocker** — the push creates no CRM row | Architecture decision already queued in AEIT; not decided here |
| **G-3** | **Every agent that consumes intake answers takes a free-text string** (`client`, `seed_brief`, `context`, `source_signal`). Nothing in the runtime checks labels, personal data or prices before a run writes its input to git | Agent frontmatter `inputs:` across 07, 02, 03, 04, 16, 17; `arika-runtime/src/memory-writer.ts` (packet §3.3) | A careless paste becomes permanent history | **Runnable now:** `intake_gate.py --scan`. Wiring it into `arika run` is a runtime change — §10 ID5 |
| **G-4** | **Audits & Diagnostics agents are shaped for offer #10, not the hospitality audit.** `audits-scoping` allows only `funnel · sales · crm · automation · acquisition · team · offer` sub-audits, tiers `lite…scale_enterprise`, 7–14 days; the hospitality audit is defined by Offer's MD1–MD8 | `.claude/agents/audits-scoping.md`, `audits-data-access-gate.md` output schemas | No agent can scope or data-gate a hotel audit — the same class as the packet's finding that no Sector agent can fit a hotel (RD4) | Not a push blocker (no audit in the push); record before S3 |
| **G-5** | **Arika's own legal entity is unresolved.** Every template carries `[ARIKA LEGAL ENTITY]` | `10_Legal/LEGAL_OS.md` changelog 2026-07-15; `SOW_TEMPLATE.md` checklist | S4 cannot complete whatever the company answers | Owner + counsel (item 59) |
| **G-6** | **No registered way to collect S2/S4 answers.** No form tool is registered, and a hosted form holding client answers would be a sub-processor (Worksheet §11 LQ2) | `13_Tech_Stack/TECHSTACK_OS.md` §3; Worksheet §11.3 | Default path: the owner types answers into the client-folder answers file | §10 ID6 |

---

## 10. Owner decisions this profile needs

Rolled up to `OWNER_INPUT_NEEDED.md` item 73. **Decide first; nothing here is applied to live CRM, agent specs or registries until decided.**

| ID | Decision | Recommended default | Blocks |
|---|---|---|---|
| **ID1** | Ratify, cut or amend this profile — and fix the **fast row set** | Fast set = every S1 and S2 row marked `R`; everything else stays in the bank, stage-gated | Using the profile on the pilot |
| **ID2** | G-1 — BOIS workspace location | Keep Branding (12) off client data until the workspace root can point at the client folder | Branding on any real client |
| **ID3** | When the pilot may be contacted for S2 | Only after packet R8 (owner review of the Offer output); prefer the property's low season (plugin P13) | S2 |
| **ID4** | Seasonal baseline — optional ask or required (Worksheet §8 #22) | Optional ask (U-K04, H-E09); M6 states the limitation when absent | M6 validity |
| **ID5** | G-3 — make `intake_gate.py --scan` a mandatory pre-run step inside `arika run`, or keep it manual | Manual for the pilot (runtime change deferred); required by packet PG2 checklist | Class-of-defect closure |
| **ID6** | G-6 — how S2/S4 answers are collected | Owner-typed notes into the client-folder answers file; no hosted form until LQ2 is answered | S2, S4 |

---

## 11. Changelog

- **2026-09-14 — Created (v0.1-draft, Claude-synthesized, owner review required).** Universal client intake profile built from a full-repository pass — `GLOBAL_OS.md`; every department's OS file; `CRM_SCHEMA.md`; `AGENCY_KPI_DICTIONARY.md`; `SECTOR_NOTION_SCHEMA.md` DB 2/4/15/16 and §3; `CONTENT_INTELLIGENCE_SCHEMA.md` DB 3–8; BOIS `client_object` schema; `finos` database schema; the Legal SOW, DPA, and IP templates; the agent input/output contracts of 28 agents across 17 departments; Client Success Draft 16 (onboarding); the two client-portfolio drafts (Offer 16, Marketing 24); and, for the pilot, the Hospitality plugin, `Draft 41`, the Delivery Capacity worksheet and the Full Push Readiness Packet. Adds: five gated stages (S1 public → S5 ongoing), six declared answer states, seven labels, storage and never-capture rules, a 21-department coverage matrix, a data-cadence table (one-time → yearly), **111 universal questions in 16 sections** (gate count; 148 with the Hospitality overlay; fast set of S1 + S2 required rows = 65) with stage, requirement, label, consumer and missing-value rule, the ClientPartner 12-input and onboarding-diagnostic mappings, six surfaced gaps (G-1 BOIS writes client workspaces into git; G-2 no CRM `Company`; G-3 free-text agent inputs; G-4 Audits agents cannot scope a hotel audit; G-5 Arika's legal entity; G-6 no answer-collection tool) and six owner decisions. Companion runnable gate `intake/intake_gate.py`. **No client data, prices, legal terms or agent changes.** — Claude Code (Opus 5)


