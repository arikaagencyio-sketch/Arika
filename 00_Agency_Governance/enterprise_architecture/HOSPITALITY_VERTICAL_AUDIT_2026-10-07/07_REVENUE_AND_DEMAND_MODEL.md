# 07 — Revenue and Demand Model

**Protocol §14:** does the OS understand *content → demand → lead → qualification → sales → booking → revenue*? Can campaigns connect to occupancy, room, F&B, MICE, event, spa, experience, package and ancillary revenue, repeat business and referrals? *"The system should never claim that content automatically caused revenue unless attribution is supported."*

---

## 1. Two revenue models, not one

| | **Agency revenue (Plane A)** | **Client revenue (Plane B)** |
|---|---|---|
| Whose money | Arika's fees from hotels | The hotel's revenue from guests, companies, intermediaries |
| Modelled where | `AGENCY_REVENUE_TARGETS.md`, Offer registry, `CRM_SCHEMA.md` Lead → Opportunity → Client → Project → Invoice, `finos-plugin` | Plugin P13/P14 KPI semantics; Draft 41 D7/M6; intake MD1–MD3 |
| Depth | Designed end to end; **no transaction has ever occurred** | **Rooms economics only**, and only as a ⚫ template populated from client systems |

## 2. Agency revenue — the hospitality offer's commercial state

| Element | State | Evidence |
|---|---|---|
| Targets | $1M/month, $35K/day — owner-confirmed; **daily × business days ≈ $759K–$770K, 23–24 % short of monthly**, reported, unresolved | `OPERATIONS_OS.md` §7 |
| Offer | Hospitality Revenue Content OS · "Direct Booking Engine"; gateway *OTA Leakage & Direct-Booking Audit* | `OFFER_OS.md` §3; Draft 41 |
| Price | **None.** Phase 11 blocked on five inputs: cost-to-deliver (money), delivery capacity, owner-approved price band, audit-fee credit policy, proof-generation method | Draft 41 §5.1 |
| Segmentation | H1/H2/H3 room bands **approved for internal pricing design only** (Decision 71); severity L1–L3 a separate axis; no hotel floor exists | Draft 41 §11.1–§11.2 |
| Pricing agent | Must return `insufficient_data`; **its spec has no rule stopping it mapping a hotel onto SaaS ARR bands** — the durable fix is an owner decision | Draft 41 §11.4 |
| Commercial shape | MVP: audit-gated, two stages, no retainer (2026-09-14). Full offer: audit + monthly retainer *vs* build + governance retainer — **open** | Worksheet §1.5; Draft 41 §9 #12 |
| Capacity | One H1/H2 MVP client at a time, owner solo + AI — **provisional, not proven** | Worksheet §6.1 |
| Invoicing | USD-priced, KES-invoiced; conversion calculator **unbuilt**; invoice creation is Class 3 with **no approval-matrix row**; Zoho Books plan **lapsed** at the 2026-07-15 check | `CRM_SCHEMA.md` platform section; `AEIT_09` HP-4 |
| Proof | Class C performance claims **banned** until a real engagement produces evidence | `CLAIMS_SUBSTANTIATION_POLICY.md` §3 |

**Verdict (`CONFIRMED`):** Arika cannot today quote, contract or invoice a Hospitality engagement. That is a known, documented state (item 71), not a discovery of this audit.

## 3. The demand chain — Plane A vs Plane B

| Stage | Plane A (agency sells to hotel) | Plane B (hotel sells to guest) |
|---|---|---|
| **Content** | Content DB 5: 3 Accommodation opportunities (*The OTA Tax*; *Are you an OTA tenant?*; *Low season is your growth season*) — Working Hypothesis, `Proof required — named` | Draft 41 D3–D5 (revenue-year calendar, direct-booking content, journey messaging) — **designed deliverables; no store has a client dimension** (`HV-11`) |
| **Demand** | Sector signals, P13 buying window | DB 7 signals + DB 16 themes + DB 15 routes (market demand); **client demand data absent** |
| **Lead** | CRM `Lead` (live list, 0 real rows); prospecting queue outside Git | Hotel's enquiries/RFPs — client systems (`EXTERNAL-BY-DESIGN`) |
| **Qualification** | `sector-icp-fit` (hospitality routes), `sector-signal-scorer`, `sales-lead-qualification` — never run on a real prospect | Hotel's sales process — not modelled |
| **Sales** | CRM `Opportunity`; proposal **blocked** | Group/MICE sales — not modelled |
| **Booking** | — | **None.** Only measurable via client exports (MD1 room-nights by channel; MD2 revenue by channel) |
| **Revenue** | `Invoice / Revenue Event` (Zoho) | ⚫ ADR, RevPAR, net RevPAR, direct share, commission — client-system-sourced only (QG6) |

