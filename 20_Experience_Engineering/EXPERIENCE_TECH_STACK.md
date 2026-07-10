# Experience Tech Stack — Motion, 3D & Pipeline Spec

**Status:** Proposed, not built. Sourced from an owner-relayed external AI session (2026-07-03) — cross-referenced from [`EXPERIENCE_ENGINEERING_OS.md`](EXPERIENCE_ENGINEERING_OS.md) §3, §4, §10. Same sibling-file rationale as Design's `19_Design/DESIGN_LANGUAGE_SYSTEM.md`: this grows independently of the OS file's doctrine section as real tool decisions and real pipeline steps get confirmed.

---

## 1. Why this exists

The source material names a specific front-end/motion/3D technology stack and two different candidate production-pipeline sequences for building interactive experiences. None of it is connected in this repo's `.mcp.json`; none of it has been confirmed adopted by the owner (distinct from Canva/OpenArt, which were verified via live API calls). This file exists so the real candidate names have a durable home instead of living only in conversation history — per `GLOBAL_OS.md` §2's "log it, don't just say it" convention — while staying honest about what's actually decided (nothing, yet).

## 2. Motion Tech Stack

| Layer | Tool | Purpose | Status |
|---|---|---|---|
| Framework | React, Next.js | Core front-end framework for building interactive web experiences | Named via owner-relayed AI session (2026-07-03), not connected |
| Scroll / Motion | GSAP + ScrollTrigger | Scroll-driven animation — the core engine behind "scroll = time" scroll-scrubbed motion | Named, not connected |
| Scroll / Motion | Framer Motion | React animation library | Named, not connected |
| Scroll / Motion | Motion One | Lightweight web animation library, named alongside Framer Motion | Named, not connected |
| Scroll / Motion | Lenis | Smooth-scroll library | Named, not connected |
| Scroll / Motion | Locomotive Scroll | Smooth-scroll library — the source itself flags this as "historically popular," i.e. a superseded/legacy candidate, not a live recommendation | Named as superseded in the source itself, not a live candidate |
| 3D | Three.js | Core WebGL/3D scene library | Named, not connected |
| 3D | React Three Fiber | React renderer for Three.js | Named, not connected |
| 3D | Drei | Helper-component library for React Three Fiber | Named, not connected |
| 3D | Threlte | Svelte component framework built on Three.js — a Svelte-ecosystem alternative to React Three Fiber | Named via owner-supplied tool list (2026-07-04), not connected |
| Scroll / Motion | Theatre.js | JS animation/keyframe-sequencing library, commonly paired with Three.js for cinematic camera work | Named via owner-supplied tool list (2026-07-04), not connected |
| 3D Authoring | Blender | Open-source 3D modeling/animation software (desktop, not MCP-queryable) | Named, not connected |
| 3D Authoring | Cinema 4D | 3D modeling/animation software (desktop) | Named, not connected |
| 3D Authoring | Spline | Browser-based real-time 3D design tool, exports to web | Named, not connected |
| 3D Authoring | Rive | Real-time interactive vector animation tool/runtime | Named, not connected |
| Motion Graphics | After Effects | Motion-graphics/VFX authoring (desktop) | Named, not connected |
| Motion Graphics | Lottie | JSON animation export/runtime format, typically paired with After Effects | Named, not connected |
| Motion Graphics | SVG animation | Native vector animation | Named, not connected |

The owner's 2026-07-04 tool list also re-named Three.js and Framer Motion (as "Three.JZ" and "npm i framer motion") — treated as reconfirmation of the existing rows above, not new tools. Full raw list and confidence triage for names Claude couldn't confidently identify: `19_Design/DESIGN_INSPIRATION.md`.

Every row: **named via owner-relayed AI session (2026-07-03) or owner-supplied tool list (2026-07-04), not connected — no MCP/integration link exists in this repo's `.mcp.json`, and none of these have been personally confirmed-adopted by the owner** (distinct in kind from Canva/OpenArt, which are real connected accounts, verified via live API calls — see `13_Tech_Stack/TECHSTACK_OS.md` §3). Cross-reference: Design (19)'s own `19_Design/DESIGN_LANGUAGE_SYSTEM.md` §2a Motion/VFX/SFX/3D-5D Tool Registry covers *asset-authoring* tools Design invokes directly (Blender/Cinema4D/Spline/Rive/After Effects/Lottie overlap both registries deliberately, since Design may author 3D/motion assets that Experience Engineering then assembles into a live build) — the code libraries here (React/Next.js/GSAP/Framer Motion/Motion One/Lenis/Three.js/R3F/Drei) are specific to *building* an interactive experience, not asset authoring, and stay in this file only.

## 2a. Motion Library — reusable animation primitives

Named in the source under "Motion System... instead of making animations every project, build a library... eventually 200+ reusable animations." 20 primitives named as a starting set:

Fade, Slide, Rotate, Scale, Morph, Elastic, Physics, Liquid, Magnetic, Particle, Blur, Glass, Ribbon, Wave, Parallax, Camera Zoom, Camera Orbit, Explosion, Assembly, Disintegration.

**Status: named, not built as real reusable code yet.** No implementation exists for any of these as an actual reusable component/function in this repo. Cross-ref `EXPERIENCE_ENGINEERING_OS.md` §3 "Motion System" row.

## 3. Creative Pipeline — reconciled, 2026-07-04

**Original source drafts, preserved verbatim for audit trail:**

