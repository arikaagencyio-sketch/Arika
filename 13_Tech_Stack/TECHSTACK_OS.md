# Tech Stack — Department OS

**Department:** Tech Stack (13)
**Position in flow:** Horizontal support layer — provides tooling/infrastructure to all other departments; reports into Agency Governance (00).
**Mandate:** Own the canonical inventory of tools/software the agency actually uses (CRM, project management, hosting, email, AI platforms, APIs), plus integration and access records for them.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Tech Stack is a **newly created department** — confirmed as a real gap during workspace exploration. The repo contains two aspirational software builds (Finance's `finos-plugin/` and Branding's `bois/`) but no canonical list of what tools the agency actually runs on day-to-day.

## 2. Status

**A 30-row inventory with 3 agents (2026-07-15).** No raw draft archive exists for this department specifically. Note: the three code scaffolds (`09_Finance/finos-plugin/`, `12_Branding/bois/`, `19_Design/design-plugin/`) — and `arika-runtime/` — are software the agency is **building**, not a record of tools it **uses**; do not conflate the two. See `00_Agency_Governance/GO_LIVE_CHECKLIST.md` for the implementation sequence.

*(This section previously read "Skeleton, with its first 3 real confirmed tools (2026-06-30)" — stale by 27 rows.)*

### 🔴 2026-07-15 live audit: 4 of §3's rows were false, in 4 different directions

This department **invented** the right discipline and then never scheduled it. §3's own rule, written when Notion and OpenArt were first registered:

> **"verified via a live API call rather than assumed from tool availability alone"**

Exactly right — and every row carries an **activation date with no expiry**. On 2026-07-15 every connectable tool was re-checked with a free, read-only call. Four rows had rotted:

| Tool | §3 claimed | Reality (live-verified 2026-07-15) | Direction |
|---|---|---|---|
| **Canva, OpenArt, Relume** | *"Confirmed real and connected"* | **All three unauthenticated.** | optimistic |
| **Zoho Books** | *"Premium Trial — **revisit before trial expires**"* | **`is_trial_expired: true`.** The row predicted its own failure; nobody revisited. | optimistic |
| **ClickUp CRM** | *"not yet implemented"* | **Fully built** — 5 CRM_SCHEMA lists, real stage statuses, real custom fields | **pessimistic** |
| **KIE.ai credits** | *"62 of 80"* | **44.** The docs logged one image's spend (18) while describing two. | optimistic |

**Drift is not always optimistic** — the ClickUp row understated reality by an entire working CRM. A department that thinks it has less than it does under-uses what it paid for.

