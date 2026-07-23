# Presence — Department Operating System (21)

**Version:** v0.1.0
**Last updated:** 2026-07-23
**Owner:** Mary Thuo (Agency Governance, 00)
**Mandate:** The agency's **Market Presence Infrastructure** — the outbound mirror of IntOS. Presence is how the agency projects itself into the market (`agency → world`) across every layer, so that every public interaction carries a revenue job and expresses one institutional behavior.
**Status:** New department (2026-07-23), seeded from the owner's Parts 1–4 presence work. **Blueprint-only, reality-gated** — the agency is solo, pre-revenue, 0-client, with zero social accounts and one subdomain-only website; this OS is the design the presence gets built to, not a record of live presence. Consciously **overrides** the repo's prior "no distribution/platform department/agent" decision (`04_Content/CONTENT_OS.md` §5; `PIL_INTEGRATION_REPORT.md` §10) — owner decision, 2026-07-23, recorded not silent.

> Read `GLOBAL_OS.md` first, then `00_Agency_Governance/AGENCY_COMMERCIAL_DOCTRINE.md` (this department's parent doctrine). Presence **inherits** the Commercial Doctrine; it does not restate it.

---

## 1. Mandate & Identity

Presence exists because the agency's outward market presence was a **genuine, un-owned gap**: the AEIT four-platform model (`enterprise_architecture/AEIT_01`) names EGOS (governance), OrchOS (runtime), RevOS (revenue), and IntOS (intelligence) — and **nothing** for how the agency behaves in public. IntOS senses `world → agency`; **Presence is its outbound twin — `agency → world`** — sharing the same canonical model (`AEIT_06`), runtime (`arika-runtime`), and governance (EGOS), run in the opposite direction.

**What Presence owns:**
- The **coordination layer** that makes ~20 visible + ~22 hidden presence layers behave as **one** system under one doctrine.
- The **currently-unowned** layers: the hidden/infrastructure presence (entity, knowledge-graph, schema, citation, GitHub/docs/API/changelogs, PR/authority signals) and **Engagement (two-way presence)** — the capability Content flagged as *"the one genuinely new gap; left open rather than invented"* (`CONTENT_OS.md` §10, COS Layer 7).
- The **four-directions** taxonomy (outreach/outbound/inbound/**inreach**) and the **Presence Economics** gate (every asset has an economic job).

**What Presence does NOT own — it consumes by contract, never re-claims** (one-owner discipline, `AEIT_00` §5):

| Capability | Stays with | Presence's relationship |
|---|---|---|
| Channel strategy, distribution, paid/demand-gen, SEO/AEO/GEO *strategy* | **Marketing (03)** (§10, `marketing-seo-aeo-geo`) | Coordinates; does not re-run distribution. *"Every platform is a distribution endpoint… content owned by Content (04)"* (`MARKETING_OS.md` §10) stands. |
| Content assets, multiplication tree, narrative, pillars/houses; platform *behavioral* intelligence (PIL) | **Content (04)** (ACCOS, `PLATFORM_INTELLIGENCE_REGISTRY.md`) | Consumes PIL as upstream; content still *"produces the tree; Marketing works the channels."* |
| Brand identity, Brand Genome, visual system, brand voice | **Branding (12)** | Expresses within brand law; never overrides it. |
| Owned-hub build + technical web discoverability | **Experience Engineering (20)** (`discoverability-architecture.md`) | Coordinates the entity/schema layer; EE builds the site. |
| Partnerships / partner ecosystem | **ClientPartner Acquisition (06)** | Coordinates ecosystem *presence signals*; 06 owns partner relationships. |
| Retention/expansion delivery | **Client Success (07)** | Routes **inreach** to 07; 07 delivers. |
| Legal governance of public assets (LGROS) | **Legal (10)** | Flags exposure via a liaison; never opines. |
| Asset production (image/video/voice) | **Design (19)** | Consumes finished assets. |
| Market truth / research inputs | **Sector (01) / IntOS** | Publishes their outputs *as* presence assets. |

---

## 2. Position in the architecture

```
IntOS (inbound: world → agency)          Presence 21 (outbound: agency → world)
   sources → verify → knowledge     ⟷      doctrine/voice → produce → publish → layers → reputation → demand
        │  shared canonical model (AEIT_06) · shared runtime (arika-runtime) · shared governance (EGOS) │
        ▼                                                     ▼
     Departments consume verified truth            Presence → demand → RevOS (pipeline → revenue)
```

Presence **consumes** IntOS (market truth, ICP tiers), PIL (platform behavior), Branding (voice/visual law), and the Commercial Doctrine (voice/economics). It **produces** qualified attention/demand into RevOS (Sales 05 / ClientPartner 06) using the `AEIT_09` handoff-packet standard. Dependency chain `Governance → 21 → existing owners → RevOS` is **acyclic**.

---

## 3. Capability Registry

Presence runs on four sub-systems.

### 3.1 The Four Directions (Part 1) — the flow model

Every presence action belongs to exactly one direction, each with a revenue role and a coordinating owner:

| Direction | Meaning | Coordinated owner(s) | Revenue role | CRM `Source` |
|---|---|---|---|---|
| **Outbound** | agency → market; the agency chooses who to approach | Sales (05) outbound engine · ClientPartner (06) | Find revenue (acquisition) | `outbound` |
| **Inbound** | market → agency; demand arrives because value/visibility exist | Marketing (03) demand-gen + discoverability | Capture demand | `inbound` |
| **Outreach** | the communication mechanism used across both | Sales/Marketing/Content | Accelerate trust | *(mechanism, not a source)* |
| **Inreach** | deepen existing relationships + internal alignment | Client Success (07) expansion · Governance/HR (internal) | Expand value (retention/expansion/referrals) | **`inreach` (new)** |

**`inreach` is genuinely new** — the term and the direction exist nowhere else in the repo. Staged edit adds `inreach` to `CRM_SCHEMA.md`'s `Source` list (currently `inbound / outbound / referral / partner / event`).

### 3.2 The Presence Layer Registry — the core artifact

The agency's manageable map of every place it can have presence. **Rule:** no layer enters without an **owner**, a **direction**, an **economic job** (Presence Economics, `AGENCY_COMMERCIAL_DOCTRINE.md` §9), and a **reality-state** (`live` / `planned` / `watchlist`). Reality-gated: nearly everything is `planned`/`watchlist` today — a maintained map, not empty structure (`REGISTRY_TAXONOMY_REFERENCE.md` "don't build empty registries").

**A. Visible presence layers (Part 2's 20-layer stack):**

| Layer | Primary owner (execution) | Economic job (example) | Reality-state |
|---|---|---|---|
| Owned — Website | EE (20) builds · Content fills · **21 coordinates** | Conversion hub; reduce sales cycle; pricing power | `live` (subdomain-only, uncommitted) |
| Owned — Newsletter · Knowledge base · Client portal | Content/Marketing · **21 (docs/KB)** | Owned trust & nurture, algorithm-independent | `planned` |
| Executive/Authority — LinkedIn, X, guest articles, podcasts, speaking | Content produces · Marketing distributes · **21 coordinates** | Executive trust → primary B2B pipeline | `planned` (no accounts) |
| Search / Discovery | Marketing (strategy) · EE (technical) · **21 (entity/schema)** | Be found at intent; inbound capture | `planned` |
| AI presence (ChatGPT/Claude/Gemini/Perplexity/Copilot recommendation) | **21 (discovery-authority)** · Marketing GEO | Be recommended by AI assistants | `planned` |
| Video / Audio | Design (19) produces · Marketing distributes · **21 coordinates** | Demonstrate thinking; searchable authority | `planned` |
| Community | **21 (engagement)** | Peer credibility; relationship building | `planned` |
| Review / Directory | **21 (authority-pr)** | Third-party trust; qualified inbound | `watchlist` |
| Partnership / Ecosystem | ClientPartner (06) · **21 coordinates signals** | Trust transfer, borrowed credibility | `planned` |
| Event / PR | **21 (authority-pr)** | Authority at scale | `watchlist` |
| Educational / Data / Tool | Content/Consulting · Sector/IntOS (data) · Automation/EE (tools) · **21 coordinates** | Thought leadership; citation-worthy; interactive proof | `planned` (assessments live on site) |
| Email | Marketing/Content · **21 coordinates** | High-ROI executive nurture | `planned` |
| Personal (founder) | **21 (authority-pr)** + owner | Founders are bought before agencies | `planned` |
| Client | Client Success (07) advocacy · **21 coordinates** | Clients become presence (referrals, joint) | `planned` (0 clients) |
| Product | Offer (02)/EE · **21 coordinates** | Tools/templates that market passively | `watchlist` |

**B. Infrastructure / hidden presence layers (Part 3's 22) — Presence's legitimate core (no other owner):**

| Layer group | Owner | Economic job | Reality-state |
|---|---|---|---|
| Public/private **GitHub repos**, **open documentation**, **API documentation**, **developer communities**, **public changelogs**, **technical blogs** | **21 (developer-surface)**; build via EE/Automation | Technical credibility; developer & AI-crawler trust; enterprise-procurement readiness | `watchlist` |
| **Research repositories**, **public datasets** | Sector (01)/IntOS produce · **21 publishes** | Original data → citations → authority → demand | `planned` |
| **schema.org metadata**, **knowledge-graph**, **entity recognition** (EEO/KGO) | **21 (discovery-authority)** · EE technical | Machines understand & recommend the agency as an entity | `planned` |
| **Branded search demand** (BSO), **citation networks**, **backlink quality** | **21 (discovery-authority)** · Marketing | Authority signals that compound; branded search growth | `planned` |
| **Digital PR footprint**, **partner mentions**, **speaker profiles**, **conference agendas**, **university references**, **investor-ecosystem mentions** | **21 (authority-pr)** · ClientPartner (06) | Third-party validation; institutional credibility | `watchlist` |
| **Browser search suggestions**, **AI assistant recommendations** | **21 (discovery-authority)** · Marketing | Control first impressions; be the recommended answer | `planned` |

*(The 9 internal capability layers from Part 2 — Intelligence, Knowledge, Narrative, Design, Video, Automation, Relationship, Measurement, Decision — are the capacities presence draws on; they are already owned by IntOS/Sector, Notion/knowledge, Content, Design, Automation, CRM, Marketing-attribution, and Presence's own decision agent respectively. Not re-created here.)*

### 3.3 Discovery, Authority & Trust engine (Part 3 — DATOS)

The discoverability disciplines, ownership split so no discipline has two owners:

| Discipline | Question it answers | Owner |
|---|---|---|
| SEO · AEO · GEO | Can we be found / be the answer / be recommended by AI? | **Marketing (03)** `marketing-seo-aeo-geo` (strategy) |
| Technical web discoverability (site structure, performance, semantic HTML) | Can the hub be crawled and extracted? | **EE (20)** `discoverability-architecture.md` |
| **EEO · KGO · BSO · semantic · citation/authority** | Do machines know *who we are* and how everything connects; do trusted sources validate us? | **Presence (21)** — the previously-unowned layers |
| SXO · CRO | Once found, is the experience great; do visits convert? | EE (20) / Marketing (03) |
| RMO (reputation) | What do people find after discovering us? | **Presence (21)** (authority-pr) |

Presence **orchestrates the engine end-to-end**; each discipline keeps its single owner.

### 3.4 Engagement — two-way presence (the genuinely-new capability)

Content's COS Layer 7, *"Engagement — conversations, not just consumption… the one genuinely new gap; left open rather than invented."* Presence takes ownership: replies, DMs, community management, conversation quality — the *"conversations hit home"* mandate. Reality-gated (no accounts, no conversations yet); DM-automation execution stays with Automation (16)'s Engagement Layer.

---

## 4. Workflow Index

Intended shape (not yet an executable automation; reality-gated):

1. **Doctrine intake** — Commercial Doctrine + Brand Genome + IntOS market truth + PIL platform behavior → the constraints every presence output inherits.
2. **Direction routing** — a presence objective is classified outbound / inbound / outreach / inreach and routed to the coordinating owner.
3. **Layer selection** — `presence-orchestrator` picks which layers get attention this cycle (by sector opportunity, buying window, economic job).
4. **Economic gate** — `presence-economics-gate` (the Presence Intelligence Filter) approves only assets with an economic job + ≥1 of the five movements.
5. **Produce → publish** — via the existing owners (Content/Design/Marketing/EE), platform-native per PIL.
6. **Engagement** — two-way response captured back into CRM (commercial memory) and IntOS (learning).
7. **Measure** — executive engagement, qualified conversations, referrals, branded-search growth, AI-recommendation frequency (Marketing attribution owns measurement truth).

---

## 5. Agent Roster — PROPOSED (design only)

> ⛔ **OWNER REVIEW GATE.** Per the approved sequence, these are the **proposed** roster; the actual `.claude/agents/presence-*.md` specs are **not written until the owner ratifies this OS + the doctrine + the boundaries.** Listed here as design, not implementation. All are **reality-gated** — runtime-wiring deferred until `ANTHROPIC_API_KEY` + real accounts exist (the whole agent layer is currently unrunnable). Advisory-first per Constitution §5.

| Proposed agent | One job | Risk class | Pattern reused |
|---|---|---|---|
| `presence-orchestrator` | The Decision layer: which direction/layer/sector gets attention; resolves conflict across presence agents | 2 | `sales-executive-intelligence` |
| `presence-layer-registrar` | Gate for entering/superseding a Presence Layer Registry row; enforces one-owner + economic-job + reality-label | 2 | `techstack-inventory-registrar` |
| `presence-economics-gate` | The Presence Intelligence Filter: no asset ships without an economic job + ≥1 of five movements | 2 | `content-publishing-gate` |
| `presence-discovery-authority` | Orchestrate entity/KGO/schema/citation/branded-search; contract to Marketing SEO/AEO/GEO + EE technical | 2 | `marketing-seo-aeo-geo` |
| `presence-engagement` | Two-way presence / community (COS Layer 7); routes DM-automation to Automation (16) | 2 | — (new capability) |
| `presence-developer-surface` | Governs *what/whether* to publish on GitHub/docs/API/changelogs/technical blogs | 2 | — |
| `presence-authority-pr` | PR footprint, speaker/conference/university/investor/partner-mention + review/directory signals | 2 | — |
| `presence-legal-liaison` | Routes presence-specific legal exposure to Legal (10); never opines | 2 | `legal-counsel-router` |

Class 3 / human sign-off on anything public-facing or money/contract-touching (e.g. actually publishing to a live account, a PR statement, a partner co-brand).

---

## 6. Skill Library Index

None yet. Candidate future skills (a "presence-audit" gate against the Presence Constitution; a "presence-economics" spec generator) deferred until the department is ratified and there is real presence to govern.

---

## 7. KPI Dictionary

Deliberately **uncalibrated** — zero presence data exists, so these are targets, not baselines (repo precedent: never fabricate a baseline). Executive engagement · qualified conversations · meetings · referrals · proposal requests · opportunity value · **branded-search growth** · **AI-recommendation frequency** · citation/backlink quality. Explicitly **excluded**: impressions, followers, likes, reach (Presence Constitution §8 rule 4).

---

## 8. Decision Log

- **2026-07-23 — Presence (21) established** as a full department with its own OS and (proposed) agents. **Conscious override** of the prior "no distribution/platform department/agent" decision (`CONTENT_OS.md` §5; `PIL_INTEGRATION_REPORT.md` §10) — owner decision, recorded like the Legal drafting override. Framed as the **outbound mirror of IntOS**, not a new "distribution" layer; owns coordination + the previously-unowned hidden layers + Engagement, and consumes (never re-claims) Marketing/Content/Branding/EE. — Claude Code (Opus 4.8)
- **2026-07-23 — `inreach` introduced** as the fourth direction; nonexistent elsewhere in the repo. Staged CRM `Source` edit queued (not applied). — Claude Code (Opus 4.8)
- **2026-07-23 — One-owner discipline preserved.** Every presence capability resolved to exactly one execution owner; DATOS disciplines split (Marketing strategy / EE technical / Presence entity-layer) to avoid a second claimant (`AEIT_00` §5). — Claude Code (Opus 4.8)

## 9. Risk / Incident Log

- **Standing risk — structure ahead of content.** This department is a blueprint over a 0-client, $0-revenue, zero-social-account agency; a Presence Layer Registry that reads full of `live` rows when nothing is live would be the exact drift disease the repo has caught four times. Mitigation: every row carries an honest reality-state; nearly all start `planned`/`watchlist`.
- **Standing risk — reopened decision.** Overriding the declined-distribution stance risks re-fragmenting the ownership Content/Marketing deliberately consolidated. Mitigation: §1 consume-by-contract table; `presence-layer-registrar` enforces one-owner on every new row.
- **Standing risk — unrunnable agents.** Like all 106 agents, the proposed roster cannot run (`ANTHROPIC_API_KEY` unset). Specs are gated behind activation; §5 says so.

## 10. Standards & SOPs Index

- **Presence Economics standard** (`AGENCY_COMMERCIAL_DOCTRINE.md` §9) — every asset has an economic job; enforced by `presence-economics-gate` and `presence-layer-registrar`.
- **The Presence Intelligence Filter** (`AGENCY_COMMERCIAL_DOCTRINE.md` §10) — the seven pass/fail questions before publish.
- **Presence Constitution** (`AGENCY_COMMERCIAL_DOCTRINE.md` §8) — the six non-negotiables.
- **Boundary standard** — the §1 consume-by-contract table is the department's anti-duplication SOP.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Presence coordination + Layer Registry | Presence (21) | Governance (00) | Marketing 03 · Content 04 · Branding 12 · EE 20 | all |
| Four-directions routing | Presence (21) | Governance (00) | Sales 05 · Marketing 03 · Client Success 07 | RevOS |
| Hidden/infrastructure layers | Presence (21) | Governance (00) | EE 20 · Automation 16 · Sector 01 | — |
| Engagement (two-way) | Presence (21) | Governance (00) | Automation 16 · Content 04 | — |
| Legal exposure of public assets | Legal (10) | Legal (10) | Presence (21) liaison | Governance |

## 12. Triggers / Automation Hooks

None live. Proposed agents will register `triggers/execution/risk_class/output_schema/memory_stream/emits` on `arika-runtime` **only after** the review gate and activation. Any live automation needs an `AUTOMATION_APPROVAL_MATRIX.md` row *before* firing (Constitution rule).

## 13. Grandfathered code layer

None — new department, no pre-existing code (unlike Finance/Branding).

## 14. Raw Archive Pointer

No raw `Draft N.md` archive. Seeded directly from the owner's Parts 1–4 presence conversation (2026-07-23), captured in the Commercial Doctrine and this OS. No unverified raw material to migrate.

## 15. Changelog

- **v0.1.0 (2026-07-23):** Department created. Mandate, four-directions model, Presence Layer Registry (20 visible + 22 hidden layers), DATOS engine, Engagement capability, proposed agent roster (design only, pre-gate), KPIs, standards, RACI. Blueprint-only, reality-gated. — Claude Code (Opus 4.8)

## 16. Honest State

Presence has **produced nothing** — no account, no post, no repo, no citation. Its one real footprint is a website it does not own (built by EE, live only on a `.vercel.app` subdomain, uncommitted in git). The department is **entirely structure ahead of content**, declared so. What is real is the *design*: a single coordinating owner for a presence that was previously ownerless, a doctrine it inherits, and an honest map of every layer with nothing faked as live. The gate before the next phase (agents) is deliberate — no agent is written until the owner ratifies this.