**Draft A (13 steps)** — "Agencies Treat Them Like Film Production":
```
Discovery → Narrative → Creative Direction → Storyboard → Wireframes →
Motion Storyboards → 3D Production → Video Production → UI Design →
Development → Performance Optimization → Testing → Launch
```

**Draft B (16 steps)** — "Creative Pipeline... I would make this non-negotiable":
```
Business Strategy → Brand Research → Narrative → Scene Planning →
Storyboarding → Wireframing → Moodboards → Art Direction → Motion Direction →
3D Production → UI Design → Content → Development → QA → Optimization → Launch
```

**Resolved** (`00_Agency_Governance/OWNER_INPUT_NEEDED.md` item 52, `GO_LIVE_CHECKLIST.md` item 34) — for the same reason and by the same method the AI Creative Orchestra's two rosters were reconciled into 11 canonical roles rather than picking one draft: both source drafts are genuinely non-identical but non-contradictory, so this is a union, not a choice.

**Canonical Creative Pipeline (17 steps):**
```
Business Strategy → Brand Research → Narrative → Scene Planning →
Creative/Art Direction → Moodboards → Storyboarding → Wireframing →
Motion Direction → 3D Production → UI Design → Video Production →
Content → Development → QA/Testing → Performance Optimization → Launch
```

**Traceability** (every canonical step maps to one or both original drafts — nothing invented):

| # | Canonical step | From Draft A (13 steps) | From Draft B (16 steps) |
|---|---|---|---|
| 1 | Business Strategy | implicit in "Discovery" | Business Strategy |
| 2 | Brand Research | implicit in "Discovery" | Brand Research |
| 3 | Narrative | Narrative | Narrative |
| 4 | Scene Planning | implicit in "Creative Direction" | Scene Planning |
| 5 | Creative/Art Direction | Creative Direction | Art Direction |
| 6 | Moodboards | — | Moodboards |
| 7 | Storyboarding | Storyboard | Storyboarding |
| 8 | Wireframing | Wireframes | Wireframing |
| 9 | Motion Direction | Motion Storyboards | Motion Direction |
| 10 | 3D Production | 3D Production | 3D Production |
| 11 | UI Design | UI Design | UI Design |
| 12 | Video Production | Video Production | — |
| 13 | Content | — | Content |
| 14 | Development | Development | Development |
| 15 | QA/Testing | Testing | QA |
| 16 | Performance Optimization | Performance Optimization | Optimization |
| 17 | Launch | Launch | Launch |

Draft A's single "Discovery" step is split into Draft B's more granular "Business Strategy" + "Brand Research" (both pre-narrative research stages — kept separate since they're genuinely distinct activities, not synonyms). Draft B's "Moodboards" and "Content" steps had no Draft A counterpart and are adopted as real, distinct steps. Draft A's "Video Production" had no Draft B counterpart (Draft B likely folds it into "Content") and is kept as its own step since video is a distinct production output from copy/text content.

This is now the department's one authoritative Creative Pipeline — both original drafts are preserved above only for audit-trail purposes, not as live alternatives.

## 4. MCP Integration Categories

The source names 10 capability categories a "studio" needs, framed as "what capabilities does my studio need" rather than "which MCPs should I install":

Design file access (example given: Figma), Project management (example: Linear, ClickUp), Documentation (example: Notion), Code repositories (example: GitHub), Asset storage (example: Google Drive/cloud storage), Browser automation for testing, Design inspiration libraries, CMS and content management, Analytics, Deployment platforms.

**This is not a second tool inventory.** `13_Tech_Stack/TECHSTACK_OS.md` §3 remains this repo's one canonical, real tool inventory. Cross-checking against it: **Notion** is already a real, proposed entry there (registered per `GLOBAL_OS.md`'s 2026-07-01 changelog entry); every other category above has no tool chosen in this repo yet — "proposed category, no tool chosen," not a gap unique to this file.

## 5. Registration note

Once any tool named in §2 or §2a is confirmed/connected, add a real row to `13_Tech_Stack/TECHSTACK_OS.md` §3 (same pattern already used for Canva/OpenArt/Remotion) and cross-link back to this file. This file is the design-surface/production view; Tech Stack (13) stays the canonical inventory of record.

## Changelog

- 2026-07-03 — File created alongside Experience Engineering (20)'s founding. Captures the Motion Tech Stack, the 20-item Motion Library, both non-identical Creative Pipeline drafts (13-step and 16-step), and the 10 MCP integration categories from the owner-relayed source session — none connected, none confirmed-adopted. — Claude Code (Sonnet 5)
- 2026-07-04 — Added Threlte and Theatre.js to §2's Motion Tech Stack table, from an owner-supplied raw tool list (full triage in `19_Design/DESIGN_INSPIRATION.md`). Noted that the same list re-confirmed (via typo'd names) Three.js and Framer Motion, already present. Neither addition is connected or confirmed-adopted — same status as every other row in this table. — Claude Code (Sonnet 5)
- 2026-07-04 — **§3 Creative Pipeline reconciled** into one canonical 17-step sequence (union of both drafts, full traceability table), per owner direction to resolve tracker item 52 the same way the AI Creative Orchestra roster was reconciled — closing `OWNER_INPUT_NEEDED.md` item 52 and `GO_LIVE_CHECKLIST.md` item 34. Both original drafts kept verbatim above for audit trail. Prompted by scoping the first real Experience Engineering project — `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md`. — Claude Code (Sonnet 5)