**This is the third department in a row with the same disease**, and the pattern is now conclusive: Automation (16)'s routine was dead 11 days while docs said "LIVE"; Tech Stack's connectors and trial rotted while docs said "connected". **The repo records decisions with activation dates and never re-checks them.** The convention lives here, so the fix lives here: `techstack-connection-verifier` (§5) is the cron this department's own rule always implied.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| ClickUp | CRM + project management platform — implements the Lead/Opportunity/Client/Partner pipeline defined in `00_Agency_Governance/CRM_SCHEMA.md` via ClickUp Lists, custom fields, and pipeline views; free tier available | **🟢 Confirmed real, connected, AND BUILT — live-verified 2026-07-15.** Supersedes Zoho CRM (confirmed 2026-06-30, superseded 2026-07-01). **This row said "not yet implemented" until 2026-07-15 and was badly wrong** — the CRM is a real, faithful implementation. Live: workspace `90152608658` → space **Sales CRM** (`901511301824`) → folder **Arika Agency CRM** (`901516593347`) → 5 lists = **Lead · Opportunity · Client · Engagement / Project · Partner**, matching CRM_SCHEMA's core objects. The `Lead` list's own description cites `CRM_SCHEMA.md` by name; its statuses are the schema's real stage workflow (`new → contacted → qualified → opportunity → closed won/lost`); its 6 custom fields are real (`Source` dropdown with inbound/outbound/referral/partner/event, `ICP Fit Score`, `Contact Email`, `Contact name`, `Company`, `Source Campaign`). **Zero tasks** — built, never used. **3 real members**: `support@arikaagency.com`, `growth@arikaagency.com`, `mary.thuo@arikaagency.com`. **⚠️ Two conflicting CRMs in one space — see the note under this table.** |
| Zoho Books | Accounting/invoicing platform for Finance (09) — invoice generation, expense tracking, and the Project→Invoice handoff (`CRM_SCHEMA.md` "Handoff Points"); connected via claude.ai's Zoho Books connector, exposing direct MCP tools (`create_invoice`, `create_contact`, `list_invoices`, etc.) — no native ClickUp app or Zapier needed | **🔴 CONNECTED BUT THE TRIAL HAS EXPIRED — live-verified 2026-07-15.** `list_organizations` returns **`is_trial_expired: true`**, `plan_name: "PREMIUM TRIAL"`, `plan_type: 0`, `is_trial_period_extended: false`. Org created **2026-06-26**, ID `929138528`, "Arika Agency," Kenya, base currency **KES**, `support@arikaagency.com`, fiscal year starts month 6. **This row itself said "not permanently free — revisit before trial expires." Nobody revisited. It expired.** ⚠️ `isOrgActive: true` still reads true alongside the expired trial — **do not read "active" as "fine."** Re-supersedes QuickBooks (abandoned 2026-07-01: paid subscription/business registration required before authentication, no free tier — which is exactly why the owner came back here for the free tier, and the org is **not** on the free tier, it is on an expired trial). **Real currency decision**: offers priced in USD, invoices issued in KES via a **not-yet-built** conversion calculator. **Owner decision needed: downgrade to Zoho's free tier, pay, or re-open the accounting choice.** Finance (09) and CRM_SCHEMA's Invoice/Revenue Event object both depend on this. |
| Claude (Anthropic API) | Agency-standard LLM backing AI agent execution — confirmed for Finance (09)'s 7-agent roster and Branding (12)'s 20-agent roster; the default choice once Sales (05)/Marketing (03)'s markdown-defined agent rosters get executable runtimes | **Confirmed real (2026-06-30)**, not yet wired — `finos-plugin` and `bois` both still have zero LLM SDK dependency as of this entry |
| Canva | Creative Assembly platform for Design (19) — carousels, video, presentations, ads; premium tier | **🔴 UNAUTHENTICATED as of 2026-07-15** — was *"Confirmed real and connected (2026-07-01) — the only tool in this table actually usable today."* That claim is **14 days stale**: this session's environment reports Canva as requiring authentication before its tools can be used. Re-authenticate via claude.ai connector settings. **Design (19)'s Creative Assembly stage and the "Claude Design" row below both run on this account.** |
| Notion | System-of-record for content briefs (Content, 04) — script/story/caption/visual-direction schema documented at `04_Content/CONTENT_OS.md` §10 | **Confirmed real and connected (2026-07-03)** — verified via a live `notion-get-users` call, real workspace user "Arika Agency" (`arikaagency.io@gmail.com`). Content-brief database itself not yet built — connection exists, schema not yet applied |
| ManyChat | Proposed DM/comment-automation platform for Automation (16)'s Engagement Layer (`16_Automation/AUTOMATION_OS.md` §3-4) | **Proposed (2026-07-01), account not yet created** — no social media accounts (Instagram Business, Facebook Page, X, Pinterest, LinkedIn profile+page, Tumblr) exist yet either; see `00_Agency_Governance/OWNER_INPUT_NEEDED.md` |
| OpenArt | AI image/video generation, enhancement & upscaling vendor feeding Design (19)'s Production Engine (`19_Design/DESIGN_OS.md` §3) — 100+ models incl. GPT Image, Nano Banana Pro, Sora 2, Kling 3.0, Seedance; output handed to Canva for assembly. MCP server: `https://mcp.openart.ai/mcp` | **🔴 UNAUTHENTICATED as of 2026-07-15, AND the credit pool is at 0.** Was *"Confirmed real and connected (2026-07-03) — Free plan, 40 credits… likely a real constraint on production volume."* **Both halves of that warning came true.** All 40 Free-plan credits were spent in one afternoon (2026-07-04, `19_Design/DESIGN_OS.md` §10) and the pool has been at **0** since — which is why Design built the KIE.ai path. The connector now also requires re-authentication. **Doubly unusable: no auth, no credits.** |
| Claude Design | Anthropic's own AI visual-generation product (Opus 4.7, research preview) — describe a visual, Claude generates/refines it; exports directly into Canva | **Confirmed available (2026-07-03)** — included in the owner's existing Claude Pro plan, no separate account/MCP required |
| KIE.ai — Nano Banana Pro API | Direct API access to Google's Nano Banana Pro (Gemini 3 Pro Image) model, feeding Design (19)'s Production Engine (`19_Design/DESIGN_OS.md` §3) as a second image-generation path alongside OpenArt. Real code connector: `19_Design/design-plugin/src/integrations/kie-nano-banana-pro.ts`. Base: `https://api.kie.ai/api/v1` (`/jobs/createTask`, `/jobs/recordInfo`) | **🟢 Confirmed real and connected — re-verified live 2026-07-15: `GET /chat/credit` → `{"code":200,"msg":"success","data":44.0}`. Balance is 44, NOT the 62 recorded everywhere.** Free read-only endpoint, no generation credits spent. Real account (`arikaagency.io@gmail.com`); started at 80. **The 62 figure was an arithmetic error**: `DESIGN_OS.md` §10 records two Nano Banana Pro images generated 2026-07-07 at *"18 credits each"* — 2 × 18 = 36, so 80 − 36 = **44**. The docs logged one image's spend while describing two. **This matters operationally**: `design-production-engine-coordinator` estimates credit spend against this number and was over-counting the budget by a full image. **Runway: 44 ÷ 18 = 2 more images**, then image generation stops agency-wide (OpenArt is at 0). **The only working image path the agency has.** Plain REST API, not an MCP server, so not in `.mcp.json`; auth via `KIE_API_KEY` in `19_Design/design-plugin/.env` (owner-supplied, not committed) |
| KIE.ai — Seedance API | Direct API access to Bytedance's Seedance 1.5 Pro video model, feeding Design (19)'s Production Engine as a second video-generation path alongside OpenArt. Real code connector: `19_Design/design-plugin/src/integrations/kie-seedance.ts`. Same KIE job API base as Nano Banana Pro | **Confirmed real and connected (2026-07-07)** — same KIE.ai account/key/credit balance as the Nano Banana Pro row above (80 credits, live-verified), not a separate credential |
| Relume | **Corrected 2026-07-04**: not a sitemap-generation AI — its actual live MCP surface is a real React/TSX component library (50 categories: navbars, hero sections, pricing, testimonials, FAQ, CTA, forms, etc.), searchable/fetchable as ready-to-use component code, plus a one-time Tailwind/alias setup tool | **🔴 UNAUTHENTICATED as of 2026-07-15.** Was *"Confirmed real and connected (2026-07-04)"* — `list_categories` did succeed live that day (50 real categories). **This is a genuine auth lapse, not another transient 502**: the environment now names Relume as requiring authentication, which is a different signal from 2026-07-03's Cloudflare 502 (recorded, correctly, as *inconclusive* and re-verified fine the next day). Both precedents matter and `techstack-connection-verifier` encodes the distinction: **a service error is inconclusive; an auth error is a finding.** Cf. the Notion cloud-routines connector's stale "zero connectors" reading (`OWNER_INPUT_NEEDED.md` item 54) |
| Vercel | Hosts the React site exported from Relume; connects the confirmed real domain `arikaagency.com` (currently registered but not yet pointed at any live site — see `AGENCY_OPERATING_CONSTITUTION.md` §2) | **Confirmed (2026-07-03)** — chosen over Netlify and over all-in-one Webflow hosting (cost-driven, "Option B"). Not yet set up; current domain registrar also not yet confirmed |
| Remotion | Programmatic, React-based motion-graphics/video tool — owner-named for Design (19)'s Motion & Transition tool registry (`19_Design/DESIGN_LANGUAGE_SYSTEM.md` §2a) | **Named by owner (2026-07-03), not connected** — no entry in this repo's `.mcp.json`, no MCP/integration link supplied yet. Not usable until the owner confirms the actual integration path. Also cross-referenced by Experience Engineering (20)'s own Motion Tech Stack (`20_Experience_Engineering/EXPERIENCE_TECH_STACK.md` §2) for the video-as-code vs. live-interactive-web distinction |
| GSAP + ScrollTrigger | Scroll-driven animation library (JS) — candidate motion/scroll engine for Experience Engineering (20)'s interactive-experience builds (`20_Experience_Engineering/EXPERIENCE_TECH_STACK.md` §2) | **Named via owner-relayed AI session (2026-07-03), not connected** — a generic code library, not an account-based vendor like Canva/OpenArt; no adoption decision made |
| Framer Motion | React animation library — candidate motion layer for Experience Engineering (20) | **Named via owner-relayed AI session (2026-07-03), not connected** — generic code library, not an account-based vendor |
| Motion One | Lightweight web animation library, named alongside Framer Motion as a candidate | **Named via owner-relayed AI session (2026-07-03), not connected** — generic code library, not an account-based vendor |
| Three.js / React Three Fiber / Drei | WebGL/3D scene libraries (Three.js core, React Three Fiber = React renderer, Drei = R3F helper library) — candidate 3D layer for Experience Engineering (20) | **Named via owner-relayed AI session (2026-07-03), not connected** — generic code libraries, not account-based vendors |
| Lenis | Smooth-scroll library — candidate scroll engine for Experience Engineering (20) | **Named via owner-relayed AI session (2026-07-03), not connected** — generic code library, not an account-based vendor |
| Blender | Open-source 3D modeling/animation software — candidate 3D-asset-authoring tool (desktop, not MCP-queryable) for Design (19)/Experience Engineering (20) | **Named via owner-relayed AI session (2026-07-03), not connected** |
| Cinema 4D | 3D modeling/animation software (desktop) — candidate 3D-asset-authoring tool alongside Blender | **Named via owner-relayed AI session (2026-07-03), not connected** |
| Spline | Browser-based real-time 3D design tool, exports to web — candidate 3D-asset-authoring tool | **Named via owner-relayed AI session (2026-07-03), not connected** |
| Rive | Real-time interactive vector animation tool/runtime — candidate 3D/motion-asset-authoring tool | **Named via owner-relayed AI session (2026-07-03), not connected** |
| After Effects / Lottie | Motion-graphics authoring (After Effects) + its JSON animation export/runtime format (Lottie) — candidate VFX/transitions tool for Design (19)'s Motion/VFX/SFX/3D-5D Tool Registry (`19_Design/DESIGN_LANGUAGE_SYSTEM.md` §2a) | **Named via owner-relayed AI session (2026-07-03), not connected** |
| Next.js / Tailwind CSS | Front-end framework + utility-first styling — the real stack the `20_Experience_Engineering/arika-website` project is built and deployed on; the base of Experience Engineering (20)'s Spec System (`EXPERIENCE_SPEC_SYSTEM.md`) | **In real use (2026-07-04)** — a deployed Next.js + Tailwind app exists; generic frameworks, not account-based vendors, no MCP |
| Whimsical | Sitemap/wireframe diagramming tool — named for the Spec System's Sitemap (Station 2) and Wireframe (Station 4) stations | **Named (2026-07-09), connection unverified** — the owner's source docs describe it as "connected," but no Whimsical MCP exists in this repo's `.mcp.json`; treat as not-connected until confirmed. `OWNER_INPUT_NEEDED.md` item 56 |
| TanStack Query | Data-fetching/caching library for the frontend→backend layer (Elite Web Build System §5) | **Named via the Elite Web Build reference set (2026-07-09), not connected** — generic code library |
| Formspree | Form-submission service — the "buy the backend, don't build it" form path in the Discoverability & Architecture pillar (`20_Experience_Engineering/build-system/discoverability-architecture.md`) | **Named (2026-07-09), not connected** — no account created; `GO_LIVE_CHECKLIST.md` Phase 10 |
| Sanity | Candidate headless CMS — lets website content be edited without a rebuild; the CMS option in the Discoverability & Architecture pillar | **Named (2026-07-09), not connected** — no account created |
| Plausible / Google Analytics | Candidate web-analytics for the Spec System's Measure stage (Workflow Run-Sheet Phase 4) | **Named (2026-07-09), not connected** — no account created |
| Google Search Console | Free indexing/verification tool — the "confirm you're indexed" step of the discoverability pillar | **Named (2026-07-09), not connected** — not registered |

