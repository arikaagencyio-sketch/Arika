# LinkedIn — Platform Operating Dossier (Presence 21)

**Version:** v0.1.0
**Last updated:** 2026-08-07
**Owner:** Mary Thuo (Agency Governance, 00) · coordinated by **Presence (21)**
**Status:** **S1 — personal profile exists, Company Page BLOCKED, nothing published, zero automation.** This file is the single consolidated LinkedIn source of truth: every LinkedIn decision, strategy, and constraint that was scattered across 6 departments, reconciled in one place.

> **Reading order:** `GLOBAL_OS.md` → `21_Presence/PRESENCE_OS.md` → `21_Presence/CONTENT_DISTRIBUTION_ENGINE.md` → **this file.**
> Companions: `21_Presence/PLATFORM_ONBOARDING_TRACKER.md` (account health, all 10 platforms) · `04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md` (platform behaviour) · `04_Content/CONTENT_OS.md` §10 (pillars, houses, Notion schema).

---

## 1. What this file is — and what it does not own

LinkedIn is the agency's **position-1 platform**: first in the confirmed 10-platform launch order, the designated **first end-to-end test of the whole distribution engine**, and the only platform whose revenue function is *primary B2B pipeline*. It also had the most developed content strategy in the repo (`04_Content/Linkedin Stratergy. Draft 13.md`, ~1,550 lines) — written before any account existed, and never reconciled against the account reality that now exists.

This dossier **consolidates and reconciles**; it does not re-own capability (one-owner discipline, `PRESENCE_OS.md` §1):

| What | Owner | This file's role |
|---|---|---|
| Content assets, pillars, narrative, post construction | **Content (04)** | Carries the LinkedIn-specific execution layer of Content's strategy |
| Distribution strategy, channel role, measurement truth | **Marketing (03)** | Records the confirmed channel role + KPI |
| Platform behavioural intelligence | **Content (04)** PIL | Consumes the LinkedIn profile |
| Brand voice, visual law | **Branding (12)** | Expresses within it |
| Executor runtime, cron, approval rows | **Automation (16)** | Names the gate, doesn't build it |
| Tool registration + `verified_at` | **TechStack (13)** | Flags what must be registered |
| ICP, buyer titles, LinkedIn outreach intelligence | **Sector (01)** | Consumes for connection targeting |
| Account health, anti-flag stage model | **Presence (21)** tracker | Deepens it for this one platform |

---

## 2. Reality state — what is actually true today (2026-08-07)

| Fact | State | Source |
|---|---|---|
| Personal LinkedIn profile | ✅ **Created** ("Arika") | `PLATFORM_ONBOARDING_TRACKER.md` §4 |
| Company Page | 🔴 **BLOCKED** — new account lacks the connections/profile maturity LinkedIn requires | tracker §5.1 |
| Connections | 🔴 Effectively none — the blocking constraint | owner, this session |
| Posts published | 🔴 **Zero** | — |
| Developer app / API access | 🔴 Not started — **and cannot start**: LinkedIn requires the dev app to attach to a **Company Page** | tracker §5.1 |
| Postiz connection (the executor) | 🔴 Not connected — 0 channels connected on a live instance | `CONTENT_DISTRIBUTION_ENGINE.md` §2 |
| Executor infrastructure | ✅ **LIVE** — Postiz + Postgres + Redis healthy on Hostinger KVM 2 + Coolify | tracker §4 |
| Content strategy | ✅ Fully written, ⚠️ **not publishable as written** — see §7.7 | `Draft 13` |
| Content brief database (Notion) | ✅ Built, **empty**; has a `LinkedIn` platform option | `CONTENT_OS.md` §10 |
| Launch date | 🔴 Never set — open owner decision since 2026-06-30 | `GO_LIVE_CHECKLIST.md` item 14 |

**The honest summary:** the infrastructure is ahead of the account, and the strategy is ahead of both. The single thing standing between here and everything else is **connections**.

---

## 3. Why LinkedIn is position 1 (the confirmed strategic role)

