# LinkedIn — Platform Operating Dossier (Presence 21)

**Version:** v0.1.0
**Last updated:** 2026-08-07
**Owner:** Mary Thuo (Agency Governance, 00) · coordinated by **Presence (21)**
**Status:** **S1 — personal profile exists, Company Page BLOCKED, nothing published, zero automation.** This file is the single consolidated LinkedIn source of truth: every LinkedIn decision, strategy, and constraint that was scattered across 6 departments, reconciled in one place.

> **Reading order:** `GLOBAL_OS.md` → `21_Presence/PRESENCE_OS.md` → `21_Presence/CONTENT_DISTRIBUTION_ENGINE.md` → **this file.**
> **Actual posts** (first two weeks, drafted 2026-08-09): [`LINKEDIN_LAUNCH_CONTENT.md`](LINKEDIN_LAUNCH_CONTENT.md).
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
| **A** — Mary Thuo personal profile | ✅ **Exists and is mature** — real history, connections, professional credentials | owner, 2026-08-08 |
| **B** — "Arika" personal profile | ⚠️ Created, S1, **company-named personal account = policy risk** (§4.3) | tracker §4 |
| **C** — Company Page | 🔴 Not created — but **no longer blocked**: creatable from A (§4.7) | owner, 2026-08-08 |
| Connections | ✅ On A, real. 🔴 On B, effectively none — which no longer matters | owner, 2026-08-08 |
| Posts published | 🔴 **Zero** | — |
| Developer app / API access | 🔴 Not started — must attach to **C**, and be created by an admin of C | tracker §5.1 |
| Postiz connection (the executor) | 🔴 Not connected — 0 channels connected on a live instance | `CONTENT_DISTRIBUTION_ENGINE.md` §2 |
| Executor infrastructure | ✅ **LIVE** — Postiz + Postgres + Redis healthy on Hostinger KVM 2 + Coolify | tracker §4 |
| Content strategy | ✅ Fully written, ⚠️ **not publishable as written** — see §7.7 | `Draft 13` |
| Content brief database (Notion) | ✅ Built, **empty**; has a `LinkedIn` platform option | `CONTENT_OS.md` §10 |
| Launch date | 🔴 Never set — open owner decision since 2026-06-30 | `GO_LIVE_CHECKLIST.md` item 14 |

**The honest summary (revised 2026-08-08):** the infrastructure is ahead of the account and the strategy is ahead of both — but the account situation is better than it looked. A mature founder profile already exists; it just wasn't being counted as the agency's asset. The blocker was never connections, it was **which identity does the work** (§4).

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

## 4. Identity architecture — three identities, one system

**Revised 2026-08-08 (owner input).** An **established personal profile exists** — Mary Thuo's own, carrying real history, connections, and professional credentials — and the Company Page can be created from it. The previous pass assumed the only available profile was the brand-new connectionless one, which made connections the gate on everything. That assumption was wrong, and most of the blocking chain dissolves.

### 4.1 The three identities in play

| | Identity | What it is | State |
|---|---|---|---|
| **A** | **Mary Thuo — personal profile** | The real founder. Established, connected, credentialed | ✅ exists, mature |
| **B** | **"Arika" — personal profile** | A company-named *personal* account — ✅ **confirmed by owner 2026-08-08**: opened under the agency name, not a person's name | ⚠️ exists, S1, **policy risk** |
| **C** | **Arika Agency — Company Page** | The institutional entity | 🔴 not created |

### 4.2 The structural fact that decides the arrangement

**A LinkedIn Company Page never has its own login.** It is not an account — it is an object administered by personal profiles. Its creator becomes **Super Admin**, and every post, comment, and setting change is executed by a human acting through their own profile. Additional admins can be added (Super Admin · Content Admin · Curator · Analyst), but there is no credential set that *is* the Page.

So "the agency should eventually have its own LinkedIn account" is not a state LinkedIn offers. The Page **is** the agency's own presence — it just runs on a person's hands, permanently. The only real question is whose.

### 4.3 ⚠️ Identity B is a liability, not an asset

LinkedIn's User Agreement requires a personal profile to represent a **real natural person**. Company-named personal profiles are a standing removal category — this is not an edge case, it is one of the patterns LinkedIn actively polices. Three consequences:

1. **B can be restricted or removed at any time**, without warning, and with no history worth appealing for.
2. **If B were the Super Admin of the Page, a removal orphans the Page** — the asset the entire API path depends on, stranded behind a dead profile.
3. **There is no supported profile → Page conversion** on LinkedIn (unlike Facebook). B cannot become C. Its only outcomes are: renamed to a real person who will actually use it, or closed.

