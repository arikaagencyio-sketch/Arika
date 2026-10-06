# 16 — Hospitality Pilot Readiness

**Protocol §26:** score the existing Agency OS across 24 dimensions — `0` absent · `1` conceptual · `2` partially implemented · `3` operational · `4` mature · `5` highly integrated — with evidence for every score.

**Scoring rule used here.** `3 · operational` requires that the capability has **actually run on real (non-fixture) input** with a dated record. Nothing reaches `4`, because no capability has run *for a client* — there are none. This is the protocol's scale read through the repository's own `AEIT_11` rule: *a state may only be claimed with its named test*.

---

## 1. Scores

| # | Dimension | Score | Evidence for the score | What holds it there |
|---|---|---|---|---|
| 1 | **Governance** | **3** | Constitution risk classes enforced in code (`governance.ts`; 71/71 runtime tests, 2026-10-06); authorisation registers used and spent (CRM-PROV-1, SECTOR-SF1/SF2, D21, OFFER-F2/F3); five runnable gates; `AEIT_11` reality standard | Truth gate red (HV-01); RACI frozen (HV-31); tracker lag (HV-07); R1/R3 unenacted (HV-21); every legal template unreviewed (HV-04) |
| 2 | **Intelligence** | **3** | 16 live Sector DBs (217 findings, 33 sources, 13 places, 5 routes, 3 destinations); 15 dated skill runs; Gate F passed ×3; tiered provenance | DB 9/DB 10 row provenance empty (0/28, 0/399); no return edge from outcomes; P3 (Plane B demand) unauthored |
| 3 | **Client management** | **2** | ClickUp `Client`/`Project` lists live; intake gate built; onboarding/retention/offboarding workflows specified | 0 clients; Company/Pilot not verified live (HV-05); intake unratified; S3–S5 blocked; no client separation (HV-11) |
| 4 | **Prospecting** | **2** | `PROSPECT-H-20261003-01` executed on real public evidence; tested validator (8/8); Hospitality routes in three agents | 0 sends; CRM rows unverified; scorecard never run; record lacks archetype/timing/trigger (HV-36) |
| 5 | **Strategy** | **2** | OEOS structural engineering of the offer (Draft 41); MVP scope decisions; Commercial Doctrine | No client strategy ever produced; contradictory public positioning (HV-02); group strategy undefined (HV-03) |
| 6 | **Experience architecture** | **1** | P5 demand themes; intake H-A05 facilities question; P2 archetypes | No experience/offering model; "Experience" name taken (HV-39); Pre-Experience absent (HV-15) |
| 7 | **Calendar** | **3** | DB 7 live with activation offsets; Resolution Engine run on real places (6/8 steps); origin ⇄ destination doctrine evidenced by disjoint source markets | Client step never exercised; Gate H unrun; thin coverage; seasonality-inheritance risk (HV-24) |
| 8 | **Audience** | **2** | DB 9 (4 lenses) + DB 10 (titles) + DB 6 (5-layer language) for the hotel buyer | Guest plane absent; DB 16 conflation (HV-17); Content's SaaS-only roles (HV-43) |
| 9 | **Market** | **3** | DB 1/2 (25 verticals, 321 sub-sectors, Priority Scores); Accommodation `Target`; DB 12/13 state and forecast | Second hospitality sub-sector unauthored (HV-41) |
| 10 | **Destination** | **3** | DB 16 profiles sourced to T1 (verification rejected owner hypotheses — the system working); Destination Fit gate blocks unprofiled Mombasa | No East Africa / county level; route lead times blank; universality conditional (31b) |
| 11 | **Content** | **2** | 8 Notion DBs; 3 Accommodation opportunities; one campaign/brief chain | No Content agent has ever run; no client dimension; problem-led narrative only (HV-14) |
| 12 | **Creative** | **2** | Brand Genome; Design production chain with reuse and AI-artifact gates; real generated imagery (2026-07) | Client brand rules have no home; depiction rules absent (HV-13); credit runway unknown (HV-38) |
| 13 | **AI** | **2** | 115 agents built; manual runtime `LIVE` (Offer, 5 runs); human gate enforced and tested | Scheduler unapproved; 106 agents never run on real input; synthetic-media governance absent |
| 14 | **Distribution** | **1** | Presence layer registry; LinkedIn profile + page; Postiz recorded live 2026-08-07 | Nothing published; 0 channels connected; hospitality channels unprofiled (HV-19) |
| 15 | **Sales** | **2** | 10 agents; drafts prepared and saved; qualification routes | 0 sends; proposal blocked; no negotiation parameters |
| 16 | **CRM** | **2** | 5 live lists; 4 Sector bridge fields round-trip verified (fixtures) | No real row; Company/Pilot unverified; vocabulary drift (HV-06) |
| 17 | **Revenue** | **1** | Targets; pricing hypotheses; H-bands for internal design | Hospitality unpriced; no invoice; Zoho plan lapsed at last check; rooms-only client model |
| 18 | **Measurement** | **1** | KPI formulas; P14 semantics; M6 measurement-plan design; strong claims ethics | No performance store; thresholds unset; no attribution key (HV-18) |
| 19 | **Learning** | **1** | Rich changelog lessons; memory files; IntOS learning layer designed | No learning register; empty learning log; P2 cells cannot become `observed` (HV-33) |
| 20 | **Ticketing** | **2** | ≥10 maintained registers with strong evidence; ClickUp Project pipeline | No work-item entity; colliding identifiers; no links to client/campaign/revenue (HV-10) |
| 21 | **Approvals** | **2** | Class 3 gate in code; authorisation registers; four-layer content approval | No client/creative approval record; `awaiting_review` has no resolution (HV-09) |
| 22 | **Data** | **2** | Provenance labels, honesty states, `ORG/PER/PILOT/SIM` namespaces, outside-Git custody | Identity maps split three ways (HV-44); RD2 storage half open; s.48 open (HV-04) |
| 23 | **Reporting** | **1** | D7 monthly pack designed; internal readiness reports | No dashboard spine; no client reporting template with data |
| 24 | **Scalability** | **1** | Core/plugin separation built and gated | Gate I (second sector) unrun; capacity = one H1/H2 client; group delivery absent (HV-03, HV-26) |

