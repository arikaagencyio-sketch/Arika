# Content Intelligence Layer — Notion Data Model (Schema Spec)

**Department:** Content (04) · **Status:** **BUILT 2026-08-16** — all 8 databases live in Notion with every relation, rollup and formula resolved (IDs in §6). **Seeded:** DB 1 (10 platforms) and DB 2 (10 narrative positions). **Empty by design:** DB 3, 4, 5, 6, 7 — sector-dependent rows wait on a named sub-sector; DB 8 schema live, 12 offer rows pending. The old content-brief database is **superseded but not yet deleted** — deletion is gated on the cloud routine being re-pointed and verified (§4 note 5).
**Purpose:** The build specification for the Content Intelligence Layer — 7 new Notion databases plus the rebuilt content-brief database, their fields, relations, rollups, formulas, views, and the exact field-to-field flow from Sector (01)'s live intelligence into a production-ready brief. This is the technical blueprint; it is written so the build can be executed without improvising.

> Read [`GLOBAL_OS.md`](../GLOBAL_OS.md), then [`CONTENT_OS.md`](CONTENT_OS.md) (the what) and [`PLATFORM_INTELLIGENCE_REGISTRY.md`](PLATFORM_INTELLIGENCE_REGISTRY.md) (platform behavioral doctrine) alongside this file. The Sector-side counterpart and the pattern this file follows is [`../01_Sector/SECTOR_NOTION_SCHEMA.md`](../01_Sector/SECTOR_NOTION_SCHEMA.md).

---

## 0. Design laws (read before building)

1. **Consume canonical entities; do not reinvent them** (`AEIT_06`). Sector (01) owns sector truth, audience roles, decision-makers, linguistics and signals. Offer (02) owns offers. Governance (00) owns the CRM. This layer **relates**, it does not re-store.
2. **Reference, never duplicate.** Cross-platform links (Notion → ClickUp) are **text ID fields**, never native relations. Keep IDs stable.
3. **Every field earns its place.** Each carries a purpose tag: `ID` (identity) · `RET` (retrieval/filter) · `REL` (relation) · `GOV` (governance/trust) · `EXE` (drives execution). A field with no purpose tag does not get built.
4. **Notion API constraint:** the native `Status` property type cannot have its options set via the API. Use **`Select`** for every lifecycle field. (The same fix Sector and Content both already applied.)
5. **If it can be inherited, it is not typed.** Anything reachable through a relation becomes a rollup. Retyping upstream truth into a downstream row is the duplication this layer exists to end.
6. **Structure may be empty; it may not be guessed.** A database with 0 rows is a legitimate state. A database filled with plausible-looking invented values is a constitutional breach (`AGENCY_OPERATING_CONSTITUTION.md` §3.1, §3.3).
7. **Advisory-first.** Agents recommend rows; a human writes them. Publishing externally is Risk Class 3.

---

## 1. Position in the architecture

The layer sits **between** Sector's intelligence and Content's production, and it exists because those two were previously connected by nothing:

```
MARKET / SECTOR INTELLIGENCE  (Sector 01 — 13 live Notion DBs)
        │
        ├──────────────► DB 3  Sector × Platform Matrix ◄──── DB 1 Platform Registry
        │                        │                                    ▲
        │                        │                          DB 2 Narrative Registry
        │                        ▼                                    │
        └──────────────► DB 5  Content Opportunity ◄─────── DB 4 Campaign Intelligence
                                 │                                    │
                                 ▼                                    │
                        DB 6  Content Translation Matrix ◄────────────┘
                                 │        (one truth → many native expressions)
                                 ▼
                        DB 7  Content Briefs v2  ──► Design (19) ──► Presence (21) ──► Marketing (03)
                                                     production      distribution      measurement
```

**The invariant the layer enforces:** `Core Message` is a rollup on DB 6, not a text field. A platform variant is structurally incapable of restating the strategic truth in its own words. Everything else — angle, hook, format, depth, visual, CTA, engagement — is *required* to differ.

---

## 2. The databases

Lettered IDs (DB-A…DB-H) are the approved plan's labels, retained for traceability. Numbers are build order.

### DB 1 (DB-A) — Platform Registry
**Primary entity:** one platform. **Owner:** Content (04). **Backing:** `PLATFORM_INTELLIGENCE_REGISTRY.md` §4.1/§4.2 — which **remains canonical** for the behavioral profiles and the reasoning. This is the structured mirror that carries only what other databases must relate to or roll up.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Platform | Title | ID | | |
| Code | Text | ID | `li`, `ig`, `fb`, `th`, `tt`, `pi`, `web`, `x`, `nl`, `yt` | |
| Strategic Role | Text | RET | "Why does Arika exist here?" — one sentence | |
| Revenue Function | Select | RET | `Acquisition` · `Trust-Brand` · `Authority-PR` · `Conversion` · `Owned-Trust` · `Evergreen-Discovery` · `Retention` | |
| Funnel Roles | Multi-select | RET | `Awareness` · `Consideration` · `Decision` · `Retention-Advocacy` | |
| Trust Mechanism | Text | EXE | How credibility is earned here | |
| Discovery Mechanism | Text | EXE | How content is found / spreads | |
| Native Formats | Multi-select | EXE | `Text post` · `Carousel` · `Article / Long-form` · `Short video` · `Long video` · `Static image` · `Poll` · `Thread` · `Newsletter issue` · `Live / Audio` | |
| Content Depth | Select | EXE | `Long` · `Medium` · `Short` · `Sales Asset` | |
| CTA Behaviour | Text | EXE | What a CTA may look like here | |
| Engagement Mechanism | Text | EXE | How conversation is invited | |
| KPI Hierarchy | Text | EXE | **Ordered**, per-platform. There is no universal performance score | |
| Repurposing Rules | Text | EXE | | |
| What Not To Do | Text | EXE | | |
| Posting Cadence Guidance | Text | EXE | Guidance only — the rate ceiling belongs to the L5 orchestrator | |
| Launch Priority | Number | RET | 1–10, the owner-confirmed launch order | |
| Account Status | Select | GOV | `Not created` · `Created` · `Warming` · `Connected` · `Live` | |
| *knowledge-state block* | | GOV | see §7 | |

> **Deliberately absent:** `Cadence Ceiling` (Automation 16 owns rate governance) and any measured performance value (nothing has been published).

**Seed — 10 rows, transcribed from PIL, nothing invented.** LinkedIn · Facebook · Instagram · Threads · TikTok · Pinterest · Website · X · Newsletter · YouTube, in that launch-priority order. **Tumblr is out of scope** (owner, 2026-08-02). All 10 seed `Account Status = Not created`, `Confidence = Working Hypothesis` — PIL's own status line records these as *publicly-observable platform knowledge, not agency-measured results*.

---