B also splits the effort: every hour spent warming it is an hour not spent on A, which is already warm.

### 4.4 Recommended architecture

```
  A · Mary Thuo (personal)                    C · Arika Agency (Company Page)
  ─────────────────────────                   ──────────────────────────────
  The founder voice          ──creates──►     The institutional entity
  Opinion · narrative                         Proof · offers · careers
  Manual, human                               Engine-published (Postiz)
  Super Admin ───────────────admins──────►    Developer app lives here
  Verified @arikaagency.com ──verifies──►     "a real person operates this"

  B · "Arika" (personal) ──► retire
```

**A is the engine; C is the infrastructure.** That ordering is not a compromise — it is what the platform rewards and what this repo's own doctrine already says: *"founders are bought before agencies"* (`PRESENCE_OS.md` §3.2). Personal profiles substantially out-reach Company Pages organically; the Page earns its keep as the entity that holds the dev app, verification, employees, ads, and institutional proof.

**Your instinct to link the personal profile to the agency as founder is exactly right** — and LinkedIn has a purpose-built mechanism for it: **workplace verification**. Listing Arika Agency as current experience and verifying it via a company-domain email produces a verified badge on your profile stating you work there. For a 0-client agency, "a real, credentialed person demonstrably operates this" is the scarcest credibility asset available, and it is free.

### 4.5 Merits & demerits — the three arrangements

| Arrangement | Merits | Demerits |
|---|---|---|
| **A creates + admins C; B retired** ⭐ *recommended* | Page gate clears now, not in 4–7 weeks · existing connections + credentials transfer credibility instantly · highest organic reach · workplace verification available · one identity to maintain · no policy exposure | Founder's personal network now sees business content · founder must actually show up (cannot be fully delegated) · founder's opinions become agency positions (Legal Class C) · single Super Admin = single point of failure |
| **Keep both A and B, plus C** | Preserves whatever B has accrued · nominally separates "personal" from "brand" voice | B stays a removal risk indefinitely · **doubles** warm-up, posting, and engagement load on a solo operator · the separation is illusory — C already *is* the brand voice, so B duplicates it · confuses the audience about which identity to follow |
| **B creates + admins C; A stays separate** | Keeps founder's personal network untouched | ❌ **Do not do this.** B may not clear the Page gate at all · orphans C if B is removed · forfeits the credentials that make the agency credible · the dev app, and therefore the whole engine, would hang off the weakest identity |

**On the demerits of the recommendation — they are real, and worth naming rather than waving past:**

- **Entanglement.** Your personal network becomes an agency audience. If the agency is ever sold or wound down, the Page transfers; the personal audience does not. That is the actual price of founder-led, and it is normally worth paying at this stage.
- **Delegability ceiling.** A founder-led channel cannot be handed to a hire later without losing most of its reach — this is precisely the single-point-of-failure question HR (11) owns (`hr-owner-sustainability`). Worth logging there rather than discovering it at the first hire.
- **Claims exposure.** Anything you assert from A about the agency is an agency claim, Class C, substantiable-or-silent — the same rule as §9, not a lighter one because it's "personal."
- **Succession.** One Super Admin is a single point of failure for the Page *and* the dev app. Add a second Super Admin the moment a second trusted person exists.

### 4.6 What lives where

| | **A — founder profile** | **C — Company Page** |
|---|---|---|
| Content | Opinion Stand, Narrative Lesson, Founder Thinking — the "building in the open" voice (§7.7) | Frameworks, Insights, Education, Proof (when it exists), offers, careers |
| Posting | **Manual, human.** Never fully automated | **Engine-published** via Postiz once connected |
| Engagement | All of it — comments and DMs happen here | Light; reshare and amplify |
| Connections | The connection strategy (§6) runs here | Followers, invited from A |
| Automation risk | High — automating a founder voice reads false *and* flags | Low — Pages are the intended automation surface |

This split is not just aesthetic: it means the distribution engine drives the Page while the founder voice stays human, which satisfies the anti-flag doctrine and the authenticity requirement with the same decision.

### 4.7 The revised blocking chain

What remains once A is doing the work:

```
A: verify profile + list Arika Agency  →  CREATE PAGE (C)  →  warm C manually  →  dev app  →  API/Postiz  →  engine test
   (days, not weeks)                      (days)              (1–2 weeks)         (needs C)    (needs app)   (12 stages)
```

