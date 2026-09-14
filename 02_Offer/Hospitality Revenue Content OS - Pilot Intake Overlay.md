# Hospitality Revenue Content OS — Pilot Intake Overlay

> ⚠️ **INTAKE QUESTIONS ONLY · NO CLIENT DATA · NOT QUOTABLE.** This overlay adds hospitality questions to the universal intake. It holds no property's answers — those live in the client folder. It contains no price, fee or quote language. The offer remains **Working Hypothesis / Not Quotable.**

| Field | Value |
|---|---|
| **Type** | Sector overlay — Offer (02), for Sector Plugin #001 Hospitality → Accommodation (Hotels) |
| **Core** | [`00_Agency_Governance/CLIENT_INTAKE_PROFILE.md`](../00_Agency_Governance/CLIENT_INTAKE_PROFILE.md) — stages, states, labels, storage rules and the `U-` rows |
| **Date** | 2026-09-14 · v0.1-draft · **owner review required** |
| **Pilot** | `PILOT-H-001` — one real property, supplied by the owner (`OWNER_INPUT_NEEDED.md` item 72) |
| **Sources, referenced not re-typed** | Packet OI1–OI9, RD1–RD2, PG1 stop rules · Worksheet §1.1 (MVP), §1.4 (MD1–MD8) · Plugin P1, P2, P4, P5, P6, P9, P10, P13, P14 · `Draft 41` §2, §3, §6, Phase 8 |
| **If this file and a source disagree** | The source wins — the plugin for vocabularies, the worksheet for MD1–MD8, the packet for OI/RD and stop rules |

---

## 1. How the overlay plugs into the core

- **Answer set for the pilot** = every `U-` row in the core + every `H-` row below, generated with:
  `python 00_Agency_Governance/intake/intake_gate.py --template "02_Offer/Hospitality Revenue Content OS - Pilot Intake Overlay.md" --out "<CLIENT>/intake_answers.json"`
- **Which rows run now:** Stage **S1** only (public desk profile). S2 needs owner decision ID3; S3 and S4 are blocked (core §2).
- **Packet inputs → rows:**

| Packet input | Rows |
|---|---|
| OI1 property name | U-A01 |
| OI2 website URL | U-A02 |
| OI3 booking path | U-I01 · H-B01 |
| OI4 geography | U-A07 · H-A02 |
| OI5 property type, brand/group affiliation | H-A01 · U-A04 · U-A05 |
| OI6 room count (public or owner-supplied only) | H-A03 |
| OI7 OTA inspection allowed? | H-Z01 |
| OI8 screenshots or text notes? | H-Z02 |
| OI9 owner business context | U-B02 · U-B03 · any `[OWNER-SUPPLIED]` note |
| RD1 pilot ID in repo-logged inputs | H-Z03 |
| RD2 client folder location | H-Z04 |

### 1.1 Core rows adjusted for hospitality

The overlay narrows core rows; it deletes none. The gate checks every ID below exists in the core.

| Core ID | Hospitality adjustment |
|---|---|
| U-A02 | No website → **stop: anti-ICP** (a property with no website needs a build first — `OFFER_OS.md` §3 seed) |
| U-A05 | A chain or group with a central brand.com / direct-booking team → **stop: anti-ICP** (Decision 71). H3 is out of the MVP anyway |
| U-A08 | Unit = **rooms** → answered by H-A03 |
| U-D05 | Rate parity and channel rate position = `Draft 41` class (c) evidence — **client systems only**; a (c)-dominant finding redirects (P4a) |
| U-H04 | = OTAs and wholesalers the property says it uses. Arika's own viewing of OTA pages only if H-Z01 = yes |
| U-I01 | No direct booking path → **stop: anti-ICP**. Observe only up to the public boundary — no account, no test or partial booking, no personal details in any form |
| U-J01 | Categories = the plugin P1 stack: **PMS · CRS · channel manager · RMS · CRM · POS · booking engine**, plus email/messaging tool and web analytics |
| U-K03 | = H-E01 (MD1) and H-E02 (MD2) |
| U-K04 | = H-E09 |
| U-K05 | = H-E03 (MD3) |
| U-N02 | = H-E05 (MD5) — templates only; real sent messages may contain guest data (Worksheet §11.2) |

---

## 2. Stop rules — checked at S1, before anything is carried forward

From packet PG1. Any one stops the pilot at S1; record the rule in the run sheet (§5).

