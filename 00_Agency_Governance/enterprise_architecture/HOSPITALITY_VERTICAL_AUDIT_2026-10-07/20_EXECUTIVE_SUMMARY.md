# 20 — Executive Summary

**Hospitality Vertical Forensic Audit · Arika Growth Limited Agency OS · 2026-10-07**
Audit-only: nothing in the existing system was modified. Evidence for every statement is in files 01–19 (finding IDs `HV-nn`, actions `RM-nn`, decisions `HD-nn`).

---

## The short version

The Agency OS is a **documentation-first, truth-disciplined operating system for a solo, newly incorporated, pre-revenue agency**, with a deep sector-intelligence engine, a governed advisory agent layer (115 agents, 14 skills, one runtime) and almost no operating history with clients. **Hospitality already has the right architectural home** — a sector plugin, an offer, an intake overlay and a CRM structure — and the system should not grow a "Hospitality OS". What is missing is the **guest-facing half of Hospitality**, the **Pre-Experience methodology**, and the **operational layer after a sale** (approvals, client separation, measurement, learning). Readiness: **1.9 / 5**. Not ready for a client-facing pilot; ready to continue public-only discovery once its public face stops contradicting the vertical.

Three things need attention before anything else: a **red integrity gate on master** (`HV-01`), **root documents and the website still saying the real sector is B2B SaaS — "only", on the website** (`HV-02`), and **a pilot that is not yet defined** — the intended client is a hotel group and the only deliverable engineered is a single-property MVP (`HV-03`). The legal chain (`HV-04`) remains the hard stop for any client data.

## The 24 answers

**1. What is the Agency OS actually designed to do?**
To run Arika as a "360° Cognitive Revenue Operating System" — sense a market (Sector), package offers (Offer), create demand (Marketing/Content/Presence), convert (Sales), deliver (Client Success/Operations) and get paid (Finance) — with every claim, decision and state change governed: no silent invention, Class 3+ human sign-off, reality states that must be proven, and *decide ≠ apply*. In practice it has built the sensing and governing halves thoroughly and has not yet run the delivering half (file 02).