- **Page-creation gates** (verify live at creation time — platform rules change and this repo does not treat vendor rules as permanent): profile 7+ days old · profile photo · multiple connections · minimum profile strength · **current position at Arika Agency listed** · company-domain email for verification. A plausibly clears all but the last two already; both are same-day fixes.
- ~~The mailbox is the critical path.~~ ✅ **Resolved 2026-08-08 (owner): all company emails are active.** `mary.thuo@arikaagency.com` receives, so Page-creation verification and workplace verification are both unblocked. **Page creation is now a same-day action.**
- **⚠️ The Page still needs its own warm-up.** C is a brand-new asset on day one. Creating a Page and immediately attaching a developer app and an auto-poster is the classic ban pattern the tracker's rule 6 exists to prevent (*one new asset at a time*). Post to C manually for 1–2 weeks before the dev app.
- **Page → dev app → Postiz** is unchanged: the app must attach to C and be created by an admin of C; products *Sign In with OpenID Connect* + *Share on LinkedIn* (+ *Advertising API* for token refresh); redirect `https://<postiz-domain>/integrations/social/linkedin`; creds into Coolify. ⚠️ Known Postiz OAuth *"Not enough scopes"* bug.

**Net effect: the runway shortens from 4–7 weeks to roughly 2–4**, and the long pole moves from *"earn enough connections"* to *"warm the Page and survive the OAuth setup."*

---

## 5. The warm-up runway (S1 → S6)

Extends the tracker's stage model with LinkedIn-specific actions. **Golden rule stands: no S4/S5 until S2 and S3 genuinely clear.** Automation before warm-up is the flag.

> **⚠️ Revised 2026-08-08 — this runway now applies to two assets on different clocks.**
> **Profile A (Mary Thuo)** is already warm: it likely sits at **S3 or beyond** for account-maturity purposes, so S2 below collapses to a same-day profile-completion pass and the connection ramp becomes optional acceleration rather than a gate.
> **Page C (Arika Agency)** is a **brand-new asset from the day it is created** and runs its own S2 → S3 → S4 cycle. The dev app hangs off C's maturity, not A's. Do not let A's maturity tempt you into wiring an auto-poster to a one-week-old Page — that is the exact "one new asset at a time" violation (tracker §3 rule 6).

### S2 — Humanize & verify *(days 1–3, unblocked, do now)*

*For profile A this is a completion pass, not a build: most of it likely already exists. The two rows that matter most are the current position and the verified company email — those are the Page gates.*

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

### S4 — Company Page *(created from A)*
Create C from profile A — **A becomes Super Admin** → complete the Page fully (logo, tagline, About, `arikaagency.com`, industry, specialties, location) → **verify your workplace** on A against the Page using the company email (this is the "a real person operates this" badge, §4.4) → invite A's existing connections to follow → **post to C manually for 1–2 weeks** before any dev-app work. Add a second Super Admin as soon as a second trusted person exists (§4.5, succession). **Class 3 sign-off:** the Page is a public-facing brand asset (`PRESENCE_OS.md` §5).

### S5 — Developer app + Postiz *(gated on C's maturity, not A's)*
Dev app attached to the Page → products (Sign In w/ OpenID Connect, Share on LinkedIn, Advertising API for token refresh) → redirect URI → creds into Coolify → OAuth → channel added. Register in TechStack with `verified_at` (`TECHSTACK_OS.md` discipline). **Do not create the app the same day the Page is created** — one new asset at a time (tracker §3 rule 6).

### S6 — Verified live
One real post published **through the engine** — Phase 4 of the build order, the first end-to-end test of all 12 stages. Only then does `verified_at` get set.