| Dimension | Confirmed value | Source |
|---|---|---|
| Launch priority | **1 of 10** | `CONTENT_DISTRIBUTION_ENGINE.md` §2 |
| Engine role | **First-test platform** — the full 12-stage body runs end-to-end here before any other platform scales | ibid. |
| Marketing channel role | Executive authority & B2B lead generation · **KPI: qualified leads** | `MARKETING_OS.md` §10 |
| Revenue function | **Acquisition — primary B2B pipeline surface** | PIL §4.1 |
| User intent | Professional advancement — *"help me become more successful"* | PIL §4.1 |
| Trust mechanics | Experience, results, thought leadership, professional proof | PIL §4.1 |
| Discovery mechanics | Network relevance, dwell time, meaningful comments | PIL §4.1 |
| Native language | Focused reading; declarative, credible; text-forward, clean carousels; **minimal motion** | PIL §4.1 |
| Presence layer | Executive/Authority — economic job: *executive trust → primary B2B pipeline* | `PRESENCE_OS.md` §3.2 |
| Direction | Primarily **inbound** (demand arrives) + **outreach** (the mechanism) | `PRESENCE_OS.md` §3.1 |

**The strategic frame that governs all of it** (owner-adopted 2026-06-30, "Project Realignment"): LinkedIn is **one Knowledge Distribution node among several**, not the brand. *"The agency is not a content agency and not a LinkedIn thought leadership brand. It is a Revenue Growth Operating System. Content is simply one of the interfaces of that operating system."* (`CONTENT_OS.md` §10). Draft 13 predates this and reads as if LinkedIn *is* the strategy — read it subordinated to the Realignment, not above it.

---

## 4. The blocking chain — what is actually stuck, and why

This is the core of this session. The account isn't "new and slow" — it is sitting at the head of a **five-link dependency chain**, and every downstream investment in the repo is waiting on link 1:

```
PRESENCE  →  CONNECTIONS  →  COMPANY PAGE  →  DEVELOPER APP  →  API/POSTIZ  →  ENGINE TEST
(manual)     (validated)      (LinkedIn gate)   (needs a Page)    (needs app)    (12 stages)
   ▲
   └── you are here: the only unblocked link
```

- **Presence → Connections.** Connection requests from an empty profile with no posts get ignored or marked "I don't know this person" — which is itself a restriction trigger. Presence has to exist *before* connections are asked for. This is why warm-up is strategy, not delay.
- **Connections → Page.** LinkedIn gates Page creation on personal-profile maturity. Its stated requirements are a profile that is **7+ days old**, has a **profile photo**, has **multiple connections**, meets a minimum **profile strength**, and lists a **current position at the company**; a **company-domain email** is often required for verification. ⚠️ *Verify these against LinkedIn's live requirements at creation time — platform gates change, and this repo does not treat vendor rules as permanent.*
- **Page → Dev app.** The LinkedIn developer app **must attach to a Company Page** — so there is no API path that routes around the Page.
- **Dev app → Postiz.** Products needed: *Sign In with OpenID Connect* + *Share on LinkedIn* (+ *Advertising API* for token refresh); redirect `https://<postiz-domain>/integrations/social/linkedin`; creds into Coolify. ⚠️ Known Postiz OAuth *"Not enough scopes"* bug — expect friction here (tracker §5.1).
- **Postiz → engine test.** Phase 4 of the build order: one real packet through all 12 stages.

**The asset that unblocks link 2 fastest:** the repo already confirms a real company-domain email — `mary.thuo@arikaagency.com` (`OWNER_INPUT_NEEDED.md` item 33, resolved 2026-06-30). ⚠️ *Confirm the mailbox is actually provisioned and receiving* — a confirmed address in a doc is not a working inbox, and this is exactly the class of doc-vs-reality drift this repo has caught four times.

---

## 5. The warm-up runway (S1 → S6)

Extends the tracker's stage model with LinkedIn-specific actions. **Golden rule stands: no S4/S5 until S2 and S3 genuinely clear.** Automation before warm-up is the flag.

### S2 — Humanize & verify *(days 1–3, unblocked, do now)*

| Action | Why it matters |
|---|---|
| Real profile photo + background banner | Page-creation gate; the "is this a real person" signal |
| Headline — see §7.8 for options | The single most-read line on LinkedIn |
| About section — first 2 lines carry it (the rest is behind "see more") | Positioning, and a Page-creation profile-strength input |
| **Current position: Founder, Arika Agency** | **Hard Page-creation requirement** — the Page cannot be created without the company listed as current experience |
| Verify email **and** phone | Account-trust signal; reduces restriction risk |
| Custom profile URL | Cheap, permanent, quotable everywhere else |
| Featured section — leave empty for now | Nothing substantiable to feature yet (§9) |

