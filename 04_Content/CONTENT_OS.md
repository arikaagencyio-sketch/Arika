# Content — Department OS

**Department:** Content (04)
**Position in flow:** Sits adjacent to Marketing (03), feeding content assets and narrative/messaging architecture into Marketing's demand-generation work; both then feed Sales (05).
**Mandate:** Own content strategy, creation, channel distribution, and narrative/messaging architecture — distinct from Marketing's positioning/campaign/channel-strategy mandate, though tightly coupled to it.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Content owns what gets said and how it's produced and distributed — content strategy, the content system itself, narrative/messaging architecture, and channel-specific execution (e.g. LinkedIn, Instagram). It was originally folded into Marketing during the v0.1 restructuring pass, but was corrected back to a standalone department: content was conceived from the start as one of the agency's full departments, not a Marketing sub-area, even though its current draft material is thinner than other departments.

**Note on the source material's own mental model:** the raw drafts themselves never anticipate a Content/Marketing department split — they describe one unified "Revenue Content Operating System" where content and channel/distribution strategy are a single continuous system, and one file explicitly argues content should NOT be "a marketing department function" at all ("Content is not a department... a translation layer that converts agency intelligence into market influence," `Content Intelligence System.md`). That argument is likely the actual origin of the instinct to split Content out as its own department. The Content/Marketing boundary stated in this file's header (Content = assets/narrative, Marketing = positioning/campaign/channel) was an architectural decision imposed during this restructuring, not something drawn in the source material — **confirmed by owner, 2026-06-30: keep the split.**

## 2. Status

**Live on the runtime (2026-07-14) — 6 agents, advisory-first.** See §5 for the roster
and §12 for the trigger chain. Content is the **supply side of the only Arika
automation running in production**: the Creative Pipeline cloud routine has been
running hourly since 2026-07-04 against a Notion content-brief database that is real,
correctly built, and **empty**. `content-brief-builder` exists to fill it.