**Realistic runway: ~2–4 weeks from today to S6** (revised down from 4–7 on 2026-08-08 — profile A's existing maturity removes the connection-building gate). The remaining calendar time is the Page's own warm-up, which cannot be compressed — which is precisely why the content work should run at full intensity during it.

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

### 7.8 Profile A — humanization pack (paste-ready)

Draft 13's three bios rest on fabrications and **cannot be used** (§7.7). Below is final copy built only on facts this repository confirms. **Paste it; don't compose at the keyboard.**

**Headline** *(220 char limit; this is 79)*
```
Founder, Arika Agency | Revenue infrastructure for B2B SaaS — systems, not activity
```

**About** *(2,600 char limit)*
```
I build revenue infrastructure for B2B SaaS.

Not campaigns. Not funnels. The connective system underneath them — the thing that
decides whether marketing, sales, automation and operations produce one number
together, or four reports separately.

The pattern I keep finding isn't a marketing problem or a sales problem. It's a
revenue architecture problem: functions built separately, then asked to perform as
a system nobody actually designed.

I'm building that system for my own agency first, in public — including the parts
that don't work yet. If you want to know what a revenue operating system actually
takes to build, the decisions it forces and the things that quietly break, that's
what I write about here.

What I work on:
— Revenue architecture and revenue operations
— Marketing, sales and acquisition systems
— Workflow automation and AI enablement
— CRM as revenue intelligence, not a filing cabinet
— Diagnostics: what to fix before you hire, buy, or launch

Before you hire, audit. Before you buy, diagnose.

Focused on B2B SaaS. Based in Kenya.
mary.thuo@arikaagency.com
```

⚠️ **Two lines to check before pasting:** *"I build revenue infrastructure for B2B SaaS"* states what the business does, not a results claim — that's the line to keep honest. And there is deliberately **no** "trusted by", no client count, no metrics (§9).

**Experience entry** — the Page-creation gate depends on this:

| Field | Value |
|---|---|
| Title | `Founder` |
| Company | `Arika Agency` — free text is fine before the Page exists; once created, LinkedIn associates it and pulls the logo |
| Employment type | Self-employed |
| Location | Kenya |
| Start date | ⚠️ Owner input — do not invent |
| Current role | ✅ **Must be ticked** — this is the gate |

**Rest of the humanization checklist (S2):**

| Item | Value / spec |
|---|---|
| Profile photo | Real, current, face clearly visible. Non-negotiable — the "real person" signal and a Page-creation input |
| Background banner | 1584×396, from the Canva brand kit (`GO_LIVE_CHECKLIST.md` item 20). ⚠️ Canva connector unauthorised — Design (19) or manual export |
| Custom URL | `linkedin.com/in/marythuo` (or nearest available). Permanent in practice; claim early |
| Email verified | `mary.thuo@arikaagency.com` — active as of 2026-08-08 |
| Phone verified | Account-trust signal; reduces restriction risk |
| Featured section | Leave empty until there is something substantiable to feature |
| Workplace verification | **After** the Page exists — verify via company email. This is the badge that says a real person operates the agency (§4.4) |

**Alternate headlines** if the recommended one doesn't sound like you:
- `Founder, Arika Agency | I build the revenue operating system most companies assume they already have`
- `Founder, Arika Agency | Before you hire, audit. Before you buy, diagnose`

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
- **Agents never impersonate humans** (adopted 2026-08-08, §11.2). Agents prepare and orchestrate assets for legitimate human and company identities — they do not operate fictional employee profiles, and no LinkedIn identity may exist that does not correspond to a real person or the real company. This is both a LinkedIn User Agreement requirement and the reason profile B is being retired (§4.3).
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

## 11. The agentic layer — reconciled against what already exists

**Added 2026-08-08.** The owner relayed an external-AI architecture proposal for a "LinkedIn Agentic Operating System" (orchestrator + intelligence/strategy/governance agent tiers, a content registry, five permission levels, and Claude/Foxy/OpenArt/Higgsfield tool roles). It was written without sight of this repo. Reconciled below rather than adopted or discarded wholesale.

### 11.1 Already built — do not rebuild

| Proposal element | Already exists as | Note |
|---|---|---|
| "LinkedIn shouldn't live in Marketing — it belongs in Presence/Distribution architecture" | **Presence (21)**, created 2026-07-23 for exactly this reason | ✅ Independent convergence — good validation |
| Two-layer identity: founder profile + Company Page; personal account as *administrator*, not identity | **§4** of this file, decided 2026-08-08 | ✅ Same conclusion |
| Orchestrator → intelligence/construction/governance → production → approval → publish → performance → feedback | **Content Distribution Engine**, 8 layers (L0–L7) + 12 stages | ✅ Exists and is *more* specified — the CDE also has a rate governor, retry/dead-letter, and an idempotency spine the proposal lacks |
| Human approval gate before publishing | **Gate 2 (Pre-Publish) + Class 3 sign-off** | ✅ Exists, and is stricter |
| Five permission levels (intelligence → construction → approval → publishing → feedback) | **Constitution §5's 5-tier risk classification** + `AUTOMATION_APPROVAL_MATRIX.md` | ✅ Map onto these; a parallel permission scheme would fragment governance |
| Per-post metadata registry | **Notion content-brief database** — real, built 2026-07-03, with the field names already in use | ✅ Use the real schema; the proposal's field names are a rename of it |
| Autonomous vs. approval-required content classes | **CDE §5 template-level approval** — approve a content *type* once, only new/flagged items get fresh review | ✅ Same mechanism, already designed |

### 11.2 Genuinely new — worth adopting

1. **The institutional brief format.** The proposal's worked example — personal profile carries the *argument* ("most companies don't have a marketing problem, they have a revenue architecture problem"), Page carries the *institutional artifact* ("Revenue Architecture Brief #004" with framework, evidence, model, methodology, offer, CTA) — is a real addition. This file had the founder/Page *split* (§4.6) but no signature Page format. A **numbered brief series** is citable, compounds, and feeds Presence's own "research repositories → citations → authority" hidden layer (`PRESENCE_OS.md` §3.2). **Adopted** as the Page's signature format (§12).
2. **Agents never impersonate humans.** Agents prepare and orchestrate assets for legitimate human/company identities; no AI-operated fictional employee profiles, ever. Implied by §4.3 but never stated as a rule. **Adopted** into §9 governance.
3. **Naming which content classes could eventually publish without per-item review** (curated observations, evergreen insights, approved recurring series, data updates) vs. which never can (opinions, new positions, announcements, pricing/offers, client material, performance claims). Useful specificity for the template-level approval mechanism that already exists.

### 11.3 🔴 Conflicts with decisions already made

1. **Higgsfield was explicitly rejected.** `GO_LIVE_CHECKLIST.md` item 25 (2026-07-03): *"OpenArt chosen over imagine.art and Higgsfield"* — a closed vendor decision with a live, verified connection behind it. Reintroducing Higgsfield is a **supersession**, not an addition: it needs a `techstack-inventory-registrar` decision with reasoning, not a silent slot in a diagram.
2. **Foxy is not in the inventory, and its proposed role is already filled.** No tool called Foxy appears anywhere in `TECHSTACK_OS.md`, and I can't identify which product is meant — so it cannot be assumed. More importantly, the "workflow/execution coordinator" role the proposal assigns it **is Postiz's job** (CDE layer L6), already deployed, healthy, and paid for on the Hostinger VPS. The external proposal never mentions Postiz because it didn't know it existed. Adding Foxy either duplicates Postiz or replaces it — either way it is a decision, not a diagram. ⚠️ *What is Foxy?*
3. **"360° Growth Revenue Agency" is a third positioning string.** Confirmed in the repo: the vision is *"a 360° Cognitive Revenue Operating System"* (`AGENCY_VISION.md`) and the Offer-side positioning is *"Revenue Infrastructure Partner"* (02). A third string introduced in a side conversation should not silently become the Page's official identity — see decision L10.
4. **"All of the above" for audience contradicts the confirmed ICP.** Sector (01) holds an owner-curated 3-tier B2B SaaS ICP *and an explicit Anti-ICP* (`SECTOR_OS.md` §1). A Page addressed to every decision-maker in every sector is addressed to no one — and it contradicts the N in DRAGON (niche-orientation) that the LinkedIn playbook is built on. **The reconciliation that saves it:** founders, CEOs, marketing, sales, ops, investors and partners are the **buying committee inside a Tier 1/Tier 2 account**, not a list of separate markets. Broad *roles*, narrow *accounts*. That is legitimate and is how the Page should read.
5. **L0–L9 is a third content taxonomy.** This repo already resolved a 3-way pillar conflict and settled on **7 canonical pillars × 7 Content Houses**, plus a funnel-stage field. A ten-level hierarchy is a third axis over the same content. Map instead: L0–L2 → narrative/beliefs (Branding 12 + Content narrative architecture) · L3–L5 → the 7 pillars · L6–L7 → the Conversion and Proof Houses · L8 → Presence Engagement · L9 → the existing funnel-stage field. **Do not adopt as a new axis.**
6. **⚠️ The agent layer cannot run.** All 106 agents in this repo are unrunnable — `ANTHROPIC_API_KEY` is unset (`PRESENCE_OS.md` §9). Specifying twelve new LinkedIn agents would be the fifth time this repo built structure ahead of reality. The engine's existing agents already cover the roles; wire the account first, run one real packet, *then* extend the roster against evidence.

### 11.4 The honest sequencing call

The proposal's architecture is broadly right and largely already yours. But the binding constraint today is not architectural — it is that **the Page does not exist and nothing has ever been published.** An 80/20 agentic production system has nothing to produce for, no performance data to feed back, and no approved template to approve against. Build the Page, publish manually, run one packet end-to-end through the existing engine, and let the agent layer be specified by what actually breaks.

---

## 12. Company Page — master specification

**Status: ready to execute.** All company emails are active (2026-08-08), so every gate on Page creation is clear. Fields below are draft-ready where the repo confirms the fact, and flagged where it does not. **Do not improvise the flagged ones at the keyboard** — they are brand decisions.

| Field | Value | State |
|---|---|---|
| **Page name** | `Arika Agency` | ⚠️ Should match the registered legal entity — confirm with Legal (10); the repo has no registration record |
| **Public URL** | `linkedin.com/company/arika-agency` | Claim early; permanent |
| **Website** | *(leave blank at creation)* | 🔴 **Verified 2026-08-08: `arikaagency.com` has no A record and does not resolve.** Domain is registered with DNS at Zoho, but nothing is served at the apex; the site exists only on a `.vercel.app` subdomain, uncommitted (`PRESENCE_OS.md` §3.2). Shipping it is a **DNS + deploy** task (EE 20), not a domain purchase. Field is optional and editable later — leave it empty rather than point at a dead host |
| **Industry** | `Business Consulting and Services` | ⚠️ Decision — fits "revenue infrastructure" better than `Marketing Services`, which reads as a channel vendor |
| **Company size** | `1 employee` / `1–10` | Honest. Solo + AI (`HR_OS.md`) |
| **Company type** | Privately Held | — |
| **Founded** | — | ⚠️ Owner input; do not invent |
| **Location** | Kenya | ⚠️ City not recorded in the repo — owner input |
| **Tagline** (≤120 chars) | See options below | ⚠️ Class 3 brand decision |
| **About** (≤2,000 chars) | See draft below | ⚠️ Class 3 brand decision |
| **Specialties** (≤20) | Revenue architecture · revenue operations · marketing systems · sales systems · workflow automation · AI enablement · CRM architecture · partner ecosystems · revenue audits · business operating systems | Drawn from the confirmed offer catalogue (02) |
| **Logo / cover** | From the Canva brand kit | Brand kit exists (`GO_LIVE_CHECKLIST.md` item 20, done) — Design (19) to produce at spec (300×300 · 1128×191) |
| **Custom button** | `Visit website` | Gated on the website blocker above |

**Tagline options:**
- `Revenue infrastructure for B2B SaaS. Systems, not activity.`
- `The revenue operating system most companies assume they already have.`
- `Marketing, sales, automation and operations — engineered as one revenue system.`

**About — draft (substantiable only; no clients, no team, no results):**

> Most companies don't have a marketing problem, a sales problem, or an automation problem. They have a revenue architecture problem — functions that were built separately and are asked to produce a single number together.
>
> Arika Agency builds revenue infrastructure for B2B SaaS: the connective system across marketing, sales, automation, partnerships and operations that turns disconnected activity into a machine that can be measured, diagnosed and scaled.
>
> We publish what we learn building it — frameworks, diagnostics and revenue architecture briefs — because the thinking is the proof.
>
> Before you hire, audit. Before you buy, diagnose.

⚠️ **Honesty constraints on this copy** (§9): no client counts, no results, no "trusted by", no team language, no ™. Every sentence above is substantiable today.

**Signature Page format — the brief series** (adopted from §11.2): numbered institutional artifacts, e.g. *Revenue Architecture Brief #001*, each carrying framework → evidence → model → methodology → perspective → CTA. This is what the Page publishes that the founder profile cannot: durable, citable, institutional. Start at #001 and never break the numbering.

**Founder ↔ Page relationship in practice:** profile A argues the position; the Page publishes the artifact; A reshares the Page's brief with a personal take. One strategic universe, two communication roles (§4.6).

---

## 13. Open decisions — owner input required

| # | Decision | Why it's blocking | Recommendation |
|---|---|---|---|
| L1 | **Confirm the LinkedIn launch date** (open since 2026-06-30, `GO_LIVE_CHECKLIST.md` item 14) | The one decision that starts the 4–7 week runway | Start S2 immediately; S3 posting begins within 3 days |
| L2 | ~~Profile identity: personal name or "Arika"?~~ | — | ✅ **Resolved 2026-08-08 (owner).** Profile **A (Mary Thuo)** is the founder voice and creates/admins the Page; the brand lives on Page **C**. Architecture in §4 |
| L7 | **What happens to profile B ("Arika")?** | It is a standing policy risk (§4.3) and splits a solo operator's effort; it cannot become the Page | **Retire it.** No profile→Page conversion exists — so either close it, or rename it to a real person who will genuinely use it. Do not grow it |
| L8 | **Second Super Admin for the Page** | One Super Admin is a single point of failure for the Page *and* the dev app hanging off it | Defer until a second trusted person exists — but log it now with HR (11)'s single-point-of-failure map (`hr-owner-sustainability`) rather than discovering it at the first hire |
| L9 | **Accept founder-led entanglement?** | Founder-led means the personal audience never transfers with the agency, and the channel can't be delegated later without losing its reach (§4.5) | Accept it at this stage — the credibility is worth more than the optionality — but decide it consciously, not by default |
| L10 | **Official positioning string for the Page** — "360° Growth Revenue Agency" vs. the confirmed "360° Cognitive Revenue Operating System" (vision) vs. "Revenue Infrastructure Partner" (Offer 02) | It becomes the Page name/tagline and then propagates everywhere; three competing strings is how positioning dies | Page **name** = the legal entity (`Arika Agency`); positioning lives in the **tagline**, drawn from the confirmed pair — not a fourth string invented in a side conversation |
| L11 | **Audience: "all of the above"?** | Contradicts Sector's owner-curated 3-tier ICP *and* its explicit Anti-ICP | Reframe as **broad roles, narrow accounts**: the whole buying committee *inside* Tier 1/Tier 2 B2B SaaS accounts (§11.3 item 4) |
| L12 | **Higgsfield — reinstate or keep rejected?** | It was explicitly rejected in favour of OpenArt on 2026-07-03; the diagram reintroduces it | If genuinely wanted for motion, run it as a **supersession** through `techstack-inventory-registrar` with reasoning — not a silent addition |
| L13 | **What is Foxy, and does it replace or duplicate Postiz?** | The role it's assigned is already filled by a deployed, healthy, paid executor | Identify the product first; register in TechStack; then decide replace-vs-duplicate. Default: **Postiz stays** |
| L14 | **Website blocker** — `arikaagency.com` is subdomain-only and uncommitted | The Page's primary CTA points at it | EE (20) dependency; either ship the domain or launch the Page with a different primary button |
| L3 | **Voice selection** — headline + About from §7.8 | Class 3 public-facing; gates everything | Build-in-the-open; it's the only one fully substantiable today |
| L4 | **DRAGON conflict** (unresolved since 2026-07-14, `CONTENT_OS.md` §10) — Dialogue/Relatability/Authenticity/Growth/Opinion/Niche vs. Diagnosis/Revenue-Logic/Architecture/Growth-Systems/Operational-Intelligence/Navigation | LinkedIn is where DRAGON is actually applied; the ambiguity lands here first | Keep both at different altitudes (LinkedIn DRAGON = post construction; Realignment DRAGON = operating philosophy) and **name them distinctly** — same resolution pattern as the 3-way narrative reconciliation |
| L5 | **Is `mary.thuo@arikaagency.com` a live mailbox?** | Company-domain email is a likely Page-verification requirement | Verify before attempting Page creation |
| L6 | **Proof House (15%) has nothing to fill it** | 0 clients, 0 case studies | Reallocate to Insights/Founder Thinking until real proof exists — do not manufacture |

---

## 14. Decision Log

- **2026-08-09 — Manual operation unblocked; humanization pack made paste-ready (§7.8).** Owner asked to clear whatever is blocking manual functioning. Audit found **nothing structural blocking it** — only 4 owner decisions (registration status, approve the six posts, retire profile B, founded date + city) and ~90 minutes of profile/Page setup. Everything still red is deliberately *not* on the manual path: the executor connection (1–2 weeks out by design), the Notion connector (unauthorised — the repo file is the interim queue-of-record), the website (leave the field blank), and the agent layer (unrunnable, and unnecessary for manual). Voice decision **L3 collapses into approving the six drafted posts** rather than being decided in the abstract. — Claude Code (Opus 5)
- **2026-08-08 — `arikaagency.com` verified non-resolving (live DNS check).** No A record on the apex; curl cannot resolve the host while a control host returns 200. Domain is registered, DNS at Zoho. Confirms decision L14 as a real blocker and narrows it: the site needs a **DNS record + deploy**, not a domain. The Page launches with the Website field empty. Verified rather than assumed, per TechStack discipline. — Claude Code (Opus 5)
- **2026-08-08 — Page creation form is narrower than the master spec.** LinkedIn's create-Page form requires only **Name · URL · Industry · Organization size · Organization type** plus the authorized-representative attestation; Website, Logo and Tagline are optional at creation. Everything else in §12 (About, specialties, location, founded year, cover, custom button) is added afterwards via **Edit page**. — Claude Code (Opus 5)
- **2026-08-08 — All company emails confirmed active (owner).** Removes the last gate on Page creation and on workplace verification. **Page creation is now a same-day action**; the critical path moves to the Page's own warm-up and the OAuth setup. — Claude Code (Opus 5)
- **2026-08-08 — External "LinkedIn Agentic OS" proposal reconciled, not adopted wholesale (§11).** Written without sight of this repo; ~7 of its elements already exist here (Presence department, the two-layer identity, the 8-layer/12-stage engine, Gate 2, the risk-tier permission model, the real Notion schema, template-level approval). Three adopted as genuinely new: the **numbered institutional brief series**, the **agents-never-impersonate-humans rule**, and the named autonomous-vs-approval content classes. Six conflicts logged as owner decisions L10–L14 plus the L0–L9 taxonomy rejection — notably **Higgsfield (explicitly rejected 2026-07-03)** and **Foxy (unidentified, and its role already filled by the deployed Postiz executor)**. Declined to specify twelve new LinkedIn agents: all 106 existing agents are unrunnable (`ANTHROPIC_API_KEY` unset), and the binding constraint is an unpublished Page, not missing architecture. — Claude Code (Opus 5)
- **2026-08-08 — Company Page master specification written (§12), ready to execute.** Draft-ready fields where the repo confirms the fact; flagged where it does not (founded date, city, legal name, industry category). Surfaced a real blocker the proposal missed: **`arikaagency.com` is subdomain-only and uncommitted**, so the Page's primary CTA has nowhere good to point (decision L14, EE 20 dependency). — Claude Code (Opus 5)
- **2026-08-08 — Identity architecture established; the blocking chain largely dissolves.** Owner disclosed an **established personal profile (Mary Thuo)** capable of creating the Company Page — the 2026-08-07 pass had assumed the connectionless "Arika" profile was the only one available, which made connections the gate on everything. Corrected architecture (§4): **A (founder) creates and admins C (Page); B ("Arika") retired.** Grounded in the structural fact that a LinkedIn Page has no login of its own and is always operated by personal profiles — so *"the agency gets its own account"* is not a state the platform offers; the Page is that presence, permanently run by a person. Runway revised **4–7 weeks → ~2–4**; the long pole moves from *earn connections* to *warm the Page + survive OAuth*. Founder-led demerits named rather than waved past: entanglement, delegability ceiling, claims exposure, single-Super-Admin succession risk. — Claude Code (Opus 5)
- **2026-08-08 — Profile B flagged as a liability.** A company-named *personal* profile violates LinkedIn's real-natural-person requirement and is a standing removal category; had it become Super Admin, its removal would orphan the Page and the dev app with it. No profile→Page conversion path exists. Recommended retirement, logged as open decision L7. — Claude Code (Opus 5)
- **2026-08-08 — The Page carries its own warm-up clock.** A's maturity does *not* transfer to C: a newly created Page wired straight to a developer app and auto-poster is the "one new asset at a time" violation (tracker §3 rule 6). S5 is gated on **C's** maturity, not A's. — Claude Code (Opus 5)
- **2026-08-07 — LinkedIn dossier created; all LinkedIn material consolidated.** Everything LinkedIn across `04_Content` (Draft 13, CONTENT_OS, PIL), `03_Marketing` (§10 channel role), `01_Sector` (ICP + decision-maker registry), `13_Tech_Stack`, `00_Agency_Governance` (GO_LIVE item 14, OWNER_INPUT item 44) and `21_Presence` (PRESENCE_OS, CDE, tracker) pulled into one file. No capability re-owned — Content still owns content, Marketing distribution, Sector the ICP; this is the coordination layer Presence (21) exists to be. — Claude Code (Opus 5)
- **2026-08-07 — 🔴 Draft 13's first-person content ruled unpublishable as written.** Its example posts and all three bios assert a founder history that did not happen (lost 40% of revenue, missed payroll/$80K, $50K on sales training, 4 years building the system, "Revenue Reality™", clients who fired us). Publishing them would breach no-silent-invention, Gate 2's substantiation rule, and "Never publish: Authority Without Evidence." **Structures kept, claims struck**; a substantiable "building in the open" voice proposed in its place (§7.7–7.8). Owner decision L3. — Claude Code (Opus 5)
- **2026-08-07 — Connection ramp supersedes Draft 13's 30–50/week for the warm-up period.** Draft 13's figure is safe for an aged account, restriction-triggering for a 1-week-old one; the §5 ramp reaches it by ~week 3. Anti-flag doctrine wins where the two disagree. — Claude Code (Opus 5)
- **2026-08-07 — The blocking chain named** (presence → connections → Page → dev app → API → engine test). Establishes that connections are not a vanity metric but the literal gate on the agency's position-1 platform and its first full engine test. — Claude Code (Opus 5)

## 15. Honest state

*(revised 2026-08-08)* LinkedIn has published **nothing for the agency**. What exists is a mature founder profile that has never been pointed at the agency, a company-named second profile that should not exist, no Company Page, no developer app, and no channel connected to a live and healthy executor sitting idle waiting for it. The correction this session made is that the agency was treating its strongest LinkedIn asset — a real, credentialed, connected founder — as if it were separate from the agency's presence, and warming a brand-new empty profile instead. The strategy is thorough and mostly sound — and was written for a founder who doesn't exist yet, which is the single most important thing this file corrects. What is genuinely ready: the frameworks, the pillar/house structure, an empty Notion brief database, a running Postiz instance, and a real ICP with real buyer intelligence to aim connections at. What is genuinely missing: a photo, a headline, ten posts, and a hundred connections — none of which any agent can do for the owner, and all of which unblock everything else.
