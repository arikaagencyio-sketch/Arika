# 09 — Prospecting Alignment and Agency Self-Marketing

**Protocol §16:** can the prospecting architecture classify by sector, vertical, property type, size, location, revenue potential, decision-maker, current agency situation, commercial pain, opportunity, timing, seasonality, trigger, relationship, temperature and next action — and support *broad → intelligence-led → personalised → conversation → discovery → audit → proposal*? **§17:** can the OS market the agency itself into Hospitality — and what role does each channel play?

---

## 1. The prospecting architecture that exists

| Component | Owner | What it does | Reality (test) |
|---|---|---|---|
| Sector DB 4 ICP Classification · DB 5 Prospect Signal Scores | Sector (01) | Paired classification + 90-point score per company | `BUILT`, **empty by design** — written by agents against real companies, gated on scraping |
| `sector-icp-fit` | Sector (01) | SaaS tiers **or** Hospitality route (`hospitality_group/property/outlet_discovery`) | Extended 2026-10-03; **never run on a real prospect** |
| `sector-signal-scorer` | Sector (01) | 6 categories × 0–15 → priority band → matched service; 30-day decay | Extended 2026-10-03; *"has never been run against a real prospect"* (its own spec) |
| `sales-lead-qualification` | Sales (05) | Fit, urgency, pain, authority, timing — the qualification firewall | Extended 2026-10-03; never run |
| `05_Sales/prospecting/prospecting_cycle.py` | Sales (05) | Validates public evidence (URL, observation, review window), the organisation tree (no cycles, roots match), contact provenance (published role inbox / company phone only), one touch per account; qualifies; writes an ID-only queue **outside Git** | `LIVE` once (2026-10-03); **8/8 tests pass** (2026-10-06) |
| Intake S1 (public desk profile) + Hospitality overlay | Governance (00) + Offer (02) | 37 `H-` questions incl. archetype (H-A01), destination (H-A02), rooms (H-A03), facilities (H-A05) | `DESIGNED`, unratified (item 73) |
| CRM bridge | Governance (00) | `sector`, `sub_sector`, `icp_tier`, `offer_id` on `Lead` | Round-trip verified on disposable fixtures (2026-09-29); **no real Lead tagged** |
| Messaging rules | Sector / Offer | Plugin P10 use/avoid language; QG3 benchmark labelling; QG5 no price; no guessed address; explicit stop-contact line | Enforced in code for opt-out and price/performance claims (`prospecting_cycle.py` `validate`) |
| Named-person data gate | Governance / Legal | No scraping, no enrichment, no fabricated contact | **Closed by design** (`CRM_SCHEMA.md` honesty gate) |

**Run record — `PROSPECT-H-20261003-01`:** 4 public companies researched · 23 organisation levels mapped · 3 first-touch emails + 1 switchboard script prepared · drafts saved and read back in the Zoho mailbox · **0 sent · 0 calls · 0 verified CRM rows** · owner decision: *drafts for edits, not sends* (`PROSPECTING_CYCLE.md`).

## 2. Classification coverage (protocol §16)

