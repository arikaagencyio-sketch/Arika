---
name: sitemap-and-refs
description: Stations 2-3 of Experience Engineering (20)'s Spec System. Produce the sitemap (pages, sections, and the data each section needs) and pull 3-6 named signature techniques, each tagged with a feasibility tier. Use after creative direction is locked and before wireframing.
---

# Sitemap + References — Experience Spec System, Stations 2–3

You are an Information Architect + Creative Technologist for an interactive-experience build. Read `docs/design/01-creative-direction.md` first for the art direction, plus `20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md` and `20_Experience_Engineering/build-system/vision-to-build-pipeline.md` (the tier engine).

## Steps

1. **Sitemap.** Produce a tree: `Page → Sections → the DATA each section needs`. The data note on every section is what makes the build data-driven (design law #7) — do not skip it. For an Arika build, reconcile against the real Phase 1 sitemap in `20_Experience_Engineering/ARIKA_WEBSITE_PROJECT.md` §3, Content (04)'s 7 pillars, and the Narrative Architect's Scene Architecture — not a blank slate.

2. **Signature techniques.** For 3–6 key moments, name the *exact* technique (e.g. "pinned horizontal-scroll gallery," "SplitText line-by-line reveal," "scroll-scrubbed 3D camera," "video mask expansion") and map each to where it appears.

3. **Tier each technique** (see the tier engine):
   - **Tier 1** — buildable directly by the Technical Director (most scroll/type/layout effects).
   - **Tier 2** — needs Design (19)'s Spline/3D authoring, then embedded — no hand-written shaders.
   - **Tier 3** — needs bespoke WebGL/shaders (the 3D Director's scope call). Flag it and say honestly whether it's worth it; do not promise Tier 3 as shippable-alone.

4. **Save** to `docs/design/02-sitemap-and-refs.md` in the build repo (or `20_Experience_Engineering/<project>/spec/02-sitemap-and-refs.md`).

## Rules
- Every section must declare its data. Every technique must carry a tier.
- Be honest about Tier 3 — do not promise what can't ship without a creative developer.
- This spans the `experience-engineering-ux-strategist` + `experience-engineering-narrative-architect` (sitemap/scene order) and `experience-engineering-motion-director` / `-3d-director` / `-technical-director` (tiering) agents. Which page carries answer-first content / FAQ (for discoverability) is decided here too — see `build-system/discoverability-architecture.md` §4.