## 4. Can a campaign be connected to hotel revenue? (protocol §14 list)

| Outcome | Representable? | Measurable today? | Attribution path? | Class |
|---|---|---|---|---|
| Occupancy | ✅ semantics (P14, P13 template) | Only from client PMS/RMS | Seasonally comparable baseline (M6), design open | **METRIC GAP** |
| Room revenue | ✅ (ADR, RevPAR, net RevPAR; MD2) | Only from client systems | Direct-share change vs baseline | **METRIC GAP** |
| F&B revenue | ❌ no measure | — | — | **METRIC GAP + NEW** |
| MICE revenue | ❌ (signals and themes only) | — | — | **METRIC GAP + NEW** |
| Event revenue | ❌ | — | — | **METRIC GAP + NEW** |
| Spa revenue | ❌ | — | — | **METRIC GAP + NEW** |
| Experience revenue | ❌ (no offering object) | — | — | **NEW** |
| Package revenue | ❌ | — | — | **NEW** |
| Ancillary revenue | ❌ | — | — | **NEW** |
| Repeat business | ❌ guest retention unmodelled (P11 Expansion 2, unengineered) | — | — | **NEW** (P2) |
| Referrals | Arika's only (`Lead.source = referral`) | — | — | **NEW** (guest B2C2B/B2C2C) |
| **Agency side:** campaign → lead → client → invoice | ◐ `Lead.source_campaign` is **free text**, not keyed to Content DB 4 `Campaign Code`; `finos.clients` has no FK to the CRM | No data | **Broken key** | **INTEGRATION GAP** (`HV-18`, `HV-32`) |

## 5. Measurement and attribution that exist — and they are the right kind

The repository's governance here is **already stricter than the protocol asks** (`CONFIRMED`):

- *"Every KPI comes from client systems; nothing estimated, extrapolated or fabricated"* — QG6 (Draft 41 §8).
- *"Attribution of direct bookings to content is confounded by seasonality and rate changes"* — Draft 41 Phase 6/7, which requires *"a seasonally comparable baseline before build starts."*
- The claims policy's evidence file for any future outcome claim requires *"the attribution basis (why Arika's work caused it, not correlation)"* (`CLAIMS_SUBSTANTIATION_POLICY.md` §8).
- Sector benchmarks (15–30 % effective OTA commission, 35–45 % direct share) are *"sector benchmark only… never a client-specific claim, a promised saving, or a target"* — QG3.
- P2 rule cells marked `owner_reasoning` *"may filter a calendar; they may not be cited in a client-facing claim"* (plugin P2; item 31i).

**What is absent is the measurement *machinery*, not the measurement *ethics*:**

| Missing piece | Absence type (`AEIT_11` R7) | Smallest sufficient form |
|---|---|---|
| A performance store | `OWNED-UNBUILT` — Marketing (03) owns measurement truth and holds no store | Do **not** build before a client exists. For the MVP, M6's measurement plan and baseline live in the client folder |
| A data path from client systems | `EXTERNAL-BY-DESIGN` — PMS/CRS/booking engine | Aggregated monthly exports by channel (the MD1/MD2 shape), agreed in the SOW; never raw guest data |
| Campaign keys on leads | `UNASSIGNED` | Constrain `Lead.source_campaign` to a DB 4 `Campaign Code` |
| A non-rooms revenue measure | `UNASSIGNED` | Owner decides whether the offer measures beyond rooms (`HD-08`); total-revenue measures (e.g. TRevPAR-style) would be P14 semantics, values only |
| An attribution method | `UNASSIGNED` — Draft 41 §9 #8 (per-client target + baseline) is open | Owner decision; until then, report *movement against baseline* and never *caused by* |

## 6. The demand model the vertical actually needs — and where it goes

The protocol's chain for Hospitality — *market → audience → occasion → experience → story → demand → sales → revenue → experience → retention → learning* — maps onto existing slots once Plane B is authored:

| Link | Home |
|---|---|
| market | DB 1/2, DB 12/13 |
| audience | **plugin P3** guest-segment vocabulary (to author) |
| occasion | **plugin P3** occasion vocabulary + DB 7 signal types |
| experience | client offerings via intake (client folder) — entity only if ratified (`HD-08`) |
| story | Content Story Architecture + a ratified Plane B narrative variant (`HV-14`) |
| demand | DB 7 + DB 15 + DB 16 (market); client data (actual) |
| sales → revenue | client systems (`EXTERNAL-BY-DESIGN`), read through M6/D7 |
| retention | plugin P11 Expansion 2 (unengineered) |
| learning | performance → finding → P2 `observed` promotion (**the missing return edge**) |
