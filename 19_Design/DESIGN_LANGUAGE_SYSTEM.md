# Design Language System — Spec

**Status:** Proposed, not built. This is a specification document, not working code — cross-referenced from [`DESIGN_OS.md`](DESIGN_OS.md) §6 (Skill Library Index) and §3 (Capability Registry), same relationship Branding's `bois/agents/AGENT_SYSTEM.md` has to `BRANDING_OS.md` §5.

---

## Why this exists

Per explicit owner direction during the planning session that created the Design department (19): Canva-as-assembly and an asset library aren't enough on their own. Developers and AI agents building anything — internal tooling, client deliverables, future UI/UX work — need a single place to query Arika's design language programmatically instead of re-deriving color/type/motion/spacing decisions per project. This file documents the intended surface of that system: a custom MCP server + API, plus a generalized skill catalog built against it.

## 1. Design Tokens surface

Intended to expose, once Branding's brand kit is finalized (`12_Branding/BRANDING_OS.md` §2):
- **Color tokens** — palette values (currently direction-only: Deep Navy, Charcoal Gray, Silver Mist, Accent Gold — see `DESIGN_INSPIRATION.md`; exact hex values pending finalization, not invented here)
- **Type tokens** — display/body typeface families (direction-only: Space Grotesk/Satoshi/Neue Montreal display, Inter/Manrope body) plus weight/size/line-height scales once set
- **Spacing/grid tokens** — layout grid, margin/padding scale — not yet defined anywhere in this repo; open item

This system should **read from** Branding's finalized brand kit as its source of truth, not maintain a competing copy of it.

## 2. Motion & Transition surface

Intended to expose the reusable motion primitives named in `DESIGN_OS.md` §3's Motion sub-library:
- **Executive Reveal** — logo reveals, titles, hero-section entrances
- **Data Pulse** — growing charts, metrics, revenue-node animations
- **Light Sweep** — premium highlights, metal reflections, gold accents
- **Camera Paths** — slow dolly, top-down, orbit, push-in, macro
- **Transitions** — glass dissolve, grid build, architectural assembly

None of these have defined timing curves, durations, or easing functions yet — that's the concrete content this surface needs before it's queryable. Open item, not fabricated here.

### 2a. Motion / VFX / SFX / 3D-5D Tool & MCP Registry

**Status: skeleton only.** Per owner direction (2026-07-03): this surface should eventually let Claude/other agents pull real, invokable constructs — not just named concepts — for motion graphics, transitions, VFX, SFX, and 3D/5D motion, the same way `DESIGN_OS.md` §3 registers OpenArt with a real MCP URL for image/video generation. Every row needs a **real, live link** (MCP server endpoint, plugin/marketplace URL, or docs link) before it's usable — a tool name with no link is not "action-oriented," it's a note. Nothing here is configured in this repo's `.mcp.json` (cross-check `13_Tech_Stack/TECHSTACK_OS.md` §3, the canonical tool inventory). Populating real rows is tracked as `00_Agency_Governance/OWNER_INPUT_NEEDED.md` item 48.

