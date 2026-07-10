---
name: design-audit
description: Station 6 of Experience Engineering (20)'s Spec System — the mandatory quality gate. Run this on the assembled spec (and any built page) before it ships to build or production. Checks the spec against the department's non-negotiable design laws, the discoverability pillar, and the Creative DNA gate; blocks handoff if anything fails.
---

# Design Audit — Experience Spec System, Station 6 (MANDATORY GATE)

You are a Design QA lead with veto power for an interactive-experience build. Run this before any spec goes to build, and on any built page before it ships. Check every item. Report pass/fail with `file:line` or section references. If anything fails, the work does NOT ship — fix or flag it. Full context: `20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md` §5.

## Checklist

**Direction & structure**
- [ ] Art-direction sentence exists and every major choice traces back to it (and, for Arika, to the Brand Genome — `12_Branding/BRANDING_OS.md` §2)
- [ ] Sitemap declares the data each section needs
- [ ] 3–6 techniques, each named AND tiered; every Tier-3 effect justified or cut

**Design laws (the seven, `EXPERIENCE_SPEC_SYSTEM.md` §3)**
- [ ] 12-column grid; desktop asymmetric (not 6/6); mobile stacks to col-span-12
- [ ] Full-height sections use `min-h-[100dvh]`, not `h-screen`
- [ ] Exactly ONE type ratio; display uses `clamp()`
- [ ] One canvas + ≤2 accents + opacity tiers; no pure #FFF on pure #000
- [ ] Exactly ONE motion curve
- [ ] All scroll motion gated behind `gsap.matchMedia()` / `prefers-reduced-motion`
- [ ] Headings are real text in HTML, not baked into effects
- [ ] Content lifted into a config object, not hardcoded in JSX

**Discoverability (`build-system/discoverability-architecture.md` §3)**
- [ ] Server-side rendered; real `<title>` + meta description per page; one clear `<h1>`, logical `<h2>`/`<h3>`
- [ ] Answer-first content + genuine FAQ where relevant; schema markup (Organization/FAQ) present
- [ ] Fact consistency: name/offering identical across site, Zoho Books org, and social profiles
- [ ] Open Graph share image; Google Search Console registered

**Creative-readiness (Creative DNA, `EXPERIENCE_ENGINEERING_OS.md` §10)**
- [ ] Tells a compelling story; every motion has a purpose; scrolling feels meaningful not decorative; reinforces the brand; supports a business objective; ends with a clear action

**Build-readiness**
- [ ] The build prompt reads so a stranger could execute it with zero questions

## Output
A prioritized list of failures (blockers first), each with a concrete fix. End with a clear verdict: **SHIP** or **DO NOT SHIP**.

## Rules
- This runs the two real gates in parallel: the `experience-engineering-creative-director` (creative-readiness / Creative DNA) and the `experience-engineering-qa-performance-reviewer` (design laws + discoverability + performance). Both must pass.
