# Platform Intelligence Registry (PIL)

**Owner department:** Content (04) — home of ACCOS, PIL's primary consumer
**Type:** Canonical registry — an *Intelligence* knowledge-object type ("the Platform"), not a department
**Status:** Established 2026-07-23. **Design/reference doc — reality-gated: zero social accounts exist** (`00_Agency_Governance/GO_LIVE_CHECKLIST.md` item 23), so no measured platform data exists yet. Behavioral baselines below are general, publicly-observable platform knowledge, **not** agency-measured results.
**Consumed by:** Content (04), Marketing (03), Sector (01), Design (19), Experience Engineering (20), Branding (12), **Presence (21) — downstream operational owner**; minor — Sales (05), Client Success (07), Automation (16).

> Read `GLOBAL_OS.md` first, then `04_Content/CONTENT_OS.md`. This file is the single canonical source for platform *behavioral* intelligence. It does **not** replace Marketing (03)'s distribution-role view or Content's Notion `Platform` tag — it is the upstream layer both of those already point at.

---

## 1. What PIL is — and is not

**PIL is** the agency's upstream behavioral intelligence about how each digital platform actually works as a human environment: the psychology users bring, how trust is earned, how content is discovered, and the communication / visual / motion languages that read as native there. It is consumed **before** an asset is produced, so production is *engineered for the environment*, not resized into it.

**PIL is not:**
- **Not a distribution channel.** Distribution is Marketing (03)'s mandate (`MARKETING_OS.md` §10). PIL informs distribution; it does not perform it.
- **Not a social-media document.** It governs *behavioral ecosystems*, including owned surfaces (Newsletter, Website), not "social posting."
- **Not a new department or a new agent.** It is a registry that existing agents consume (see §7). The agency already **deliberately declined** to build a distribution/platform agent (`CONTENT_OS.md` §5) — PIL honors that.

**Core principle:** *One strategic narrative → many native executions.* The agency never changes its message; it changes how the message is expressed to match each platform's behavioral expectations. The narrative itself is guarded by `content-narrative-architect` (04); PIL only governs the *native expression* of it.

---

## 2. Position in the architecture (how PIL maps onto the real model)

The agency does **not** model intelligence as a free-floating stack of layers (Sector / Audience / Brand / Revenue). It models intelligence as **departments that produce it** plus the single **IntOS pipeline** that verifies and distributes it (`00_Agency_Governance/enterprise_architecture/AEIT_07_INTOS_BLUEPRINT.md`). PIL is therefore not a new "layer" — it is **one Intelligence knowledge-object type: the Platform**, an instance of the *Intelligence* registry already anticipated in `REGISTRY_TAXONOMY_REFERENCE.md` and blueprinted inside IntOS.

```
Business Objective → Audience Intelligence → PLATFORM INTELLIGENCE (this) →
Narrative → Creative/Motion → Production → Distribution (Marketing 03) → Performance
```

- **Distributes to consumers** via the interface-contract standard (`AEIT_09`) and, once IntOS is activated, via the IntOS Distribution layer (`AEIT_07` layer 7). Until then it is a plain reference doc consumed by reading.
- **Registers as a Source** in the Global Source Registry (`AEIT_08`) only when IntOS activates — reality-gated, not populated now.

### 2.1 Reconciliation with the three artifacts that already touch platforms

PIL **reconciles with, does not duplicate**, three existing artifacts that describe the same platform objects from other angles:

| Existing artifact | The angle it owns | PIL's relationship |
|---|---|---|
| Marketing `MARKETING_OS.md` §10 "Platform roles" table (role + KPI; *"every platform is a distribution endpoint"*) | **Downstream** distribution role | PIL is the **upstream behavioral twin**. Marketing's `Distribution role` column is imported into §4 below by reference; both cite this registry as canonical. |
| Content Notion `Platform` field + ACCOS Stage 11 "Distribution Engineering" | The **operational tag** on a brief | The tag now *implies* consulting this registry. **No schema change** — the field already exists. |
| Sector `Social Media Sector Layering. Draft 14.md` (a "Social Media Sector Intelligence Layer") | Platform behavior **per sector** | PIL = the platform's **intrinsic baseline**; Sector applies a **per-sector overlay** on top of it. Baseline first, overlay second. |

---

## 3. The Platform Behavioral Profile — schema

A compressed, usable subset of the source's 13-part framework (the full 13 are aspirational; these 10 are what a content/creative decision actually needs today). No invented metrics — behavioral fields only.