### DB 2 (DB-C) — Narrative Intelligence Registry
**Primary entity:** one approved strategic position. **Owner:** Content (04), guarded by `content-narrative-architect`.
**Why it exists:** the agency's narrative currently lives as prose inside an agent's prompt file, where nothing can relate to it, version it, or supersede it. This makes a position a queryable object with an evidence state.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Position | Title | ID | One approved position, one sentence | |
| Position ID | Text (unique) | ID | `nar-enemy-fragmentation` — **the Translation Family root key** | |
| Position Type | Select | RET | `Core Narrative` · `Enemy` · `Misconception` · `Belief` · `Transformation` · `Proof Standard` · `Terminology Rule` | |
| Pillar | Select | RET | `Revenue Intelligence` · `Revenue Architecture` · `Revenue Operations` · `Revenue Transformation` · `Revenue Leadership` · `Revenue Signals` · `Revenue Reality` | |
| Core Belief | Text | ID | | |
| Strategic POV | Text | ID | | |
| Problem Frame | Text | ID | | |
| Market Misconception | Text | ID | | |
| Contrarian Position | Text | ID | | |
| Desired Reframe | Text | ID | | |
| Key Insight | Text | ID | | |
| Supporting Evidence | Text | GOV | | |
| Proof Layer | Select | GOV | `Research` · `Frameworks` · `Case Studies` · `Client Outcomes` · `Industry Data` · `Operational Demonstrations` · **`None available`** | The six layers verbatim from `content-narrative-architect`, plus the honest seventh |
| Evidence Status | Select | GOV | `Evidenced` · `Inferred` · `Speculative` · **`Unevidenced — do not assert`** | First three are `content-intelligence-hub`'s confidence enum; the fourth is the hard stop |
| Proof Requirement | Text | EXE | What evidence must exist before public assertion | |
| Approved Terminology | Text | EXE | | |
| Avoid Terminology | Text | EXE | | |
| Emotional Entry Point | Text | EXE | | |
| Intellectual Entry Point | Text | EXE | | |
| Commercial Implication | Text | EXE | | |
| CTA Direction | Text | EXE | | |
| Lands With | Multi-select | RET | `CEO` · `CMO` · `Sales Leader` · `COO` · `Investor` · `Founder` | The `audience_message.role` enum verbatim |
| Story Beat | Select | RET | `Problem` · `Insight` · `Demonstration` · `Framework` · `Proof` · `Action` | Canonical Story Architecture |
| Authority Level | Select | GOV | `Agency doctrine` · `Sector-specific` · `Campaign-specific` · `Candidate — needs validation` | |
| DRAGON Reading | Select | GOV | `LinkedIn — content construction` · `Realignment — operating philosophy` · `Not applicable` · **`Conflict — unresolved`** | Persists `CONTENT_OS.md` §10 Conflict 1 as data rather than picking a side |
| Sector Scope | Relation | REL | Optional. Empty = agency-wide | Sub-Sectors `dbe10a8b-…` |
| Linguistics | Relation | REL | Sector-specific terminology, inherited | Sector Linguistics `172efe6d-…` |
| *knowledge-state block* | | GOV | see §7 | |

> **No `Source Tier`.** This DB's sources are internal repo doctrine, not external publications; a trust tier built for external citations would be a field with no purpose (law 3).

**Formula — `Assertable`**
```
ifs(prop("Evidence Status")=="Unevidenced — do not assert", "🔴 do not assert",
    prop("Status")!="Active",                               "⚠ not approved",
    prop("Proof Layer")=="None available",                  "⚠ no proof layer — Authority Without Evidence risk",
    "✅ assertable")
```

**Seed — 10 rows, every one already owner-adopted. Zero invention.**

| # | Position | Type | Status |
|---|---|---|---|
| 1 | The agency is a Revenue Growth System — not a marketing, sales, automation or consulting agency | Core Narrative | Active |
| 2 | **Fragmentation** — the market problem is not lack of marketing; revenue is the casualty of fragmented growth systems | Enemy | Active |
| 3 | *"We need more leads"* → most organizations need better revenue systems | Misconception | Active |
| 4 | *"Marketing is the solution"* → marketing without sales integration fails | Misconception | Active |
| 5 | *"Sales is the solution"* → sales without demand generation stalls | Misconception | Active |
| 6 | *"Automation is the solution"* → automating broken processes accelerates failure | Misconception | Active |
| 7 | *"Growth comes from tactics"* → growth comes from systems | Misconception | Active |
| 8 | Reactive business → Intelligent growth organization | Transformation | Active |
| 9 | Never publish: Authority Without Evidence | Proof Standard | Active |
| 10 | DRAGON — two incompatible definitions, both tracing to adopted sources | Terminology Rule | **Validating** |

Row 9 seeds `Proof Layer = Frameworks`, `Evidence Status = Evidenced`, and a `Proof Requirement` stating plainly that **the agency has frameworks and no client outcomes**. Row 10 seeds `DRAGON Reading = Conflict — unresolved` with **both letter-sets left empty** until the owner rules.
**Deferred to a second pass:** the 10 beliefs (*revenue is a system · growth is engineered · data should drive decisions · operations create scalability · technology should amplify humans · authority creates demand · trust accelerates sales · consistency beats intensity · integration outperforms specialization · business intelligence is a growth advantage*). Real and loadable; the first load stays small on purpose.

---

### DB 3 (DB-B) — Sector × Platform Intelligence Matrix ★
**Primary entity:** one `(Sub-Sector × Platform)` intersection. **Owner:** Content (04) *(moved from Sector 01, owner ruling 2026-08-16 — `PLATFORM_INTELLIGENCE_REGISTRY.md` §5)*.
**Why it exists:** it is the artifact PIL §5 named and never built. Hospitality × LinkedIn and Hospitality × Instagram must not produce the same communication; this is the governance layer that makes duplication-disguised-as-repurposing **structurally visible** instead of a matter of judgement.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Overlay | Title | ID | `{Sub-Sector} × {Platform}` | |
| Overlay ID | Text (unique) | ID | `ovl-{subsector-slug}-{platform-code}` | |
| Sub-Sector | Relation | REL | **Required** | Sub-Sectors `dbe10a8b-…` |
| Platform | Relation | REL | **Required.** Select, not multi — one row per pair is the point | DB 1 |
| Presence Reality | Select | EXE | `Buyers active` · `Buyers passive` · `Buyers absent` · **`Unverified`** (default) | |
| **Overlay Verdict** | Select | EXE | `Primary` · `Secondary` · **`Repurpose-only`** · **`Do not publish`** · `Unverified` | **The anti-duplication control** — see below |
| Buyer Behavior Delta | Text | ID | How this sub-sector's buyers differ from the PIL baseline. **Empty until researched** | |
| Trust Proof Required | Text | EXE | What reads as credible in *this* sector on *this* platform | |
| Narrative Territory | Text | EXE | | |
| Content Territory | Text | EXE | | |
| Topics | Text | EXE | | |
| Recurring Questions | Text | EXE | | |
| Hook Families | Text | EXE | | |
| Proof Mechanism | Text | EXE | | |
| Visual Grammar | Text | EXE | | |
| Narrative Style | Text | EXE | | |
| Depth Level | Select | EXE | `Long` · `Medium` · `Short` · `Sales Asset` | |
| Native Format | Multi-select | EXE | same option set as DB 1 `Native Formats` | |
| CTA Type | Text | EXE | | |
| Engagement Pattern | Text | EXE | | |
| Seasonality | Text | EXE | | |
| Publishing Windows | Text | EXE | | |
| Do / Don't Rules | Text | EXE | | |
| Funnel Role | Select | RET | `Awareness` · `Consideration` · `Decision` · `Retention-Advocacy` | |
| Campaign Role | Text | RET | | |
| Outreach Potential | Select | EXE | `High` · `Medium` · `Low` · `None` | |
| Language Overlay | Relation | REL | Words-to-use / avoid are **inherited, never retyped** | Sector Linguistics `172efe6d-…` |
| Decision-Maker Presence | Relation | REL | Which buyer titles actually sit on this platform | Decision-Maker Registry `5566c27c-…` |
| Relevant Sector Events | Relation | REL | Timing drivers | Sector Signals `c14fedb3-…` |
| Source Tier | Select | GOV | `T1 Primary` · `T2 Institutional` · `T3 Commercial-intel` · `T4 Secondary` | T4 MUST NOT drive execution |
| *knowledge-state block* | | GOV | see §7 | |