| Dimension | Captured in the prospecting record? | Captured elsewhere? | Gap |
|---|---|---|---|
| Sector | ✅ implicitly (Hospitality run) | CRM bridge `sector` | — |
| Vertical / sub-sector | ◐ implicit | CRM `sub_sector`; DB 2 | Not a queue field |
| **Property type (archetype)** | ❌ **not in the batch schema** | intake H-A01 (plugin P2 values) | Archetype drives the calendar and P2 rules — it must travel with the record |
| Size | ✅ `published_room_count` → `mvp_size_fit_only` (30–120 = H1/H2, `prospecting_cycle.py:122`) | intake H-A03 | H3/group sizing not expressed |
| Location | ◐ `country` only; **`"Kenya"` hard-coded** (`prospecting_cycle.py:89`) | intake H-A02 destination | Destination (Nairobi/Mara/Diani) not carried; the code silently encodes the Kenya-inbound scope decision |
| Revenue potential | ❌ | — | Deliberately unestimated (no fabricated figures) — but no field for a *sourced* indicator either |
| Decision-maker | ✅ `buyer_roles` (role, not person) | DB 10 titles | Decision **level** via `target_company_level_id` ✅ |
| Current agency situation | ❌ | — | Who runs their marketing today (in-house, agency, management company) — intake H-A08 at S2 only |
| Commercial pain | ◐ in the message text | DB 3 findings (OTA tax) | Not a structured field |
| Opportunity | ✅ `offer_route` (`hospitality_group/property/outlet_discovery`) | Sector DB 8 | All routes are **unpriced discovery** |
| Timing | ❌ | P13 *"low season is Arika's buying window"*; P7 Sales offsets | Doctrine exists; not applied to the record |
| Seasonality | ❌ | DB 7 / DB 16 | as above |
| Trigger | ❌ | Offer seed triggers: *new GM, low direct share, post-renovation, portfolio-level leakage* (`OFFER_OS.md` §3) | Named, not captured |
| Relationship | ❌ | — | No prior-relationship field |
| Temperature | ❌ | Scorecard priority band (designed, never run) | — |
| Next action | ✅ `touch_state` (`awaiting_sender_and_review` / `research_only`) | follow-up cadence | — |

**Verdict:** 5 of 16 dimensions are carried, 3 partially, 8 not at all — and **six of the eight missing ones already exist elsewhere in the repository** (archetype, current agency situation, timing, seasonality, triggers, temperature). This is an integration gap, not a design gap. → `HV-36`.

## 3. The progression — broad to proposal

| Stage | Mechanism | State | Blocker |
|---|---|---|---|
| Broad prospecting | Sector DB 1/2 Priority Score → `Status = Target` | `LIVE` (Accommodation = Target) | — |
| Intelligence-led | Plugin + DB 3/6/7/9/10/16; S10 packet | `LIVE` (intelligence); S10 fixture-only | — |
| Personalised outreach | Prospecting cycle + P10 language | Drafts prepared | Owner message review; DKIM selector unknown; sender/reply checks |
| Conversation | Intake S2 (needs ID3); S2 conversation guide (overlay §4) | `DESIGNED` | ID3 decision; a reply |
| Discovery | `hospitality_*_discovery` routes — **unpriced** | `DESIGNED` | — |
| Audit | MVP Stage 1 (M1, M2) | `DESIGNED` | **S3 blocked** (signed engagement + legal review path + NDA) |
| Proposal | — | **BLOCKED** | Phase 11 (no price) + Legal (no reviewed contract) |

## 4. Where Hospitality prospecting plugs in

```
Sector (01)  plugin P1/P2/P4/P9/P10/P11 + DB 3/6/9/10/16
     │  S10 handoff packet (angle, language, buyer titles, offer match, timing)
     ▼
Sales (05)  prospecting_cycle.py  ──►  ID-only queue (outside Git)  ──►  owner review  ──►  1 manual touch
     │                                                                               │
     ▼                                                                               ▼
CRM (ClickUp)  Company tree (ORG-*) · Lead (+4 Sector tags) · Pilot Engagement (PILOT-H-*)   ◄── reply → S2 → discovery
```

**Three integration fixes make this line coherent** (all `EXTEND`, none new):

1. **Align the organisation-level vocabulary.** Code: `{group, property, outlet, shared_service}`. CRM: `organization-root, group, shared-service, brand, property, branch, outlet`. Plugin: *group → property/branch → outlet/shared-service*. A `branch` or `brand` level in a real batch is rejected by the validator; `shared_service` vs `shared-service` will not match on CRM write. → `HV-06` (P1, before any CRM write).
2. **Carry the five already-modelled dimensions** (archetype, destination, trigger, season/timing window, temperature) into the batch schema and queue. → `HV-36`.
3. **Make the Kenya scope a parameter, not a literal** — the owner's Kenya-inbound decision (2026-08-19) is plugin P4 content; the code should read it, not restate it (the plugin rule: *"a universal file MUST NOT carry a sector's rule values"*).

Also open: real identity maps live in **three places** — the Codex visualisation folder used by the 2026-10-03 run, `C:\Users\USER\Arika_Pilots\PILOT-H-001` (RD2), and the Drive `ARIKA_CLIENT_IDENTITIES` folder. A tool's scratch folder is not a durable identity store. → `HV-44`.