**Mean: 46 / 24 = 1.9.** Five dimensions at `3`, twelve at `2`, seven at `1`, none at `0` or above `3`.

**Shape of the result (`CONFIRMED`):** *upstream* — governance, intelligence, market, destination, calendar — is **operational**. *Midstream* — strategy, content, creative, sales, CRM, approvals — is **partially implemented**. *Downstream* — revenue, measurement, learning, reporting, distribution, experience architecture, scalability — is **conceptual**. The OS knows its market well and has never served a client.

## 2. Reconciliation with the repository's own measurement

`READINESS_ASSESSMENT_2026-10-02.md` (refreshed 2026-10-03) measured agency-wide **mechanism 53.0 %, simulation 53.4 %, real-pilot 16.5 %, client-facing 2.3 %**, and for the first real pilot **mechanism 72.0 %, real-pilot 15.0 %, client-facing 0.0 %**. The two methods measure different things — that assessment asks *does the machinery work and may it run on real data*; this one asks *how far is each operating dimension from serving a hospitality client* — and they agree: strong machinery, almost no real-world operation, zero client-facing permission.

Two of its recorded facts have since moved: the gate count (now **4 of 5** passing — HV-01) and D4 (largely addressed by `7d341f5` — file 14 §3). It should be re-measured, not carried forward (RM-18).

## 3. Readiness by pilot type

| Pilot type | Verdict | Conditions / blockers |
|---|---|---|
| **A. Public-only prospecting and group discovery conversations** (no client data, no price) | 🟡 **Ready with conditions** | Owner review of exact messages; sender/DKIM checks; **keep the website out of outreach until HV-02 is fixed** (already done in the batch); optional CRM write after RM-06/RM-07; decision `HD-03` |
| **B. MVP for one H1/H2 property** (audit + blueprint, client data) | 🔴 **Not ready** | Legal chain (59, 61), RD2 storage, reviewed contract/NDA/DPA, commercial basis and Phase 11 inputs (`HD-04`), approval record (HV-09), client separation (HV-11) |
| **C. Pilot with the intended multi-property group** | 🔴 **Not defined** | `HD-01`: what the group pilot delivers; no group offer; union operator unbuilt; capacity beyond one H1/H2 client unapproved |
| **D. Pre-Experience / corporate-tennis prototype** (agency demonstration, no client data) | 🔴 **Not ready — but the fastest to unblock** | `HD-10` (go/no-go and ownership), depiction rules (HV-13), a fresh `SIM-H-001` (HV-28), a Plane B narrative variant (HV-14), a generation-budget check — **no legal client-data dependency** |
| **E. The full vertical as the protocol describes it** (revenue centres, pathways, experience model) | 🔴 **Not ready** | Plane B model (P3 vocabularies, HV-12, HV-16, HV-17); measurement beyond rooms (HV-18) |

## 4. Verdict

**The Agency OS is not ready for a client-facing Hospitality pilot.** It is ready to keep doing what it has started — public-company research and carefully reviewed discovery outreach — provided the public surfaces stop contradicting the vertical. The binding constraints are not code: a pilot definition, a lawyer, a price, and an honest public face. The structural constraint behind all of them is that the OS models the agency's sale to hotels and not yet the hotel's sale to its guests.