**Rollups:** `Words to Avoid` ← Language Overlay · `Buyer Titles` ← Decision-Maker Presence (unique) · `Sub-Sector Status` ← Sub-Sector `Status` · `Platform KPI Hierarchy`, `Platform CTA Behaviour`, `Platform Depth` ← DB 1.

**Formula — `Overlay Integrity`**
```
ifs(length(prop("Sub-Sector"))==0,         "🔴 no sub-sector",
    prop("Overlay Verdict")=="Unverified",  "⚠ unverified — advisory only",
    empty(prop("Source")),                  "🔴 no source",
    prop("Source Tier")=="T4 Secondary",    "⚠ T4 — must not drive execution",
    "✅ usable")
```

> **`Overlay Verdict = Repurpose-only` is load-bearing.** It means **no new Translation Family may originate on that platform for that sub-sector** — content aimed there must attach to an existing family. That is the structural difference between multiplication and the *"ten near-identical posts is spam, not leverage"* failure `content-multiplication-engine` is instructed to avoid.

**Seed — 0 rows.** Requires a named sub-sector; all 52 currently read `Status = Reference`. When seeded: **2 rows** (`{target} × LinkedIn`, `{target} × Newsletter`) — two, because two is the minimum that proves the composite key is unique *and* that a translation family can span platforms. `Buyer Behavior Delta` and `Trust Proof Required` stay **empty even then**; filling them would be an invented agency fact.

---

### DB 4 (DB-F) — Campaign Intelligence
**Primary entity:** one campaign as a strategic container. **Owner:** Content (04) *(canonical entity moved from Marketing 03, ratified `AEIT_06` §2, 2026-08-16)*.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Campaign | Title | ID | | |
| Campaign Code | Text (unique) | ID | The FK the brief carries | |
| **Master Intelligence ID** | Text | ID | Inherited by every platform expression — answers *"which campaign's intelligence performed best?"* | |
| Business Objective | Text | EXE | | |
| Revenue Objective | Text | EXE | | |
| Campaign Thesis | Text | ID | | |
| Core Insight | Text | ID | | |
| Desired Reframe | Text | ID | | |
| Objective | Select | RET | `Authority` · `Demand Generation` · `Sales Enablement` · `Partnerships` | Verbatim from `content-multiplication-engine` |
| Funnel Objective | Text | EXE | | |
| Demand Objective | Text | EXE | | |
| Authority Objective | Text | EXE | | |
| Outreach Objective | Text | EXE | | |
| Conversion Objective | Text | EXE | | |
| Campaign Phase | Select | RET | `Problem` · `Insight` · `Reframe` · `Education` · `Proof` · `Solution` · `Commercial Relevance` · `Action` | The 8-phase strategic progression |
| Offer | Relation | REL | | DB 8 |
| Primary Platform | Relation | REL | | DB 1 |
| Supporting Platforms | Relation | REL | | DB 1 |
| Sector Scope | Relation | REL | | Sub-Sectors `dbe10a8b-…` |
| Narrative Positions | Relation | REL | A campaign may carry several | DB 2 |
| Start / End | Date | EXE | | |
| Content Volume | Number | EXE | | |
| Distribution Sequence | Text | EXE | | |
| Outreach Sequence | Text | EXE | | |
| Required Assets | Text | EXE | | |
| Dependencies | Text | GOV | | |
| KPIs | Text | GOV | | |
| Revenue Target | Number | GOV | | |
| Design Folder | Text | REL | Matches Design (19)'s campaign-first Canva structure | |
| Campaign Learning | Text | GOV | Written at close | |
| *knowledge-state block* | | GOV | see §7 | |

**Seed — 0 rows.** No campaign exists. Structure without content is permitted; fabricated rows are not.

---

### DB 5 (DB-E) — Content Opportunity
**Primary entity:** one scored content opportunity. **Owner:** Content (04), written by `content-opportunity-mapper`.
**Hard requirement:** this schema accepts that agent's existing `output_schema` **field-for-field, with no transformation shim.** A mapping table nobody owns is exactly the drift `AEIT_06` exists to prevent.

> **Distinct from two other "opportunities":** Sector's **Agency Opportunity Map** (`efd6319c-…`, the *market* opportunity) and the CRM deal-level `Opportunity` in ClickUp (`901524189126`). Three concepts, three owners, no re-storing.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Opportunity | Title | ID | | |
| Opportunity ID | Text (unique) | ID | ← `opportunity_id` | |
| Problem Category | Select | RET | `Revenue` · `Marketing` · `Sales` · `Operations` · `Automation` · `Leadership` | ← `problem_category` |
| Problem | Text | ID | ← `atomic_unit.problem` | |
| Insight | Text | ID | ← `atomic_unit.insight` | |
| Solution | Text | ID | ← `atomic_unit.solution` | |
| Proof | Text | ID | ← `atomic_unit.proof` | |
| Action | Text | EXE | ← `atomic_unit.action` | |
| Proof Status | Select | GOV | `Proof exists` · `Proof required — named` · **`No proof — do not assert`** | Enforces *"write what proof would be required"* rather than inventing one |
| Pillar | Select | RET | the canonical 7 | ← `pillar` |
| House | Select | RET | `Insights` · `Demonstrations` · `Frameworks` · `Proof` · `Founder Thinking` · `Education` · `Conversion` | ← `house` |
| Content Type | Select | RET | `Report` · `Research` · `Framework` · `Guide` · `Article` · `Newsletter` · `Video` · `Carousel` · `Case Study` | ← `content_type` |
| Funnel Position | Select | RET | `Awareness` · `Consideration` · `Decision` · `Retention-Advocacy` | **Labels remain provisional** (`CONTENT_OS.md` §10) — identical to DB 7 so both move together |
| Business Objective | Select | RET | `Authority` · `Lead Generation` · `Sales Enablement` · `Client Success` · `Revenue Expansion` | ← `business_objective` |
| Revenue Impact | Number | EXE | 1–10 | |
| Authority Impact | Number | EXE | 1–10 | |
| Demand Impact | Number | EXE | 1–10 | |
| Sales Impact | Number | EXE | 1–10 | |
| Differentiation Impact | Number | EXE | 1–10 | |
| Research Requirement | Text | EXE | ← `research_dependency` | |
| Research Satisfied | Select | EXE | `Yes` · `No` · `Not required` | |
| Platform Candidates | Relation | REL | | DB 1 |
| Decision | Select | EXE | `Backlog` · `Promoted to Brief` · `Rejected` · `Parked` | The `rejected` array becomes rows, not a second database |
| Rejection Reason | Text | GOV | ← `rejected[]` | |
| Sub-Sector | Relation | REL | | Sub-Sectors `dbe10a8b-…` |
| Source Intelligence | Relation | REL | The finding this came from | Sector Intelligence `72f90a0f-…` |
| Sector Signal | Relation | REL | **The timing driver — where the Revenue Signals pillar's real fuel lands** | Sector Signals `c14fedb3-…` |
| Audience | Relation | REL | First consumer of Sector's empty Audience Roles DB — resolves structurally, returns null until Sector loads it | Audience Roles `e0513cc9-…` |
| Platform Overlay | Relation | REL | Platform-fit as a scoring input (PIL §7) | DB 3 |
| Narrative Position | Relation | REL | | DB 2 |
| Campaign | Relation | REL | | DB 4 |
| Source Tier | Select | GOV | inherited from the source finding/signal | |
| *knowledge-state block* | | GOV | see §7 | |