**Exit criteria:** profile reads as a real founder of a real company to a stranger in 5 seconds; company-domain email verified; profile strength at LinkedIn's stated minimum for Page creation.

### S3 — Warm up: presence + connections *(weeks 1–4, manual only)*

Two tracks run in parallel, and **the posting track must lead the connection track** — outbound requests land far better when the profile has visible substance behind it.

**Track A — publish manually.** 3 posts/week for weeks 1–2, then 4/week (see §7.5 for the warm-up cadence and §7.7 for what must not be published). All published **by hand, in the LinkedIn app** — no scheduler, no Postiz, no API.

**Track B — build connections deliberately.** Conservative ramp, deliberately far below any published platform limit:

| Week | Connection requests/day | Comments on others' posts/day | Notes |
|---|---|---|---|
| 1 | 5–8 | 3 | Warm/known contacts first — highest acceptance rate |
| 2 | 8–12 | 3–5 | Begin ICP targeting |
| 3 | 12–15 | 5 | Only if acceptance rate is holding |
| 4+ | 15–20 | 5 | Hold here through the Page gate |

**Health rules:** every request carries a personal note; stop and hold the ramp if acceptance rate drops (low acceptance and "I don't know this person" reports are what trigger restrictions); one clean login location (`PLATFORM_ONBOARDING_TRACKER.md` §3 rule 5); never bulk-import contacts on a fresh account.

⚠️ Draft 13 prescribes **30–50 connection requests/week** from day one. That number is safe for an aged account, aggressive for a 1-week-old one. The ramp above reaches it by ~week 3 instead of week 1. **This ramp supersedes Draft 13's figure for the warm-up period.**

**Exit criteria:** 2+ weeks of genuine activity, real two-way conversation in comments/DMs, and a connection count that satisfies LinkedIn's Page gate.

### S4 — Company Page *(gated on S3)*
Create the Page → complete it fully (logo, tagline, About, `arikaagency.com`, industry, specialties, location) → invite existing connections to follow → post to the Page manually for at least a week before any API work. **Class 3 sign-off:** the Page is a public-facing brand asset (`PRESENCE_OS.md` §5).

### S5 — Developer app + Postiz *(gated on S4)*
Dev app attached to the Page → products (Sign In w/ OpenID Connect, Share on LinkedIn, Advertising API for token refresh) → redirect URI → creds into Coolify → OAuth → channel added. Register in TechStack with `verified_at` (`TECHSTACK_OS.md` discipline). **Do not create the app the same day the Page is created** — one new asset at a time (tracker §3 rule 6).

### S6 — Verified live
One real post published **through the engine** — Phase 4 of the build order, the first end-to-end test of all 12 stages. Only then does `verified_at` get set.

**Realistic runway: 4–7 weeks from today to S6**, assuming S2 starts immediately. Most of it is calendar time that cannot be compressed — which is precisely why the content and connection work should run at full intensity during it.

---

## 6. Connection strategy — who, and why it is a revenue activity

Connections are not a vanity count here; they are the Page gate **and** the pipeline. Target them against the confirmed ICP rather than accepting whoever appears.

**Targeting source (real, owner-curated):** `01_Sector/SECTOR_OS.md` — the 3-tier B2B SaaS ICP (§1) and the **Decision-maker registry (xlsx Sheet 09)**, which holds per-subsector buyer titles, buying-trigger signals, and **LinkedIn/outreach intelligence** specifically. Also Sheet 10 (events & communities) and Sheet 11 (22 sectors scored 🟢 Ready Now / 🟡 In Progress / 🔴 Asleep) — start with 🟢 sectors.

| Priority | Who | Why |
|---|---|---|
| 1 | Warm/known contacts | Highest acceptance rate; protects account health early |
| 2 | **Tier 1 ICP** — Series A–C, $5M–$50M ARR, 50–500 employees, 3–20 person GTM team | Primary focus; RevOps is their bottleneck and budget exists |
| 3 | **Tier 2 ICP** — post-Seed–Series A, $1M–$10M ARR, founder still selling | Secondary; drowning founders, high engagement |
| 4 | Peers/operators/amplifiers in the same conversation | Comment volume and reach come from here, not from buyers |
| — | **Anti-ICP: skip** — <$5M ARR, founder-CEO running sales solo, tiny-ACV vertical SaaS | *"Educate market, don't sell to them yet"* (`SECTOR_OS.md` §1) |