### The ClickUp CRM: this file was stale, `CRM_SCHEMA.md` was right all along

The **Sales CRM** space (`901511301824`) holds two structures, both empty:

| Structure | Lists | Status |
|---|---|---|
| Folder **Arika Agency CRM** (`901516593347`) | Lead · Opportunity · Client · Engagement / Project · Partner | **✅ Canonical** — confirmed live 2026-07-15 |
| Space-level lists | Leads · Deals · Accounts · Contacts · Contracts | **ClickUp's pre-existing, unused default template.** Deletion is an owner action; not deleted here |

**⚠️ Correction to this section's first draft (2026-07-15):** the two structures were initially written up here as a newly-found *conflict*. **They are not.** `CRM_SCHEMA.md` §"Platform selection" already recorded the arrangement on **2026-07-01** — the folder was *"created via a ClickUp MCP connector in a dedicated 'Arika Agency CRM' folder, **kept separate from the workspace's pre-existing (unused) 'Sales CRM' template**."* Deliberate, documented, and correct. The template lists are known dead weight worth deleting, not an ambiguity anyone was about to resolve wrongly.

**The real finding is narrower and worse:** **this file's §3 said "not yet implemented" while `CRM_SCHEMA.md` documented a complete implementation, in detail, from 2026-07-01.** Two governance documents disagreed about the same system for 14 days. Tech Stack is supposed to be the canonical inventory, and on its central platform it was the *less* accurate of the two. The drift wasn't doc-vs-reality — it was **doc-vs-doc**, which is harder to catch and exactly what a live verifier catches for free.