**Formulas**
```
Total Score    = Revenue + Authority + Demand + Sales + Differentiation Impact
Tier           = ifs(Total>=40, "Tier 1 — Mission Critical",
                     Total>=30, "Tier 2 — Growth Supporting",
                     Total>=20, "Tier 3 — Amplification",
                     Total>0,   "Below Tier 3 (<20) — schema gap, review",
                                "Unscored")
Tier 1 Gate    = if(and(Total>=40, Research Satisfied!="Yes"),
                    "🔴 BLOCKED — Tier 1 without research", "✅ ok")
Revenue Filter = if(Business Objective=="",
                    "⚠ no revenue path named — cannot create", "✅")
```
`Total Score` is a **formula, not a number field** — the agent is told *"`total` must equal the sum; do not round or fudge it to reach a tier,"* and a formula makes that unfudgeable. `Tier 1 Gate` does the same for *"No Tier 1 content is produced without research."*

**Rollups:** `Signal Deadline` ← Sector Signal `Action Deadline` · `Sub-Sector Status` · `Overlay Verdict` ← DB 3.

> **🔴 Agent schema gap — reported, not papered over.** `content-opportunity-mapper`'s `priority.total` allows `minimum: 5`, but its `tier` enum covers only 20–50. **Totals of 5–19 have no valid tier.** The `Tier` formula surfaces this as `"Below Tier 3 (<20) — schema gap, review"` rather than inventing a fourth tier. The fix belongs in the agent spec and is an owner/architecture call.

**Seed — 0 rows.** When seeded: `content-opportunity-mapper` is run **manually, once**, against a real Sector Intelligence finding and its output hand-applied as one row. That run is simultaneously the seed **and** the acceptance test that this schema accepts the agent's output. Do not hand-write opportunities to fill a backlog — a padded backlog is the exact failure mode the mapper's own honesty guardrails name.

---

### DB 6 (DB-D) — Content Translation Matrix ★
**Primary entity:** one `(Narrative × Platform × Audience)` expression. **Owner:** Content (04), written by `content-multiplication-engine` — the multiplication tree *is* the set of translations.
**Content Concepts (spec DB 09) is folded in here**: a concept is a narrative committed to a platform with a chosen angle. A separate database would add a hop and a sync burden for zero information.

| Field | Type | Purpose | Options / Notes | Relates to |
|---|---|---|---|---|
| Translation | Title | ID | `{Family} · {Platform} · {Audience}` | |
| **Translation Family ID** | Text | ID / RET | **The measurement spine.** Text, not rollup, so views can group by it | |
| Source Truth | Relation | REL | One of Source Truth / Source Intelligence is required | DB 2 |
| Source Intelligence | Relation | REL | Alternative source: an interpreted sector finding | Sector Intelligence `72f90a0f-…` |
| Platform | Relation | REL | | DB 1 |
| Audience Role | Select | RET | `CEO` · `CMO` · `Sales Leader` · `COO` · `Investor` · `Founder` | |
| Platform Overlay | Relation | REL | Inherits `Overlay Verdict` + `Presence Reality` | DB 3 |
| Campaign | Relation | REL | Supplies `Master Intelligence ID` | DB 4 |
| Opportunity | Relation | REL | | DB 5 |
| Platform Angle | Text | EXE | **Varies** | |
| Hook Type | Text | EXE | **Varies** | |
| Hook | Text | EXE | **Varies** | |
| Narrative Translation | Text | EXE | **Varies** | |
| Vocabulary | Text | EXE | **Varies** | |
| Emotional Entry | Text | EXE | **Varies** | |
| Proof Method | Text | EXE | **Varies** | |
| Visual Translation | Text | EXE | **Varies** | |
| Format | Select | EXE | **Varies.** Same option set as DB 1 `Native Formats` | |
| Content Depth | Select | EXE | **Varies.** `Long` · `Medium` · `Short` · `Sales Asset` | |
| CTA | Text | EXE | **Varies.** Never passive — no "Click here" / "Learn more" | |
| Engagement Mechanism | Text | EXE | **Varies.** Presence (21) consumes; Content authors | |
| Repurposing Rule | Text | EXE | | |
| Outreach Connection | Text | EXE | | |
| Asset Tier | Select | RET | `Tier 1 Strategic` · `Tier 2 Framework` · `Tier 3 Authority` · `Tier 4 Distribution` | Verbatim `source_asset.tier` |
| Distribution Objective | Select | RET | `Authority` · `Demand Generation` · `Sales Enablement` · `Partnerships` | *"Content should not be distributed by platform. It should be distributed by objective."* |
| Distribution Wave | Select | RET | `Owned` · `Audience Expansion` · `Authority Amplification` · `Sales Activation` | Verbatim `wave` enum |
| Narrative Preserved | Select | GOV | `Yes` · `No` · **`Unknown`** | PIL §8 check. `Unknown` is honest; a guessed `Yes` is not |
| Approved By | Text | GOV | | |
| *knowledge-state block* | | GOV | see §7 | |

**Rollups — this is where the database earns its existence**

| Name | Source | What it prevents |
|---|---|---|
| **`Core Message`** | Source Truth → `Position` | **The invariant.** Read-only and inherited — a platform variant physically cannot restate the strategic truth in its own words |
| `Family Source ID` | Source Truth → `Position ID` | |
| `Master Intelligence ID` | Campaign → `Master Intelligence ID` | Campaign-altitude measurement |
| `Avoid Terminology` | Source Truth → `Avoid Terminology` | Banned phrasing being re-derived per platform |
| `Platform Verdict` | Platform Overlay → `Overlay Verdict` | |

**Formulas**
```
Family Integrity =
if(empty(prop("Family Source ID")), "⚠ no source truth",
   if(prop("Translation Family ID") == format(prop("Family Source ID")),
      "✅ intact", "🔴 family mismatch"))

Publishable Here =
ifs(format(prop("Platform Verdict"))=="Do not publish", "🔴 overlay: do not publish here",
    format(prop("Platform Verdict"))=="Unverified",     "⚠ overlay unverified",
    prop("Narrative Preserved")!="Yes",                 "⚠ narrative check outstanding",
    "✅ clear")
```

**Two family IDs, deliberately, at different altitudes.** One narrative can span several campaigns; one campaign can carry several narratives. `Translation Family ID` answers *"which platform translation of this truth performed best?"*; `Master Intelligence ID` answers *"which campaign's intelligence performed best?"* Collapsing them into one field makes one of those two questions permanently unanswerable.