**The sequence that turns a connection into revenue** (Draft 13's system, kept intact — it is sound):
`Attract (post) → Engage (reply within the hour) → Invite (personal note) → Listen (read their last 5 posts) → Offer (value, not a pitch) → Convert (diagnostic call)`.

**Rule that governs the last two steps:** no pitch in a connection request, and no offer that the agency cannot substantiate today (§9). With 0 clients and no case studies, the credible offer is a *diagnostic*, not a *result*.

---

## 7. Content strategy — the Revenue Reality LinkedIn playbook, reconciled

Source: `04_Content/Linkedin Stratergy. Draft 13.md` — the most concretely developed channel file in the repo. Everything below is consolidated from it, **subordinated to the Realignment** (§3) and **corrected against reality** (§7.7).

### 7.1 The LinkedIn core belief
*"LinkedIn is not a portfolio. It is a conversation."* The post is not the product — the post is the invitation; the comment thread is the first conversation, the DM the second, the call is where the work begins. **Everything before the call is permission.**

### 7.2 The 4 LinkedIn pillars (compressed from the 7 canonical pillars)
Seven pillars are too many to hold in rotation on LinkedIn. Draft 13's compression, mapped to `CONTENT_OS.md` §10's canonical set:

| LinkedIn pillar | Compressed from | Job on LinkedIn |
|---|---|---|
| **Revenue Decisions** | Revenue Anatomy + The Revenue Decision Chain | Practical frameworks they can use today |
| **Revenue Reality** | The Authenticity of Chaos + The Complexity Filter | Raw narrative; builds trust |
| **Unpopular Opinions** | The Growth-Opinion Stance | Sharp, shareable stance; makes you memorable |
| **Revenue Beyond Money** | The 5 Forms of Revenue + The Pre-Hire Revenue Audit | Counterintuitive angles |

The **Revenue Body** metaphor (skeleton/heart/lungs/nervous system/immune system) runs *underneath* all four as recurring diagnostic language.

Every brief still gets tagged with a **canonical pillar** *and* a **Content House** (Insights 25% · Demonstrations 25% · Frameworks 15% · Proof 15% · Founder Thinking 10% · Education 5% · Conversion 5%) in the Notion database — the crossed-axes model is canonical (`CONTENT_OS.md` §10). ⚠️ **Proof (15%) is unfillable today** — zero clients, zero case studies. Reallocate to Insights/Founder Thinking until there is real proof, rather than manufacturing it.

### 7.3 The 4 post formats

| Format | Structure | Use for |
|---|---|---|
| **Hook-and-Pivot** | Bold statement → "most people think X, but…" → framework in bullets → question | Revenue Decisions |
| **Narrative Lesson** | Specific raw moment (time/place/feeling) → what happened → what I realized → what I did → question | Revenue Reality |
| **Framework Drop** | Problem frame → "here is a framework" → 3–5 clear steps → where to start → question | Revenue Beyond Money |
| **Opinion Stand** | The unpopular opinion, unsoftened → why most believe the opposite → why they're wrong → what you believe → invitation to disagree | Unpopular Opinions |

### 7.4 Post architecture (every post, regardless of format)

| Element | Length | Purpose |
|---|---|---|
| Hook | 1–3 lines | Stop the scroll — name a pain felt *this week* |
| Bridge | 1–2 lines | "Here's what most people miss" |
| Body | 5–10 lines | Insight/framework/story; short paragraphs, liberal line breaks |
| CTA | 1 line | A specific personal question — **never** "thoughts?" |
| Comment starter | 1 line, first comment | Your own prompt to open the thread |

**Tactical rules (already standing agency SOP, `CONTENT_OS.md` §10):** reply to comments within 1 hour · never use passive CTAs ("Click here", "Learn more") · **put links in the first comment, not the post body**.

### 7.5 Cadence — warm-up vs. steady state

Draft 13's rhythm is the **steady state**, and it assumes an established account. During S3 it is deliberately throttled:

| Day | Format | Pillar | ⚠️ Warm-up (S3) |
|---|---|---|---|
| Mon | Hook-and-Pivot | Revenue Decisions | ✅ post |
| Tue | Narrative Lesson | Revenue Reality | ✅ post (wk 3+) |
| Wed | Opinion Stand | Unpopular Opinions | ✅ post |
| Thu | Framework Drop | Revenue Beyond Money | ✅ post (wk 3+) |
| Fri | Light / community | Any | comments only |
| Sat | — | — | rest |
| Sun | Comment-thread engagement | Any | ✅ engage |

**Warm-up throttle:** weeks 1–2 → Mon/Wed/Fri (3 posts). Weeks 3–4 → Mon/Tue/Wed/Thu (4 posts). Steady state → the full table. All manual until S5.

**The 90-day launch plan (Draft 13) — Phase 1 starts at S3, not at S1:** Phase 1 Identity (wks 1–2, opinion + story, no frameworks) → Phase 2 Value (wks 3–6, introduce frameworks) → Phase 3 Depth (wks 7–10, all 4 formats, weave the Revenue Body metaphor) → Phase 4 Community (wks 11–12, feature others, start threads).

### 7.6 Engagement doctrine
On LinkedIn **comments outweigh the post** — the algorithm weights deep threads heavily, and PIL confirms discovery runs on *network relevance, dwell, meaningful comments*. Reply within the hour; reply with value, never "thanks"; go deep with thoughtful commenters; end comments with questions; tag 1–2 people in your first comment only when genuinely relevant. This is **Presence's Engagement capability** (`PRESENCE_OS.md` §3.4, COS Layer 7) — the two-way layer no other department owns. DM *automation*, when it exists, routes to Automation (16)'s Engagement Layer.

### 7.7 🔴 What must NOT be published — the fabricated-persona problem

**This is the most important correction in this file.** Draft 13 is an external-AI (Sider Fusion) output written in a founder voice that **does not match this agency's reality**. Its example posts, and all three bio options, assert as fact:

- *"I once lost 40% of my revenue in one email"* — did not happen; the agency is pre-revenue with 0 clients.
- *"The month I missed payroll… I had 14 days to find $80,000"* — did not happen; there is no payroll.
- *"I have spent over $50,000 on sales training"* — unsubstantiated.
- *"I spent the last 4 years building a system around those 7 decisions"* — unsubstantiated.
- *"Revenue Reality™"* — **a trademark claim.** Nothing is registered; Legal (10) has no engaged counsel and nothing lawyer-reviewed.
- *"The client who fired us and saved us"*, *"we changed our revenue model in 48 hours"* — no clients, no such events.

Publishing any of these would break three standing rules at once: the constitution's **no silent invention**; Gate 2's **every claim substantiated (Legal Class C)**; and Content's **"Never publish: Authority Without Evidence."**

**What survives, and is genuinely valuable:** the *structures* — DRAGON, the 4 pillars, the 4 formats, the post architecture, the cadence, the comment strategy, the lead-gen sequence, the 7 pillar series outlines. Those are frameworks, not claims.
**What must be rewritten:** every first-person war story, every number, every ™.

**The honest voice that is actually available** — and is arguably stronger on a platform drowning in performed authority — is *building in the open*: the agency is constructing a 360° Cognitive Revenue Operating System right now, and the observations, frameworks, and hard calls coming out of that construction are real, current, and nobody else's. That is a defensible position for a founder with no client roster. Draft 13's own thesis ("stop performing business", the 15% Gap, "does this make the reader feel less alone") supports it exactly — it just supplied a borrowed biography to carry it.

### 7.8 Profile copy — rebuilt on true facts

Draft 13's three bios all rest on the fabrications above and **cannot be used as written**. Options built only on confirmed repo facts (Revenue Growth Operating System positioning, Revenue Infrastructure Partner, B2B SaaS focus, the 7-decisions framework):

**Headline (pick one):**
- `Founder, Arika Agency — Revenue infrastructure for B2B SaaS. Systems, not activity.`
- `Founder, Arika Agency — I build the revenue operating system most companies assume they already have.`
- `Founder, Arika Agency — Before you hire, audit. Before you buy, diagnose.`

**About — opening two lines (the only ones most people read):**
- *Framework-forward:* "Most revenue problems are decision problems wearing a costume. I write about the 7 decisions that have to happen before any dollar moves."
- *Opinion-forward:* "Most revenue advice is dangerous because it ignores context. I write about the systems underneath the number — marketing, sales, automation, partnerships as one machine, not four departments."
- *Build-in-the-open:* "I'm building a revenue operating system — the thing agencies sell you pieces of. I write down what it actually takes, while it's happening, including the parts that don't work yet."

⚠️ **Owner decision required** — voice selection is a Class 3 public-facing brand call, and must clear Branding (12). Do not ship a headline without that.

---

## 8. Orchestration — how LinkedIn runs inside the engine

LinkedIn is the **proving ground** for the whole Content Distribution Engine. Once it works here, platforms 2–10 follow the same body.

**The 8 layers, LinkedIn instance** (`CONTENT_DISTRIBUTION_ENGINE.md` §3):

| Layer | LinkedIn reality today |
|---|---|
| L0 Foundation | ✅ Hostinger KVM 2 + Coolify, Postiz healthy |
| L1 Supply | Design (19) — text-forward + clean carousels; **minimal motion** (PIL) |
| L2 Multiply | Content (04) `content-multiplication-engine` — 1 asset → the LinkedIn variants |
| L3 Reservoir | Notion brief DB (built, empty) — `Platform: LinkedIn` |
| L4 Governance | G1 `presence-economics-gate` + G2 `content-publishing-gate` |
| L5 Orchestration | Not built — cadence engine + rate governor (Automation 16) |
| L6 Executor | Postiz — 🔴 **LinkedIn channel not connected** (blocked at §4) |
| L7 Monitor | Not built — token expiry, gap sentinel, `verified_at` |

**The 12 stages** run unchanged for LinkedIn: `Conceived → ◇G1 Concept Gate → Define Success → Plan the Tree → Package → Produce → ◇G2 Pre-Publish → Schedule → Publish → Verify → Measure → Archive`.

**During S2–S4 the engine is bypassed by design.** Stages 08–10 (Schedule/Publish/Verify) are performed **by hand** — that is the warm-up. Stages 01–07 (concept through pre-publish) should run *properly* even for manual posts, so that by the time the API connects, the gates, the briefs, and the packet discipline are already habits rather than new machinery.

**Handoffs:** Content produces → Design supplies → Presence gates the economics → human signs off Class 3 → (later) Automation schedules and Postiz publishes → Marketing measures → qualified conversations route into **RevOS** (Sales 05 / ClientPartner 06) via the `AEIT_09` handoff packet.

---

## 9. Governance & guardrails

- **Class 3 human sign-off** on everything public-facing: the Page, the headline/About, and every post (Gate 2). Non-negotiable, `AGENCY_OPERATING_CONSTITUTION.md` §5.
- **Presence Economics:** no post ships without an **economic job** + ≥1 of the five commercial movements (`AGENCY_COMMERCIAL_DOCTRINE.md` §9). *"No cup that no one drinks from."*
- **Never publish:** Offer Before Problem · Solution Before Insight · **Authority Without Evidence** (`CONTENT_OS.md` §10). The third one is the live risk here — see §7.7.
- **Legal Class C:** every claim substantiable. No client results, no revenue figures, no ™, no implied track record. Route anything doubtful via `presence-legal-liaison` → Legal (10). ⚠️ Legal has **no engaged counsel** — so the safe default is to make no claim at all.
- **Excluded metrics** (`PRESENCE_OS.md` §7, Presence Constitution §8): impressions, followers, likes, reach. Draft 13 independently reached the same conclusion — it excludes impressions and follower count in its own "what NOT to track."
- **Anti-flag doctrine** (tracker §3): no automation before warm-up · complete and verify the profile first · genuine native content, not cross-posts · gradual ramp · one clean login location · **one new asset at a time** · respect rate limits.
- **Approval-matrix row required** before any LinkedIn cron fires (Automation 16 rule) — no row, no automation.

---

## 10. Measurement

Track only what indicates commercial movement:

| Metric | Why | Draft 13's 90-day target |
|---|---|---|
| Comments per post | Engagement depth — people are thinking | 10–20 quality comments |
| DMs received/week | Interest signal | 5–10/week by wk 6 |
| Connection requests sent/accepted | Intentional network growth | 30–50 quality/week |
| Conversations → calls | **The real one** — pipeline | 3–5 discovery calls/month by month 3 |
| Qualified leads | Marketing's confirmed channel KPI | — |
| Branded-search growth | Presence KPI (compounding authority) | — |

⚠️ **Every number above is an uncalibrated template, not a baseline.** Zero LinkedIn data exists; the repo's standing rule is never to fabricate a baseline (`CONTENT_OS.md` §7, `PRESENCE_OS.md` §7). Treat them as hypotheses to be replaced by the first 30 days of real data. Draft 13's "200–500 profile views/week" sits closer to a vanity metric than the excluded list allows — **deprioritized here.**

---

## 11. Open decisions — owner input required

| # | Decision | Why it's blocking | Recommendation |
|---|---|---|---|
| L1 | **Confirm the LinkedIn launch date** (open since 2026-06-30, `GO_LIVE_CHECKLIST.md` item 14) | The one decision that starts the 4–7 week runway | Start S2 immediately; S3 posting begins within 3 days |
| L2 | **Profile identity: personal name or "Arika"?** The tracker records the profile as "Arika" | LinkedIn Pages must be created by a *person*; a company-named personal profile can be restricted, and *"founders are bought before agencies"* (`PRESENCE_OS.md` §3.2) | Personal profile = **Mary Thuo, Founder at Arika Agency**; the brand lives on the Page |
| L3 | **Voice selection** — headline + About from §7.8 | Class 3 public-facing; gates everything | Build-in-the-open; it's the only one fully substantiable today |
| L4 | **DRAGON conflict** (unresolved since 2026-07-14, `CONTENT_OS.md` §10) — Dialogue/Relatability/Authenticity/Growth/Opinion/Niche vs. Diagnosis/Revenue-Logic/Architecture/Growth-Systems/Operational-Intelligence/Navigation | LinkedIn is where DRAGON is actually applied; the ambiguity lands here first | Keep both at different altitudes (LinkedIn DRAGON = post construction; Realignment DRAGON = operating philosophy) and **name them distinctly** — same resolution pattern as the 3-way narrative reconciliation |
| L5 | **Is `mary.thuo@arikaagency.com` a live mailbox?** | Company-domain email is a likely Page-verification requirement | Verify before attempting Page creation |
| L6 | **Proof House (15%) has nothing to fill it** | 0 clients, 0 case studies | Reallocate to Insights/Founder Thinking until real proof exists — do not manufacture |

---

## 12. Decision Log

- **2026-08-07 — LinkedIn dossier created; all LinkedIn material consolidated.** Everything LinkedIn across `04_Content` (Draft 13, CONTENT_OS, PIL), `03_Marketing` (§10 channel role), `01_Sector` (ICP + decision-maker registry), `13_Tech_Stack`, `00_Agency_Governance` (GO_LIVE item 14, OWNER_INPUT item 44) and `21_Presence` (PRESENCE_OS, CDE, tracker) pulled into one file. No capability re-owned — Content still owns content, Marketing distribution, Sector the ICP; this is the coordination layer Presence (21) exists to be. — Claude Code (Opus 5)
- **2026-08-07 — 🔴 Draft 13's first-person content ruled unpublishable as written.** Its example posts and all three bios assert a founder history that did not happen (lost 40% of revenue, missed payroll/$80K, $50K on sales training, 4 years building the system, "Revenue Reality™", clients who fired us). Publishing them would breach no-silent-invention, Gate 2's substantiation rule, and "Never publish: Authority Without Evidence." **Structures kept, claims struck**; a substantiable "building in the open" voice proposed in its place (§7.7–7.8). Owner decision L3. — Claude Code (Opus 5)
- **2026-08-07 — Connection ramp supersedes Draft 13's 30–50/week for the warm-up period.** Draft 13's figure is safe for an aged account, restriction-triggering for a 1-week-old one; the §5 ramp reaches it by ~week 3. Anti-flag doctrine wins where the two disagree. — Claude Code (Opus 5)
- **2026-08-07 — The blocking chain named** (presence → connections → Page → dev app → API → engine test). Establishes that connections are not a vanity metric but the literal gate on the agency's position-1 platform and its first full engine test. — Claude Code (Opus 5)

## 13. Honest state

LinkedIn has published **nothing**. One personal profile exists, with no photo confirmed, no posts, effectively no connections, no Company Page, no developer app, and no channel connected to a live and healthy executor that is sitting idle waiting for it. The strategy is thorough and mostly sound — and was written for a founder who doesn't exist yet, which is the single most important thing this file corrects. What is genuinely ready: the frameworks, the pillar/house structure, an empty Notion brief database, a running Postiz instance, and a real ICP with real buyer intelligence to aim connections at. What is genuinely missing: a photo, a headline, ten posts, and a hundred connections — none of which any agent can do for the owner, and all of which unblock everything else.