`CRM_SCHEMA.md` records substantially more than the live audit re-derived: every custom field live on its matching List, cross-object FK relationships as real ClickUp `list_relationship` fields, and all 5 status pipelines written via a ClickUp **OAuth App** token after a personal token proved silently unable to write statuses (a real, confirmed platform limitation). It also records a hard lock still standing: **custom-field rename/delete is blocked under both token types** (`"Access denied for updating field api"`).

**Invoice / Revenue Event** — the 6th CRM_SCHEMA object — has no ClickUp list **by design**; it belongs to the accounting platform. Correct in principle, except: (a) Zoho Books' trial is **expired** (§3), so the agency's 6th CRM object sits on a lapsed plan; and (b) **`CRM_SCHEMA.md` still says that object is "the object QuickBooks owns"** — a stale reference that survived the 2026-07-01 QuickBooks→Zoho Books reversal, inside the very section that documents the reversal. Flagged there.

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| Weekly stack verification | Cron `23 7 * * 1` (`techstack-connection-verifier`) | Free read-only call per connectable tool → compare to §3's claim → report drift + dependents at risk | `STACK_VERIFIED` / `STACK_DRIFT_DETECTED` | Mary Thuo |
| Daily cost check | Cron `29 7 * * *` (`techstack-cost-guardian`) | Free balance/plan call per paid account → runway in units, not credits → flag expiring trials **before** they lapse | `STACK_COST_HEALTHY` / `_DEGRADED` / `STACK_CAPABILITY_BLOCKED` | Mary Thuo |
| Tool registration | `TOOL_PROPOSED` (`techstack-inventory-registrar`) | Classify → verify live (or record `verifiable: false`) → assign status class → record supersession chain | `TOOL_REGISTERED` / `_BLOCKED` | Mary Thuo |

## 5. Agent Roster

**3 agents, built 2026-07-15** — all three exist because the 2026-07-15 audit (§2) proved this department's §3 discipline was real but unscheduled.

