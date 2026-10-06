# 12 — AI Governance and Production

**Protocol §9:** where does AI belong — *"it should NOT automatically be treated as the product"*? Classify AI activities as strategic, operational, production, experimental or governance-sensitive, and identify missing governance for truthfulness, representation of real property, synthetic people, synthetic experiences, disclosure, IP, brand safety, client approval and factual accuracy.

> 🔴 Nothing in this file is legal advice. The repository's Legal department is explicit that *"Claude is not counsel"* and that its seven templates are unreviewed drafts. Every legal point below is framed as a **question for counsel**, which is how `legal-counsel-router` is designed to route such matters.

---

## 1. Where AI sits — substrate, not product

**`CONFIRMED`:** AI is the agency's operating substrate and a production tool; the *product* is revenue infrastructure.

- Positioning is *"Revenue Infrastructure Partner"* — explicitly not an automation or AI agency (`OFFER_OS.md` §1). AI appears in the pitch as *"AI-native operations… the same kind of system it installs for clients"* (company profile §13, point 7).
- Every agent is **advisory**: it recommends and logs; a human performs every state change; Class 3+ requires human sign-off with no convenience exceptions (Constitution §3, §5; `arika-runtime/src/governance.ts`).
- AI *is* sold in two offers — AI Workflow Infrastructure (#6) and AI Transformation Systems (#11) — but not in the Hospitality offer, where AI appears only as *"Future AI: channel-data parsing for the audit · draft messaging generation · booking-mix anomaly detection — all human-validated"* (Draft 41 Phase 12).

## 2. AI activities — present, where, and of what kind

Categories: **A** strategic · **B** operational · **C** production · **D** experimental · **E** governance-sensitive.

| Activity | Present? | Where (evidence) | Category | Reality |
|---|---|---|---|---|
| Research | ✅ | Sector skills S01/S03/S05 run by interactive Claude Code with web tools (cloud routines have none) | A · **E** (sources and claims) | `LIVE` (15 skill-run records) |
| Intelligence | ✅ | `sector-intelligence-mapper`, `sector-signal-refresher`, S06 state distiller | A | agents never run; skills `LIVE` |
| Ideation | ✅ | `content-opportunity-mapper`, Marketing chiefs | B | never run |
| Strategy support | ✅ | `offer-orchestrator`, `offer-oeos-engineer`, `marketing-chief-strategist`; Consulting agents **deliberately do not produce advice** (delegability ban) | A · E | Offer `LIVE` (5 manual runs) |
| Pricing support | ✅ | `offer-pricing-floor-analyst` | A · **E** | `LIVE` once; **spec gap** — nothing stops it mapping a hotel onto SaaS ARR bands (Draft 41 §11.4) |
| Qualification | ✅ | `sector-icp-fit`, `sector-signal-scorer`, `sales-lead-qualification` | B · **E** (people data) | never run on a real prospect |
| Visualisation / pre-visualisation | ✅ | Design storyboard (7 fields); EE storyboard (9 fields); Claude Design | C · **E** (real property) | storyboard routine `LIVE` once |
| Image generation | ✅ | KIE.ai Nano Banana Pro; OpenArt; Claude Design → Canva | C · **E** | `LIVE` (website imagery, 2026-07-04/07) |
| Video generation | ✅ | KIE.ai Seedance; OpenArt | C · **E** | `BUILT` (mock-tested); no recorded real video |
| Editing / enhancement | ✅ | Production Engine *Enhancement/Upscale* stage | C | `DESIGNED` |
| Localisation / translation | ❌ | **None.** Content DB 6 "Translation Matrix" means *platform* translation, not language | D (absent) | — (`HV-24` languages row) |
| Campaign adaptation | ✅ | `content-multiplication-engine`; DB 6 one-truth-many-expressions with `Core Message` as a locked rollup | B | never run |
| Automation | ◐ | `arika-runtime` (manual only — **scheduler not approved**, 30 declared triggers vs 2 matrix rows); Creative Pipeline cloud routine | B · **E** | manual `LIVE` |
| Analytics | ◐ | `marketing-attribution-modeling`; finos engines | B | no data |
| Decision support | ✅ | `operations-daily-command`, `operations-opportunity-filter`, `sales-executive-intelligence` | A | never fired |
| Production acceleration | ✅ | `content-brief-builder` → Design chain | C | partial |
| Legal routing | ✅ | `legal-counsel-router` — *decides whether something needs a lawyer; never answers it* | **E** | `BUILT` |
| Governance gating | ✅ | `ai-enablement-governance-gate` — **blocked by design** while no legal reviewer exists | **E** | `BUILT` |

## 3. Safeguards that exist — and they are substantial

| Safeguard | Evidence | Reality |
|---|---|---|
| Human sign-off at Class 3+; unattended dispatch of gated specs refused **before any model call**; a run awaiting review advertises no events | `governance.ts`; `executor.ts:61`, `:150`; `tests/approval-dispatch.test.mjs` | `BUILT`, **71/71 tests pass (2026-10-06)** |
| No silent invention; structure may be empty, never guessed | Constitution §3 | doctrine, widely enforced in specs |
| Human review of every client-facing AI output — *"no fully autonomous client-facing AI without a review gate"* | `API_AND_AI_TOOLING_TERMS.md` §2 (from Automation `Draft 35` Phase 3 immutable) | draft, unreviewed |
| AI-use disclosure **to the client**, consent or restriction per SOW | `API_AND_AI_TOOLING_TERMS.md` §1 | draft, unreviewed |
| No imitation of an identifiable third party's work, marks or **likeness** | same, §3.3 and internal rule 7 | draft, unreviewed |
| AI-generated material's copyright status flagged *"genuinely unsettled"*; Arika assigns whatever rights it holds — *"which may be none"* | `IP_COPYRIGHT_TRADEMARK_TERMS.md` §4 | draft, unreviewed |
| Claims classes A–D; Class C banned; Class D disciplined | `CLAIMS_SUBSTANTIATION_POLICY.md` | draft, unreviewed |
| AI-artifact quality gate before shipping an asset | `design-brand-environment-consistency-checker`; `DESIGN_OS.md:123`, `:260` | `BUILT`; caught a real defect once |
| Reuse gate before credit spend | `design-asset-librarian` | `BUILT` |
| Network-blocking fixture lane; memory streams guarded | `offline_guard/`; `fixture.ts` | `BUILT`, 46 + 71 tests |
| Client data to AI vendors treated as sub-processing | `API_AND_AI_TOOLING_TERMS.md` §4; `DPA.md` Annex B | draft; **s.48 basis undocumented** (item 61) |
| Simulated evidence bounded to mechanisms only | A001 D20; extended to SYNCO-01 | in force |
| Secret handling — exposed key rotated and revoked | Item 57 / AG-19: owner-attested 2026-09-21; replacement verified by use | closed |

## 4. Missing governance — the protocol's nine requirements

| Requirement | What exists | What is missing | Owner | Priority |
|---|---|---|---|---|
| **Truthfulness** | Claims classes for statements | A **depictive class**: an image or film of an experience is an implied Class A/B claim with no rule | Legal (10) → Content/Design gates | **P1** before any AI depiction of a real property |
| **Representation of real property** | — | Rule that a depiction shows only facilities, food, layouts and services that exist and are available as shown; otherwise labelled *visualisation* | Legal (10); enforced by Design checker | **P1** |
| **Synthetic people** | SYNCO-01 excludes synthetic people **as fixture data**; nothing for marketing imagery | Rule: no identifiable synthetic faces; no real likeness without written release; the protocol's *faceless* convention as policy, not style | Legal (10) / Design | **P1** |
| **Synthetic experiences** | — | Rule for previewing an event or experience that has not happened (labelling, date-subject-to-confirmation, link to DB 7 change versioning) | Content / Legal | P1 for the prototype · P2 otherwise |
| **Disclosure** | AI-use disclosure to the **client** | Disclosure to the **consumer** (the hotel's guests), per the jurisdictions of the audience — including EU/UK origin markets | Legal (10) — counsel question | **P1** |
| **Intellectual property** | IP terms §4 (unsettled); no-imitation rule | Music/sound licensing record per asset; ownership position a client can rely on | Legal (10) — counsel | P1 before client delivery |
| **Brand safety** | Brand Genome; brand/environment checker | The checker enforces **Arika's** environment doctrine; a **client's** brand rules have no home (`HV-11`) | Design / Branding | P1 before client delivery |
| **Client approval** | Draft 41 per-deliverable client approvals (prose) | An approval record, and specifically approval of every depiction of the client's property (`HV-09`) | Operations / Governance | **P1** |
| **Factual accuracy** | QG3 benchmark labelling; QG6 client-system data only; claims classes A/B | AI-drafted copy about a property's facts has no specific verification step | Content | P2 |

## 5. Proposed rule set — "depictive claims and synthetic media" (draft for owner and counsel; not applied)

Extend `CLAIMS_SUBSTANTIATION_POLICY.md` with one class rather than writing a new policy:

| # | Proposed rule |
|---|---|
| V1 | A depiction of a **real** property shows only what exists and is available as depicted. Anything else is labelled *visualisation* in or beside the frame. |
| V2 | **No identifiable synthetic person.** No real person's likeness without a written release. Faceless, silhouette, hands and back-of-frame conventions are policy. |
| V3 | A preview of a future event or experience says so, and its date is *subject to confirmation* until the DB 7 signal is `Confirmed`. |
| V4 | The client approves every depiction of its property **before** publication, recorded in the approval register (`HD-06`). |
| V5 | Consumer-facing AI disclosure follows the rules of the **audience's** jurisdiction — counsel to specify for Kenya and each origin market targeted. |
| V6 | Every generated asset carries provenance: tool, model, prompt reference, source images, music/sound licence, approver, date. |
| V7 | No imitation of a third party's property, brand or trade dress (already AI tooling terms §3.3 — restated for imagery). |
| V8 | Factual statements about the property inside creative follow Classes A/B — true today, deliverable now. |
| V9 | A **fictional demonstration property** (`SIM-*`) is labelled as such everywhere it appears and is never presented as a client, a case or a typical result. |

**Where it would be enforced (EXTEND, no new agent):** `design-brand-environment-consistency-checker` (V1, V2, V6, V7) · `content-publishing-gate` given a plane-aware path for client and demonstration content (V3, V8, V9) · the approval register (V4) · the SOW (V5).

## 6. Questions for counsel (to add to the existing counsel brief — not answered here)

1. What advertising-standards and consumer-protection rules apply to AI-generated or AI-altered imagery of a **Kenyan** hospitality property, and to the same campaign shown to audiences in **the UK, Germany, Italy and the US** (the current origin markets in DB 15)?
2. Do any of those jurisdictions require a consumer-facing label on AI-generated or synthetic imagery or video, and in what form?
3. Who owns AI-generated imagery delivered to a hotel client under Kenyan law, and what may Arika honestly tell the client (`IP_COPYRIGHT_TRADEMARK_TERMS.md` open item 1)?
4. What licensing record is sufficient for AI-generated or library music and sound used in client advertising?
5. Does depicting a real property's facilities in an "imagined" scenario create misrepresentation exposure for the **client** (the advertiser), the **agency**, or both?