| Rule | Row | Stop when |
|---|---|---|
| No website | U-A02 | No website |
| No direct booking path | U-I01 · H-B01 | No direct path exists |
| Outside geography scope | H-A02 | Outside Kenya-inbound, **or** a destination with no Destination Profile — Mombasa and any unprofiled place are blocked unless the owner commissions a profile first (skill S05) |
| Unresolvable archetype | H-A01 | `Hospitality Group` (the plugin's union operator is unimplemented). `Destination Property` is unruled — flag and continue with reduced Sector grounding |
| Central brand team | U-A05 | A chain with a central brand.com / direct-booking team |
| Outside the MVP size | H-A03 | H3 (121–250 rooms or 2–5 properties) or under 30 rooms. Unknown → continue with `H-band: UNKNOWN`; MVP fit stays unconfirmed |

---

## 3. Hospitality question bank

Same format as the core (`| ID | Question | Stage | Req | Label | Feeds | If missing |`).

### H-Z — Handling permissions *(owner, before S1)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-Z01 | OI7 — may OTA pages be inspected manually? | S1 | R | OWNER-SUPPLIED | Packet §3.1 · H-B04 | Treated as **No** |
| H-Z02 | OI8 — public screenshots, or text notes only? | S1 | R | OWNER-SUPPLIED | Packet §3.1 · client folder | Treated as **text notes only** |
| H-Z03 | RD1 — pilot identity in repo-logged inputs: pilot ID or real name? | S1 | R | OWNER-SUPPLIED | Packet §3.3 · `intake_gate.py --scan --key` | **Pilot ID `PILOT-H-001`** |
| H-Z04 | RD2 — client folder path, outside every git working tree and **not** `ChatGPT\Agency.Repo` | S1 | R | OWNER-SUPPLIED | Packet PG0 · core §5 | **Stop — nowhere to store answers** |

### H-A — Property profile

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-A01 | Property archetype — exactly one plugin P2 value: City / Conference Hotel · Business Hotel · Beach Resort · Safari Lodge · Tented Camp · Boutique Property · Serviced Apartment · Villa · Destination Property · Hospitality Group | S1 | R | PUBLIC | Plugin P2 signal rules · DB 16 archetypes · `Draft 41` §9 #18 archetype scope · packet R2 | `UNKNOWN` — Sector grounding reduced |
| H-A02 | Destination — Nairobi · Maasai Mara · Diani (profiled) · Mombasa or other (blocked by Destination Fit) | S1 | R | PUBLIC | Plugin P4 · DB 11 · DB 16 · Resolution Engine Destination Fit | **Stop** (§2) |
| H-A03 | Room count — **only if published or owner-supplied** → H-band: H1 30–60 · H2 61–120 (MVP) | S1 | O | PUBLIC | `Draft 41` §11.1 (Decision 71) · Worksheet §1.1 | `H-band: UNKNOWN` — never estimated |
| H-A04 | Room types and number of each, as published | S1 | O | PUBLIC | Offer seed context · messaging hierarchy (M4) | `NOT PUBLISHED` |
| H-A05 | Non-room demand facilities — restaurants/bars, meeting and event space (capacity if published), spa, activities | S1 | O | PUBLIC | Plugin P2 `Sales/MICE` cells · P5 themes | `NONE FOUND` |
| H-A06 | Official classification or star rating, if published | S1 | O | PUBLIC | Positioning context | `NOT PUBLISHED` |
| H-A07 | Months of operation — open all year, or seasonal closure months | S1 | O | PUBLIC | Plugin P13 · campaign timing | `UNKNOWN` |
| H-A08 | Who controls marketing, the website and the booking engine — owner, GM, management company, franchisor, group | S2 | R | CLIENT-SUPPLIED | Anti-ICP · H3 condition · U-B06 approver | `UNKNOWN` — anti-ICP unconfirmed |

### H-B — Booking path & distribution

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-B01 | Direct booking path, observed to the public boundary — booking engine present, steps, desktop and mobile, main book-direct call-to-action | S1 | R | PUBLIC | MD4 (public side) · `Draft 41` class (b) messaging vs technical · packet R1 | **Stop** if no direct path |
| H-B02 | Booking-engine vendor, if visible on the page | S1 | O | PUBLIC | Class (b)/(d) context · U-J01 | `NOT VISIBLE` |
| H-B03 | How the direct path presents offers — inclusions, packages, cancellation terms, trust signals | S1 | O | PUBLIC | M3 message strategy · M4 blueprint | `NOT OBSERVED` |
| H-B04 | OTA presence — which OTAs list the property and as what property type; **no reviews, no reviewer names**. *Condition: H-Z01 = yes* | S1 | C | PUBLIC-OTA | Distribution context · audit hypothesis only | `NOT CHECKED` |
| H-B05 | Trade distribution — tour operators, DMCs, travel agents, wholesalers, GDS, corporate or MICE contracts | S2 | R | CLIENT-SUPPLIED | Plugin P6 `Travel-Trade` · P2 cells · U-I02 | `UNKNOWN` |
| H-B06 | Travel-trade shows or events the property attends | S2 | O | CLIENT-SUPPLIED | Sector DB 7 `Travel-Trade` relevance | `UNKNOWN` |
| H-B07 | How dependent on OTAs the property feels, and its own estimate of direct-booking share — **an estimate, never a measured value** | S2 | R | CLIENT-SUPPLIED | `Draft 41` journey stage 1 exit criterion · L1 severity | `UNKNOWN` |
| H-B08 | Who manages rates — in-house revenue manager, GM, outsourced, RMS — and the parity policy as stated | S2 | R | CLIENT-SUPPLIED | Class (c) redirect signal · H2 buying-process condition | `UNKNOWN` |

### H-C — Guests & demand *(aggregates only)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-C01 | Guest mix — leisure · corporate · group/MICE · domestic · international — shares only if measured | S2 | R | CLIENT-SUPPLIED | Plugin P14 `Demand Direction` segments · content focus | Shares `UNKNOWN` |
| H-C02 | Origin markets — Kenya domestic · regional Africa · Germany · UK · US · other | S2 | R | CLIENT-SUPPLIED | DB 15 Market Routes relevance · origin-side clocks (plugin P7) | `UNKNOWN` |
| H-C03 | Which plugin P5 demand themes the property believes apply (e.g. Corporate, Conferences/MICE, Safari/Wildlife, Beach, Family, Weddings, Romance/Honeymoon) | S2 | O | CLIENT-SUPPLIED | Content angles — **the property's belief, never a DB 16 assignment** | `UNKNOWN` |
| H-C04 | Events and periods that fill or empty the property — conferences, public and school holidays, migration season, sports, trade shows | S2 | R | CLIENT-SUPPLIED | Plugin P2 falsifiers (an observation can challenge an `owner_reasoning` cell; promotion to `observed` still needs a real outcome) · content calendar | `UNKNOWN` |
| H-C05 | Group business present — weddings, school groups, incentives, conferences | S2 | O | CLIENT-SUPPLIED | P2 `Sales/MICE` · P5 themes | `UNKNOWN` |
| H-C06 | Typical length of stay and booking lead time — from systems | S3 | O | CLIENT-SYSTEM | Plugin P7 offsets check · campaign windows | `NOT MEASURED` |

### H-D — Hospitality measures & revenue systems

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-D01 | Measures tracked today — occupancy · ADR · RevPAR · net RevPAR · direct-booking share · channel cost · pickup · comp-set reports | S2 | R | CLIENT-SUPPLIED | Plugin P14 · `Draft 41` QG6 · M6 measurement plan | `UNKNOWN` |
| H-D02 | Revenue-management tooling — RMS in use, comp-set data subscription | S2 | O | CLIENT-SUPPLIED | Class (c)/(d) context · Transformation rung signal | `UNKNOWN` |

### H-E — MVP minimum audit data set *(owner-approved, Worksheet §1.4 — S3, blocked today)*

| ID | Question | Stage | Req | Label | Feeds | If missing |
|---|---|---|---|---|---|---|
| H-E01 | MD1 — room-nights by channel, last three months: direct website · phone/email/WhatsApp direct · OTA · corporate/group/other if available — **aggregated counts, not a raw booking export** | S3 | R | CLIENT-SYSTEM | M1 · M2 verdict · analytics band | **Audit cannot proceed** |
| H-E02 | MD2 — booking revenue by channel, last three months, if available | S3 | O | CLIENT-SYSTEM | M1 · leakage quantification | Audit proceeds; **revenue leakage unquantified**; analytics band L |
| H-E03 | MD3 — OTA commission rate, or the property's effective commission estimate | S3 | R | CLIENT-SYSTEM | M1 · QG6 | Recorded `UNKNOWN` — **never invented**; no benchmark substitutes (QG3) |
| H-E04 | MD4 — current direct-booking path: booking-engine URL, screenshots or notes of the journey, main CTA, any active landing or offer page | S3 | R | CLIENT-SUPPLIED | M2 class (b) · M4 | **Audit cannot proceed** |
| H-E05 | MD5 — guest communication assets: booking confirmation, pre-arrival message, WhatsApp scripts — **templates or redacted samples only** | S3 | O | CLIENT-SUPPLIED | M3 · M4 — reviewed only, no nurture | No sufficiency rule set |
| H-E06 | MD6 — content and campaign assets: homepage or rooms page, direct-booking promotions, recent social or email campaigns | S3 | O | CLIENT-SUPPLIED | M3 · M5 | No sufficiency rule set |
| H-E07 | MD7 — one buyer interview with the GM, Owner/MD or Revenue Manager: perceived OTA dependency, direct-booking blockers, operational constraints. **Typed notes; no recording by default** | S3 | R | CLIENT-SUPPLIED | M2 diagnosis · Worksheet §5.2 #4 | **Desk review only — not a diagnosis; Stage 2 cannot open** |
| H-E08 | MD8 — constraints: tool access limits, brand/legal approval needs, whether pricing/rate strategy or booking-engine technology problems are suspected | S3 | R | CLIENT-SUPPLIED | Redirect detection (M7) | No sufficiency rule set |
| H-E09 | Seasonal baseline — the same three months last year by channel, *if available* | S3 | O | CLIENT-SYSTEM | M6 — Worksheet §8 #22 (open) | M6 states the limitation |

---

## 4. S2 conversation guide — hospitality *(for when owner decision ID3 opens S2)*

Not a script — Sales (05) and Content (04) own scripts (`SECTOR_ACTIVATION_CONTRACT.md` §14.3). These are the constraints any S2 conversation must respect.

| Rule | Source |
|---|---|
| Talk to the GM, Owner/MD or Revenue Manager — not IT | `Draft 41` §2.2 |
| **Use:** *net RevPAR* · *the OTA tax* · *direct-booking share*. **Avoid:** *more bookings* · *awareness* | Plugin P10 |
| Sector benchmarks (15–30% effective OTA commission; 35–45% direct-share benchmark) are **Medium-confidence sector figures** — say so, and never apply them to this property or promise them | `Draft 41` §2.1, QG3 |
| No price, fee, quote, proposal or outcome promise. The honest next step is a diagnosis on the property's own data | QG5 · `Draft 41` §1 |
| Prefer the property's low season — the GM/RM has capacity to engage then | Plugin P13 |
| Ask the S2 `R` rows in this order: U-L03 → H-B07 → U-L05 → U-B04 → U-B07 → U-E05 / H-C04 → H-C01 / H-C02 → U-J01 → U-J03 / H-D01 → U-B05 → U-L06 → U-L01 / U-L02 → the rest | Problem before data; data owner before data request |
| Record every figure said aloud as `[CLIENT-SUPPLIED]` | Core §4 |

---

## 5. Pilot run sheet — `PILOT-H-001` *(pseudonymous; fill as stages pass)*

Nothing identifying goes in this table. The name, URL and answers stay in the client folder.

| Stage | Opened | Gate result (`intake_gate.py --answers`) | `R` rows answered / unknown / withheld / blocked | Stop rule hit | Carried to |
|---|---|---|---|---|---|
| S1 Public desk profile | — | — | — | — | Packet R1 → R2 fit record |
| S2 Discovery conversation | — | — | — | — | Sales / Offer notes |
| S3 Audit data set | ⛔ blocked (G5; no engagement) | — | — | — | — |
| S4 Onboarding | ⛔ blocked (Phase 11; Legal) | — | — | — | — |
| S5 Ongoing measurement | ⛔ blocked (retainer deferred) | — | — | — | — |

---

## 6. Changelog

- **2026-09-14 — Created (v0.1-draft, owner review required).** Hospitality overlay for the universal intake (`00_Agency_Governance/CLIENT_INTAKE_PROFILE.md`), for the first pilot `PILOT-H-001`. Maps packet OI1–OI9 and RD1–RD2 onto rows; narrows 11 core rows for hospitality; restates PG1's six stop rules against their rows; adds **37 `H-` questions** (gate count; 148 with the core) — handling permissions, property profile (plugin P2 archetype, P4 destination, H-bands), booking path and distribution, guests and demand (P5, P14), hospitality measures, and the owner-approved MVP audit data set MD1–MD8 plus an optional seasonal baseline (Worksheet §8 #22, open); an S2 conversation guide bound to plugin P10 language and QG3/QG5; and a pseudonymous run sheet. **No property named, no client data, no prices; still Working Hypothesis / Not Quotable.** — Claude Code (Opus 5)
