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

**Skeleton, with its first 3 real confirmed tools (2026-06-30).** No raw draft archive exists for this department specifically. Note: the two code scaffolds (`09_Finance/finos-plugin/`, `12_Branding/bois/`) are aspirational software the agency is building, not a record of tools it currently uses — do not conflate the two when this department's content gets built out. None of the 3 tools below are implemented yet — confirmed as the real platform decisions, not yet wired up. See `00_Agency_Governance/GO_LIVE_CHECKLIST.md` for the implementation sequence.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| ClickUp | CRM + project management platform — implements the Lead/Opportunity/Client/Partner pipeline defined in `00_Agency_Governance/CRM_SCHEMA.md` via ClickUp Lists, custom fields, and pipeline views; free tier available | **Confirmed real (2026-07-01)**, not yet implemented — supersedes Zoho CRM (confirmed same-day 2026-06-30, superseded 2026-07-01) |
| Zoho Books | Accounting/invoicing platform for Finance (09) — invoice generation, expense tracking, and the Project→Invoice handoff (`CRM_SCHEMA.md` "Handoff Points"); connected via claude.ai's Zoho Books connector, exposing direct MCP tools (`create_invoice`, `create_contact`, `list_invoices`, etc.) — no native ClickUp app or Zapier needed | **Confirmed real and connected (2026-07-01)** — pre-existing org (created 2026-06-26), ID `929138528`, "Arika Agency," Kenya, base currency **KES**, Premium Trial plan (not permanently free — revisit before trial expires). Re-supersedes QuickBooks (abandoned same day: paid subscription/business registration required before authentication, no free tier). **Real currency decision**: offers priced in USD, invoices issued in KES via a not-yet-built conversion calculator. |
| Claude (Anthropic API) | Agency-standard LLM backing AI agent execution — confirmed for Finance (09)'s 7-agent roster and Branding (12)'s 20-agent roster; the default choice once Sales (05)/Marketing (03)'s markdown-defined agent rosters get executable runtimes | **Confirmed real (2026-06-30)**, not yet wired — `finos-plugin` and `bois` both still have zero LLM SDK dependency as of this entry |
| Canva | Creative Assembly platform for Design (19) — carousels, video, presentations, ads; premium tier | **Confirmed real and connected (2026-07-01)** — MCP tools live in this environment; the only tool in this table that is actually usable today, not just decided |
| Notion | System-of-record for content briefs (Content, 04) — script/story/caption/visual-direction schema documented at `04_Content/CONTENT_OS.md` §10 | **Confirmed real and connected (2026-07-03)** — verified via a live `notion-get-users` call, real workspace user "Arika Agency" (`arikaagency.io@gmail.com`). Content-brief database itself not yet built — connection exists, schema not yet applied |
| ManyChat | Proposed DM/comment-automation platform for Automation (16)'s Engagement Layer (`16_Automation/AUTOMATION_OS.md` §3-4) | **Proposed (2026-07-01), account not yet created** — no social media accounts (Instagram Business, Facebook Page, X, Pinterest, LinkedIn profile+page, Tumblr) exist yet either; see `00_Agency_Governance/OWNER_INPUT_NEEDED.md` |
| OpenArt | AI image/video generation, enhancement & upscaling vendor feeding Design (19)'s Production Engine (`19_Design/DESIGN_OS.md` §3) — 100+ models incl. GPT Image, Nano Banana Pro, Sora 2, Kling 3.0, Seedance; output handed to Canva for assembly. MCP server: `https://mcp.openart.ai/mcp` | **Confirmed real and connected (2026-07-03)** — verified via a live `openart_account_get` call: real account (`arikaagency.io@gmail.com`), **Free plan, 40 credits**. Plan/credit level is likely a real constraint on production volume — worth revisiting once real usage starts |
| Claude Design | Anthropic's own AI visual-generation product (Opus 4.7, research preview) — describe a visual, Claude generates/refines it; exports directly into Canva | **Confirmed available (2026-07-03)** — included in the owner's existing Claude Pro plan, no separate account/MCP required |
| KIE.ai — Nano Banana Pro API | Direct API access to Google's Nano Banana Pro (Gemini 3 Pro Image) model, feeding Design (19)'s Production Engine (`19_Design/DESIGN_OS.md` §3) as a second image-generation path alongside OpenArt. Real code connector: `19_Design/design-plugin/src/integrations/kie-nano-banana-pro.ts`. Base: `https://api.kie.ai/api/v1` (`/jobs/createTask`, `/jobs/recordInfo`) | **Confirmed real and connected (2026-07-07)** — verified via a live `getCredits()` call (`GET /chat/credit`, a free read-only endpoint, no generation credits spent): real account (`arikaagency.io@gmail.com`), **80 credits available**. Plain REST API, not an MCP server, so it is not in `.mcp.json`; auth via `KIE_API_KEY` in `19_Design/design-plugin/.env` (owner-supplied, not committed) |
| KIE.ai — Seedance API | Direct API access to Bytedance's Seedance 1.5 Pro video model, feeding Design (19)'s Production Engine as a second video-generation path alongside OpenArt. Real code connector: `19_Design/design-plugin/src/integrations/kie-seedance.ts`. Same KIE job API base as Nano Banana Pro | **Confirmed real and connected (2026-07-07)** — same KIE.ai account/key/credit balance as the Nano Banana Pro row above (80 credits, live-verified), not a separate credential |
| Relume | **Corrected 2026-07-04**: not a sitemap-generation AI — its actual live MCP surface is a real React/TSX component library (50 categories: navbars, hero sections, pricing, testimonials, FAQ, CTA, forms, etc.), searchable/fetchable as ready-to-use component code, plus a one-time Tailwind/alias setup tool | **Confirmed real and connected (2026-07-04)** — `list_categories` succeeded live (50 real categories returned). The earlier "Cloudflare 502, inconclusive" reading (2026-07-03) was transient/stale, not a persistent block — same pattern as the Notion cloud-routines connector's stale "zero connectors" reading (`OWNER_INPUT_NEEDED.md` item 54) |
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

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 5. Agent Roster

*(placeholder — none yet)*

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

*(placeholder — empty; e.g. vendor lock-in, API deprecation risk, once real content exists)*

## 10. Standards & SOPs Index

*(placeholder — canonical tool inventory, access/credential management process, integration documentation)*

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

*(placeholder — structure only)*

## 13. Existing OS Sub-Layer

None yet. (Note: `09_Finance/finos-plugin/`, `12_Branding/bois/`, and `19_Design/design-plugin/` are department-specific aspirational software builds, not Tech Stack inventory — see those departments' own §13 sections.)

## 14. Raw Archive Pointer

None. This is a genuinely new department with no inherited backlog.

## 15. Changelog

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

*(placeholder — structure only, no agent roster exists yet to generate real memory/feedback entries; see §5, which reads "placeholder — none yet.")* Once this department has a real or code-based agent roster (per the Tier 1 pattern in `05_Sales/SALES_OS.md` §16), this section should define: **Memory** (where Decision/Learning/Prompt-Evolution logs live), **Feedback Loop** (what happens when a §7 KPI misses threshold), and **Cadence** (which of the 7 Cognitive Calendars — `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` §4 — this department's workflows run against, and how often).
