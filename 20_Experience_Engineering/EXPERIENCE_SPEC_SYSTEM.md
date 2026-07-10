# Experience Spec System — the Design-the-Spec discipline

**Status:** Real and runnable — the six stations map onto Experience Engineering (20)'s existing 11 agents (no new roles) and four real skills (`.claude/skills/`). Aligned into this repo 2026-07-09 from the owner's "Design Department" plugin + Elite Web Build reference set. Cross-referenced from [`EXPERIENCE_ENGINEERING_OS.md`](EXPERIENCE_ENGINEERING_OS.md) §3, §6, §10.

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) §2 first. This is a sibling spec file of Experience Engineering (20), same status as `EXPERIENCE_TECH_STACK.md`, `AI_CREATIVE_ORCHESTRA.md`, and `PROMPTING_SYSTEM.md`.

---

## 0. What this is, and why it lives in Experience Engineering (20)

The owner supplied a fully-formed "Design Department" plugin — a six-station assembly line that turns a brief into a build-ready spec for an interactive website, plus a four-document reference set (the elite stack, the feasibility-tier engine, the run-sheet, and the discoverability layer). Despite the word "Design" in its name, **it is not about Design (19)** — Design (19) produces *assets* (images, video, motion primitives, Canva assemblies). This system specs and builds *interactive websites* (Next.js · Tailwind · GSAP · Lenis · Spline), which is **Experience Engineering (20)'s** mandate. Its stack is line-for-line identical to `EXPERIENCE_TECH_STACK.md`. So it is homed here, as the department's **front-half discipline**: the "Design the Spec" phase that precedes the build.

**What it adds that the department didn't already have codified:**
1. A **runnable, gated, station-by-station spec process** — turning EE's soft front-of-pipeline into an owner-facing assembly line with a mandatory audit before build.
2. **Seven hard design laws** — hardening EE's Visual/Motion/Interaction "Language Systems" (`EXPERIENCE_ENGINEERING_OS.md` §3) into enforceable, checkable rules.
3. A genuinely new **Discoverability & Architecture pillar** (SEO/AEO/GEO + frontend/backend "buy don't build") — the one thing EE had no home for. See `build-system/discoverability-architecture.md`.

**The one law of this system:** *nothing moves to build until the spec is complete enough that a stranger — or an agent — could execute it with zero questions.* If the build would have to guess, the spec isn't finished.

**What it is NOT:** the brief (the input — purpose/audience/feeling, which comes from the project scope, e.g. `ARIKA_WEBSITE_PROJECT.md`) and not the build (the output's destination — the Technical Director's Next.js build, Framer, v0/Bolt, or Spline).

---

## 1. The data contract — inputs and outputs

### INPUT (required before Station 1; if any is missing, go back to the project scope)
- **Purpose** — what the site is for, one sentence.
- **Audience** — who it's for (for Arika: Sector 01's real B2B-SaaS 3-tier ICP).
- **One feeling** — the single emotion it should provoke. *One.*
- **Must-have sections** — the non-negotiable content.
- **Hard constraints** — the Brand Genome (`12_Branding/BRANDING_OS.md` §2) is a hard constraint for every Arika build, plus deadline/budget tier.

### OUTPUT (the department is "done" only when all five exist)
1. **Sitemap** — every page, section, and the data each section needs.
2. **Reference set** — 3–6 named techniques, each tagged Tier 1/2/3.
3. **Wireframe** — a low-fi layout per page.
4. **Style tokens** — type scale, color, spacing, radius, one motion curve (derived from the Brand Genome).
5. **The filled master build prompt** — all of the above assembled, self-audited.

Store the five in a per-project spec folder: `docs/design/` inside the build repo (e.g. `20_Experience_Engineering/arika-website/docs/design/`), or `20_Experience_Engineering/<project>/spec/` when speccing a project that has no site repo yet. That folder *is* the deliverable that hands to the Creative Pipeline (`EXPERIENCE_TECH_STACK.md` §3).

---

## 2. The six stations → the 11 real agents (no new roles)

The stations are the owner-facing view; each is performed by agents that **already exist** under `.claude/agents/experience-engineering-*.md`. This is why the system needed no new roster — it is the operating manual for the roster EE already built (2026-07-04).

