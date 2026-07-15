# Experience Engineering — Department OS

**Department:** Experience Engineering (20)
**Position in flow:** Horizontal support layer — sits downstream of Design (19) the same way Design sits downstream of Branding (12). Design curates/produces assets and motion primitives; Experience Engineering assembles them into finished interactive experiences (websites, presentations, product launches, interactive reports). Feeds Marketing (03)'s distribution and, once packaged as a client offer, Offer (02)'s future catalog. Reports into Agency Governance (00).
**Mandate:** Own the agency's interactive/experiential production discipline — scroll-driven, cinematic, motion- and 3D-native digital experiences — as its own department rather than a Design (19) sub-task, for Arika's own flagship builds first, and (once packaged) as a future client offer.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Experience Engineering is the agency's interactive/experiential production discipline — building whole interactive experiences (scroll-driven websites, motion- and 3D-native presentations, product launches, interactive reports) rather than individual creative assets. It exists because Design (19)'s mandate stops at asset production (storyboards, images, video, motion primitives assembled in Canva) — nothing in this repo before this owned whole-experience assembly *with code*: scroll orchestration, 3D scenes, camera language, live web builds. Also referred to in its source material as scrollytelling, scroll-driven storytelling, immersive web experiences, interactive storytelling, narrative web design, experiential websites, cinematic websites, motion-first web design, or interactive product storytelling — "these names overlap depending on the agency" (see `EXPERIENCE_ENGINEERING_VISION.md` §2).

**The naming/numbering decision here is real, made directly by the owner in this planning session** — "Experience Engineering," department 20, chosen over three alternatives (Interactive Experience Lab, Digital Storytelling Lab, Creative Technology Division), positioned downstream of Design (19). **Everything else in this file** — the 16-system architecture, the AI Creative Orchestra, the tool names, the Experience Pattern Library, and the framing ideas below — is captured from an owner-relayed external AI chat session, not Claude's own analysis or an owner-confirmed operating decision. Full source text preserved in [`EXPERIENCE_ENGINEERING_VISION.md`](EXPERIENCE_ENGINEERING_VISION.md); this file is the distilled/structured version.

**Positioning frame** (from the source, captured as context): a 3-layer hierarchy — **Business Operating System** (how the business operates, makes money, decides) → **Experience Operating System** (how the business communicates, educates, sells, creates memorable experiences — this department) → **Delivery Systems** (the outputs). The source names 16 candidate output types this department could eventually produce: website, presentation, pitch deck, sales deck, social carousel, interactive report, annual report, proposal, product launch, trade show display, investor portal, training platform, learning experience, mobile app, dashboard, digital signage. None of these are committed production lines yet — see §2 Status.

