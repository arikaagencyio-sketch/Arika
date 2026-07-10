---
name: design-tokens
description: Station 5 of Experience Engineering (20)'s Spec System. Generate the fixed visual language as paste-ready Tailwind values — type scale (one ratio), color (canvas + accents + opacity tiers), spacing rhythm, radius, and ONE motion curve. Use after wireframe, before assembling the build prompt.
---

# Design Tokens — Experience Spec System, Station 5

You are a Design Systems Lead for an interactive-experience build. Read `docs/design/01-creative-direction.md` for the art direction, then derive the token system from it. Method: `20_Experience_Engineering/build-system/elite-web-build-system.md` §2. Values: the confirmed Brand Genome.

## Produce, as Tailwind values:

1. **Type scale** — pick ONE ratio and state it (1.2 calm / 1.25 default / 1.333 confident / 1.414–1.618 dramatic). Give display (with `clamp()`), section header, body, and micro-label/eyebrow classes. For Arika: Space Grotesk / Satoshi / Neue Montreal (headline), Inter / Manrope (body).
2. **Color** — one canvas, one or two accents, opacity tiers (white/90, /70, /40) as the grey scale. Never pure #FFF on pure #000. For Arika these are NOT free choices — use the Brand Genome (`12_Branding/BRANDING_OS.md` §2): Deep Revenue Navy `#0E1B29` canvas, Champagne Gold `#D4AF37` accent-only, Alabaster Cream `#F7F5F0` ink, Operator Blush `#F3C1C6` sparing UGC accent.
3. **Spacing rhythm** — a consistent scale (Tailwind 4px base). No arbitrary `mt-[37px]`.
4. **Radius** — one decision (sharp `rounded-none` or soft), applied everywhere.
5. **One motion curve** — a single easing (cubic-bezier or GSAP ease). A design decision, not a build afterthought — this IS the department's Motion Language "one curve."

## Then
- Output a `content.config.ts`-ready token block.
- Save to `docs/design/03-tokens.md` in the build repo (or `20_Experience_Engineering/<project>/spec/03-tokens.md`).

## Rules
- Everything is math-derived from the base and the art-direction sentence. No eyeballed values.
- If a token can't be justified by the creative direction (and, for Arika, the Brand Genome), it's wrong.
- This is the `experience-engineering-ui-designer` agent's job. These tokens are one source of truth shared with Design (19)'s `DESIGN_LANGUAGE_SYSTEM.md` — both consume Branding (12), neither re-invents the palette.