**Seed — 0 rows.** When seeded: 2 rows, one family, two platforms, `Status = Draft`, with `Platform Angle` / `Hook` / `CTA` / `Visual Translation` / `Engagement Mechanism` **left empty** — writing a hook is authoring, and the honest first pass is a human working from advisory output, not a seed.

---

### DB 7 (DB-G) — Content Briefs v2
**Primary entity:** one production specification. **Owner:** Content (04). **Replaces** `collection://1f0ed36e-a548-4743-9947-f408f8811140` (18 properties, 0 rows) — rebuilt fresh per owner decision, not modified in place.

> ### 🔴 The hardest constraint — it survives the rebuild
> The Creative Pipeline cloud routine (`trig_01WyyrXEkFZck1D49tm6BfKv`) reads properties **by name** and matches the option string **exactly**. The new database MUST reproduce, byte-identically:
> - property names `Title` · `Script` · `Caption` · `Visual Direction` · `Canva Instructions` · `Publishing Status`
> - `Publishing Status` as a **`Select`** (never native `Status`) with options `Not started` · `In progress` · **`Ready for Design`** · `Done`, in that order
>
> One character's difference breaks the trigger **even after the connector is re-pointed**. The old database is not deleted until a live test proves the new one fires.

**Authored fields (the brief's own):** `Title` · `Objective` · `Script` · `Caption` · `Visual Direction` · `Canva Instructions` · `Publishing Status` · `Engagement Follow-up` · `Target Publish Date` (Date — the reason a calendar *view* replaces a calendar database; **stays empty**, there is no launch date).

**Inherited (rollups — 11):** `Pillar` · `Content House` · `Funnel Stage` · `Problem` · `Desire` · `Objection` · `Proof` ← DB 5 · `Persona` ← DB 6 `Audience Role` · `Story/Hook/Narrative` ← DB 6 `Hook` · `Core Message` ← DB 2 · `Translated Platforms` ← DB 6 `Platform` (unique).

**Relations:** `Opportunity` → DB 5 (**required**) · `Narrative Position` → DB 2 · `Translation` → DB 6 · `Campaign` → DB 4 · `Sector × Platform` → DB 3 · `Sub-Sector` → `dbe10a8b-…` · `Offer` → DB 8 · `Platform` (multi-select, the 10-set — the packet's target platform *set*; per-platform expression is a DB 6 row).

**Reserved for Presence (21)'s L3 Reservoir:** `packet_id` · `variant_id` · `Packet State` (`conceived` → `planned` → `in_production` → `produced` → `approved` → `scheduled` → `published` → `measured` → `archived`).

**Formula — `Brief Integrity`**
```
ifs(length(prop("Opportunity"))==0,         "🔴 no upstream opportunity",
    length(prop("Narrative Position"))==0,  "🔴 no approved narrative position",
    length(prop("Translation"))==0,         "🔴 no translation row",
    empty(prop("Visual Direction")),        "⚠ design handoff incomplete",
    empty(prop("Canva Instructions")),      "⚠ design handoff incomplete",
    "✅ ready to consider")
```
This makes `content-brief-builder`'s `ready_for_design: false` rule a **red cell in Notion**, not just a field in an agent's JSON — so the credit-burning failure mode (a brief marked ready with hollow visual direction) is visible before a human flips the switch.

**Fixes carried by the rebuild:**
- `Platform` realigned to the owner-confirmed 10 — **gains** `Threads`, `TikTok`, `YouTube`; **drops** `Tumblr`. This is the reconciliation staged in PIL §9 on 2026-08-02 and never applied.
- `Problem` / `Desire` / `Objection` stay **three separate fields**, and `content-brief-builder`'s single `problem_desire_objection` string is split to match. The old database already had three columns while the agent emitted one — a live mismatch.
- The knowledge-state block is added; the old database had none.
- **No second `Status` field.** `Publishing Status` is the lifecycle field; a second would be a field that has not earned its place *and* an invitation to confuse the trigger.

> **⚠️ Accepted trade-off — no escape hatch (owner decision).** Notion rollups are **not API-writable**. With 11 inherited fields, a brief with no `Opportunity` relation shows them blank and flags red — and **the manual "quick brief" path ceases to exist.** Practical consequence: until DB 5 has rows, no usable brief can be created at all. That is correct. It is this department's founding argument — *content must not start from "what should we post today?"* — enforced structurally rather than by instruction.

**Seed — 0 rows.** A brief must not exist before an opportunity and a translation exist, and a seeded brief is one careless click from firing real generation against real credits.

---

### DB 8 (DB-H) — Offer Registry (thin)
**Primary entity:** one offer. **Owner:** Offer (02). **Backing:** the Offer Engineering Registry (`02_Offer/OFFER_OS.md` §3), which **remains canonical**.
**Why it exists:** the registry is a markdown table; Notion cannot relate to a markdown row, so the commercial half of every brief was unrelatable. Same thin-mirror pattern as DB 1.

`Offer` (title) · `Offer ID` · `Division` · `Capability Family` · `Problem Solved` · `Transformation` · `Mechanism` · `Business Outcome` · `Ideal Sector` → Sub-Sectors · `Ideal Persona` · `Entry Stage` · `Expansion Stage` · `Buying Trigger` · `Objections` · `Proof Requirements` · `Content Territories` · `Relevant Platforms` → DB 1 · `CTA Types` · `Offer Status` (`Active` · `In engineering` · `Not quotable` · `Contested`) · *knowledge-state block*.

> **🔴 No price fields. Deliberately.** Tier and retainer figures stay in `OFFER_OS.md` only. Offer #12 (CPAROS)'s figures are explicitly marked *"Never quote them"* — Claude-generated draft output, never validated, **not agency pricing** — and offers #8/#12 are unreconciled. Mirroring prices into a relatable store would put unquotable numbers one rollup away from a client-facing brief.

**Seed — 12 rows** (the registry's own offers). `Confidence` inherits from each row's `Status` column: the **7 Claude-synthesized offers seed as `Working Hypothesis`**, not `Confirmed`. Offer #12 seeds `Status = Draft`, `Offer Status = Not quotable`. Offer #10 (Revenue Infrastructure Audit) is the named Gateway Offer.

---

## 3. Field-to-field data flow

### Sector (01) → this layer

| From | Field | To | Field | Mechanism |
|---|---|---|---|---|
| Sub-Sectors `dbe10a8b` | `Sub-Sector Name` | DB 3, 5 | `Sub-Sector` | Relation |
| Sub-Sectors | `Status` | DB 3, 5 | `Sub-Sector Status` | **Rollup** — engagement honesty propagates, never retyped |
| Sector Linguistics `172efe6d` | words to use / avoid | DB 3 | `Words to Avoid` → DB 2 `Avoid Terminology` | **Rollup.** ⚠️ **DB is empty** — returns null until Sector loads it |
| Decision-Maker Registry `5566c27c` | `Buyer Title` | DB 3 | `Buyer Titles` | **Rollup** → informs DB 6 `Audience Role` |
| Decision-Maker Registry | `Outreach Intelligence` | — | *(read via relation)* | **Not copied** — Sector owns this field |
| Sector Intelligence `72f90a0f` | `Finding` | DB 5 | `Source Intelligence` | Relation |
| Sector Intelligence | `Strategic Implication` | DB 5 | `Insight` | **Authored** by `content-opportunity-mapper` from the finding — the translation act, provenance logged in `Source` |
| Sector Intelligence | `Evidence` | DB 5 | `Proof` + `Proof Status` | The 52 Sheet-03 findings are owner-curated **hypothesis ranges** at `Confidence = Medium` → `Proof Status = Proof required — named` |
| Sector Intelligence | `Confidence` | DB 5 | `Confidence` | **Mapped** (see §7) — a Medium-confidence finding cannot produce a Confirmed opportunity |
| Sector Signals `c14fedb3` | `Signal` | DB 5 | `Sector Signal` | Relation — the timing driver |
| Sector Signals | `Action Deadline` | DB 5 | `Signal Deadline` | **Rollup.** How the **Revenue Signals** pillar gets real, source-cited fuel instead of generic backlog topics |
| Sector Signals | `Source Tier` | DB 3, 5 | `Source Tier` | Carried, not dropped — **T4 MUST NOT drive execution** |
| Audience Roles `e0513cc9` | `Audience Profile` | DB 5 | `Audience` | Relation. ⚠️ **DB is empty** — resolves structurally, returns null. **Not filled with guesses** |

### Within this layer

| From | Field | To | Field | Mechanism |
|---|---|---|---|---|
| DB 2 | `Position` | DB 6 | **`Core Message`** | **Rollup — the invariant** |
| DB 2 | `Position ID` | DB 6 | `Family Source ID` → `Family Integrity` | Rollup + formula |
| DB 1 | behavioral fields | DB 3 | platform rollups | Rollup |
| DB 3 | `Overlay Verdict` | DB 6 | `Platform Verdict` → `Publishable Here` | Rollup + formula |
| DB 3 | `Overlay Verdict` | DB 5 | `Overlay Verdict` | Rollup — platform-fit scoring input |
| DB 4 | `Master Intelligence ID` | DB 6 | `Master Intelligence ID` | Rollup |
| DB 5 | 5 impact scores | DB 5 | `Total Score` → `Tier` → `Tier 1 Gate` | Formula chain |

### This layer → Content Briefs v2

| From | Field | To brief field | Mechanism |
|---|---|---|---|
| DB 5 | `Pillar` · `House` · `Funnel Position` · `Problem` · `Desire` · `Objection` · `Proof` | same names | Rollup ×7 |
| DB 6 | `Hook` | `Story/Hook/Narrative` | Rollup |
| DB 6 | `Audience Role` | `Persona` | Rollup |
| DB 6 | `Platform` | `Translated Platforms` | Rollup (unique) |
| DB 2 | `Position` | `Core Message` | Rollup |
| DB 6 | `Visual Translation` | *informs* `Visual Direction` | **Authored, not rolled up** — Design needs a brief-specific editable instruction, and the trigger reads this exact property |
| — | — | `Publishing Status` | **Human-set. The trigger. Never inherited.** |

**The distribution spine, honestly stated.** `CONTENT_DISTRIBUTION_ENGINE.md` §3 defines `packet_id · variant_id · publish_record`. After this build, `packet_id` ≈ the brief page ID and `variant_id` ≈ the DB 6 row ID — the first two segments already exist as real keys. Only `publish_record` needs a new store, and a publish record cannot exist until something is published. That is why the Reservoir extension is deferred, not forgotten.

---

## 4. Build notes

1. **Dependency order** (each step's relation targets must already exist): parent page + 5 sub-pages → **DB 1** → **DB 8** → **DB 2** → **DB 3** → **DB 4** → **DB 5** *(omit its `Translations` relation)* → **DB 6** *(with relations to 1/2/3/4/5)* → **DB 7**.
2. **The circular dependency between DB 5 and DB 6 resolves in one operation:** creating DB 6's relation to DB 5 **auto-creates the reverse `Translations` property on DB 5**. Do not attempt two passes.
3. All lifecycle/status fields are **`Select`** (law 4).
4. **DB 7 is built last** — it is the only step touching the live trigger. Everything upstream is proven first.
5. **Do not delete `1f0ed36e-…`** until the re-pointed routine has fired successfully against DB 7 (§9 Gate 1 check 6).
6. Register every new data-source ID in §6 below, in `CONTENT_OS.md` §10/§13, and in `13_Tech_Stack/TECHSTACK_OS.md` §3 with `verified_at`. *(Sector's §4 note 5 gave this same instruction on 2026-08-11 and it was never done — Tech Stack currently registers zero Notion database IDs and still claims the content-brief DB is "not yet built.")*
7. **Notion view DSL accepts only absolute ISO dates.** Rolling "next 7/30/90 days" windows are added as native relative-date filters in the UI, not as built views.

**Companion agent-spec edits — dependencies, not part of the Notion build:**

| Agent | Edit required |
|---|---|
| `content-brief-builder` | `platform` enum drops `tumblr`, adds `threads`/`tiktok`/`youtube`; split `problem_desire_objection` into three; add `opportunity_id`, `translation_id`, `narrative_position_id`; `pillar`/`content_house`/`funnel_stage` become read-only echoes of rollups |
| `content-opportunity-mapper` | Resolve the 5–19 tier gap; add `sub_sector_id`, `source_intelligence_id`, `sector_signal_id`, `platform_overlay_id` |
| `content-multiplication-engine` | Emit `translation_family_id` plus per-derivative `platform` + `audience_role` so the tree can be written as DB 6 rows |
| `content-narrative-architect` | Emit `position_id` and `dragon_reading` so the DRAGON conflict persists as data |

---

## 5. Coverage check — the owner specification, item by item

Of the 19 databases specified: **8 built** (the 6 named as the spec's own "minimum core", plus the rebuilt brief and the Offer mirror) · **1 folded** · **5 already exist elsewhere** · **6 blocked by reality gates**.

| Spec DB | Disposition |
|---|---|
| 01 Platform Intelligence Registry | **DB 1** (thin) + markdown canonical |
| 02 Sector × Platform Matrix | **DB 3** ★ |
| 03 Audience Intelligence | **Extend Sector DB 9/10** with 6 missing fields — no new DB |
| 04 Offer Intelligence | **DB 8** (thin mirror) |
| 05 Narrative Intelligence Registry | **DB 2** |
| 06 Content Translation Matrix | **DB 6** ★ |
| 07 Campaign Intelligence | **DB 4** |
| 08 Content Opportunity Database | **DB 5** |
| 09 Content Concepts | **Folded into DB 6** |
| 10 Content Briefs | **DB 7** (rebuilt) |
| 11 Production Asset Registry | Not built — Design (19) owns; 5 images produced ever |
| 12 Distribution & Publishing | Not built — Presence (21) owns; specced as a brief-DB extension; Postiz has 0 channels |
| 13 Outreach Intelligence | Not built — ClickUp CRM owns (0 leads); DB 10 already has `Outreach Intelligence` |
| 14 Performance Intelligence | Not built — *"would have to invent every metric it reported"* |
| 15 Content Learnings | Not built — depends on 14; `_memory/runtime.jsonl` already is the store |
| 16–19 Calendars | **Views, never stores** — `SECTOR_ACTIVATION_CONTRACT.md` §12 forbids a calendar per type/view |

**The calendars as views:** Editorial → DB 7 `Target Publish Date` · Opportunity → DB 5 by `Total Score` DESC · Sector/Market → the 12 views already on Sector Signals · Intelligence Review → cross-DB on `Next Review` · Distribution → **blocked**; when unblocked, a view on the Reservoir.

**The feedback loop, designed-for but not built.** Performance → Learning → Platform / Sector×Platform / Audience / Narrative / Campaign is the specification's closing loop. Its attachment points exist now: every database carries `Last Reviewed` / `Next Review` / `Version` / `Supersedes`, so a learning record **supersedes** an intelligence row rather than overwriting it. Revenue attribution (Lead → Opportunity → Pipeline → Revenue Influence) attaches at DB 7 via the ClickUp text-ID pattern once the CRM has rows. Nothing is lost by deferring — the sockets are cut.

---

## 6. Live Notion IDs *(built 2026-08-16)*

**Workspace:** `dac21e15-eb93-8125-ba65-0003e8debaf5` (Arika Agency's Space).
**Parent page:** `ContentOS — Content Intelligence Layer` — `3be21e15-eb93-81df-8f9d-fc7639d7d534` · <https://app.notion.com/p/3be21e15eb9381df8f9dfc7639d7d534>

| # | Database | Data source (`collection://`) | DB page | Rows |
|---|---|---|---|---|
| 1 | Platform Registry | `3fe9685e-6cb0-4a62-9a12-a3db999dc88e` | `bb3f22054ccf4f39bdf0507a202452c7` | **10** |
| 2 | Narrative Intelligence Registry | `e76c2bec-8077-4b84-9db3-f1f819000745` | `326500c11b0e4053854baa22835e7d09` | **10** |
| 3 | Sector × Platform Intelligence Matrix | `bb21b3fc-b14f-4237-b5cd-9affd08b98fc` | `09c2f29dada84e2fba9213cc4ab06764` | 0 — needs a named sub-sector |
| 4 | Campaign Intelligence | `6f1f092b-2b26-4bef-94e6-b87e00ba9fb6` | `722d957d420f4663aba3974e54ad2a0b` | 0 — no campaign exists |
| 5 | Content Opportunity | `b9cd2f53-1e6a-4765-aaf4-4742d7d12520` | `df33ddf3ed1b4323bebc95457e42a1fe` | 0 — seeded by an agent run |
| 6 | Content Translation Matrix | `9abf586d-d3bd-4401-b416-d5e0af1f3162` | `c6bf37b321d34ac79435a4a80f71b215` | 0 — needs DB 3 |
| 7 | Content Briefs | `761b3f94-bdbf-4b3d-8234-4cda579697ca` | `264db3ec98834c359a7d314f52765ebb` | 0 — by design |
| 8 | Offer Registry (thin) | `850f5a23-6533-4f48-89f3-ef6bc7f360b6` | `ec38bf406989477ba4f991915a711ce5` | 0 — **12 rows pending** |

**Group sub-pages:** `01 Intelligence` `3be21e15-eb93-81a7-a403-c20f6247b218` (DB 1, DB 8) · `02 Strategy` `3be21e15-eb93-8191-b9c5-cb5c5460b6b6` (DB 2, DB 3, DB 6) · `03 Content` `3be21e15-eb93-8111-925d-d9e587966850` (DB 4, DB 5, DB 7) · `04 Execution` `3be21e15-eb93-81aa-a046-c327a561ed0d` *(empty, reserved)* · `05 Feedback` `3be21e15-eb93-81ed-b111-c7ed9096612c` *(empty, reserved)*. The two empty groups are deliberate — they name where the blocked layers attach and why each is blocked.

**⚠️ Superseded but NOT deleted:** `collection://1f0ed36e-a548-4743-9947-f408f8811140` (Content Briefs v1, 18 properties, 0 rows). It remains the target of cloud routine `trig_01WyyrXEkFZck1D49tm6BfKv`. **Do not delete until** the routine is re-pointed at DB 7 and a live test fires (§9 Gate 1 check 6). Until then the old database is still the production one.

**Sector DB page IDs recovered during this build** — `SECTOR_NOTION_SCHEMA.md` §6 records these three as "no DB-page ID recorded": Geography `10f2b1c23a234d8797e91b8658de4359` · Sector State `ece654da35194ba5b12f5a4bfd5d1d9c` · Sector Forecast `09a9c41ef2794e8dacd6d0ac98c4ff39`. Worth back-filling there.

### Build deviations from the spec — recorded, not silently absorbed

1. **`empty()` does not work on a rollup in Notion formulas** (returns `Type error with formula`); it *does* work on a relation. `Family Integrity` and `Publishable Here` were rewritten to test `format(prop("X")) == ""` instead. `Overlay Integrity` and `Brief Integrity` test relations, so they use `empty()` unchanged. **Carry this into any future formula on this layer.**
2. **`Desire` and `Objection` are authored text on DB 7, not rollups.** The spec assumed they inherit from DB 5, but the atomic content unit is `Problem → Insight → Solution → Proof → Action` — it has no Desire or Objection field. Their natural upstream is Sector's Audience Roles (`Wants` / `Rejects`), which is **empty**. Authoring them on the brief is the honest interim; the field comments record the intended source.
3. **`Supersedes` self-relations exist on DB 6 and DB 7 only.** DBs 1–5 and 8 still need them — a two-step operation Notion requires after creation. Outstanding.

---

## 7. Operating mode & shared conventions

**Operating mode = MANUAL APPLY, by design.** No unattended writer, therefore **no `AUTOMATION_APPROVAL_MATRIX.md` row is required** — the same doctrine Sector operates under. Agents recommend; a human applies. The moment any database gets a real unattended writer, it gets a matrix row *first*, and this section names it.

**The knowledge-state block — on every database in this layer:**

| Field | Type | Options |
|---|---|---|
| Confidence | Select | `Confirmed` · `Strong Signal` · `Working Hypothesis` · `Experimental` · `Deprecated` |
| Status | Select | `Draft` · `Validating` · `Active` · `Superseded` · `Archived` |
| Source | Text | |
| Source Type | Select | `Repo doctrine` · `Owner-curated` · `Agent run` · `External research` · `Vendor / platform` |
| Research Date | Date | |
| Research Owner | Text | |
| Evidence | Text | |
| Effective Date | Date | |
| Last Reviewed | Date | |
| Next Review | Date | |
| Version | Number | |
| Supersedes | Relation (self) | |

**🔴 Two status axes, kept separate on purpose.** `Status` above is **knowledge maturity** — is this record trustworthy and current? Sector's `Reference · Target · Active · Dormant` is **engagement lifecycle** — is this a market we are actually in? They answer different questions and are never merged. Sector's value arrives here only as the `Sub-Sector Status` rollup. Collapsing them would lose the ability to state *"a validated narrative about a market we are not yet in"* — which describes almost everything in this layer today.

**🔴 Confidence mapping at the Sector boundary.** Sector's databases use `Low · Medium · High`; this layer uses the five-value system above. Sector's vocabulary is **not ours to change**. Any rollup crossing the boundary maps:

| Sector | → | This layer |
|---|---|---|
| `High` | → | `Confirmed` |
| `Medium` | → | `Working Hypothesis` |
| `Low` | → | `Experimental` |

Without this mapping, a cross-boundary rollup silently misrepresents certainty — which is the precise failure the knowledge-state attributes exist to prevent.

---

## 8. Agent read/write governance

**Read flow — the order an agent consumes the system:**
Sector Intelligence → DB 3 overlay → Audience (Sector DB 9/10) → DB 8 offer → DB 2 narrative → DB 4 campaign → DB 5 opportunity → DB 6 translation → DB 7 brief → Design (19) → Distribution (Presence 21) → Performance (Marketing 03).

| Database | Recommends (advisory) | Reads |
|---|---|---|
| DB 1 Platform | *(human, from PIL)* | opportunity-mapper · brief-builder · multiplication-engine · publishing-gate |
| DB 2 Narrative | `content-narrative-architect` | brief-builder · publishing-gate · multiplication-engine |
| DB 3 Sector × Platform | *(human; `sector-intelligence-mapper` advises)* | all four content agents |
| DB 4 Campaign | *(human)* | all content agents |
| DB 5 Opportunity | `content-opportunity-mapper` | brief-builder · narrative-architect |
| DB 6 Translation | `content-multiplication-engine` | brief-builder · publishing-gate · narrative-architect (drift) |
| DB 7 Brief | `content-brief-builder` | publishing-gate · `design-storyboard-generator` (19) · the cloud routine |
| DB 8 Offer | *(human; `offer-orchestrator` (02) advises)* | opportunity-mapper · brief-builder |

**No downstream agent overwrites upstream intelligence.** Publishing externally is Risk Class 3 — human sign-off, no exceptions. `content-brief-builder` recommends `Publishing Status` but **never flips `Ready for Design`**; that is a human action, because flipping it starts real generation against real credits.

---

## 9. Verification protocol — two gates

Structure is fully verifiable at build time; the spine walk is not, because **a rollup with no source row returns null whether the relation is correct or broken.** Stated plainly rather than declaring a pass on checks that cannot run.

### Gate 1 — structural (at build)
1. **Identity** — fetch each data source; assert property counts and that `Platform` returns the **same 10 strings** in DB 1, DB 3, DB 6, DB 7, with `Tumblr` **absent from all four**.
2. **Relation wiring** — assert every relation property exists, points at the correct target data source, and auto-created its reverse property on the target. Proves wiring, not traversal.
3. **Traversal smoke test** — create one disposable row in each of DB 3, DB 6, DB 5 linked to a real DB 2 position; confirm `Core Message` inherits **byte-identically**; **delete all three.** Proves traversal without seeding invented sector data.
4. **Formulas compute** — on the disposable DB 5 row, impacts summing to 41 with `Research Satisfied = No` → `Tier 1 Gate` reads `🔴 BLOCKED`. On the disposable DB 6 row, corrupt `Translation Family ID` → `Family Integrity` flips to `🔴 family mismatch`. Revert.
5. **Seeded rows are honest** — DB 1: 10 platforms, all `Account Status = Not created`. DB 2: 10 positions, DRAGON at `Validating` with both letter-sets empty. DB 8: 12 offers, **no price field exists at all**, the 7 synthesized offers at `Working Hypothesis`, offer #12 `Not quotable`. No row reads `Confirmed` without `Evidence`.
6. **🔴 Trigger regression — non-negotiable.** Assert DB 7's `Publishing Status` is a `Select` with the four options unrenamed and in order; assert the five other trigger-read properties exist with original names. Create one throwaway brief, set `Ready for Design`, confirm the routine posts its Notion comment within the hourly window (`7 * * * *`), delete the row. **If it does not fire, check routine health before blaming the schema** — the routine was auto-disabled once before (`auto_disabled_repo_access`, dead 2026-07-04 → 2026-07-15) and its hourly cadence is **still unproven post-restoration**. Record the outcome either way; this is its first real test since.
7. **No orphans** — grep the repo for `1f0ed36e`: zero hits outside changelog/history entries. All new IDs registered per §4 note 6.

### Gate 2 — spine proof (once a sub-sector is named)
8. **Confidence mapping holds** — a Sector row at `Medium` surfaces as `Working Hypothesis`, not blank and not `Confirmed`.
9. **Rollups inherit real data** — `Sub-Sector Status` reads its true value; `Words to Avoid` returns Linguistics content **or honest null if Sector has not loaded it**.
10. **The family mechanism works** — group DB 6 by `Translation Family ID`: both rows in one group, **one identical `Core Message`, two different `Platform` values.** This is the single check that proves the architecture does the job it was built for, and it cannot run before Gate 2.
11. **Agent acceptance** — `content-opportunity-mapper` run manually; every output field maps to a real property with no shim.

---

## 10. Decision Log

- **2026-08-16 — Content Intelligence Layer specified.** Seven new databases plus a rebuilt brief database, landing exactly on the owner specification's own "minimum core" — no expansion, no shortfall. Six proposed databases deliberately not built, each with the rule that forbade it recorded rather than a silent omission; four calendar databases converted to views per `SECTOR_ACTIVATION_CONTRACT.md` §12. Four corrections applied during review: the five-value confidence vocabulary adopted over Sector's three (with a documented boundary mapping, §7); knowledge-maturity and engagement lifecycles kept as separate axes rather than collapsed; the five-field source block adopted; and a field-level audit finding that Sector covers ~15 of 27 audience fields, with the 6 missing ones to be added to Sector's DB 9/10 as an **extension** rather than a second Content-owned store. Two genuine defects surfaced and left for the owner rather than papered over: `content-opportunity-mapper`'s tier gap (totals 5–19 have no valid tier in its own enum), and the DRAGON conflict (persisted as data at `Validating`). — Claude Code (Opus 5)
- **2026-08-16 — BUILT. All 8 databases live.** Connector returned; pre-flight confirmed the brief database still had **0 rows** (the condition the whole rebuild depended on) and all 13 Sector data sources resolved. Built in dependency order; the DB 5 ↔ DB 6 circular dependency resolved in one operation as designed (creating DB 6's relation auto-created the reverse on DB 5). Every relation, rollup and formula resolved to its intended target — verified in the returned schemas, not assumed. Seeded DB 1 (10 platforms) and DB 2 (10 narrative positions), both sector-independent. **Honesty audit passed:** DB 2 returns 9 `Active`/`Confirmed` + 1 `Validating`/`Working Hypothesis` (DRAGON, `Proof Layer = None available`, both letter-sets empty); DB 1 returns `Revenue Function = null` on exactly the three platforms PIL profiles lightly (Threads, TikTok, YouTube) and `Account Status = Not created` on all ten. Nothing was invented to fill a field. Three build deviations recorded in §6 rather than absorbed silently. **The old brief database and its cloud routine are untouched** — the rebuild is additive until the routine is re-pointed. — Claude Code (Opus 5)
- **2026-08-16 — Build blocked at Phase 2 (superseded same day).** The Notion MCP connector disconnected mid-session; verified unavailable twice. This specification was the buildable artifact produced instead. — Claude Code (Opus 5)

## 11. Changelog

- **v0.1 (2026-08-16):** Created. Companion to `CONTENT_OS.md` §8's architecture approval; follows the pattern of `01_Sector/SECTOR_NOTION_SCHEMA.md`. — Claude Code (Opus 5)