**2. What category does Hospitality belong to?**
A **combination**, each part with one owner: a **sector operating model / configuration** (Sector Plugin #001, 14 slots), a **commercial model** (the Hospitality Revenue Content OS in Offer 02), a **client-type configuration** (CRM `Company` group → property → outlet structure and the intake overlay), and a **client instance** computed per engagement (never stored). It is not a department and not a separate OS (file 03 §1–§2).

**3. Is Hospitality currently supported?**
**Partly.** Accommodation economics (OTA leakage, direct booking, seasonality, destinations, origin markets) and the agency's sale to hotels are supported deeply. The hotel's sale to its guests, companies and intermediaries — revenue centres, offerings, occasions, guest segments, relationship pathways, Pre-Experience — is not. "Pre-experience", "tennis", "B2B2C", "B2C2B", "B2C2C" and "revenue centre" have **zero** matches in the repository (file 01 §7).

**4. Where exactly should the Hospitality vertical live?**
- Market truth, rules, timing, places → `01_Sector/sector_plugins/hospitality/` (P1–P14), Sector DBs 7/11/14/15/16.
- Guest-side demand (segments, occasions, pathways, revenue centres) → **plugin slot P3**, the one substantive slot still unauthored.
- Commercial offer and gateway audit → `02_Offer/` (Draft 41 and its worksheet).
- Organisations and pilots → CRM `Company` + `Pilot Engagement` (`CRM_SCHEMA.md`).
- Client intake → universal core + Hospitality overlay.
- Each client's calendar and plan → Tier 3 resolution, outputs in Content and CRM — with a client reference added (`HV-11`).

**5. What existing components can be reused?**
The three-tier Core/Plugin/Instance architecture; the Resolution Engine (skill S09); DB 7/15/16 and the origin ⇄ destination doctrine; plugin P2/P5/P7/P13/P14; Draft 41's diagnostic gate, 17-stage journey and QG1–QG8; the MVP decisions (M1–M7, MD1–MD8); the intake gate; the prospecting cycle; the CRM and its governed provisioner; Content's 8 databases; Design's production chain with reuse and AI-artifact gates; EE's spec system; the claims policy; the runtime's human gate; the authorisation-register pattern; the `ORG/PER/PILOT/SIM` namespaces (file 03 §3).

**6. What must be extended?**
The CRM (`Company`/`Pilot Engagement` live; one organisation-level vocabulary — `HV-05`, `HV-06`); Content and Design stores (a client reference — `HV-11`); ClickUp `Project` (approval fields — `HV-09`); Content DB 4 (a status — `HV-08`); the claims policy (a depictive class — `HV-13`); narrative doctrine and the publishing gate (a guest-facing variant — `HV-14`); plugin P3 (guest-side vocabularies — `HV-12`, `HV-16`); the prospecting record (archetype, timing, trigger — `HV-36`); the platform registry (WhatsApp, Google Business Profile, review sites, OTAs — `HV-19`).

**7. What must be created?**
Very little: a **Pre-Experience methodology** (one document, Content-owned) and production recipe (Design); a **fresh simulated demonstration property** `SIM-H-001` for the corporate-tennis prototype — not A001 or SYNCO-01, which are mechanism-only fixtures aligned to real brands (`HV-28`); a **depiction / synthetic-media rule set** (V1–V9, file 12 §5); later, a group/portfolio offer. A canonical `Client Offering` entity only if a second department must reference offerings by ID (`HD-08`).

**8. What is duplicated?**
Seven lifecycle models with no crosswalk (`HV-22`); three audience vocabularies, one hard-coded to SaaS executives (`HV-17`, `HV-43`); a second client registry in `finos` (`HV-32`); real identity maps in three places (`HV-44`); "Experience" at risk of meaning two things (`HV-39`); an "8th calendar" claim against a "never an eighth" rule (`HV-23`). The three "Opportunity" concepts are deliberate and documented — not a defect.

**9. What is disconnected?**
Sector → Marketing and Sector → Operations have no route (`HV-20`); nothing agent-to-agent is ever published, so every handoff is carried by a person; audit redirects lead to offers that do not exist (`HV-27`); the hospitality gateway audit sits outside the Audits department's scoping (`HV-30`); campaigns are not keyed to leads (`HV-18`); and the loop closes nowhere — **there is no performance store, so outcomes cannot become learning** (`HV-18`, `HV-33`).

**10. What is missing from the information architecture?**
The guest plane: guest segments, occasions, relationship pathways, revenue centres, client offerings, bookings, intermediaries; a role model that includes **booker**; a property-identity decision (Company vs Geography — `HD-11`); and a client dimension on content and creative records (file 04).

**11. What is missing from governance?**
Commit-time enforcement of the gates that already exist (`HV-01`); reconciliation of root truth with live strategy (`HV-02`); a current decision tracker (`HV-07`); enactment tracking for ratified decisions (`HV-21`); a Definition of Ready (`HV-08`); a current RACI (`HV-31`); a recorded apply-approval for the 2026-10-03 reconciliation (`HV-46`); depiction rules (`HV-13`); and, externally, reviewed contracts and an s.48 basis (`HV-04`).

**12. What is missing from operations?**
A capacity model and SLAs (`HV-26`); a deliverable and approval record (`HV-09`); client separation (`HV-11`); and first real runs of the agents a delivery would use — none of Marketing, Content, Client Success, Operations or Presence has ever run (`HV-45`).

**13. What is missing from revenue operations?**
A price (Phase 11 blocked on five inputs) and a pricing agent that cannot mis-map hotels to SaaS bands (`HV-27`); invoicing readiness (lapsed Zoho plan at last check, bank account pending, USD→KES calculator unbuilt); any revenue measure beyond rooms; campaign-to-lead keys; a performance store. The **ethics** of measurement are already excellent — no fabricated metrics, no causal claims without attribution (file 07 §5).

**14. What is missing from prospecting?**
Carrying what the OS already knows — archetype, destination, trigger, season and timing window, temperature — into the prospecting record (`HV-36`); one organisation-level vocabulary across code and CRM, and Kenya scope read from the plugin rather than hard-coded (`HV-06`); a live CRM registration path (`HV-05`); a consolidated identity store (`HV-44`); and a public face that matches the outreach (`HV-02`).

**15. What is missing from calendar intelligence?**
Not architecture — coverage. Five routes, three destinations, blank lead times, four unauthored timing rows, no guest-segment or occasion tagging, no input home for a property's own events, Gate H unrun, and one modelling risk to verify: a country-level "Kenya's peak is Dec–Jan" signal inherited by safari destinations whose rule follows the migration calendar (`HV-24`, `HQ-05`). **None of the protocol's fifteen calendars needs a new store** (file 06).

**16. What is missing from B2B/B2C relationship modelling?**
All five pathways on the client side; an intermediary model (travel trade, DMCs, planners) distinct from Arika's own partners; the booker and advocate roles; and the protocol's B2C2B case (employee → HR → proposal) has no representation (`HV-16`, file 08).

**17. What is missing from AI governance?**
Rules for **depicting a real property** truthfully, for **synthetic people** (faceless as policy), for **previews of experiences that have not happened**, for **consumer-facing disclosure**, for **client approval of depictions**, and a **provenance record** per generated asset — plus counsel's answers on AI-output ownership and origin-market advertising rules. Strong existing safeguards (human gate in code, advisory-first agents, client-facing disclosure, no-imitation rule) cover operations, not depiction (file 12).

**18. What is missing from ticket/work-item governance?**
A work-item shape. Work lives in ≥10 well-maintained registers with ≥15 identifier schemes that collide (`R1`, `G1`, `D1`, `P1`), free-text statuses, and no link to client, campaign, revenue, calendar, audience or channel. Approvals are rigorous for *system* actions (authorisation registers) and absent for *client* work (file 13).

**19. What must be decided by humans before implementation?**
Nineteen decisions (file 18). The five that block everything: **HD-01** what the pilot is · **HD-02** the sector truth statement · **HD-04** the commercial basis of the first engagement · **HD-05** the client-data posture · **HD-14** whether failing gates may reach GitHub. Close behind: **HD-17** (confirm the 2026-10-03 apply), **HD-10** (Pre-Experience and the prototype), **HD-16** (depiction rules).

**20. Is the Agency OS ready for the Hospitality pilot?**
**No** for anything client-facing; **yes, with conditions,** for continued public-only prospecting and group discovery conversations (file 16 §3). This agrees with the repository's own measurement (real-pilot ≈ 15–20 %, client-facing 0 %).

**21. If not, what are the minimum P0/P1 changes?**
P0: fix the gate (`RM-01`) and stop red gates reaching GitHub (`RM-02`); reconcile the sector statement across root, website and claims policy (`RM-03`); define the pilot (`RM-04`); advance counsel, s.48 and storage (`RM-05`). P1: CRM `Company`/`Pilot` live with one vocabulary (`RM-06`, `RM-07`); tracker re-sync and the apply confirmation (`RM-08`, `RM-09`); ready glossary and campaign status (`RM-10`); approval fields (`RM-11`); client separation (`RM-12`); depiction rules (`RM-13`); a commercial basis and a fixed pricing-agent rule (`RM-14`); one identity store (`RM-15`); audit ownership (`RM-16`); a minimal, honest self-marketing line (`RM-17`); re-measured readiness (`RM-18`) (file 15).

**22. What should explicitly NOT be changed?**
The three-tier plugin architecture and its "values, never stores" rule; the CRM `Company` as the only organisation registry; the diagnostic gate and redirect-as-valid-outcome; the ban on fabricated hotel metrics and on unevidenced outcome claims; identity separation (`ORG/PER/PILOT/SIM`); advisory-first agents and Class 3 sign-off; "one store, many views" for calendars. And no new department, calendar stores, ticketing platform, B2B2C CRM or Pre-Experience agents (file 03 §7, file 15 §6).

**23. What information should the agency team provide next?**
The ★ items in file 17, in this order: the pilot definition and level (IR-Q1, IR-F2); the commercial basis (IR-D1, IR-D2, IR-J2); the sector statement (IR-G1); confirmation of the 2026-10-03 apply (IR-B1); the release conditions for the three drafts (IR-F1); the data posture — identity store, retention, s.48, AI sub-processors (IR-N1–N3, IR-M2); the depiction rules (IR-K2); and who else, if anyone, will work on the pilot (IR-C1).

**24. What should be the exact next implementation phase?**
**Phase H0 — Integrity and definition**, inside Governance (00) and Sector (01) only, in line with the owner's one-department-at-a-time cadence. All small, all offline, none needs an external party:
1. `RM-01` — renumber the changelog; `sector_truth_gate.py` must exit 0.
2. `HD-14` → `RM-02` — gates run in the Stop hook; a failure keeps work local and tells the owner.
3. `HD-02` → `RM-03` — one sector statement applied to `GLOBAL_OS.md`, `SECTOR_OS.md`, the website copy and the claims policy, with a runnable string check.
4. `HD-17` → `RM-09` and `RM-08` — the apply decision recorded; the tracker re-synced with an age warning.
5. `HD-01` + `HD-04` → `RM-04` — the pilot defined as one decision.

**Exit test for H0:** all five gates exit 0; the hook reports gate status; no public surface says "B2B SaaS only"; the tracker's date is not older than the newest department changelog; dated decision entries exist for HD-01, HD-02, HD-04, HD-14 and HD-17.
**Then Phase H1 — the pilot's record and controls** (`RM-06`, `RM-07`, `RM-10`–`RM-16`), and only after a real pilot exists, **Phase H2 — the guest-side model** (P3 vocabularies, Pre-Experience methodology, the `SIM-H-001` prototype).

---

### Most important principle, applied

The protocol asks the OS to support *information → decision → action → outcome → learning*, and for Hospitality *market → audience → occasion → experience → story → demand → sales → revenue → experience → retention → learning*. The Agency OS runs the first three links of the first loop with unusual rigour and the first link of the second loop with real data. **Both loops break at the same point — the outcome, because nothing yet records what happened for a client.** The way to close them is not more structure; it is one defined pilot, run honestly, with its approvals, its data and its results recorded where the rest of the system can read them.