| Field | What it answers |
|---|---|
| **Mission** | Why the platform exists / why users are there |
| **User intent & psychology** | The mindset and need on opening the app |
| **Trust mechanics** | How credibility is earned here |
| **Discovery mechanics** | How content is found / spreads |
| **Communication language** | Tone, formality, sentence rhythm, etiquette |
| **Visual language** | Composition, density, format, aspect ratio expectations |
| **Motion language** | Pacing, hooks, loop behavior (feeds Design 19 / EE 20) |
| **Narrative compatibility** | Which content forms succeed (educational, demo, opinion, framework…) |
| **Distribution role** | Role + KPI — *imported from `MARKETING_OS.md` §10*, not re-invented |
| **Revenue function** | Where it sits in authority → trust → acquisition → revenue |

---

## 4. Platform registry

**Scope note (a real reconciliation, flagged for owner):** Marketing §10 and Content's Notion `Platform` field currently name **different** platform sets — Marketing lists YouTube / TikTok / Threads (not in the Notion field); Content's field lists Tumblr / Website (not in Marketing's table). This registry proposes the **canonical union** below and recommends both artifacts converge to it. **Which platforms are actually in scope is an owner decision** — profiled rows are behavioral baselines, not a commitment to activate every account. `[OWNER: confirm the canonical in-scope set]`

### 4.1 Core set (named in both artifacts or clearly primary)

| Platform | Mission / user intent | Trust mechanics | Discovery | Native language (comm / visual / motion) | Distribution role (Mktg §10) | Revenue function |
|---|---|---|---|---|---|---|
| **LinkedIn** | Professional identity & career/business advancement — *"help me become more successful"* | Experience, results, thought leadership, professional proof | Network relevance, dwell, meaningful comments | Focused reading; declarative, credible; text-forward, clean carousels; minimal motion | Executive authority & B2B lead gen · KPI: qualified leads | **Acquisition** — primary B2B pipeline surface |
| **Instagram** | Identity, aspiration, visual inspiration — *"show me who you are"* | Consistency, execution quality, authenticity | Reels, Explore, saves, shares | Fast visual scroll; warm, concise; high-craft imagery; punchy Reel pacing, strong first-frame hook | Brand storytelling & visual education · KPI: engagement | **Trust/brand** — perception & proof of execution |
| **Facebook** | Social relationships & communities — *"keep me connected"* | Community participation, group value | Groups, shares, retargeting audiences | Conversational; community-native visuals; light motion | Community & retargeting · KPI: community growth | **Retention/retargeting** support |
| **X (Twitter)** | Real-time ideas & public conversation — *"what's happening now"* | Timely, clear opinions; being early/right | Replies, reposts, trending, quote-tweets | Terse, opinionated; text-first; minimal motion | Real-time insights & conversation · KPI: impressions, discussions | **Authority/PR** — founder voice, industry presence |
| **Pinterest** | Future planning & inspiration — *"I'm planning something"* | Useful, saveable, evergreen ideas | Keyword + visual search (evergreen) | Aspirational; vertical, text-overlaid visuals; static | Visual discovery · KPI: website traffic | **Evergreen inbound discovery** |
| **Newsletter / Substack** | Direct publisher→audience relationship — *"subscribe to your thinking"* | Depth, consistency, owned trust | Owned list; referrals; no algorithm | Long-form, considered; typographic; static | Owned audience · KPI: subscribers | **Owned trust & nurture** — algorithm-independent |
| **Website (owned hub)** | The authority hub where all platform traffic converts | Proof, clarity, credibility signals | Search (SEO/AEO/GEO, Mktg 03) + inbound links | Authoritative; full brand system; scroll/interactive (EE 20's domain) | Conversion hub (Content §10 COS) | **Conversion** — leads/opportunities land here |

### 4.2 Named-once set (in one artifact only — profile lighter; confirm scope)

| Platform | Mission / user intent | Native language | Distribution role | Note |
|---|---|---|---|---|
| **YouTube** | Deep learning & long-form trust — *"teach me"* | Long sessions; demonstration, depth; strong motion/edit discipline | Long-form education & SEO · KPI: watch time, subscribers | Marketing §10 only — strong candidate for canonical scope |
| **TikTok** | Entertainment-driven discovery — *"surprise me"* | Rapid entertainment loops; native, high-energy motion | Discovery & reach · KPI: views, shares | Marketing §10 only |
| **Threads** | Casual conversational networking | Light, conversational; text-first | Thought leadership · KPI: engagement | Marketing §10 only |
| **Tumblr** | Niche community & subculture expression | Informal, community-native; visual + text | *(no Marketing role assigned)* | Content Notion field only — **weakest scope signal; confirm before profiling deeper** |

### 4.3 Watchlist (not built — per `REGISTRY_TAXONOMY_REFERENCE.md` "don't build empty registries")

Reddit, Discord, WhatsApp/Telegram communities, Medium, Quora, Behance/Dribbble, GitHub, Podcasts (Spotify/Apple), Google Business Profile, review platforms. **Add a full profile only when the agency actually intends to operate there** — a maintained watchlist, not empty structure.

---

## 5. The per-sector overlay (Sector 01)

The profiles in §4 are each platform's **intrinsic baseline**. `01_Sector/Social Media Sector Layering. Draft 14.md` argues correctly that *"each sector uses social media differently"* — buyers, trust systems, urgency cycles, language, and proof differ by sector. That is a **per-sector overlay** applied on top of the baseline, owned by Sector (01), not a competing definition. Order of operations: **baseline (this registry) → sector overlay (Sector) → audience/persona → narrative → production.** Surfacing that draft into `SECTOR_OS.md` is a staged edit in the integration report.

---

## 6. Where PIL enters ACCOS (the upstream design constraint)

PIL is consumed at these ACCOS stages (`CONTENT_OS.md` §3) — it is an **upstream constraint**, not a downstream publishing step:

| ACCOS stage | How PIL is used |
|---|---|
| **2 — Audience Mapping** | Map audiences by platform behavior, not only role/demographics |
| **5 — Content Opportunity Mapping** | Score which platform environment best fits each opportunity |
| **7 — Content System Design** | Platform-native templates for copy / visual / motion |
| **10 — Content Multiplication** | One asset → *native executions* per platform, not resizes |
| **11 — Distribution Engineering** | Sequence per behavioral fit + buyer journey (executed by Marketing 03) |

---

## 7. AI agents that consume PIL (no new agent)

| Agent | Dept | How it uses PIL |
|---|---|---|
| `content-opportunity-mapper` | 04 | Platform-fit as a scoring input |
| `content-brief-builder` | 04 | Sets `Platform` tag + platform-native `Visual Direction` from the profile |
| `content-multiplication-engine` | 04 | Generates native executions per platform, not resizes |
| `content-publishing-gate` | 04 | Sharpens the existing **Distribution** governance alignment ("does it fit the target platform's behavioral profile?") — a fold, not a new gate |
| `marketing-demand-generation`, `marketing-seo-aeo-geo` | 03 | Consume behavioral profile for channel execution / discoverability |
| `design-storyboard-generator`, `design-production-engine-coordinator` | 19 | Visual/motion language + format/aspect ratio per target platform |

These are **consumption/reasoning references**, staged in the integration report — not applied in the pass that created this registry.

---

## 8. Validation principles (folded into existing gates)

The source's approval questions are **not** a new gate — they sharpen `content-publishing-gate`'s existing structure. Before an asset is approved, in addition to its current checks:

- **Platform-native?** Does the asset match the target platform's behavioral profile (comm/visual/motion language)? → sharpens the existing *Distribution* governance alignment.
- **Narrative preserved?** Native execution must not alter the strategic narrative (`content-narrative-architect`).
- **Right journey stage?** Platform's revenue function matches the intended buyer-journey stage.

Everything else (the 8 validation filters, 3 never-publish rules, 4-layer approval, `unevidenced_claims`) is unchanged.

---

## 9. Decision Log

- **2026-07-23 — Platform Intelligence Registry established** as a Content (04)-owned canonical *Intelligence* knowledge-object type, right-sized and reconcile-first (owner decisions, 2026-07-23). Modeled onto the real IntOS architecture rather than as a free-floating "layer." Reconciled against Marketing §10 (downstream distribution twin), Content's Notion `Platform` field (operational tag, no schema change), and Sector's Social Media Sector Layering draft (per-sector overlay). **No new department, no new folder, no new agent, no schema change.** Cross-department cross-reference edits staged in `00_Agency_Governance/enterprise_architecture/PIL_INTEGRATION_REPORT.md`, not applied in this pass. — Claude Code (Opus 4.8)
- **2026-07-23 — Flagged Marketing §10 vs. Content Notion `Platform` set divergence** (YouTube/TikTok/Threads vs. Tumblr/Website). Proposed canonical union in §4; `[OWNER: confirm in-scope set]`. Not resolved by invention.
- **2026-07-23 — Presence department (21) established downstream of PIL.** The owner consciously overrode the "no distribution/platform department" stance PIL cites (§1). PIL is **unchanged**: it remains the upstream *behavioral intelligence* (how each platform works), Content/IntOS-owned; §1's "not a distribution channel / not a new agent for *this registry*" still holds. Presence (21) is the *operational* owner that **consumes** PIL to run presence across layers — a consumer, not a rewrite. — Claude Code (Opus 4.8)

## 10. Changelog

- **v0.1 (2026-07-23):** Created. — Claude Code (Opus 4.8)