**Adoption confirmed, connection still pending (2026-07-04).** Owner confirmed every candidate tool below (across both this table and Experience Engineering's overlapping motion/3D list, `20_Experience_Engineering/EXPERIENCE_TECH_STACK.md` §2) as adopted candidates — resolving the *selection* half of tracker items 48/49. Real MCP/integration links are deliberately deferred until each tool is actually invoked in production; wiring them up is tracked separately as tracker items 36/48's *connection* half. No row is "configured" until it has a real link.

**Note on overlap with Experience Engineering (20):** the code libraries a live interactive *build* consumes (Three.js, React Three Fiber, Drei, GSAP+ScrollTrigger, Framer Motion, Motion One, Lenis) are registered in `20_Experience_Engineering/EXPERIENCE_TECH_STACK.md` and `13_Tech_Stack/TECHSTACK_OS.md` instead of here — this table covers *asset-authoring* tools Design invokes directly (Blender/Cinema4D/Spline/Rive/After Effects/Lottie deliberately appear in both registries, since Design may author a 3D/motion asset that Experience Engineering then assembles into a live build), not code libraries a build imports.

| Category | Tool / MCP | Purpose | Link | Status |
|---|---|---|---|---|
| Motion Graphics / Video-as-Code | Remotion | Programmatic, React-based video generation — owner-named as an existing/intended tool | *(pending — owner to supply the MCP server URL or integration path)* | **Named by owner (2026-07-03), not configured** — no Remotion entry exists in `.mcp.json` or this environment's connected MCP list |
| Transitions / VFX | After Effects, Lottie | Transition effects, compositing, motion-graphics authoring (After Effects) + its lightweight JSON animation/export runtime (Lottie) | *(pending — no MCP/integration path supplied)* | **Named via owner-relayed AI session (2026-07-03), not configured** — candidates surfaced through Experience Engineering (20)'s founding session (`20_Experience_Engineering/EXPERIENCE_ENGINEERING_VISION.md`), not a Design-direct owner decision; no `.mcp.json` entry |
| SFX / Sound Design | Boom Library, Sonniss, Pro Sound Effects (Useful Interface), SoundMorph, Soundly | UI sound, cinematic stingers, ambient beds — feeds the Sound sub-library in `DESIGN_OS.md` §3. Boom Library/Sonniss/Pro Sound Effects are library vendors (PSE's "Useful Interface" pack is UI-sound-specific); SoundMorph covers synthetic/digital design; Soundly is the cloud search/organization layer for dragging assets into a workflow, not an asset vendor itself | *(pending — no MCP/integration path or licensing decision supplied)* | **Named via owner-relayed AI session (2026-07-04), not configured** — first candidates ever named for this category; none adopted, licensed, or connected yet |
| 3D / 5D Motion | Blender, Cinema 4D, Spline, Rive | 3D scene/camera authoring (Blender, Cinema 4D — desktop), browser-based real-time 3D (Spline), real-time interactive vector/motion runtime (Rive). What "5D" concretely means is still unclarified by the owner — flag stands, unresolved | *(pending — no MCP/integration path supplied)* | **Named via owner-relayed AI session (2026-07-03), not configured** — candidates surfaced through Experience Engineering (20)'s founding session, not a Design-direct owner decision; no `.mcp.json` entry |
| Color / Palette | Khroma | AI color-palette generator trained on liked/disliked color combinations | *(pending — link not supplied)* | **Named by owner (2026-07-04), not configured** — new category, no prior entry |
| Motion Graphics / Video-as-Code | Jitter | Browser-based motion-graphics design tool (alongside the existing Remotion row above) | *(pending — link not supplied)* | **Named by owner (2026-07-04), not configured** |
| 3D / 5D Motion | Threlte, Theatre.js | Svelte component framework built on Three.js for 3D web scenes (Threlte); JS animation/keyframe-sequencing library commonly paired with Three.js for cinematic camera work (Theatre.js) | *(pending — link not supplied)* | **Named by owner (2026-07-04), not configured** |
| UI Component / Design-Engineering Reference | 21st.dev | AI-curated/generated React UI component marketplace, a common design-engineering reference | *(pending — link not supplied)* | **Named by owner (2026-07-04), not configured** — new category, no prior entry |
| 3D / 5D Motion | PeachWeb | "Stunning Interactive 3D Websites Without Code" — no-code builder for interactive 3D websites (or hire-an-expert option), aimed at designers/brands | `https://www.peachweb.io/` | **Confirmed via owner-supplied URL (2026-07-04), cross-checked via web search — not configured/adopted**, an alternative/adjacent candidate to Spline for no-code 3D web builds |

The owner's 2026-07-04 tool list also re-named Spline, Three.js, and Framer Motion (as "Spine.desgins," "Three.JZ," and "npm i framer motion") — treated as reconfirmation of the existing rows/entries above and in `EXPERIENCE_TECH_STACK.md` §2, not new tools. Full raw list and confidence triage: `DESIGN_INSPIRATION.md`.

Once a real tool is confirmed for any row here, register it in `13_Tech_Stack/TECHSTACK_OS.md` §3 too (same pattern as Canva/OpenArt/Relume) — this table is the design-surface view, Tech Stack is the canonical inventory of record.

## 3. UI/UX Pattern surface

Component-level patterns (buttons, cards, navigation, dashboard widgets) consistent with the brand's visual direction. **Not yet defined anywhere in this repo** — needs joint Branding (identity rules) + Design (production application) work before this section can hold real content.

## 4. Skill Catalog (generalized, not Arika-only)

Each skill below is meant to be parameterized by brand/client rather than hardcoded, so the same catalog serves Arika's own content production and future external client/sector design engagements (direct owner requirement — "not just for use but also for when we design for other businesses"):

| Skill | Purpose | Status |
|---|---|---|
| Storyboard Generation | Produce a scene-by-scene storyboard (hook/visual/camera/voice/music/duration/prompt) from a content brief | Proposed |
| Brand Motion Application | Apply the Motion surface (§2) consistently to a given asset | Proposed |
| UI/UX Pattern Application | Apply the UI/UX surface (§3) to a given interface/deliverable | Proposed |
| Environment/Character Consistency Check | Validate a generated asset against the Creative Digital Twin doctrine (`DESIGN_OS.md` §10) and Character Library specs | Proposed |
| Asset Enhancement & Upscale | Run raw AI-generated output through the Production Engine's enhancement/upscale stage (`DESIGN_OS.md` §3) before it reaches Canva | Proposed |
| Canva Assembly | Assemble approved, enhanced assets into a finished Canva deliverable following the campaign-first folder structure (`DESIGN_OS.md` §10) | Proposed |

**Prompt-construction cross-reference:** the prompt-construction half of skills like Storyboard Generation and Asset Enhancement & Upscale is intended to eventually be standardized by Experience Engineering (20)'s structured, ID'd/stateful Prompting System — see `20_Experience_Engineering/PROMPTING_SYSTEM.md`, a shared system explicitly designed to serve Design's own live Production Engine (OpenArt, Claude Design), not just Experience Engineering's future builds. Not built yet.

## 5. Intended consumers

- Internal developers building agency tooling
- AI agents (Claude Code, and once wired, Branding's/Design's own agent rosters) needing consistent design-language answers instead of re-deriving them per task
- Future client-facing design work, once Design is packaged as a sellable offer (cross-ref Offer, 02 — not built here)

## 6. Build status & open questions

**Nothing in this file is built.** Before real implementation, the following need real decisions (not guesses):
- Hosting/runtime for the MCP server
- Auth model (who/what can query it — internal-only vs. client-facing)
- Schema format for the token/motion/pattern data (JSON Schema, protobuf, or otherwise)
- Whether this is a bespoke MCP server or built on an existing design-token tooling standard

These are flagged as open build/decision items, not resolved here — see `00_Agency_Governance/OWNER_INPUT_NEEDED.md` and `00_Agency_Governance/GO_LIVE_CHECKLIST.md`.

## Changelog

- 2026-07-01 — Spec created alongside the Design department (19), per explicit owner follow-up that the Skill Library Index (`DESIGN_OS.md` §6) should be a real catalog, not a placeholder, and that a design-language MCP/API is in scope now rather than deferred. — Claude Code (Sonnet 5)
- 2026-07-03 — Added §2a, a skeleton Motion/VFX/SFX/3D-5D Tool & MCP Registry, per owner request for a queryable, "action-oriented, live-link" catalog of motion-graphics/transition/VFX/SFX/3D tools (beyond Canva/OpenArt, which already live in `DESIGN_OS.md` §3). Registered **Remotion** as owner-named but not yet configured anywhere in this repo — no fabricated tool names or links for the 3 remaining open categories (Transitions/VFX, SFX/Sound Design, 3D/5D Motion), per the no-silent-invention rule. Real tool names/links tracked as `OWNER_INPUT_NEEDED.md` item 48. — Claude Code (Sonnet 5)
- 2026-07-03 — Updated §2a with real candidate tool names for Transitions/VFX (After Effects, Lottie) and 3D/5D Motion (Blender, Cinema 4D, Spline, Rive), sourced from Experience Engineering (20)'s founding session — partially informs, does not resolve, item 48 (SFX/Sound Design still genuinely unnamed). Added a note distinguishing this table's asset-authoring tools from Experience Engineering's own code-library tech stack. Cross-referenced the new `PROMPTING_SYSTEM.md` from §4's Skill Catalog. — Claude Code (Sonnet 5)
- 2026-07-04 — Added 4 further §2a rows from an owner-supplied raw tool list (full triage in `DESIGN_INSPIRATION.md`): Khroma (new Color/Palette category), Jitter (Motion Graphics/Video-as-Code), Threlte + Theatre.js (3D/5D Motion), 21st.dev (new UI Component/Design-Engineering Reference category). Further partially informs, does not resolve, item 48 — none configured/connected. Several other names in the raw list were low-confidence or unverified and were deliberately left out of this table rather than guessed at — see `DESIGN_INSPIRATION.md` for the full confidence triage. — Claude Code (Sonnet 5)
- 2026-07-04 — Added a 5th §2a row: **PeachWeb** (`https://www.peachweb.io/`), confirmed via an owner-supplied URL and cross-checked via web search — a no-code interactive-3D-website builder, an alternative/adjacent candidate to Spline. Moved out of `DESIGN_INSPIRATION.md`'s Reference Galleries list since it's a tool, not a browsable inspiration source. — Claude Code (Sonnet 5)
- 2026-07-04 — **SFX/Sound Design named for the first time**: Boom Library, Sonniss, Pro Sound Effects (Useful Interface), SoundMorph, Soundly, via an owner-relayed AI session — closes the "genuinely empty" gap flagged 2026-07-03, though none are adopted/licensed/connected yet. **Owner also confirmed adoption** (selection only, not connection) of every other candidate tool in this table and in Experience Engineering's overlapping motion/3D list — resolves tracker items 48/49's selection half; real MCP/integration links remain deferred (items 36/48's connection half, unchanged). — Claude Code (Sonnet 5)