| Agent | Class | Trigger → emits | Role |
|---|---|---|---|
| `techstack-connection-verifier` | 1 | weekly cron `23 7 * * 1` → `STACK_VERIFIED` / `STACK_DRIFT_DETECTED` | Proves each tool answers a **free read-only call**; reports drift vs. §3 in **both** directions |
| `techstack-cost-guardian` | 1 | daily cron `29 7 * * *` → `STACK_COST_HEALTHY` / `_DEGRADED` / `STACK_CAPABILITY_BLOCKED` | Plans, trials, credits, quotas. Converts balances into **runway** ("2 images left", not "44 credits") |
| `techstack-inventory-registrar` | 2 | `TOOL_PROPOSED` → `TOOL_REGISTERED` / `_BLOCKED` | The gate into §3 — enforces live verification, the **named-vs-connected** distinction, and an unbroken supersession chain |

**`techstack-connection-verifier` is the cron this department's own rule always implied.** §3 said *"verified via a live API call rather than assumed"* — correct, and never scheduled, which is why 4 rows rotted undetected.

**`techstack-inventory-registrar` is Class 2** — §3 is canonical and 11 other departments cite it, so a wrong row propagates agency-wide. It also enforces §2's rule that `finos-plugin`, `bois`, `design-plugin`, and `arika-runtime` are **software the agency builds, not tools it uses** — they never belong in §3.

### Boundary with Automation (16)

| Agent | Watches |
|---|---|
| `automation-reliability-monitor` (16) | **Automations** — routines and crons: did they *fire*? |
| `techstack-connection-verifier` (13) | **Tools** — vendors and connectors: do they *answer*? |

They meet exactly where an automation dies because its connector did — which is what happened on 2026-07-04, when the Creative Pipeline routine was auto-disabled for `auto_disabled_repo_access` (`16_Automation/AUTOMATION_OS.md` §9). Each hands findings to the other.

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder)* | | | | | |

## 8. Decision Log

- 2026-07-01 — Canva registered as confirmed real/connected (supports new Design department, 19). Notion and ManyChat registered as proposed, pending account/workspace creation. See §3.
- 2026-07-03 — OpenArt confirmed as the Production Engine vendor (chosen over imagine.art and Higgsfield). Claude Design registered as an already-available capability (Claude Pro plan). Relume confirmed as the website-creation tool. Hosting path confirmed as React + external host ("Option B"), specific platform still open. See §3.
- 2026-07-03 — **Vercel confirmed** as the hosting platform (over Netlify). Domain registrar for `arikaagency.com` still unconfirmed — the one remaining piece before DNS/SSL setup can happen.
- 2026-07-04 — **Relume, Canva, and OpenArt re-verified live** ahead of starting the actual Arika website build. Relume's `list_categories` succeeded (50 real component categories) — the 2026-07-03 Cloudflare 502 was transient, not a persistent block. **Correction**: Relume's real MCP surface is a React/TSX component library (search/fetch pre-built sections), not an AI sitemap-generation tool as originally described — that description is corrected in §3. Canva (`help`) and OpenArt (`openart_account_get`, Free plan, 40 credits) both responded live, superseding this session's earlier stale "needs re-authorization" reading.
- 2026-07-03 — **Remotion registered** as owner-named for Design (19)'s new Motion/VFX/SFX/3D-5D Tool Registry (`19_Design/DESIGN_LANGUAGE_SYSTEM.md` §2a) — not connected, no MCP/integration link exists yet. 3 other tool categories (Transitions/VFX, SFX, 3D/5D Motion) remain open with no tool named, per the no-silent-invention rule — see `OWNER_INPUT_NEEDED.md` item 48.
- 2026-07-03 — **Notion and OpenArt confirmed real and connected**, each verified via a live API call rather than assumed from tool availability alone: Notion's `notion-get-users` returned a real workspace user, OpenArt's `openart_account_get` returned a real account (Free plan, 40 credits). **Relume's connection status is inconclusive** — connector present, but its own service returned a Cloudflare 502 twice in a row, not an auth failure.
- 2026-07-03 — **Batch-registered 10 motion/3D/interactive candidate tools** (GSAP+ScrollTrigger, Framer Motion, Motion One, Three.js/React Three Fiber/Drei, Lenis, Blender, Cinema 4D, Spline, Rive, After Effects/Lottie), sourced from Experience Engineering (20)'s founding session — an owner-relayed external AI chat, not a personal owner adoption decision the way Canva/OpenArt/Notion were each individually confirmed and verified via a live API call. All registered "named, not connected" — distinct in kind from this table's account-based vendors, since most are generic code libraries or desktop authoring tools rather than SaaS accounts. See `20_Experience_Engineering/EXPERIENCE_TECH_STACK.md` and `00_Agency_Governance/OWNER_INPUT_NEEDED.md` item 49.
- 2026-07-07 — **KIE.ai's Nano Banana Pro and Seedance APIs added** as a second image/video path for Design (19)'s Production Engine, alongside OpenArt — owner-supplied, already has a live API key. Unlike OpenArt/Canva, KIE.ai is a plain REST API (not an MCP server), so a real code connector was built: `19_Design/design-plugin` (`KieClient` shared job client + `NanoBananaProConnector`/`SeedanceConnector`), tested (13 passing tests against a mocked KIE API, no real credits spent). See §3 and `19_Design/DESIGN_OS.md` §3, §13.