## 5. Agency self-marketing into Hospitality (protocol §17)

**Pathway:** *agency → hospitality market → decision makers → awareness → authority → interest → conversation → discovery → proposal → client → retention → referral.*
**State (`CONFIRMED`):** only **direct outreach** is operational, and it is drafts-only. Everything else is designed for B2B SaaS or not designed at all. The single biggest defect is that the agency's public surfaces **contradict** the vertical it is approaching (`HV-02`).

| Channel | Role it should play in the commercial system | Current state (evidence) | Verdict |
|---|---|---|---|
| **Direct outreach** | Primary acquisition for a solo pre-revenue agency: one coordinated, evidence-based first touch per account | Live-once; 3 drafts (`PROSPECTING_CYCLE.md`) | **Keep as the primary channel** — release after HD-03 |
| **Website** | Proof and conversion hub that a GM checks after any touch | `.vercel.app` subdomain; apex DNS unresolved; **says "Arika's confirmed ICP is B2B SaaS only"** (`arika-website/src/app/industry-solutions/page.tsx:24`; meta in `layout.tsx:22`); omitted from the outreach batch | 🔴 **Liability until reconciled** — `HV-02` |
| **LinkedIn** | Founder authority with GM / Revenue Manager / group commercial leaders | Profile + Company Page exist; launch content drafted, awaiting Class 3 sign-off; **0 hospitality mentions** across `LINKEDIN_PRESENCE_OS.md`, `LINKEDIN_LAUNCH_CONTENT.md` | **Extend**: the three Accommodation content opportunities are ready-made authority pieces |
| **Thought leadership** | Authority without proof — the *only* honest authority while Class C is banned | DB 5 opportunities (*The OTA Tax*, *Are you an OTA tenant?*, *Low season is your growth season*); sector intelligence called *"the single strongest content asset in this repo, and almost entirely unused"* (`LINKEDIN_LAUNCH_CONTENT.md` §1) | **Strongest available asset** |
| **Personalised audits** | The bridge from conversation to paid diagnosis | Paid gateway designed (M1/M2); a *public-data* desk profile (S1) exists as an intake stage | **Decision** — whether an S1 desk profile may be shown to a prospect, and under what Class D labelling (`HD-12`) |
| **Prototypes** | Capability proof that is *not* a client claim (claims policy §3 permits *"real, non-client proof"*) | **None** — corporate tennis and Pre-Experience absent | **New**, governed by `HV-13` — file 11 |
| **Pitch decks** | Discovery-meeting support | None for Hospitality; pitch logic exists (company profile §13); EE lists pitch/sales decks as candidate outputs | Build only after positioning is reconciled |
| **Case studies** | Proof | **Banned** (Class C) until a real engagement | Correctly absent |
| **Email marketing** | Owned nurture of an opted-in audience | Newsletter `planned`; a public role inbox is *"neither buyer authority nor consent to a marketing sequence"* | Not a cold channel; later, consented only |
| **WhatsApp** | Client coordination after engagement (Draft 41 Phase 8) | PIL watchlist; not in the prospecting cycle | **Not a prospecting channel** (consent); keep for clients |
| **Events / travel trade** | Trust in a relationship-driven industry | Plugin P7 already carries **Arika's own attendance clock** (*Travel-Trade (Arika's own attendance)*: T-120 → T-14); trade sources registered | **Decision** — which, if any, the owner attends (`IR-F4`) |
| **Partnerships** | Borrowed trust (associations, hotel-tech vendors as Enablers) | ClientPartner (06) categories; DB 9 `Enabler` lens | Not started — owner decision |
| **Referrals** | Compounding acquisition | 0 clients | Later |

**Recommendation (minimum sufficient):** fix truth on the public surfaces first (P0/P1), then run **two** channels for the pilot — direct outreach and LinkedIn thought leadership built from the existing Accommodation opportunities — and treat the prototype (file 11) as a sales-enablement asset once its governance exists. Do not open channels merely because the Presence registry lists them.