**Content migration: first pass complete (2026-06-30).** All 10 files read in full. No independently-built OS sub-layer exists here. Like every other department migrated so far, contains **no real historical operating data** — no real client, campaign, published-content reference, or business outcome anywhere. The one partial exception: LinkedIn and Instagram are named as real, intended channels (not hypothetical examples like other departments' industry/sector placeholders), and `Project Realignment Stratergy.md` is the most "decision-like" document found in any department to date — see §10 below.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Content Intelligence System | Pulls from 5 internal sources (Sector, Market, Offer, Client, Sales intelligence) to find content angles | Draft/aspirational |
| Content System Design (ACCOS) | 12-stage workflow: Context Acquisition → Audience Mapping → Problem Mapping → Insight Discovery → Content Opportunity Mapping → Narrative Architecture → Messaging Architecture → Content System Design → Content Planning → Content Construction → Content Multiplication → Distribution Engineering → Performance Intelligence | Draft/aspirational, most elaborate framework in this department |
| Content multiplication | One strategic asset → many distribution formats (e.g. 1 Report → 3 Executive Articles → 5 Thought Leadership Pieces → 10 LinkedIn Posts → ... ) | Draft/aspirational |
| Narrative architecture | Core narrative, "the enemy" (fragmentation), 10 agency beliefs, 7 canonical content pillars (Revenue Intelligence/Architecture/Operations/Transformation/Leadership/Signals/Reality) | Draft/aspirational, but pillar structure now resolved — see §10's pillar synthesis |
| Messaging architecture | Inverted-pyramid structure, 4 messaging pillars, audience messaging matrix (CEO/CMO/Sales Leader/COO/Investor), 7-stage revenue journey messaging | Draft/aspirational, explicitly borrowed/generic framework per its own source file |
| LinkedIn channel execution | "Revenue Reality" voice, DRAGON framework, 4 content pillars, 4 post formats, weekly cadence, 90-day launch plan | Most concretely developed file in the department — real channel, forward-looking 90-day targets (see §7) |
| Instagram channel execution | 5-tier content pyramid, pivoted mid-file to "Implementation Strategy" (community that acts, not just consumes) | Real channel; concept evolved within the source file itself |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Content Execution Operating System | New content cycle | 10 layers: Priority Matrix → Backlog → Publishing Sequence → Research Dependencies → Asset Production → Approval → Calendar Logic → Distribution Sequencing → Repurposing → Authority-Building Roadmap | Published, sequenced content | Mary Thuo | `Content Planning Execution.md` |
| Asset Production Workflow | New asset needed | Research → Insight Extraction → Outline → Draft → Strategic Review → Brand Review → Final Approval → Distribution Prep → Publishing → Performance Tracking | Approved, published asset | Mary Thuo | same |
| Content Priority Scoring | New content idea | Score 5 dimensions (Revenue/Authority/Demand/Sales/Differentiation Impact) out of 50; Tier 1 ≥40 "Mission Critical", Tier 2 30-39, Tier 3 20-29 | Prioritized backlog | Mary Thuo | same |
| LinkedIn 90-day launch | New channel activation | Phase 1 Identity → Phase 2 Value → Phase 3 Depth → Phase 4 Community | Established LinkedIn presence | Mary Thuo | `Linkedin Stratergy.md` |

## 5. Agent Roster

**6 runtime agents, live in `arika-runtime` (2026-07-14).** Every agent is a spec at
`.claude/agents/content-{name}.md`, loaded by the shared executor. **Advisory-first**
— they recommend and log; humans publish. Full pattern: `GLOBAL_OS.md` §5.

| Agent | ACCOS stage | Class | Triggers | Emits |
|---|---|---|---|---|
| `content-intelligence-hub` | 1–4 (Context → Audience → Problem → Insight) | 1 | manual · `SECTOR_MAPPED` · `MARKET_SIGNAL_MAPPED` · `OFFER_ENGINEERED` · `ADVOCACY_CAPTURED` · `BUYER_PSYCHOLOGY_MAPPED` · Mon 08:00 | `CONTENT_INSIGHT_CAPTURED`, `INTELLIGENCE_STARVED` |
| `content-opportunity-mapper` | 5 (Content Opportunity Mapping) | 1 | manual · `CONTENT_INSIGHT_CAPTURED` | `CONTENT_OPPORTUNITY_MAPPED`, `CONTENT_OPPORTUNITY_REJECTED` |
| `content-narrative-architect` | 6 / 6.5 (Narrative + Messaging) | 1 | manual · `CONTENT_OPPORTUNITY_MAPPED` · `NARRATIVE_REVIEW_REQUESTED` | `NARRATIVE_APPROVED`, `NARRATIVE_DRIFT` |
| `content-brief-builder` | 7–9 (System Design → Planning → Construction) | **2** | manual · `CONTENT_OPPORTUNITY_MAPPED` · `NARRATIVE_APPROVED` | `CONTENT_BRIEF_READY`, `CONTENT_BRIEF_BLOCKED` |
| `content-publishing-gate` | governance (pre-publish) | **2** | manual · `CONTENT_BRIEF_READY` · `PUBLISH_GATE_REQUESTED` | `CONTENT_APPROVED`, `CONTENT_REJECTED` |
| `content-multiplication-engine` | 10 (Content Multiplication) | 1 | manual · `CONTENT_APPROVED` | `MULTIPLICATION_TREE_READY` |

**The 5 Content Intelligence sources are now real event listeners, not a diagram.**
Each of the five sources named in `Content Intelligence System. Draft 2.md` maps
onto an event a real agent actually emits — this is what makes the Content
Intelligence Database executable rather than aspirational:

| Source (Draft 2) | Real event | Emitting agent |
|---|---|---|
| Sector Intelligence | `SECTOR_MAPPED` | `sector-intelligence-mapper` (01) |
| Market Intelligence | `MARKET_SIGNAL_MAPPED` | `marketing-market-intelligence` (03) |
| Offer Intelligence | `OFFER_ENGINEERED` | `offer-oeos-engineer` (02) |
| Client Intelligence | `ADVOCACY_CAPTURED` | `client-success-advocacy` (07) |
| Sales Intelligence | `BUYER_PSYCHOLOGY_MAPPED` | `sales-customer-psychology` (05) |

**Content → Design is wired to the live pipeline.** `content-brief-builder` emits
`CONTENT_BRIEF_READY`, and `design-storyboard-generator` (19) now listens for it
(trigger added 2026-07-14) — its description always said *"use when a content brief
needs turning into a storyboard"*; nothing had ever produced that brief.
Downstream, `content-multiplication-engine` hands `distribution_waves` to
`marketing-demand-generation` (03) and `sales_assets` to `sales-enablement-playbooks` (05).

**🔴 Deliberately NOT built — 4, with reasons** (building these would rebuild the
fragmentation this department exists to attack):
- **Distribution / platform agent** → Marketing (03) owns it, and says so: *"Every platform is a distribution endpoint, not a separate content strategy — content itself is owned by Content (04)... not reinvented per-platform here"* (`MARKETING_OS.md` §10). Content produces the tree; Marketing works the channels.
- **Asset production agent** → Design (19) owns the Production Engine (storyboard → image → video → voice → animation → music → enhance → assemble). Content produces the **brief**; Design produces the **asset**. The Notion schema's `Visual Direction` + `Canva Instructions` + `Ready for Design` are that handoff, already designed.
- **Market/sector intelligence agent** → Sector (01) owns foundational sector truth; `marketing-market-intelligence` owns campaign/demand intelligence. Content **consumes** both (sources 1 and 2 above).
- **Performance intelligence agent** (ACCOS Stage 12 / COS Layer 10) → **deferred, not dismissed.** It is real doctrine, but it has zero possible input: nothing has been published, zero social accounts exist (`GO_LIVE_CHECKLIST.md` item 23), and no BI is connected. It would have to invent every metric it reported. `marketing-attribution-modeling` (03) already owns measurement truth. Build when there is real published content to measure. See §7's vanity-metric exclusion list, which survives as the standard.

**Messaging Architecture (Stage 6.5) folded, not built.** Its usable part (the
CEO/CMO/Sales Leader/COO/Investor audience matrix) lives in
`content-narrative-architect`. The rest is filler — this file's own §14 records its
sensory-language tables were *"lifted from an unrelated branding context."* No agent
was built on filler.

## 6. Skill Library Index

*(placeholder — none yet; the 6 agents in §5 carry their doctrine inline rather than
via shared skills, matching the pattern in every other migrated department.)*

## 7. KPI Dictionary (department-local)

**All values are forward-looking targets, not historical results. Confirmed by owner, 2026-06-30: not launched yet, no launch date set** — these remain a ready-to-use template, not a live countdown. Revisit once a real date exists.

| Metric | Target | Window | Source |
|---|---|---|---|
| Comments per post | 10-20 quality comments | Ongoing | `Linkedin Stratergy.md` |
| DMs received | 5-10/week | By week 6 | same |
| Connection requests | 30-50 quality connections/week | Ongoing | same |
| Profile views | 200-500/week | By week 8 | same |
| Newsletter subscribers | 500 | By day 90 | same |
| Discovery calls | 3-5/month | By month 3 | same |
| Instagram | Profile visits, CTR, saves, shares, qualified DMs, consultation requests | No targets given, categories only | `Instagram as a Business Tool.md` |

**Explicitly excluded as vanity metrics** (per the LinkedIn file itself): impressions, follower count, direct LinkedIn-attributed revenue — "what NOT to track" in the first 90 days. Worth carrying this exclusion list forward as a standard, not just a one-off note.

## 8. Decision Log

- **2026-06-30 — Confirmed Content/Marketing department split stays as-is.** See §1.
- **2026-06-30 — Adopted the Project Realignment's broader repositioning** (Revenue Intelligence/Architecture/Engineering, LinkedIn as one node among several) as real agency strategy. See §10.
- **2026-06-30 — Resolved the 3-way pillar-naming conflict** by synthesizing all three sets into one canonical 7-pillar structure rather than picking one and discarding the others. See §10's mapping table.
- **2026-06-30 — Confirmed LinkedIn/Instagram have not launched; no date set yet.** §7's targets remain a template. See §7.
- **2026-07-01 — Added Content Houses as a second, intent-based axis crossed with the existing 7 topic pillars** (owner-confirmed, among 3 presented options — crossed axes chosen over replacing the pillars or scoping houses to a subset). Added Story Architecture, Campaign Architecture, and a target Notion content-brief schema. See §10.
- **2026-07-03 — Notion content-brief database actually built**, matching the documented schema exactly (verified via `notion-create-database`, real data source ID returned). Empty and ready for content — see §10.
- **2026-07-03 — Reconciled a 4-way "narrative" naming collision** created by the founding of Experience Engineering (20): this department's Story Architecture (content-sequencing), Branding (12)'s Narrative Engineering stack (brand-identity), and Experience Engineering's two candidate Narrative Arc drafts (experience-orchestration) are all real, non-competing concepts at different altitudes — cross-reference note added to §10, mirrored in `12_Branding/BRANDING_OS.md` §3 and `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` §1.
- **2026-07-14 — Content went live on the runtime: 6 agents built** (§5), covering ACCOS Stages 1–10 plus the publishing gate. The 5 Content Intelligence sources were wired to 5 real events that real agents already emit, making the Content Intelligence Database executable rather than a diagram. Content → Design connected (`CONTENT_BRIEF_READY`), closing the supply gap to the live Creative Pipeline routine. 4 candidate agents deliberately not built (distribution → Marketing; asset production → Design; market intelligence → Sector/Marketing; performance intelligence → deferred for want of any real input). Two genuine source conflicts surfaced and left open for the owner — the DRAGON redefinition and the Instagram Implementation Strategy pivot (§10).
- **2026-07-04 — Integrated the owner's 10-layer Content Operating System (COS) model** into §10 as an elaboration of this file's existing structures, for the new Arika website project (`20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`). 9 of 10 layers mapped onto capabilities already documented here; layer 7 (Engagement) flagged as a genuine gap, not invented.

## 9. Risk / Incident Log

*(placeholder — empty)*

## 10. Standards & SOPs Index

**Content publishing rules** (recurring across files):
- "If a content piece cannot reach revenue eventually: DO NOT CREATE IT."
- "Never publish: Offer Before Problem. Never publish: Solution Before Insight. Never publish: Authority Without Evidence."
- "No Tier 1 content is produced without research."
- North Star: aim to be "Trusted, not Popular"; "Most referenced, not Most viewed"; "Most influential, not Most viral."

**LinkedIn tactical rules**: reply to comments within 1 hour; never use passive CTAs ("Click here," "Learn more"); put links in comments, not the post body.

**The "Project Realignment" — adopted by owner, 2026-06-30.** `Project Realignment Stratergy.md` repositions the agency's content effort: *from* a LinkedIn-centric "Revenue Reality" philosophy where LinkedIn was the primary expression of the strategy, *to* a broader "Revenue Intelligence / Revenue Architecture / Revenue Engineering" philosophy where LinkedIn becomes one "Knowledge Distribution" node among several (Newsletter, Website, Reports, Frameworks, Playbooks, Workshops, Community, Sales Assets). Stated reasoning: *"the agency is not a content agency and not a LinkedIn thought leadership brand. It is a Revenue Growth Operating System. Content is simply one of the interfaces of that operating system."* This is now confirmed real agency strategy, not draft reasoning — it also fits cleanly with the already-confirmed "Revenue Infrastructure Partner" agency positioning (Offer, 02).

**Pillar synthesis — resolved, 2026-06-30.** Three unreconciled pillar sets existed; rather than picking one and discarding the others, all three are mapped into a single canonical structure that leverages the now-adopted repositioning:

**Canonical top-level: the Realignment's 7 "knowledge domain" pillars** (these are the ones to use in content planning, calendars, and the Capability Registry above) — each populated with sub-topics drawn from the generic 7-pillar/35-sub-pillar set (`Content System Design. Draft 4.md`), which maps onto them cleanly enough to use as a real topic backlog:

| Canonical pillar (Realignment) | What it covers | Sub-topics inherited from the generic set | Generic-set source pillar |
|---|---|---|---|
| Revenue Intelligence | Why revenue behaves the way it does | Data Intelligence, Analytics, Market Intelligence, Competitive Intelligence, Strategic Intelligence | "Business Intelligence" |
| Revenue Architecture | Designing the systems that produce revenue | Revenue Strategy, Revenue Operations, Revenue Forecasting, Revenue Systems, Revenue Intelligence | "Revenue Growth" — note the sub-topic names "Revenue Operations" and "Revenue Intelligence" collide with two other top-level pillar names; keep as sub-topics under Architecture, don't rename the top-level pillars to avoid them |
| Revenue Operations | Executing those systems consistently | Sales Systems, Sales Operations, Conversion Optimization, Sales Enablement, Opportunity Management + Process Design, Operational Excellence, Resource Optimization, Delivery Systems, Organizational Scale | "Sales Acceleration" + "Business Operations" (merged — both are execution-focused) |
| Revenue Transformation | Scaling via AI, automation, sales, marketing, partnerships, operational redesign | Workflow Automation, AI Systems, Process Optimization, Operational Efficiency, Digital Transformation | "Automation & AI" |
| Revenue Leadership | Leadership decisions that determine growth | Strategic Planning, Growth Leadership, Organizational Design, Risk Management, Decision Architecture | "Leadership & Decision Making" |
| Revenue Signals | Future trends / market signal sensing | Market Positioning, Lead Generation, Demand Capture, Demand Conversion, Customer Acquisition | "Demand Generation" — the loosest of the 6 mappings; **stronger real fuel for this pillar going forward is Sector (01)'s new 6-category buying-signal framework and 90-point scorecard** (`01_Sector/SECTOR_OS.md` §3, §7) — real, owner-curated content, not generic placeholder topics. Use that as primary source for this pillar; treat the generic sub-topics as backup. |
| Revenue Reality | The original DRAGON-framework voice — now one node, not the whole brand, per the Realignment's own intent | Keeps its own native 7 sub-pillars **unchanged**: Revenue Anatomy, The Complexity Filter, The Revenue Decision Chain, The Authenticity of Chaos, Revenue Beyond Money, The Pre-Hire Revenue Audit, The Growth-Opinion Stance (`Linkedin Stratergy. Draft 13.md`) — each already has a fully built 5-post series + 1 framework-PDF bonus asset, ready to publish specifically under this pillar once the LinkedIn channel launches | (LinkedIn-specific set, kept intact rather than merged) |

No content was discarded — the generic set's topic granularity and the LinkedIn set's fully-built post series both survive, correctly subordinated under the Realignment's broader structure rather than competing with it.

**Content Houses — a second, orthogonal axis (added 2026-07-01).** The 7 canonical pillars above answer "what is this piece about" (topic). They don't answer "why are we publishing it" (intent) — that gap surfaced during the Design (19) department's founding planning session. Rather than replacing the resolved pillar structure, **every content brief now gets tagged with both a pillar and a house** — confirmed by owner as the resolution among 3 presented options (crossed axes, vs. replacing pillars, vs. houses-as-informal-subset).

| Content House | Purpose | Examples | Starting ratio (adjustable, not fixed) |
|---|---|---|---|
| Insights | Teach | Industry analysis, market shifts, AI developments, growth lessons | 25% |
| Demonstrations | Show | Website builds, automation workflows, CRM walkthroughs, dashboard creation, before/after transformations | 25% |
| Frameworks | Explain | Revenue Engine, Growth Flywheel, Client Journey, Automation Blueprint | 15% |
| Proof | Build trust | Client wins, case studies, metrics, testimonials | 15% |
| Founder Thinking | Build brand | Leadership philosophy, agency decisions, lessons, future-of-work/AI perspective | 10% |
| Education | Reduce friction | FAQs, tutorials, explainers, beginner guides | 5% |
| Conversion | Generate demand | Offers, audits, lead magnets, workshops, consultations | 5% |

These ratios are a recommended starting allocation, not a hard rule — expected to shift during launches or campaigns, same spirit as the pillar sub-topics being a backlog rather than a mandate.

**Story Architecture — every content piece follows the same narrative logic**: Problem → Insight → Demonstration → Framework → Proof → Action. This is the sequencing rule Claude (or any future content-production agent) should apply consistently, regardless of which pillar/house a piece belongs to.

**Cross-department narrative-layer distinction (added 2026-07-03; ⚠️ now 3-way, updated 2026-07-15).** **Experience Engineering (20)'s two candidate Narrative Arcs were reconciled on 2026-07-15** into one canonical arc — **`Attention → Problem → Transformation → Proof → Offer`** — settled by EE's own Scene Architecture corroborating that ordering, with the 9-stage draft's extra beats absorbed and its "Retention" stage routed out to Client Success (07)/`marketing-lifecycle` (03). So this is now a **3-way** distinction, not 4-way: Content's content-sequencing layer, Branding's brand-identity layer, and EE's single experience-orchestration arc. Full reasoning: `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` §3. The original text below is otherwise unchanged and still correct.

Four different "narrative" concepts now exist across this repo and are not duplicates or a conflict. This Story Architecture is the **content-sequencing layer** — how one piece of content is paced internally. Branding (12)'s Narrative Engineering stack (`12_Branding/BRANDING_OS.md` §3) is the **brand-identity narrative layer** — why the brand exists. Experience Engineering (20)'s Narrative Engine (`20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` §3) supplies **two candidate experience-orchestration arcs** sitting above this one — how an entire multi-scene interactive experience (a whole website or presentation, which may itself contain many Story-Architecture-sequenced pieces) is paced: Draft A (`Attention → Problem → Transformation → Proof → Offer`) and Draft B (`Attention → Curiosity → Education → Trust → Proof → Transformation → Offer → Action → Retention`), not yet reconciled with each other. See the other two files for their own version of this note.

**Campaign Architecture — the organizing unit above both pillars and houses.** Every piece of content belongs to a campaign, not just a pillar/house pairing (e.g. "360 Revenue System" campaign → Episode 1-4 → book-a-strategy-session CTA). This matches Design (19)'s campaign-first Canva folder structure (`19_Design/DESIGN_OS.md` §10) exactly, so the two departments share one unit of work rather than reconciling two different groupings later.

**Content Operating System (COS) — 10-layer elaboration (added 2026-07-04, alongside the Arika website project, `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`).** The owner's pasted vision frames content as a 10-layer operating system rather than a calendar. This is **not a new department or a competing structure** — it's an elaboration of this department's existing Capability Registry (§3) and the structures already resolved above (7 pillars, 7 Content Houses, Story Architecture, Campaign Architecture, the real Notion schema below). Each layer maps onto something that already exists in this file rather than being built fresh:

| COS Layer | What it is | Maps onto (already real in this file) |
|---|---|---|
| 1. Intelligence | Research/inputs feeding content angles | Content Intelligence System (§3) — pulls from Sector/Market/Offer/Client/Sales intelligence |
| 2. Strategy | Why content exists, for whom | The Realignment repositioning + pillar synthesis (this section, above) |
| 3. Planning | Roadmap from annual theme to daily distribution | Content Execution Operating System (§4) + Content Priority Scoring (§4) |
| 4. Production | Turning a brief into a real asset | Asset Production Workflow (§4) |
| 5. Asset Management | Treating content as reusable IP | The Notion content-brief schema (below) + Design (19)'s Asset Library (`19_Design/DESIGN_OS.md` §3) — not a third inventory |
| 6. Distribution | One idea, many touchpoints | Content multiplication (§3) + Marketing's new Social Ecosystem repurposing flow (`03_Marketing/MARKETING_OS.md` §10) |
| 7. Engagement | Conversations, not just consumption | Not yet a named capability here — genuinely new; candidate future addition to §3, not built out in this pass |
| 8. Conversion | Every asset points to a next step | Story Architecture's `Problem → Insight → Demonstration → Framework → Proof → Action` sequencing (this section, above) |
| 9. Analytics | Measuring business impact, not vanity metrics | §7 KPI Dictionary's explicit vanity-metric exclusion list |
| 10. Optimization | Using performance data to improve the system | Distribution Engineering / Performance Intelligence, the last two stages of Content System Design (ACCOS) (§3) |

No new registry created — this table exists so the owner's 10-layer mental model has a durable, cross-referenced home without duplicating what §3/§4/§10 already define. Layer 7 (Engagement) is the one genuinely new gap; left open rather than invented.

**🔴 Two genuine conflicts surfaced by the 2026-07-14 agent build — owner decisions, not Claude's to make.**

**Conflict 1 — DRAGON has two incompatible definitions, and both trace to adopted sources.**

| | LinkedIn draft (`Draft 13`) | Project Realignment (`Project Realignment Stratergy.md`) |
|---|---|---|
| **D** | Dialogue | Diagnosis |
| **R** | Relatability | Revenue Logic |
| **A** | Authenticity | Architecture |
| **G** | Growth | Growth Systems |
| **O** | Opinion | Operational Intelligence |
| **N** | Niche-orientation | Navigation |

The Realignment was **adopted by the owner on 2026-06-30** (§8) and explicitly states
*"Now DRAGON becomes an agency operating philosophy rather than merely a content
framework."* But that adoption took the Realignment's **pillars** and
**repositioning** — the **DRAGON redefinition rode along unnoticed**, and §3 above
still describes DRAGON as the LinkedIn voice. Both readings are defensible: the
LinkedIn DRAGON is a *content-construction* framework (how to write a piece); the
Realignment DRAGON is an *operating philosophy* (how the agency thinks). They may
both be real at different altitudes — exactly like the 4-way narrative distinction
resolved on 2026-07-03 — or one may supersede the other. **Unresolved.**
`content-brief-builder` must name which it applied and flag the conflict on every run.

**Conflict 2 — the Instagram "Implementation Strategy" pivot was noted but never absorbed.**
§3 records that `Instagram as a Business Tool. Draft 14.md` *"pivoted mid-file to
'Implementation Strategy'"*, but three concrete structures from that pivot never
entered this file:
- **A 5th stage on the atomic content unit:** the file explicitly argues for `Problem → Insight → Solution → Proof → **Implementation**`, replacing `Action` — *"When every post ends with a concrete implementation step, your Instagram feed stops being a library of ideas and becomes an execution environment."*
- **Action Pillars** (Think Better → Diagnose → Decide → Implement → Measure) — *"these aren't content categories. They're stages of execution."* Possibly a **third axis** alongside pillars (topic) and houses (intent), or possibly a replacement for the funnel-stage field.
- **The Implementation Scorecard** — 6 behaviour-change metrics (decision influence, action rate, accountability rate, conversation quality, commercial intent, long-term value) that would replace §7's engagement KPIs entirely.

This matters because the pivot's thesis — *"the bottleneck isn't knowledge, the
bottleneck is action... Knowledge is becoming a commodity. Execution is not"* —
is the same argument Operations (08)'s constitution is built on (*"action, execution,
not planning"*), and it aligns with the confirmed "Revenue Infrastructure Partner"
positioning. **It may be the strongest unadopted idea in this department.** Left
unadopted rather than absorbed by assumption. Story Architecture (below) remains
canonical until the owner rules.

*Sequencing note:* four near-identical sequences exist across the drafts — Story
Architecture (`Problem → Insight → Demonstration → Framework → Proof → Action`),
Narrative Level 9 (`… → Consequence → Solution → …`), the atomic content unit
(`… → Solution → Proof → Action`), and the Instagram evolution (`… → Implementation`).
**Story Architecture is canonical**; the agents use it and flag genuine need for the
other beats rather than silently substituting.

**Notion content-brief database — BUILT 2026-07-03.** Real database created (`https://app.notion.com/p/fef061abc3c440e2bb7979df9461b1d0`, data source `collection://1f0ed36e-a548-4743-9947-f408f8811140`), matching this schema exactly: Title, Objective, Content House (select, all 7 houses above), Pillar (select, all 7 pillars), Campaign, Funnel Stage (select: Awareness/Consideration/Decision/Retention-Advocacy — provisional labels, not sourced from elsewhere in this repo, adjust if a different funnel-stage model is preferred), Platform (multi-select: Instagram/LinkedIn/Facebook/X/Pinterest/Tumblr/Newsletter/Website), Persona, Problem/Desire/Objection, Story/Hook/Narrative, Script, Caption, Visual Direction (handoff notes to Design, 19), Canva Instructions, Publishing Status (select: Not started/In progress/**Ready for Design**/Done — converted 2026-07-04 from Notion's native status type, which doesn't support custom options via the available API, specifically so "Ready for Design" could exist as the Creative Pipeline Automation's real trigger value), Engagement Follow-up (which DM-automation trigger, if any — cross-ref `16_Automation/AUTOMATION_OS.md`'s Engagement Layer). Structure is real; zero content briefs exist in it yet — it's an empty, ready-to-use database, not populated data.

## 11. RACI / Ownership

Solo owner + AI. "Responsible" below means the agent that produces the recommendation;
**Accountable is always Mary Thuo** — advisory-first means no agent publishes.

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Content intelligence (5 sources) | `content-intelligence-hub` | Mary Thuo | Sector (01), Marketing (03), Offer (02), Client Success (07), Sales (05) | — |
| Opportunity mapping + priority scoring | `content-opportunity-mapper` | Mary Thuo | Sector (01) for Revenue Signals fuel | — |
| Narrative + messaging integrity | `content-narrative-architect` | Mary Thuo | Branding (12), Experience Engineering (20) — adjacent narrative altitudes | — |
| Content brief → Notion | `content-brief-builder` | Mary Thuo | Design (19) | Automation (16) — engagement follow-up |
| Publish / reject decision | `content-publishing-gate` | Mary Thuo | Sales Risk & Trust Governance (05), Legal (10) for claims | — |
| Multiplication tree | `content-multiplication-engine` | Mary Thuo | Marketing (03) — channel execution | Sales (05) — enablement assets |
| **Publishing the asset** | **Mary Thuo (human)** | Mary Thuo | — | All of the above |

## 12. Triggers / Automation Hooks

**The chain (all real, all wired):**

```
SECTOR_MAPPED ─┐
MARKET_SIGNAL_MAPPED ─┤
OFFER_ENGINEERED ─────┼─→ content-intelligence-hub ─→ CONTENT_INSIGHT_CAPTURED
ADVOCACY_CAPTURED ────┤                                        │
BUYER_PSYCHOLOGY_MAPPED ┘                                      ▼
                                              content-opportunity-mapper
                                                               │ CONTENT_OPPORTUNITY_MAPPED
                                          ┌────────────────────┴────────────────┐
                                          ▼                                     ▼
                            content-narrative-architect ──→ content-brief-builder
                                   NARRATIVE_APPROVED              │ CONTENT_BRIEF_READY
                                                    ┌──────────────┴──────────────┐
                                                    ▼                             ▼
                                       content-publishing-gate      design-storyboard-generator (19)
                                                    │ CONTENT_APPROVED
                                                    ▼
                                       content-multiplication-engine
                                                    │ MULTIPLICATION_TREE_READY
                                    ┌───────────────┴───────────────┐
                                    ▼                               ▼
                    marketing-demand-generation (03)   sales-enablement-playbooks (05)
```

**Scheduled:** `content-intelligence-hub` runs **Mondays 08:00** (`0 8 * * 1`) — a
weekly sweep of the five sources independent of whether any upstream event fired,
so starvation surfaces on a cadence rather than by silence.

**The production hook:** `Publishing Status = "Ready for Design"` in the Notion
content-brief database is the real trigger value of the **Creative Pipeline cloud
routine** (`trig_01WyyrXEkFZck1D49tm6BfKv`, hourly `7 * * * *` —
`GO_LIVE_CHECKLIST.md` items 42–43). **This is the only Arika automation in
production, and Content is its supply.** `content-brief-builder` recommends the
status but never flips it — that is a human action (Class 2), because flipping it
starts real generation against real credits.

> **🔴 Corrected 2026-07-15 — this section said "enabled 2026-07-04" and that was
> misleading for 11 days.** The routine fired **once** on 2026-07-04 and was
> auto-disabled 3 hours later (`auto_disabled_repo_access`). It was dead until
> 2026-07-15, when it was restored and re-verified. **Nothing was lost — the brief
> database is empty — but had Content ever marked a brief "Ready for Design" in that
> window, nothing would have picked it up while this file said otherwise.** Content is
> the supply for an automation Content cannot see the health of; that is now
> `automation-reliability-monitor` (16)'s job. Incident: `16_Automation/AUTOMATION_OS.md`
> §9. **Last verified: 2026-07-15T09:36:46Z (forced run); the hourly cadence is not yet
> proven post-restoration.**

## 13. Existing OS Sub-Layer

No department-local code. Content runs entirely on the shared `arika-runtime`
substrate (`arika-runtime/DESIGN.md`) plus two real external systems it does not own:
the **Notion content-brief database** (live, 18 properties, **empty**) and the
**Creative Pipeline cloud routine** (hourly; **dead 2026-07-04 → 2026-07-15**, restored
and last verified 2026-07-15T09:36:46Z). See §12.

## 14. Raw Archive Pointer

10 files, all read in full for the 2026-06-30 content migration (no "Draft N" numbering convention used consistently here, and no `00_Workspace_Intelligence_Inventory/` backlog — this folder predates that convention): `Revenue Content Stratergy. Draft 1.md`, `Content Intelligence System. Draft 2.md`, `Content Opportunity Mapping. Draft 3.md`, `Content System Design. Draft 4.md`, `Content Planning Execution. Draft 5.md`, `Narrative Architure Framework. Draft 6.md`, `Messaging Architure Framework. Draft 7.md`, `Linkedin Stratergy. Draft 13.md`, `Instagram as a Business Tool. Draft 14.md`, `Project Realignment Stratergy.md`.

**One named real-world external reference** found anywhere in this department: an Instagram creator referred to as "homozy" (likely a garbled transcription), used as a contrast example in the Instagram file, not as the agency's own model — not otherwise significant, noted for completeness.

`Messaging Architure Framework.md` contains a section of generic sensory-language copywriting tables (e.g. "luxury hospitality," "high-end beverage") that read as lifted from an unrelated branding context — treat as filler/generic, not agency content, if migrating further.

## 15. Changelog

- 2026-06-30 — Department created as part of v0.1 skeleton restructuring; was initially merged into Marketing as `360_Agency_Content/`, then corrected to a standalone department per explicit owner feedback (it was conceived as a full department, not a Marketing sub-area), with all subsequent departments renumbered (Sales 04→05, ClientPartner Acquisition 05→06, Client Success 06→07, Operations 07→08, Finance 08→09, Legal 09→10, HR/People Ops 10→11, Branding 11→12, Tech Stack 12→13, Cross-Domain Synthesis 13→14).
- 2026-06-30 — Content migration: all 10 files read in full. Capability Registry, Workflow Index, KPI Dictionary, and Standards & SOPs Index populated. `Project Realignment Stratergy.md` confirmed as the most "decision-like" document found in any department to date (real document lineage, clear from/to/why argument) but flagged as unconfirmed reasoning, not a logged decision. Unresolved 3-way content-pillar naming conflict across source files documented rather than silently picking one. Content/Marketing department boundary flagged as an imposed architectural decision, not one drawn in the source material — added to owner-input tracker for confirmation.
- 2026-06-30 — Owner resolved all 4 open items (tracker 15-18): confirmed the Content/Marketing split, adopted the Project Realignment repositioning, and asked for the 3 pillar sets to be synthesized rather than picking one — built a canonical 7-pillar structure (Realignment's top level) populated with the generic set's sub-topics and the LinkedIn set's fully-built post series, with Sector (01)'s new real signal framework flagged as the strongest fuel for the "Revenue Signals" pillar. Confirmed no launch date set yet for LinkedIn/Instagram. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-01 — Added the Content Houses intent axis, Story Architecture, Campaign Architecture, and a target Notion content-brief schema, per the new Design (19) department's founding planning session. Cross-linked Design (19)'s campaign-first Canva structure and Automation (16)'s new Engagement Layer (DM automation follow-up). Notion workspace itself flagged as not yet created — schema is a target, not live data. — Claude Code (Sonnet 5)
- 2026-07-03 — **Notion content-brief database built for real**, matching the §10 schema exactly (18 properties, all select/multi-select options populated). Closes tracker item 43. — Claude Code (Sonnet 5)
- 2026-07-04 — **Added the Content Operating System (COS) 10-layer model** (§10, §8), mapping the owner's pasted COS vision onto this file's already-real structures (Content Intelligence System, Execution OS, Asset Production Workflow, pillar/house synthesis, Story Architecture, KPI exclusion list, ACCOS's Distribution Engineering/Performance Intelligence stages) rather than building a competing framework. One genuine gap surfaced (Layer 7, Engagement) and left open. Companion to the new Arika website project — `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`. — Claude Code (Sonnet 5)

- 2026-07-14 — **Department revived on `arika-runtime`.** Diagnosis first: all 11 source files re-read; found Content **doctrine-rich but agent-dead** — §5, §6, §11, §12, §13 and §16 were all placeholders while §3/§4/§10 carried the most fully-resolved doctrine of any department. Built **6 agents** (`content-{intelligence-hub, opportunity-mapper, narrative-architect, brief-builder, multiplication-engine, publishing-gate}`), populating §5, §11, §12, §13, §16. Triaged 4 candidate agents out with reasons rather than duplicating Marketing (03), Design (19), and Sector (01) — the fragmentation this department's own narrative names as the enemy. Added a `CONTENT_BRIEF_READY` event trigger to `design-storyboard-generator` (19), whose description always claimed a content brief as its input but had no trigger to receive one. Verified: `arika list` → 54 agents, `npm test` → 8/8. Surfaced two genuine unresolved source conflicts (§10) rather than silently picking: the **DRAGON redefinition** (the owner-adopted Realignment redefined all six letters; the adoption captured its pillars but not this) and the **Instagram Implementation Strategy pivot** (a 5th atomic-unit stage, Action Pillars, and an Implementation Scorecard, noted in §3 but never absorbed). Left ACCOS Stage 12 / COS Layer 10 (Performance Intelligence) deliberately unbuilt — it has zero possible input until something is published. — Claude Code (Opus 4.8)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 6 agents append to `04_Content/_memory/runtime.jsonl` in the shared
bois-compatible envelope (`{timestamp, agent, department, stream, event_type,
source:"arika-runtime", payload}` — `arika-runtime/DESIGN.md`). This is the only
record of what Content agents actually did, and the only evidence
`operations-state-monitor` (08) can use to mark this department `live` rather than
`documented`. **The stream is empty until the first run.**

**Feedback loop.** §7's KPIs cannot miss a threshold yet — nothing is published and
no accounts exist. The loop that *is* live is different and more useful right now:
`content-intelligence-hub` emits **`INTELLIGENCE_STARVED`** whenever any of the 5
sources has never fed it. Given the agency has no client outcomes yet, the Client
Intelligence source (`ADVOCACY_CAPTURED`) is expected to report `empty` — that is a
true reading of the business, not a bug. ACCOS Stage 12 (Performance Intelligence)
is the real closing loop and is **deliberately unbuilt** until there is published
content to measure (§5).

**Cadence** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — the 7 Cognitive
Calendars): Content runs primarily against the **Opportunity Calendar** (the
opportunity mapper's scored backlog is an opportunity register) and the **Strategic
Calendar** (authority compounds over the 4-phase roadmap: Credibility 1–3mo →
Recognition 4–6mo → Thought Leadership 7–12mo → Category Leadership Yr2+). It is
**not** on the Revenue Calendar — content influences revenue but does not book it,
and `operations-daily-command` (08) should not expect same-day revenue from it.
The one hard beat is `content-intelligence-hub`'s **Monday 08:00** sweep.

**Note on the Authority-Building Roadmap:** its phases are measured in months from
launch, and **there is no launch date** (§7, `GO_LIVE_CHECKLIST.md` item 14). The
roadmap is a ready template, not a running clock.