## 9. Risk / Incident Log

### INCIDENT 2026-07-15 — 4 inventory rows found false in one audit pass

No longer a placeholder. All four were live-verified with free, read-only calls on 2026-07-15.

| # | Tool | Claimed | Reality | Days stale | Who depends on it |
|---|---|---|---|---|---|
| 1 | **Canva** | Connected (2026-07-01) | **Unauthenticated** | 14 | Design (19) Creative Assembly; the "Claude Design" capability |
| 2 | **OpenArt** | Connected, 40 credits (2026-07-03) | **Unauthenticated AND 0 credits** | 12 | Design (19) Production Engine |
| 3 | **Relume** | Connected (2026-07-04) | **Unauthenticated** | 11 | Experience Engineering (20) component library |
| 4 | **Zoho Books** | *"revisit before trial expires"* | **`is_trial_expired: true`** | 19 since org creation | Finance (09); CRM_SCHEMA's Invoice/Revenue Event |
| 5 | **KIE.ai** | 62 of 80 credits | **44** | 8 | Design (19) — the **only working image path** |
| 6 | **ClickUp CRM** | *"not yet implemented"* | **Fully built** (pessimistic drift) | 14 | Sales (05), ClientPartner (06), Client Success (07), Operations (08) |

**Root cause — identical to Automation (16)'s 11-day outage 4 days earlier:** the repo records a decision with an **activation date** and no expiry, and nothing re-checks it. The claim *"Confirmed real and connected (2026-07-01)"* is a statement about 2026-07-01. It was read as a statement about now.

**Why it went undetected:** this department had **no agents**. §3 was maintained by hand, at the moment of decision, by whoever happened to be making it. There was no second look, ever.

**The compounding risk:** #2 and #5 together mean the agency has **2 images of generation runway left**, agency-wide, and both #1 and #2 must be re-authenticated before Design can produce anything at all. That is not visible from any single row — only from checking them together, which is `techstack-cost-guardian`'s job.

**Fix applied:** 3 agents (§5). **Not fixed:** the connectors themselves — re-authentication needs a browser and the account owner, and the Zoho plan decision is the owner's money. Both are owner actions, surfaced rather than silently worked around.