**Dual mandate**, same pattern as Design (19) and Automation (16): internal flagship builds first (Arika's own website/presentations, once scoped — §4), a future sellable "Experience Intelligence System" offer for other businesses later (cross-ref Offer, 02 — not built here, same "pattern noted, not built" treatment Automation gives its own internal-automation angle). The source illustrates this with industry examples (real estate, hospital, manufacturing, university delivery-output lists) — captured in `EXPERIENCE_ENGINEERING_VISION.md` §4 as illustrative only, not real Arika engagements.

**Cross-department narrative-layer note (3-way distinction — was 4-way until 2026-07-15).** Three different "narrative" concepts exist across this repo and are not duplicates or a conflict — they operate at different altitudes:
1. Content (04)'s Story Architecture (`04_Content/CONTENT_OS.md` §10): `Problem → Insight → Demonstration → Framework → Proof → Action` — the **content-sequencing layer** (how one piece of content is paced).
2. Branding (12)'s Narrative Engineering stack (`12_Branding/BRANDING_OS.md` §3): Truth Core → Narrative Framework → Narrative Modules → Translation Layer → Feedback/Evolution — the **brand-identity layer** (why the brand exists).
3. This department's **Narrative Arc** (§3): **`Attention → Problem → Transformation → Proof → Offer`** — the **experience-orchestration layer**, sitting *above* Content's Story Architecture: one multi-scene interactive experience may itself contain many Story-Architecture-sequenced content pieces.

**Items 3 and 4 were previously two unreconciled candidate arcs** (a 5-stage and a 9-stage version, from two points in the same pasted source conversation). **Reconciled 2026-07-15** into the single canonical arc above — settled by this department's own Scene Architecture, which independently corroborates that ordering. Full reasoning, the absorption map for the 9-stage version's extra beats, and why Retention was routed out to Client Success (07)/`marketing-lifecycle` (03): §3's Narrative Engine reconciliation note. Both original drafts remain preserved verbatim in `EXPERIENCE_ENGINEERING_VISION.md` §2/§3 — nothing was deleted, only subordinated. See `04_Content/CONTENT_OS.md` §10 and `12_Branding/BRANDING_OS.md` §3 for their own copies of this note.

## 2. Status

**Newly created department (2026-07-03)**, seeded entirely from an owner-relayed external AI chat session — not yet operationally run against a real project or client. **Updated 2026-07-04**: the department's Agent Roster (§5) is now real and invokable — 11 Claude Code subagents, not a proposed roster — making this the first department in this repo with a live agent layer from its founding week. **Updated again 2026-07-04**: the first real project is now scoped — Arika's own flagship website (`ARIKA_WEBSITE_PROJECT.md`), closing tracker item 51 — and the Creative Pipeline is reconciled into one canonical sequence (`EXPERIENCE_TECH_STACK.md` §3), closing tracker item 52. **Updated again same day**: Relume/Canva/OpenArt were re-verified live (earlier "blocked"/"needs auth" readings were stale) and a real build has started — a Next.js site at `20_Experience_Engineering/arika-website/` with a fully built Homepage (`ARIKA_WEBSITE_PROJECT.md` §7). This is the first genuinely real, running artifact this department has produced — not just architecture documentation. **Updated 2026-07-07**: the site is now fully built (all 14 Phase 1 pages, 5 real generated images, the real Arika logo wired into Navbar/Footer/favicon) and **deployed to production on Vercel** — `https://arika-agency-website.vercel.app`, all routes verified live. One owner action remains before the custom domain goes live (`arikaagency.com` DNS record at Zoho Domains — `ARIKA_WEBSITE_PROJECT.md` §7, `GO_LIVE_CHECKLIST.md` item 30). Everything else remains architecture-only: zero connected motion/3D tools in this repo's `.mcp.json`, and the Capability Registry (§3) below is still proposed/not-built except where it explicitly says otherwise. **Updated 2026-07-09**: the department's front-half **spec discipline** is now codified and runnable — [`EXPERIENCE_SPEC_SYSTEM.md`](EXPERIENCE_SPEC_SYSTEM.md) (the six-station "Design the Spec" process), four reference docs in [`build-system/`](build-system/), and **four real skills** in `.claude/skills/` (`creative-direction`, `sitemap-and-refs`, `design-tokens`, `design-audit`), aligned from the owner's "Design Department" plugin + Elite Web Build reference set. The six stations map onto the existing 11 agents (no new roles); the seven hard **design laws** and a previously-unowned **Discoverability & Architecture** pillar (SEO/AEO/GEO + frontend/backend) are added to §10. This is process/standard/skill work, not new tool connections — the tool-connection status above is unchanged.

**Two ideas from the source are explicitly flagged as far-future and NOT built as structure in this pass** — no folder, no OS file, no registry entry for either:
- An **"Enterprise Experience Operating System (EXOS)"** sitting above this and every other department's experience work (12-subsystem breakdown captured in `EXPERIENCE_ENGINEERING_VISION.md` §4).
- A future **"Experience Science"** department studying *why* experiences work (psychology/neuroscience/behavioral economics/etc. — 12-discipline breakdown, also captured in the vision file §4).

## 3. Capability Registry

Grouped rather than a flat list, since the source names ~25 distinct systems/sub-inventories across two inconsistent drafting passes (a 9-item outline in Pass 1 that doesn't cleanly match its own 9 elaborated section headers, then "16 systems" in Pass 2 that aren't a clean superset — see `EXPERIENCE_ENGINEERING_VISION.md` for the full source text). Every row below: **Proposed — owner-relayed AI session, 2026-07-03, architecture only, not built.**

### Strategy Layer

| Capability | Description | Status |
|---|---|---|
| Business Strategy System | Inputs: business model, revenue goals, customer journey, KPIs, competitive positioning, market research. Outputs: experience strategy, conversion strategy, success metrics | Proposed, name/inputs/outputs only |
| Experience Strategy System | Answers 5 questions before any design starts: why should this experience exist? What should people feel? What should people remember? What should people do next? How does this support revenue? | Proposed |

### Narrative & Scene Layer

| Capability | Description | Status |
|---|---|---|
| Narrative Engine | **✅ RECONCILED 2026-07-15 — one canonical arc.** **`Attention → Problem → Transformation → Proof → Offer`** (5 stages, formerly "Draft A"). Draft B's 9 stages are absorbed, not discarded — see the reconciliation note below | **Canonical** — owner-confirmed among 4 options; the department's last unreconciled source conflict, now closed |
| Scene Architecture | `Opening → Hook → Discovery → Problem → Transformation → Features → Evidence → Testimonials → Offer → CTA → Ending` — "think like Pixar, not pages: scenes" | **Canonical scene-level expansion of the arc above** — and the evidence that settled the reconciliation |

**🔴→✅ Narrative Arc reconciliation (2026-07-15) — the department's last open source conflict, closed.** Two non-identical arcs had stood since founding, both preserved, neither canonical — while this department's *other* two source conflicts (the Creative Pipeline's 2 drafts, the AI Orchestra's 2 rosters) were both reconciled on 2026-07-04 by owner direction. This one was left because the drafts don't merely differ in granularity — **they disagree on order**:

| | Draft A (5) | Draft B (9) |
|---|---|---|
| | Attention → Problem → **Transformation → Proof** → Offer | Attention → Curiosity → Education → Trust → **Proof → Transformation** → Offer → Action → Retention |

A places Transformation **before** Proof; B places Proof **before** Transformation. A union cannot dodge that — an arc has one order.

**What settled it: this department's own Scene Architecture** (row above), a third sequence never previously compared against either draft. It independently runs `… Problem → **Transformation** → Features → **Evidence** → Testimonials → Offer → CTA …` — **Transformation before Evidence**, corroborating **Draft A's ordering** from inside the department's own material rather than from an outside preference.

**Canonical arc: `Attention → Problem → Transformation → Proof → Offer`.** Draft B's extra beats are **absorbed, not dropped** — each already had a home:

| Draft B beat | Absorbed into | Why |
|---|---|---|
| Curiosity, Education | Scene Architecture's **Discovery** | Same function at scene granularity |
| Trust | Scene Architecture's **Evidence / Testimonials** | Trust is what proof produces, not a separate beat |
| Action | Scene Architecture's **CTA** | Same beat, different name |
| **Retention** | **Routed out** — Client Success (07) + `marketing-lifecycle` (03) | **Not an experience beat.** A website visit doesn't retain; a relationship does. Retention already has two real owners; importing it here would have duplicated their mandates — the same scope-collision this department caught twice on 2026-07-04 (Brand Strategist vs Branding 12; Copywriter vs Offer 02) |

The 4-way cross-department narrative note (§1) still holds — this reconciliation collapses items 3 and 4 into one, making it a **3-way** distinction: Content (04)'s content-sequencing layer, Branding (12)'s brand-identity layer, and this department's single experience-orchestration arc. Mirrored in `04_Content/CONTENT_OS.md` §10 and `12_Branding/BRANDING_OS.md` §3.

### Language Systems

| Capability | Description | Status |
|---|---|---|
| Emotional Design System | 11-item emotion library: Wonder, Luxury, Speed, Innovation, Security, Curiosity, Confidence, Exclusivity, Urgency, Delight, Nostalgia — "design emotions, not just interfaces" | Proposed |
| Visual Language System | 9 items: Composition principles, Grid systems, Typography hierarchy, Iconography, Illustration styles, Photography direction, Lighting direction, Material language, Color psychology | Proposed — overlaps Branding's identity work and `19_Design/DESIGN_LANGUAGE_SYSTEM.md` §1's token surface; not a competing spec, just captured |
| Motion Language System | 7 motion "dialects" (Premium, Playful, Minimal, Luxury, Tech, Industrial, Organic), each parameterized by Timing/Easing/Speed/Acceleration/Deceleration/Curves/Scale | Proposed — likely overlaps the Motion System capability below (both named across the source's two passes) |
| Interaction Design System | 9 items: Scroll behavior, Cursor interactions, Hover states, Click feedback, Gestures, Drag interactions, Touch interactions, Keyboard interactions, Accessibility interactions. Includes the source's AI-personalization example (site content/animation changes by visitor-selected role, e.g. "Marketing Manager" vs. "Architect") | Proposed |

### Production Systems

| Capability | Description | Status |
|---|---|---|
| Motion System | 15 motion categories (Entrance/Exit/Hover/Camera/Scroll/Depth/Object/Background/Cursor Motion, Page Transition, Micro Interaction, Text/Video/Loading/Idle Motion) plus a 20-primitive Motion Library (Fade, Slide, Rotate, Scale, Morph, Elastic, Physics, Liquid, Magnetic, Particle, Blur, Glass, Ribbon, Wave, Parallax, Camera Zoom, Camera Orbit, Explosion, Assembly, Disintegration) — full list in `EXPERIENCE_TECH_STACK.md` §2a | Proposed |
| Storyboard Library | Every scene sketched before development, 9-field entry template: Scene, Camera, Lighting, Object, Text, Narration, Motion, Interaction, Goal | Proposed — extends Design (19)'s existing storyboard-before-generation doctrine (`19_Design/DESIGN_OS.md` §10) to full multi-scene experiences |
| Experience Components | 11 named reusable "experiences" (bigger than UI components): Hero Experience, Product Reveal, Timeline Experience, Comparison Experience, Gallery Experience, Property Tour, Feature Reveal, Statistics Reveal, Pricing Experience, Checkout Experience, Footer Experience | Proposed |
| Camera System | 10 named camera moves: Zoom, Orbit, Track, Pan, Tilt, Reveal, Focus, Follow, Transition, Fly Through | Proposed |
| 3D Experience Framework | 8 items: Camera paths, Lighting, Materials, Textures, Scene optimization, Physics, Particle systems, Environmental effects | Proposed |
| Sound Design System | 7 items: Ambient audio, Product sounds, UI feedback, Transition effects, Spatial audio, Voice-over, Music direction | Proposed — overlaps Design (19)'s existing Sound sub-library (`19_Design/DESIGN_OS.md` §3 Asset Library); no tool/vendor named for this category anywhere in the source, stays genuinely open |

### Tech & Pipeline

| Capability | Description | Status |
|---|---|---|
| Motion Tech Stack | React, Next.js, GSAP+ScrollTrigger, Framer Motion, Motion One, Lenis, Three.js, React Three Fiber, Drei, Blender, Cinema 4D, Spline, Rive, After Effects, Lottie — full detail in `EXPERIENCE_TECH_STACK.md` §2 | Proposed — none connected |
| Creative Pipeline | Two non-identical candidate sequences from the source, both preserved (not merged): **Draft A** (13 steps) `Discovery → Narrative → Creative Direction → Storyboard → Wireframes → Motion Storyboards → 3D Production → Video Production → UI Design → Development → Performance Optimization → Testing → Launch`; **Draft B** (16 steps) `Business Strategy → Brand Research → Narrative → Scene Planning → Storyboarding → Wireframing → Moodboards → Art Direction → Motion Direction → 3D Production → UI Design → Content → Development → QA → Optimization → Launch` — full detail in `EXPERIENCE_TECH_STACK.md` §3 | Proposed |

### Intelligence & Orchestra

| Capability | Description | Status |
|---|---|---|
| AI Creative Orchestra | Two non-identical candidate rosters, both preserved — full contracts in `AI_CREATIVE_ORCHESTRA.md`: **Draft A** (10 roles, "AI Department") — Creative Director AI, Narrative AI, UX Strategist AI, Storyboard AI, Motion Director AI, 3D Director AI, Brand Strategist AI, Copywriter AI, Developer AI, QA AI; **Draft B** (12 roles, "AI Creative Orchestra") — Executive Creative Director, Brand Strategist, Narrative Architect, UX Strategist, UI Designer, Motion Director, 3D Artist, Technical Director, Front-end Engineer, QA Reviewer, Accessibility Reviewer, Performance Engineer | Proposed, not built — no LLM wiring, no Claude Code sub-agent definitions exist |
| Knowledge Graph | Two distinct knowledge concepts, both from the source: a **project-memory store** (8 items — previous projects, best practices, brand guidelines, animation recipes, successful storytelling patterns, technical solutions, performance benchmarks, case studies) and a separate **"internal academy" training corpus** (16 topics — Interaction Psychology, Color Psychology, Typography, Motion Psychology, Film Direction, Storytelling, Animation, Game Design, Camera Theory, 3D Lighting, Cinematography, Branding, UX, Behavioral Economics, Marketing, Sales Psychology) | Proposed — flagged as two distinct, non-competing concepts, not merged |
| Asset Intelligence System | 10 asset types with searchable metadata: Images, Icons, Videos, 3D models, Textures, Fonts, Music, Motion presets, UI components, Brand assets | Proposed — overlaps Design (19)'s Asset Library (`19_Design/DESIGN_OS.md` §3); same domain, not a competing inventory |
| Prompting System | Structured, ID'd, stateful prompt architecture for every generative step in the Creative Pipeline — full spec in [`PROMPTING_SYSTEM.md`](PROMPTING_SYSTEM.md) | Proposed, not built — zero real Prompt Records exist |

### Quality & Measurement

| Capability | Description | Status |
|---|---|---|
| Quality Assurance Framework | 11-item technical/production checklist: Business alignment, Narrative flow, UX quality, Accessibility, Performance, SEO, Animation quality, Browser compatibility, Mobile responsiveness, Code quality, Security | Proposed — distinct from the Creative DNA checklist below (that one is creative/story-level, this is technical/production-level) |
| Performance Engineering | 8 standards: Asset budgets, Frame rate targets, Core Web Vitals, GPU optimization, Lazy loading, Progressive loading, Image optimization, Font optimization | Proposed |
| Creative Research Department | 7 research topics: Competitors, Industry trends, Visual trends, Motion trends, User behavior, Audience expectations, Technical innovations | Proposed |
| Measurement & Continuous Improvement | 9 metrics: Scroll depth, Engagement, Time on page, Interaction rates, Conversion, Bounce rate, Heatmaps, Session recordings, A/B tests — feeds back into the Knowledge Graph's project-memory store per the source's own framing | Proposed |

### Governance & Reuse

| Capability | Description | Status |
|---|---|---|
| Creative Governance | A layer above all systems, not itself a system — 8 items: Creative principles, Technical standards, Naming conventions, Documentation requirements, Version control, Approval workflows, Review gates, Handoff standards | Proposed |
| Experience Pattern Library | 12 named reusable patterns (Product reveal, Before/after transformation, Timeline journey, Feature comparison, Property walkthrough, Manufacturing process, Founder story, Interactive case study, Data storytelling, Investment pitch, Sustainability impact, Portfolio showcase), each intended to carry a 9-field template (Business objective, Narrative structure, Storyboard, Motion choreography, 3D opportunities, **AI prompts**, Development implementation, Performance guidelines, QA checklist) | Proposed, zero real patterns built — the "AI prompts" field is the explicit link to `PROMPTING_SYSTEM.md` |

**Future offer angle (not built):** per the source, this architecture is intended to eventually generalize beyond Arika's own content into a sellable "Experience Intelligence System" offer for other businesses (real estate, hospitals, manufacturing, universities — see `EXPERIENCE_ENGINEERING_VISION.md` §4 for the illustrative industry breakdowns). Cross-reference Offer (02); not built here, just the pattern noted, same dual-mandate treatment Design (19) and Automation (16) already carry.

**Spec discipline & build standard (real, 2026-07-09).** The department's front-half — turning a brief into a build-ready spec — is now a codified, runnable discipline rather than a proposed capability: the six-station **Experience Spec System** ([`EXPERIENCE_SPEC_SYSTEM.md`](EXPERIENCE_SPEC_SYSTEM.md)), backed by four reference docs ([`build-system/`](build-system/): `elite-web-build-system.md`, `vision-to-build-pipeline.md`, `workflow-run-sheet.md`, `discoverability-architecture.md`) and four real skills (`.claude/skills/`). It reconciles with, rather than competes against, the Language Systems above: the Visual/Motion/Interaction Language Systems become the seven hard **design laws** (§10), and the previously-unowned **Discoverability & Architecture** pillar (SEO/AEO/GEO + frontend/backend "buy don't build") is added (§10). Aligned from the owner's "Design Department" plugin + Elite Web Build reference set — see the 2026-07-09 Decision Log entry.

## 4. Workflow Index

**Updated 2026-07-04 — role-to-agent mapping added**, now that the Agent Roster (§5) is real. **Updated again 2026-07-04 — tracker item 52 now resolved**: the Creative Pipeline is one canonical 17-step reconciled sequence, not two open drafts — see `EXPERIENCE_TECH_STACK.md` §3. The role-level handoff below was originally written to hold under either draft; it holds equally well under the reconciled version, since the reconciliation didn't change the underlying shape, just merged the two step-granularities.

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Creative Pipeline (experience build) | Design (19)'s Creative Production Pipeline output reaches an experience-scale project (a whole website/presentation, not a single asset) — **first real instance: the Arika website project, `ARIKA_WEBSITE_PROJECT.md`** | Canonical 17-step reconciled sequence — `EXPERIENCE_TECH_STACK.md` §3. **Role-level handoff**: **Narrative Architect** (Narrative Arc + Scene Architecture + Hook choice) → **UX Strategist** (interaction patterns) + **Brand Strategist** (voice/visual consistency check) → **Storyboard Artist** (9-field entry per scene) → **UI Designer** + **Motion Director** + **3D Director** (visual/motion/camera specs, in parallel) → **Copywriter** (scene copy) → **Technical Director** (build) → **Creative Director** (creative-readiness gate) + **QA & Performance Reviewer** (technical-readiness gate, both required) → Launch | Launched interactive experience | Mary Thuo | Owner-relayed AI session, 2026-07-03; role mapping added 2026-07-04; pipeline reconciled 2026-07-04 |

## 5. Agent Roster

**Real, invokable — built 2026-07-04.** The AI Creative Orchestra's 11 canonical roles are backed by real Claude Code subagents under `.claude/agents/experience-engineering-*.md`, callable via the Agent tool today. Full roster index, reconciliation history, and shared Creative Philosophy/Decision Framework/Output Structure live in the dedicated sibling file [`AI_CREATIVE_ORCHESTRA.md`](AI_CREATIVE_ORCHESTRA.md) — kept out of this file for the same reason Branding's 20-agent roster lives in `bois/agents/AGENT_SYSTEM.md` rather than inline in `BRANDING_OS.md` §5.

The 11 roles: Creative Director, Narrative Architect, UX Strategist, Storyboard Artist, UI Designer, Motion Director, 3D Director, Technical Director, Brand Strategist, Copywriter, QA & Performance Reviewer. Each file's content was built by reconciling this department's own two source-draft rosters with 11 additional owner-relayed "Sider Fusion" sessions (one per role) — every session was checked for runtime mismatches (several proposed standalone Python apps, live 3D/game engines, or robotics motion-planning systems that don't fit this repo's actual Claude-Code-subagent architecture) and department-scope collisions (the Brand Strategist thread duplicated Branding (12)'s mandate; the Copywriter thread partially overlapped Offer (02) and Branding (12)) before anything was adopted — full audit trail in `EXPERIENCE_ENGINEERING_VISION.md` §5.

This is the first department in this repo to have a real, invokable agent roster from day one, rather than a markdown-only proposed roster maturing later.

**✅ ALL 11 ON THE RUNTIME 2026-07-15 — and with them, the last legacy specs in the repo are gone.** Until now all 11 were quarantined: real, reconciled, invokable by hand, but carrying only `name` + `description`, so `arika-runtime` couldn't see them. **All 11 now have triggers, output schemas, risk classes, and event wiring; bodies untouched** — the reconciliation work of 2026-07-04 was already right, only frontmatter was missing. `arika list` → **80 agents**, **0 legacy specs remaining** (the migration's own regression test now asserts zero, having previously asserted "at least one legacy spec is skipped").

**The shared output schema is this department's own Communication Protocol, not an invention.** Every agent returns `vision` → `rationale` → `technical_notes` → `risks_contradictions` → `handoffs` (the Output Structure + return contract in [`AI_CREATIVE_ORCHESTRA.md`](AI_CREATIVE_ORCHESTRA.md)), plus the runtime's base advisory envelope and role-specific fields.

| Agent | Class | Triggers on | Emits |
|---|---|---|---|
| `narrative-architect` | 1 | `EXPERIENCE_PROJECT_SCOPED` | `NARRATIVE_ARC_SET` |
| `ux-strategist` | 1 | `NARRATIVE_ARC_SET` | `UX_PATTERNS_SET` |
| `brand-strategist` | 1 | `NARRATIVE_ARC_SET` | `EXPERIENCE_BRAND_CHECKED` |
| `storyboard-artist` | 1 | `UX_PATTERNS_SET` | `EXPERIENCE_STORYBOARD_READY` |
| `ui-designer` | 1 | `EXPERIENCE_STORYBOARD_READY` | `UI_SPEC_READY` |
| `motion-director` | 1 | `EXPERIENCE_STORYBOARD_READY` | `MOTION_SPEC_READY` |
| `3d-director` | 1 | `EXPERIENCE_STORYBOARD_READY` | `CAMERA_SPEC_READY` |
| `copywriter` | 1 | `UI_SPEC_READY` | `SCENE_COPY_READY` |
| `technical-director` | **2** | `SCENE_COPY_READY` | `BUILD_SPEC_READY` |
| `creative-director` | **2** | `BUILD_SPEC_READY` | `CREATIVE_GATE_PASSED` / `FAILED` |
| `qa-performance-reviewer` | **2** | `BUILD_SPEC_READY` | `TECHNICAL_GATE_PASSED` / `FAILED` |

**Risk classes:** the nine specification roles are **Class 1** — they produce specs and reasoning, touch nothing. The three that gate or build are **Class 2**: the Technical Director's output drives a real, **production-deployed** codebase (`arika-website`, live on Vercel), and the two launch gates decide what ships to the public.

**Schemas encode the department's own hard rules, so they can't be skipped:**
- The Narrative Architect's `narrative_arc` is an enum of exactly the **five canonical stages** (§3) — it cannot emit a different arc.
- The Storyboard Artist's `storyboard` requires all **9 fields** (Scene/Camera/Lighting/Object/Text/Narration/Motion/Interaction/Goal) — the repo-wide "8-field" mislabeling caught on 2026-07-04 can't recur.
- The UI Designer's `design_law_check` enumerates all **seven design laws** (§10).
- The Creative Director's `creative_dna_check` enumerates all **7 Creative DNA questions**; the QA Reviewer's `qa_checklist` enumerates all **11 QA Framework items** (§3). Both gates must answer every one.

## 6. Skill Library Index

**Updated 2026-07-09 — four skills are now real, not proposed.** The Experience Spec System's stations are backed by four real Claude Code skills under `.claude/skills/` — the department's first real skill layer of any kind:

| Skill | Station | Runs (agents) |
|---|---|---|
| `creative-direction` | 1 — Creative Direction | Creative Director (+ Brand Strategist check) |
| `sitemap-and-refs` | 2–3 — Sitemap + Reference Pull (tiered) | UX Strategist + Narrative Architect + Motion/3D/Technical Directors |
| `design-tokens` | 5 — Style Tokens | UI Designer (consumes the Brand Genome) |
| `design-audit` | 6 — Spec Assembly + Audit (mandatory gate) | Creative Director + QA & Performance Reviewer |

Full spec: [`EXPERIENCE_SPEC_SYSTEM.md`](EXPERIENCE_SPEC_SYSTEM.md).

Proposed initial catalog (still "Proposed, not built"): Scene Sequencing, Scroll Choreography (GSAP ScrollTrigger application), 3D Scene Assembly (Three.js/React Three Fiber), Camera Path Design, Sound Design Application, Performance Budget Enforcement, Experience QA Pass, **Structured Prompt Generation** (cross-ref [`PROMPTING_SYSTEM.md`](PROMPTING_SYSTEM.md) — turning a Storyboard Library entry into a real, ID'd Prompt Record). Cross-ref `EXPERIENCE_TECH_STACK.md` for the tool surface these would invoke.

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder — no real builds have happened yet; candidate metrics once they do: experience load time / performance-budget adherence, scene-completion rate, QA pass rate, build-to-launch cycle time)* | | | | | |

## 8. Decision Log

- **2026-07-15 — 🔴→✅ NARRATIVE ARC RECONCILED — this department's last open source conflict is closed.** Owner-confirmed among 4 options. Two non-identical arcs had stood since founding while the department's *other* two source conflicts (2 Creative Pipeline drafts, 2 AI roster drafts) were both reconciled on 2026-07-04. This one survived because the drafts **disagree on order**, not just granularity: Draft A places Transformation *before* Proof, Draft B places Proof *before* Transformation — a union can't dodge that, an arc has one order. **Settled by evidence from inside the department**: its own **Scene Architecture** (never previously compared against either draft) independently runs `Problem → Transformation → Features → Evidence → Testimonials`, corroborating Draft A's ordering. **Canonical: `Attention → Problem → Transformation → Proof → Offer`.** Draft B's beats absorbed, not dropped (Curiosity/Education → Discovery; Trust → Evidence/Testimonials; Action → CTA), and **Retention routed out** to Client Success (07) + `marketing-lifecycle` (03) — a website visit doesn't retain, a relationship does, and importing it would have duplicated two live mandates (the same scope-collision discipline this department applied on 2026-07-04). Both original drafts remain verbatim in `EXPERIENCE_ENGINEERING_VISION.md`. The cross-department narrative note drops from **4-way to 3-way** (§1), mirrored in `04_Content/CONTENT_OS.md` §10 and `12_Branding/BRANDING_OS.md` §3. The canonical arc is now **enum-enforced** in `experience-engineering-narrative-architect`'s schema — it cannot emit a different one. — Claude Code (Opus 4.8)
- **2026-07-15 — All 11 agents joined the runtime; the repo's legacy migration is complete.** The 11 specs gained frontmatter — triggers, schemas, risk classes, event wiring — **bodies untouched**; the 2026-07-04 reconciliation was already right, only frontmatter was missing. **These were the last 11 legacy specs in the repo**: `arika list` → **80 agents, 0 skipped**. The runtime's own regression test was updated from "at least one legacy spec is skipped" to "**zero legacy specs remain**" — the migration completing broke the test that measured it being incomplete. Schemas were derived from this department's **own Communication Protocol** (`AI_CREATIVE_ORCHESTRA.md`: Vision → Rationale → Technical Notes → Next Steps, plus risks/handoffs), not invented, and they hard-encode the department's rules: the 5 canonical arc stages, the 9-field storyboard, the 7 design laws, the 7 Creative DNA questions, the 11 QA items. 9 specification roles are **Class 1**; the Technical Director and both launch gates are **Class 2** (the build is production-deployed; the gates decide what reaches the public). — Claude Code (Opus 4.8)
- **2026-07-15 — 🔴 Runtime gap found and flagged, not worked around: `arika-runtime` has no join/barrier.** This department's pipeline is genuinely parallel (UI+Motion+3D concurrently; Creative + QA gates "both required"), but an EventEmitter bus can fan out and never join. Four emits therefore have no agent listener — `EXPERIENCE_BRAND_CHECKED`, `MOTION_SPEC_READY`, `CAMERA_SPEC_READY` (parallel siblings; subscribing the downstream role to each would fire it 2–3×, so they're wired as context) and `CREATIVE_GATE_PASSED`/`TECHNICAL_GATE_PASSED` (the "both required" join is performed by a human, who then launches). **Documented in §12 as known parallel/human joins rather than silently fake-wired**, so `operations-state-monitor` (08) doesn't read them as broken links. A real fix is a `waits_for: [A, B]` trigger type in the runtime — same class of gap as auto-dispatch being declared but unimplemented. — Claude Code (Opus 4.8)
- 2026-07-03 — Department created, numbered 20, named "Experience Engineering" — direct owner decision among 4 named alternatives (Interactive Experience Lab, Digital Storytelling Lab, Creative Technology Division, Experience Engineering). Positioned downstream of Design (19).
- 2026-07-03 — Seed content sourced from an owner-relayed external AI chat session, flagged per the sourcing-honesty convention (same treatment as Branding's Brand Genome) — full text preserved in `EXPERIENCE_ENGINEERING_VISION.md`, distilled/grouped version in this file's §3.
- 2026-07-03 — The 16-system architecture and Experience Pattern Library captured as proposed/architecture-only. The source's own internal inconsistencies — Pass 1's 9-item outline not matching its own 9 elaborated headers; Pass 1 vs. Pass 2 naming the same likely-concept twice (Story System/Narrative Engine, Motion System/Motion Language System, AI Department/AI Creative Orchestra); two non-identical Creative Pipeline drafts; two non-identical AI-role rosters; two non-identical narrative-arc drafts — are all presented as-given throughout this file and its sibling files, not silently reconciled into a single synthetic version.
- 2026-07-03 — Cross-department reconciliation: the 4-way narrative distinction (Content's Story Architecture, Branding's Narrative Engineering stack, and this department's two Narrative Arc drafts) documented here (§1) and mirrored in `04_Content/CONTENT_OS.md` §10 and `12_Branding/BRANDING_OS.md` §3.
- 2026-07-03 — Motion Tech Stack, Motion Library, and both Creative Pipeline drafts captured in `EXPERIENCE_TECH_STACK.md`; named tools registered as proposed/not-connected in `13_Tech_Stack/TECHSTACK_OS.md` §3.
- 2026-07-03 — AI Creative Orchestra captured in `AI_CREATIVE_ORCHESTRA.md` (both role-draft versions), BOIS-style lightweight contracts, explicitly not built.
- 2026-07-03 — **Prompting System added** (`PROMPTING_SYSTEM.md`), per direct owner request for a structured, ID'd, stateful prompting architecture (reference-image workflow, sequencing, a concrete "hyper-realistic, hyper-efficient" quality bar) rather than leaving "AI generation" as a vague capability name. Built from Design (19)'s existing no-visible-AI-artifacts standard plus the source's Creative DNA and QA Framework checklists — not invented fresh.
- 2026-07-03 — Enterprise EXOS and "Experience Science" flagged aspirational-only in §2 — no structure built for either, full text preserved in the vision file for completeness only.
- 2026-07-03 — Design (19)'s open Motion/VFX/SFX/3D-5D Tool Registry (`DESIGN_LANGUAGE_SYSTEM.md` §2a, tracker item 48) partially informed by this department's source material (real candidate names now exist for Transitions/VFX and 3D/5D Motion) — not fully resolved, since the owner hasn't personally confirmed adopting them the way OpenArt was confirmed.
- 2026-07-04 — **AI Creative Orchestra made real.** Owner directed: (1) build real, invokable Claude Code subagents rather than documentation-only contracts; (2) reconcile this department's own two source-draft rosters into one canonical roster rather than leaving both open; (3) hold off spending OpenArt's limited credits on speculative asset generation. Reconciled the two drafts into 11 canonical roles (full mapping in `AI_CREATIVE_ORCHESTRA.md`). For each role, the owner then supplied a further owner-relayed "Sider Fusion" AI session — 11 in total, one per role — each reconciled against this repo's real architecture: adopted genuinely reusable content (persona philosophy, hook/alignment taxonomies, storyboard rigor rules, cinematography knowledge, copywriting frameworks), rejected content assuming infrastructure this repo doesn't have (standalone Python/Streamlit apps, live 3D/game engines, robotics motion planners, vector databases, third-party LLM API wiring), and caught two real department-scope collisions (the Brand Strategist thread would have duplicated Branding (12)'s mandate; the Copywriter thread partially overlapped Offer (02)/Branding (12) territory) rather than building competing systems. Also caught and fixed a repo-wide mislabeling: the Storyboard Library's entry template is 9 fields, not 8 as previously written in 5 places. Full audit trail: `EXPERIENCE_ENGINEERING_VISION.md` §5. Closes `OWNER_INPUT_NEEDED.md` item 50 and `GO_LIVE_CHECKLIST.md` item 37. SFX/Sound Design remains genuinely unnamed.

- 2026-07-04 — **§3 Motion Tech Stack row updated**: owner-supplied raw tool list added Threlte and Theatre.js as real candidate libraries in `EXPERIENCE_TECH_STACK.md` §2 — same "named, not connected" status as every other row. Full triage of the raw list (including names Claude couldn't confidently identify) lives in `19_Design/DESIGN_INSPIRATION.md`, since the owner shared it as one combined Design+Experience Engineering direction list rather than department-scoped.
- 2026-07-04 — **First real project scoped: Arika's own flagship website.** Owner supplied a full 6-layer website vision, a social-ecosystem plan, and a Content Operating System model. Closes tracker item 51 (this department's founding blocker) — new file `ARIKA_WEBSITE_PROJECT.md` captures the phased scope (Phase 1 marketing site now; Client Portal and Academy/Community as undecided future roadmap) and a reconciled Phase 1 sitemap, cross-referenced against Content's real 7 pillars, Sector's real B2B-SaaS ICP, Audits & Diagnostics' real Gateway Offer, and Offer's real positioning rather than treated as a blank slate. **Same session, tracker item 52 also resolved**: the two Creative Pipeline drafts reconciled into one canonical 17-step sequence (`EXPERIENCE_TECH_STACK.md` §3), same reconciliation method already used for the AI Creative Orchestra roster. §2 Status, §4 Workflow Index, and §12 Triggers updated accordingly. Confirmed scope for this pass: planning + an execution-ready example-imagery brief only — no frontend code, no Client Portal/Academy build-out, and no image generation until Canva/OpenArt are re-authorized. — Claude Code (Sonnet 5)
- 2026-07-09 — **Experience Spec System aligned in — the department's front-half "Design the Spec" discipline is now codified and runnable.** The owner supplied a fully-formed "Design Department" plugin (a six-station brief→spec assembly line + four reference docs: Elite Web Build System, Vision-to-Build Pipeline, Workflow Run-Sheet, Discoverability & Architecture) and asked for it to be aligned into the repo. **Placement decision (owner-confirmed via explicit choice among 3 options): homed in Experience Engineering (20), not Design (19)** — despite the plugin's "Design" name, its stack (Next.js/Tailwind/GSAP/Lenis/Spline) is line-for-line identical to `EXPERIENCE_TECH_STACK.md` and its output is an interactive-website build prompt, which is this department's mandate, not Design (19)'s asset/media production. **Scope decision (owner-confirmed): full wiring.** Built: `EXPERIENCE_SPEC_SYSTEM.md` (the six stations mapped onto the existing 11 agents — no new roles), four reference docs under `build-system/`, and four real skills under `.claude/skills/` (`creative-direction`, `sitemap-and-refs`, `design-tokens`, `design-audit`). The plugin's Visual/Motion/Interaction Language Systems (§3) were hardened into seven checkable **design laws** (§10); its previously-unowned **Discoverability & Architecture** pillar (SEO/AEO/GEO + frontend/backend) was added (§10). Deliberately did **not** copy the plugin's standalone `CLAUDE.md` — a second root-authority file would violate `GLOBAL_OS.md` §2 (one root, thin pointers); its rules were distilled into the spec-system doc and the skills instead. New named-not-connected tools registered in `13_Tech_Stack/TECHSTACK_OS.md` §3 (Whimsical, Lenis, TanStack Query, Formspree, Sanity, Plausible/GA, Google Search Console); new tracker items in `OWNER_INPUT_NEEDED.md` and `GO_LIVE_CHECKLIST.md`. — Claude Code (Opus 4.8)

## 9. Risk / Incident Log

*(placeholder — empty. Standing doctrine note: once real builds exist, heavy 3D/motion experiences that sacrifice load time or accessibility for spectacle should be treated as a quality failure, not a style choice — mirrors Design's "no visible AI artifacts" doctrine note, `19_Design/DESIGN_OS.md` §9.)*

## 10. Standards & SOPs Index

**Storyboard-before-build.** Extends Design (19)'s existing storyboard-before-generation doctrine (`19_Design/DESIGN_OS.md` §10) to full multi-scene experiences: every scene gets its 9-field Storyboard Library entry (Scene/Camera/Lighting/Object/Text/Narration/Motion/Interaction/Goal, §3) before any generation or development work starts on it.

**Performance-first.** Performance budgets (Core Web Vitals, frame rate targets, asset budgets — full list in §3's Performance Engineering row) are defined before launch, not measured only after — cross-ref Performance Engineering, §3.

**Creative DNA — creative-level evaluation gate.** Before any experience ships, it should be checked against 7 questions from the source material: does it tell a compelling story? Does every motion have a purpose? Does scrolling feel meaningful rather than decorative? Is it accessible and performant? Does it reinforce the brand? Does it support a business objective? Does it end with a clear action for the user? Distinct from the Quality Assurance Framework's 11-item technical checklist (§3) — this is the creative/story-level gate, that's the technical/production-level gate. Both apply.

**The seven design laws (`EXPERIENCE_SPEC_SYSTEM.md` §3).** Every interactive build obeys seven non-negotiable laws, hardened from the §3 Language Systems into checkable rules: asymmetric 12-column grid (`min-h-[100dvh]`, never `h-screen`); one type ratio with `clamp()`; restraint (one canvas, ≤2 accents, opacity tiers, never #FFF-on-#000 — for Arika, the Brand Genome is the palette); one motion curve; `prefers-reduced-motion` gating via `gsap.matchMedia()`; real text in HTML; data-driven `content.config.ts` content. Enforced by the `design-audit` skill (Station 6, the mandatory gate) before any build ships.

**Discoverability-first (`build-system/discoverability-architecture.md`).** Cinematic and findable are not opposites, but both must be built deliberately: SSR (Next.js/Framer), real semantic headings, answer-first content + FAQ + schema markup, fact-consistency across every profile (site = Zoho Books org = social accounts), Open Graph share image, Google Search Console. The department's fourth pillar — previously unowned in any codified form. Part of the Station-6 audit.

**Pointers:** the six-station spec discipline + seven laws → [`EXPERIENCE_SPEC_SYSTEM.md`](EXPERIENCE_SPEC_SYSTEM.md); the build bible, feasibility tiers, run-sheet, and discoverability layer → [`build-system/`](build-system/). Full Motion Tech Stack, Motion Library, and both Creative Pipeline drafts → `EXPERIENCE_TECH_STACK.md`. Agent roster → `AI_CREATIVE_ORCHESTRA.md`. Structured prompting architecture → `PROMPTING_SYSTEM.md`.

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Interactive experience build | Experience Engineering (20) | Experience Engineering (20) | Design (19), Content (04), Branding (12) | Marketing (03), Offer (02) |
| Motion/3D tool adoption decisions | Experience Engineering (20) | Mary Thuo | Design (19), Tech Stack (13) | All departments |
| Experience Pattern Library | Experience Engineering (20) | Mary Thuo | Design (19), Offer (02) | All departments |

## 12. Triggers / Automation Hooks

**✅ UPDATED 2026-07-15 — the handoffs are real *events* now, not just cross-references.** The claim that stood here ("nothing here is *automated*") is no longer true: all 11 agents run on `arika-runtime`'s event bus (§5).

```
EXPERIENCE_PROJECT_SCOPED
        ▼
  narrative-architect ── NARRATIVE_ARC_SET ──┬─→ ux-strategist ── UX_PATTERNS_SET ─┐
                                             └─→ brand-strategist ─(context)─┐     │
                                                                             ▼     ▼
                                                                     storyboard-artist
                                                                             │ EXPERIENCE_STORYBOARD_READY
                                              ┌──────────────┬───────────────┤
                                              ▼              ▼               ▼
                                        ui-designer   motion-director   3d-director
                                              │         (context)        (context)
                                    UI_SPEC_READY
                                              ▼
                                         copywriter ── SCENE_COPY_READY ─→ technical-director
                                                                                  │ BUILD_SPEC_READY
                                                              ┌───────────────────┴──────────────────┐
                                                              ▼                                      ▼
                                                     creative-director                  qa-performance-reviewer
                                                   CREATIVE_GATE_PASSED                TECHNICAL_GATE_PASSED
                                                              ╚═══════ ⟨ HUMAN: both required ⟩ ═══════╝
                                                                            Launch
```

**🔴 Real runtime gap found while wiring: `arika-runtime` has no join/barrier primitive.** This department's pipeline is genuinely **parallel** — §4 runs "UI Designer + Motion Director + 3D Director… in parallel" and requires "Creative Director + QA & Performance Reviewer… **both required**" before launch. An `EventEmitter` bus can **fan out but never join**: there is no way to say *"run X only once A and B have both finished."*

Consequently four emits have **no agent listener**, and wiring them naively would be worse than leaving them:
- **`EXPERIENCE_BRAND_CHECKED`, `MOTION_SPEC_READY`, `CAMERA_SPEC_READY`** — these are **parallel siblings feeding one downstream agent**. Subscribing the Storyboard Artist to both `UX_PATTERNS_SET` *and* `EXPERIENCE_BRAND_CHECKED` would fire it **twice**; subscribing the Technical Director to all three spec events would fire it **three times**. They are wired as **context the downstream role reads**, not as triggers — which is what §4's parallel notation actually means.
- **`CREATIVE_GATE_PASSED`, `TECHNICAL_GATE_PASSED`** — **both must pass, then a human launches.** The "both required" join is performed by a person, and launching a public site is a human act regardless (same shape as Design (19)'s `DELIVERABLE_ASSEMBLED`).

**This is a runtime limitation, not an EE modelling error** — the same class of gap as agent-to-agent auto-dispatch being declared in specs but not yet implemented (`arika-runtime/DESIGN.md`). A real fix is a join/barrier trigger type (`waits_for: [A, B]`). Recorded here so `operations-state-monitor` (08) reads these four as **known parallel/human joins, not broken links.**

**Still not built — the upstream trigger.** `EXPERIENCE_PROJECT_SCOPED` currently has no emitter: Design (19)'s pipeline ends at a Canva deliverable (`DELIVERABLE_ASSEMBLED`), which is asset-scale, not experience-scale. A real trigger condition is now *definable* (tracker item 51 resolved — the Arika website is the first real experience-scale project), but deciding what promotes a Design output to an experience-scale project is an open modelling question, **not** something to invent here. Until then this chain starts by hand.

**No approval-matrix row needed yet:** all 11 are advisory, and the only state-changing act (launch) is human by design.

## 13. Existing OS Sub-Layer

**Real skill layer added 2026-07-09: four Claude Code skills** under `.claude/skills/` (`creative-direction`, `sitemap-and-refs`, `design-tokens`, `design-audit`) backing the Experience Spec System — the department's first real skill layer of any kind. No code-based agent scaffold like Finance's `finos-plugin` or Branding's `bois` exists; the department's real running-code artifact is the project itself (`arika-website`, a live Next.js app), not a reusable OS sub-layer.

Sibling spec/reference documents (same status as Design (19)'s sibling files): [`EXPERIENCE_SPEC_SYSTEM.md`](EXPERIENCE_SPEC_SYSTEM.md), `EXPERIENCE_TECH_STACK.md`, `AI_CREATIVE_ORCHESTRA.md`, `PROMPTING_SYSTEM.md`, `EXPERIENCE_ENGINEERING_VISION.md`, and the four reference docs in [`build-system/`](build-system/).

## 14. Raw Archive Pointer

No department-local `Draft N.md` corpus — genuinely new department, no inherited backlog, same status Design (19) and Tech Stack (13) had at creation. Unlike those two, this department's entire seed is one pasted external-AI-session conversation rather than an owner planning session narrated directly — preserved in full at `EXPERIENCE_ENGINEERING_VISION.md` rather than only summarized here.

## 15. Changelog

- 2026-07-15 — **All 11 agents live on `arika-runtime` — the repo's legacy migration is now complete (80 agents, 0 skipped)** — and the department's **last unreconciled source conflict is closed**. Diagnosis first: the 11 agents were real, reconciled, and invokable by hand but carried only `name` + `description`, so the runtime couldn't see them; and the two Narrative Arc drafts had stood open since founding while the department's other two source conflicts were reconciled on 2026-07-04. **Cured the arc** (owner-confirmed): canonical `Attention → Problem → Transformation → Proof → Offer`, settled by the department's **own Scene Architecture** corroborating that ordering — Draft B's extra beats absorbed, Retention routed out to Client Success (07)/`marketing-lifecycle` (03) rather than duplicating two live mandates. Wired all 11 (**bodies untouched**), deriving the shared schema from the department's own Communication Protocol rather than inventing one, and hard-encoding its rules as enums (5 arc stages, 9-field storyboard, 7 design laws, 7 Creative DNA questions, 11 QA items). **Flagged a real runtime gap rather than fake-wiring around it**: `arika-runtime` has no join/barrier, so this department's genuinely parallel steps (UI+Motion+3D; both launch gates) can't be auto-joined — 4 emits are documented in §12 as known parallel/human joins. Corrected §16, stale since 2026-07-04. Updated the runtime's regression test from "≥1 legacy spec skipped" to "0 legacy specs remain". Verified: `arika list` → 80, `npm test` → 9/9. — Claude Code (Opus 4.8)
- 2026-07-09 — **Experience Spec System aligned in** (see Decision Log). Homed the owner's "Design Department" plugin + Elite Web Build reference set here (owner-confirmed placement: Experience Engineering 20, not Design 19; scope: full wiring). New files: `EXPERIENCE_SPEC_SYSTEM.md`, four docs under `build-system/`, four skills under `.claude/skills/`. Edited §2 Status, §3 Capability Registry, §6 Skill Library Index (four skills now real), §10 Standards (seven design laws + Discoverability pillar), §13 Existing OS Sub-Layer. Companion edits: `13_Tech_Stack/TECHSTACK_OS.md` §3 (7 named-not-connected tools), `19_Design/DESIGN_OS.md` §1 (cross-ref note), `GLOBAL_OS.md` (§5 flow note + changelog + version bump), `OWNER_INPUT_NEEDED.md` + `GO_LIVE_CHECKLIST.md` (new items). Did not copy the plugin's standalone `CLAUDE.md` (would breach the one-root rule). — Claude Code (Opus 4.8)
- 2026-07-04 — **First real project scoped and Creative Pipeline reconciled** — closes tracker items 51 and 52, the two open decisions blocking this department since founding. New file `ARIKA_WEBSITE_PROJECT.md` (Phase 1 marketing-site sitemap, Phase 2/3 roadmap flags); `EXPERIENCE_TECH_STACK.md` §3 now has one canonical 17-step Creative Pipeline instead of two unreconciled drafts. §2, §4, §12 updated to reflect both. Companion edits: `03_Marketing/MARKETING_OS.md` §10 (Social Ecosystem), `04_Content/CONTENT_OS.md` §10 (Content Operating System 10-layer model), `19_Design/DESIGN_OS.md` §10 (Example Imagery Brief). No frontend code and no image generation happened in this pass — Relume remains down and Canva/OpenArt need re-authorization. — Claude Code (Sonnet 5)
- 2026-07-04 — **Confirmed this department's §12 trigger cannot yet be specified** (unlike Design 19's equivalent, which is now fully specified in `16_Automation/AUTOMATION_OS.md` §12) — no real project or "experience-scale" flag exists to define a trigger condition against. Revisit once tracker item 51 resolves. — Claude Code (Sonnet 5)
- 2026-07-04 — **Workflow Index (§4) and Triggers (§12) updated** with a role-level agent handoff sequence (Narrative Architect → UX Strategist/Brand Strategist → Storyboard Artist → UI Designer/Motion Director/3D Director → Copywriter → Technical Director → Creative Director/QA & Performance Reviewer) that holds under either open Creative Pipeline draft — does not resolve tracker item 52, which draft is authoritative remains an open owner decision. Explicitly distinguished "agent handoffs are real and invokable" from "nothing is automated yet" in §12. — Claude Code (Sonnet 5)
- 2026-07-04 — **Agent Roster made real.** Built 11 real, invokable Claude Code subagents under `.claude/agents/experience-engineering-*.md`, replacing the proposed-only roster. Reconciled the two source-draft rosters into one canonical 11-role roster (`AI_CREATIVE_ORCHESTRA.md`), then incorporated 11 further owner-relayed AI sessions (one per role) — adopting reusable content, rejecting infrastructure mismatches, and catching 2 real department-scope collisions (Brand Strategist vs. Branding 12; Copywriter vs. Offer 02/Branding 12). Fixed a repo-wide "8-field" → "9-field" mislabeling of the Storyboard Library template across 5 files. Updated §2 Status and §5 Agent Roster to reflect the real roster. Closes `OWNER_INPUT_NEEDED.md` item 50, `GO_LIVE_CHECKLIST.md` item 37. — Claude Code (Sonnet 5)
- 2026-07-03 — Department created. Seeded from an owner-relayed external AI chat session on scroll-driven/cinematic interactive web design; numbered 20, named "Experience Engineering" (direct owner decision among 4 alternatives), positioned downstream of Design (19). Built `EXPERIENCE_ENGINEERING_VISION.md` (full verbatim source capture), this OS file (grouped Capability Registry across 8 groups, ~25 sub-inventories), `AI_CREATIVE_ORCHESTRA.md` (2 non-identical proposed rosters), `EXPERIENCE_TECH_STACK.md` (tool list + 2 non-identical Creative Pipeline drafts), and `PROMPTING_SYSTEM.md` (new — structured/ID'd/stateful prompting architecture, per direct owner follow-up request). Documented all of the source's internal inconsistencies (9-vs-16 systems, 2 pipeline drafts, 2 AI-roster drafts, 2 narrative-arc drafts) as-given rather than silently reconciled. Added the 4-way cross-department narrative note (Content, Branding, and this department's 2 arcs) — mirrored in `04_Content/CONTENT_OS.md` §10 and `12_Branding/BRANDING_OS.md` §3. Partially informed (not resolved) Design (19)'s open Motion/VFX/SFX/3D-5D Tool Registry (`DESIGN_LANGUAGE_SYSTEM.md` §2a, tracker item 48). Added to `GLOBAL_OS.md` §4 Department Index, and new items to `OWNER_INPUT_NEEDED.md` (49-53) and `GO_LIVE_CHECKLIST.md` Phase 8 (34-40). Flagged "Enterprise EXOS" and "Experience Science" as aspirational-only, not built. — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

*(This section's old text — "no agent roster exists yet" — was stale from the day §5 was built on 2026-07-04, the same staleness Design (19) §16 carried. Corrected 2026-07-15.)*

**Memory.** All 11 agents append to `20_Experience_Engineering/_memory/runtime.jsonl` in the shared bois-compatible envelope (`arika-runtime/DESIGN.md`) — the only record of what EE agents actually did, and the only evidence `operations-state-monitor` (08) can use to mark this department `live` rather than `documented`. When `PROMPTING_SYSTEM.md`'s Prompt Records become real, they should land in this same stream rather than a second store.

**Feedback Loop.** §7's KPIs remain a placeholder (no build has run through this chain), but two real gates now run as code, and both are **schema-enforced rather than trusted**:
- **The Creative DNA gate** (`experience-engineering-creative-director`) must answer all **7** creative questions — its `creative_dna_check` enum won't accept a partial answer.
- **The technical gate** (`experience-engineering-qa-performance-reviewer`) must answer all **11** QA Framework items plus a discoverability check. Both gates are required before launch (§12), and the join between them is a **human**.

The standing doctrine note in §9 — *"heavy 3D/motion experiences that sacrifice load time or accessibility for spectacle are a quality failure, not a style choice"* — is now enforceable rather than aspirational: `accessible_and_performant` is one of the Creative DNA questions, `accessibility` and `performance` are two of the 11 QA items, and `prefers-reduced-motion` gating is one of the seven design laws the UI Designer must report on.

**Cadence.** Event-driven, not calendar-driven — EE produces when a project is scoped, not on a schedule. No cron. Maps loosely to the **Opportunity Calendar** (per-project) and the **Strategic Calendar** (the flagship builds that compound authority); deliberately **not** on the Revenue Calendar — an experience influences revenue, it doesn't book it.

**Honest state.** This department has **shipped a real thing**: `arika-website` is live in production on Vercel (14 pages, 5 real generated images, the real logo). But it was **hand-built, not produced by this chain** — the chain as wired has **never executed a full pass**, and `EXPERIENCE_PROJECT_SCOPED` has no emitter yet (§12). Zero motion/3D tools are connected. Nothing here is evidence of a working pipeline; it is a wired one, attached to a department that happens to have already shipped by hand.