| # | Station | Turns… | …into | Real agent(s) | Skill |
|---|---|---|---|---|---|
| 1 | **Creative Direction** | the brief | one art-direction sentence + moodboard | Creative Director (+ Brand Strategist check) | `/creative-direction` |
| 2 | **Sitemap** | the direction | pages, sections, data-per-section | UX Strategist (+ Narrative Architect for scene order) | `/sitemap-and-refs` |
| 3 | **Reference Pull** | the sitemap | 3–6 named techniques, tiered | Motion Director + 3D Director + Technical Director (tiering) | `/sitemap-and-refs` |
| 4 | **Wireframe** | references + sitemap | low-fi layout per page | UI Designer | *(manual / Whimsical / Relume)* |
| 5 | **Style Tokens** | direction + wireframe | the fixed visual language | UI Designer (consumes Brand Genome + Design 19's Design Language System) | `/design-tokens` |
| 6 | **Spec Assembly + Audit** | all of the above | one build-ready prompt, self-checked | Creative Director (creative gate) + QA & Performance Reviewer (technical gate) | `/design-audit` |

### Station 1 — Creative Direction
Decide the emotional target and art direction before any layout exists. Output: one north-star sentence (e.g. *"Executive infrastructure meets editorial UGC — deep-navy canvas, oversized serif headlines over glass/metal grids, champagne-gold used only on the metric that matters, motion that settles rather than bounces"*) + a ≤9-image moodboard. For Arika, this sentence must answer to the Brand Genome and the Creative Digital Twin room doctrine (`19_Design/DESIGN_OS.md` §10) — it does not invent a new aesthetic per project. The Brand Strategist agent checks it against Branding (12) rather than re-doing brand strategy.

### Station 2 — Sitemap
Information architecture: pages → sections → **the data each section needs** (the data note is what makes the build data-driven, law #7). For Arika, reconcile against the real Phase 1 sitemap in `ARIKA_WEBSITE_PROJECT.md` §3, Content (04)'s 7 pillars, and the Narrative Architect's Scene Architecture — don't produce a blank-slate tree.

### Station 3 — Reference Pull
Translate the moodboard's feelings into **named techniques**, each honestly tiered (see `build-system/vision-to-build-pipeline.md`):
- **Tier 1** — the Technical Director builds it directly (most scroll/type/layout effects: Lenis, SplitText, pin-and-scrub, horizontal scroll, video mask).
- **Tier 2** — Design (19)'s Spline/3D authoring produces the scene, the Technical Director embeds it (no hand-written shaders).
- **Tier 3** — bespoke WebGL/shaders/navigable 3D worlds: the 3D Director flags it and it is justified or cut. Do not promise Tier 3 as shippable-alone.

### Station 4 — Wireframe
Layout and focus hierarchy before styling. Carry in law #1: 12-column grid, asymmetric desktop splits (7/5, not 6/6), everything stacks to `col-span-12` on mobile, full-height sections `min-h-[100dvh]`. Place the Station-3 techniques into their zones. Tool: Whimsical or Relume (both named/not-yet-confirmed for this repo — see `13_Tech_Stack/TECHSTACK_OS.md` §3); pen and paper is fine for low-fi.

### Station 5 — Style Tokens
Lock the fixed language, math-derived, per §3 laws. Pull the *method* from `build-system/elite-web-build-system.md` §2 (one type ratio, opacity tiers as greys, one motion curve) but the *values* from the Brand Genome. Output a `content.config.ts`-ready token block. This is also where Design (19)'s `DESIGN_LANGUAGE_SYSTEM.md` token surface and this system meet — same tokens, one source of truth (Branding 12), consumed by both departments.

### Station 6 — Spec Assembly + Self-Audit
Assemble Stations 1–5 into one master build prompt (Elite Web Build System §6 shell), then run `/design-audit` — the **mandatory gate**. The Creative Director runs the creative-readiness check (the Creative DNA 7 questions, `EXPERIENCE_ENGINEERING_OS.md` §10); the QA & Performance Reviewer runs the technical-readiness check (the 7 laws + discoverability). Both must pass. Only then does the spec fold into the Creative Pipeline at the Development step.

---

## 3. The seven non-negotiable design laws

Hardened from EE's §3 Language Systems into checkable rules. The `design-audit` skill checks every one.

1. **Asymmetric grid.** 12-column; desktop asymmetric (7/5, not 6/6); mobile stacks to `col-span-12`; full-height sections use `min-h-[100dvh]`, never `h-screen`.
2. **One type ratio.** A single modular scale; every size derived from it; display headings use `clamp()`.
3. **Restraint reads as luxury.** One canvas, one or two accents, opacity tiers as the grey scale. Never pure `#FFF` on pure `#000`. (For Arika: the Brand Genome *is* the palette — gold is accent-only.)
4. **One motion curve.** A single easing language across the whole site — chosen at token time, not improvised in the build. This is the same "one motion curve" that lives in EE's Motion Language System.
5. **Respect `prefers-reduced-motion`.** Gate all scroll animation behind `gsap.matchMedia()`. (Same doctrine as the §9 Risk-Log note: spectacle that sacrifices accessibility is a quality failure.)
6. **Real text in HTML.** Headings are real text, not baked into effects — for findability and accessibility. This is the same rule as the discoverability pillar's SSR/semantic-HTML requirement.
7. **Data-driven from day one.** Never hardcode content in JSX. Lift it into `content.config.ts` and map over it, so swapping in a real API (or CMS) later is a one-line change.

---

## 4. The tool stack for this discipline

Deliberately small.

| Station | Primary tool | Status in this repo |
|---|---|---|
| Creative Direction | Design (19) Inspiration Brackets + moodboard search | Inspiration Brackets real but empty (`19_Design/DESIGN_INSPIRATION.md`) |
| Sitemap / Wireframe | Whimsical, or Relume | Whimsical: source claims connected — **unverified in this repo** (`.mcp.json` has no Whimsical); Relume MCP present but needs auth |
| Style Tokens | Elite Web Build System §2 method + Brand Genome | Brand Genome real and confirmed (`12_Branding/BRANDING_OS.md` §2) |
| Spec Assembly | The master shell (Elite Web Build System §6) | Real reference doc, `build-system/` |
| Build (destination) | Next.js (the Arika path) / Framer / v0 / Bolt / Spline | Next.js real (`arika-website`); the rest named, not connected |

---

## 5. The per-project run-sheet (the audit gate, Station 6)

Tick every box before the spec leaves the discipline. This is the checklist the `design-audit` skill runs.

**Intake**
- [ ] Purpose, audience, and *one* feeling written down
- [ ] Must-have sections listed
- [ ] Hard constraints noted (Brand Genome referenced, not re-invented)

**Design**
- [ ] Art-direction sentence locked and traceable to the Brand Genome (Station 1)
- [ ] Moodboard ≤ 9 images
- [ ] Sitemap: every section names the data it needs (Station 2)
- [ ] 3–6 techniques named AND tiered; every Tier-3 justified or cut (Station 3)
- [ ] Wireframe per page, asymmetric grid, mobile-stacked (Station 4)
- [ ] One type ratio; canvas + accents + opacity tiers set from the Brand Genome (Station 5)
- [ ] Exactly ONE motion curve chosen

**Handoff audit (Station 6 — both gates)**
- [ ] Content lifted into a config object, not hardcoded (law #7)
- [ ] `prefers-reduced-motion` gate included (law #5)
- [ ] Real text in headings, not baked into effects (law #6 + discoverability)
- [ ] SSR/semantic-HTML/schema/Search-Console checklist run (`build-system/discoverability-architecture.md` §3)
- [ ] Creative DNA 7 questions pass (`EXPERIENCE_ENGINEERING_OS.md` §10)
- [ ] The build prompt reads so a stranger could execute it with zero questions

If all boxes tick, ship to the Creative Pipeline's Development step. If not, the discipline isn't done.

---

## 6. Reference material

Full detail lives in `20_Experience_Engineering/build-system/`:
- `elite-web-build-system.md` — the stack, tokens, grid, scrolltelling, master prompts (the build bible)
- `vision-to-build-pipeline.md` — the Tier 1/2/3 feasibility engine + Reference Library template
- `workflow-run-sheet.md` — the four-phase human run-sheet for one build
- `discoverability-architecture.md` — the frontend/backend split + SEO/AEO/GEO pillar

And the runnable skills in `.claude/skills/`: `creative-direction`, `sitemap-and-refs`, `design-tokens`, `design-audit`.

**Visual walkthrough:** [`EXPERIENCE_SPEC_SYSTEM.html`](EXPERIENCE_SPEC_SYSTEM.html) (this folder) — a self-contained, browsable one-page walkthrough of this system (the six stations, seven laws, feasibility tiers, tokens, discoverability pillar, and audit gate). Deliberately styled in the real Brand Genome (`12_Branding/BRANDING_OS.md` §2) so the page itself obeys the seven laws it explains. Open it directly in a browser — no build step or network needed.

---

## Changelog

- 2026-07-09 — File created. Aligned the owner's "Design Department" plugin + Elite Web Build reference set into Experience Engineering (20) as the department's codified spec discipline. Mapped the six stations onto EE's existing 11 agents (no new roles), hardened the seven design laws from EE's §3 Language Systems, and registered the previously-unowned Discoverability & Architecture pillar. Companion reference docs written to `build-system/`; four skills written to `.claude/skills/`. Did **not** copy the plugin's standalone `CLAUDE.md` (would create a second root-authority file, which `GLOBAL_OS.md` §2 forbids) — its rules are distilled here and into the skills instead. — Claude Code (Opus 4.8)
- 2026-07-09 — Added `EXPERIENCE_SPEC_SYSTEM.html`, a self-contained, browsable visual walkthrough of this system, styled in the real Brand Genome so the page demonstrates the seven laws while explaining them. Companion to this doc; opens standalone in any browser. — Claude Code (Opus 4.8)