**The generalizable rule (now in §3's convention):** a row is a **claim with a shelf life**. Record `verified_at`, not just "confirmed". Cf. `AUTOMATION_APPROVAL_MATRIX.md`'s identical lesson: *"we turned it on" and "it is on" are different claims.*

### Standing risks (structural, not incidents)

- **`ANTHROPIC_API_KEY` is not set.** Every `prompt` agent in the repo — **93 of them, including all 3 of this department's** — depends on Claude, and the key exists nowhere. The single largest dependency in the stack is unverified and unverifiable (there is no free call to test a key that doesn't exist).
- **Vendor concentration in Design:** OpenArt (0 credits, unauthenticated) and KIE.ai (44 credits) are the only two image paths, and Claude Design was ruled out for photographic scenes on real evidence (`DESIGN_OS.md` §10). One vendor lapse from zero capability.
- **Zoho Books bills in KES; offers are priced in USD**, via a conversion calculator that **has not been built**. An expired trial makes this concrete rather than theoretical.
- **Domain/registrar:** `arikaagency.com` is registered and has **live mailboxes** (`support@`, `growth@`, `mary.thuo@` — observed in ClickUp's real member list, 2026-07-15), yet §3 records no email/DNS provider and the registrar remains unconfirmed (§8, 2026-07-03). **Real infrastructure the canonical inventory does not name.**

## 10. Standards & SOPs Index

*(placeholder — canonical tool inventory, access/credential management process, integration documentation)*

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

Two real cron triggers on `arika-runtime` (§5): `techstack-connection-verifier` weekly (`23 7 * * 1`) and `techstack-cost-guardian` daily (`29 7 * * *`).

**⚠️ Both are subject to the exact failure they detect.** They are runtime cron triggers, and **the runtime is not booted as a persistent service** — no `ANTHROPIC_API_KEY`, no daemon. So they are **declared, not scheduled**: today, the stack's only verification is a human running `arika run techstack-connection-verifier`. This is the same recursion Automation (16) documented for its own monitor (`AUTOMATION_OS.md` §16), and it has the same cause — **the runtime's 23 cron triggers still have 1 approval-matrix row between them** (`AUTOMATION_APPROVAL_MATRIX.md`). Until that is resolved, these agents are on-demand tools, not standing controls.

Stating it plainly: **the fix for "nobody re-checks the stack" is itself something nobody has scheduled yet.**

## 13. Existing OS Sub-Layer

None yet. (Note: `09_Finance/finos-plugin/`, `12_Branding/bois/`, and `19_Design/design-plugin/` are department-specific aspirational software builds, not Tech Stack inventory — see those departments' own §13 sections.)

## 14. Raw Archive Pointer

None. This is a genuinely new department with no inherited backlog.

## 15. Changelog

- 2026-07-15 — **🔴 LIVE AUDIT: 4 of §3's rows were false, in 4 different directions** (§2, §9). Every connectable tool re-checked with a free read-only call. **Canva, OpenArt, Relume — all three unauthenticated** while §3 said *"Confirmed real and connected."* **Zoho Books' Premium Trial expired** (`is_trial_expired: true`) — the row itself said *"revisit before trial expires"* and nobody did. **KIE.ai's balance is 44, not the 62 recorded everywhere** — an arithmetic error (two images × 18 = 36; 80 − 36 = 44; the docs logged one image's spend while describing two), corrected in `DESIGN_OS.md` too, where `design-production-engine-coordinator` estimates spend against it. **And the inverse: the ClickUp CRM is fully built while §3 said "not yet implemented"** — drift is not always optimistic. **Root cause is identical to Automation (16)'s 11-day outage 4 days earlier:** an activation date with no expiry, and nothing re-checking. Not fixed here: re-authentication needs a browser and the account owner; the Zoho plan is the owner's money. — Claude Code (Opus 4.8)
- 2026-07-15 — **Department built: 3 agents wired onto `arika-runtime`** (§5) — `techstack-connection-verifier` (weekly; **the cron this department's own "verify, don't assume" rule always implied and never got**), `techstack-cost-guardian` (daily; converts balances into **runway** — "2 images left", not "44 credits"), `techstack-inventory-registrar` (Class 2; gates §3, enforcing the named-vs-connected distinction and the supersession chain). Boundary set with `automation-reliability-monitor` (16): **16 asks whether automations *fired*; 13 asks whether tools *answer*.** They meet where an automation dies because its connector did — exactly 2026-07-04's `auto_disabled_repo_access`. **⚠️ Both crons are declared, not scheduled** (§12) — the runtime isn't booted, so the fix for "nobody re-checks the stack" is itself unscheduled. — Claude Code (Opus 4.8)
- 2026-07-15 — **🟢 ClickUp CRM confirmed BUILT and declared canonical** (owner-decided). Live: space **Sales CRM** → folder **Arika Agency CRM** → 5 lists matching `CRM_SCHEMA.md`'s core objects, with the schema's real stage statuses and 6 real custom fields, and the `Lead` list citing `CRM_SCHEMA.md` by name. Zero tasks — built, never used. **⚠️ Conflict found: a second, parallel CRM (ClickUp's default Leads/Deals/Accounts/Contacts/Contracts template) sits in the same space.** The folder is canonical; the 5 template lists are flagged for deletion but **not deleted** — live workspace objects, owner's call. **Schema gap:** CRM_SCHEMA defines 6 objects; ClickUp implements 5. Invoice/Revenue Event lives in Zoho Books — correctly, except that trial is expired. — Claude Code (Opus 4.8)
- 2026-07-15 — **§2 corrected**: read *"Skeleton, with its first 3 real confirmed tools (2026-06-30)"* — stale by 27 rows. **Real infrastructure found that §3 does not name**: three live `@arikaagency.com` mailboxes (`support@`, `growth@`, `mary.thuo@`), observed in ClickUp's real member list — so the domain has working email while §3 records no email/DNS provider and the registrar is still unconfirmed. — Claude Code (Opus 4.8)
- 2026-07-09 — **Registered 8 tools for Experience Engineering (20)'s new Experience Spec System** (`20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md`): Next.js/Tailwind (in real use — the deployed `arika-website`), Whimsical (connection unverified — source claims connected, no MCP present), and the discoverability/last-mile layer (TanStack Query, Formspree, Sanity, Plausible/Google Analytics, Google Search Console — all named, not connected). None are new adoption decisions; they're the tool surface the Spec System references. Cross-ref `OWNER_INPUT_NEEDED.md` item 56 (Whimsical) and `GO_LIVE_CHECKLIST.md` Phase 10. — Claude Code (Opus 4.8)
- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap. — Claude Code (Sonnet 4.6)
- 2026-07-03 — **Notion and OpenArt verified real and connected** via live API calls. **Relume's status left inconclusive** pending its own service coming back up (Cloudflare 502 on two tries). — Claude Code (Sonnet 5)
- 2026-07-01 — **QuickBooks confirmed** as accounting/invoicing platform, superseding Zoho Books (whose selection rationale — native Zoho CRM sync — no longer applied once Zoho CRM was replaced by ClickUp). ClickUp↔QuickBooks integration closes the CRM→Invoice handoff. — Claude Code (Sonnet 4.6)
- 2026-07-01 — **ClickUp supersedes Zoho CRM** as the CRM/pipeline platform — owner decision, free tier, replaces the Zoho CRM confirmed same day 2026-06-30. Consequence: Zoho Books' selection rationale (native CRM↔Books sync) no longer holds — accounting/invoicing platform re-opened as an unresolved gap (closed same day by QuickBooks confirmation). Claude (Anthropic API) unchanged. — Claude Code (Sonnet 4.6)
- 2026-06-30 — First 3 real tool decisions recorded: **Zoho CRM** (supersedes the earlier HubSpot selection, `CRM_SCHEMA.md`), **Zoho Books** (Finance's accounting platform, closes tracker item 25), and **Claude (Anthropic API)** as the agency-standard LLM for AI agent execution (Finance's 7 agents + Branding's 20 agents). All 3 are real decisions, none implemented yet — see `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence (structure-only placeholder, per the go-live plan in 00_Agency_Governance/GO_LIVE_CHECKLIST.md). — Claude Code (Sonnet 5)
- 2026-07-01 — **Zoho Books confirmed real and connected** — `list_organizations` confirmed a pre-existing org (ID `929138528`, Kenya, KES, Premium Trial). Real currency decision: USD offers, KES invoicing via conversion calculator (not yet built). — Claude Code (Sonnet 5)
- 2026-07-01 — **QuickBooks abandoned, reverted to Zoho Books.** Real QuickBooks account creation confirmed a paid subscription/business registration is required before authentication is even possible — no free tier exists, unlike ClickUp. Owner reverted to Zoho Books (free tier), re-superseding the same-day QuickBooks decision. ClickUp↔Zoho Books integration path not yet re-verified (previously verified only for QuickBooks). See `00_Agency_Governance/GO_LIVE_CHECKLIST.md` items 2, 4, 9. — Claude Code (Sonnet 5)
- 2026-07-01 — **Canva confirmed real and connected** (MCP tools live in this environment, premium tier) — the department's first genuinely usable-today tool, registered to support the new Design (19) department. **Notion and ManyChat added as proposed, not yet created** — no workspace/account exists for either. AI image/video generation vendor flagged as unresolved (owner named Higgsfield as a maybe, not a decision). — Claude Code (Sonnet 5)
- 2026-07-03 — **OpenArt confirmed** as the Production Engine vendor, closing that unresolved row — compared directly against imagine.art (near-identical model coverage) and Higgsfield before the owner chose OpenArt only. Added **Claude Design** (already available on the owner's Claude Pro plan, exports to Canva) and **Relume** (website sitemap/wireframe/component tool, own MCP) as newly confirmed real tools. Added the **website hosting platform** row — path confirmed as React + external host over all-in-one Webflow hosting (cost-driven), specific platform (Vercel vs. Netlify) still open, as is which registrar currently holds `arikaagency.com`. — Claude Code (Sonnet 5)
- 2026-07-03 — **Vercel confirmed** as the hosting platform, closing the Vercel-vs-Netlify half of the decision. Domain registrar for `arikaagency.com` remains the one open piece before DNS/SSL setup. — Claude Code (Sonnet 5)
- 2026-07-07 — **KIE.ai Nano Banana Pro and Seedance APIs registered and connected** — owner-supplied API key, real REST integration (not an MCP server, so no `.mcp.json` entry). Design (19) now has its own real code sub-layer, `19_Design/design-plugin` (`KieClient` + two model connectors, 13 passing tests) — noted in §13's cross-reference alongside `finos-plugin`/`bois`. — Claude Code (Sonnet 5)
- 2026-07-07 — **KIE.ai verified real and connected via a live API call** — `getCredits()` (`GET /chat/credit`, free, no credits spent) confirmed the real account and returned an 80-credit balance, same verification discipline already applied to Notion/OpenArt. — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

**Memory.** All 3 agents (§5) write to `13_Tech_Stack/_memory/runtime.jsonl` in the runtime's bois-compatible JSONL envelope. **This stream is the department's real deliverable**, more than §3 is: §3 is a snapshot that rots, while the stream is a *history of verifications* with timestamps. The 2026-07-15 audit found 4 false rows precisely because there was no such history — only a table of claims, each true on the day it was written. A row in §3 says what someone decided; a line in this stream says what was true, when, and how it was checked.

**Feedback Loop.** §7's KPIs are still placeholders, but two real loops now exist and both are honest about what they can't do:
- `techstack-connection-verifier` → `STACK_DRIFT_DETECTED` → `techstack-cost-guardian` + `automation-reliability-monitor` (16). Drift is reported; **a human re-authenticates** — that needs a browser and an account owner, which no agent has.
- `techstack-cost-guardian` → `STACK_CAPABILITY_BLOCKED` → `design-production-engine-coordinator` (19) + `finance-cashflow-agent` (09). **A capability the agency cannot currently afford is a Design planning input and a Finance cost**, not just a Tech Stack note.

**No KPI is proposed yet, deliberately.** The obvious candidate — *"% of §3 rows verified in the last 7 days"* — would read **0%** for the entire history of this department up to 2026-07-15, and would read 100% only if the runtime were booted, which it isn't (§12). Setting a threshold before the control that measures it actually runs would repeat this department's own error: recording an intention as a fact.

**Cadence.** Against the **Operational Calendar** (`00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4) — weekly verification, daily cost check. Registration is event-driven, not calendared: a tool is proposed when a department needs it.

**⚠️ Both crons are declared, not scheduled** (§12). Until the runtime runs persistently — which needs approval-matrix rows first — this department's cadence is *aspirational*, and the stack's only real check is a human choosing to run it. Said plainly because the alternative is exactly the failure this department just documented.
