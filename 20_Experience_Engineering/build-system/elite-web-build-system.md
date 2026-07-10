# The Elite Web Build System

> **Repo-alignment header (added 2026-07-09).** This is one of four reference documents in the owner's "Elite Web Build" reference set, homed here under Experience Engineering (20) because it governs *interactive web builds* (the department's mandate), not Design (19)'s asset/media production. It is the canonical build bible behind `20_Experience_Engineering/EXPERIENCE_SPEC_SYSTEM.md` (the runnable 6-station spec discipline) and reconciles with `EXPERIENCE_TECH_STACK.md` (the department's tool inventory) — the stack below is identical to that file's, stated more prescriptively. Preserved substantially as the owner supplied it, per this repo's "capture source as-given" convention. Companion files: `vision-to-build-pipeline.md`, `workflow-run-sheet.md`, `discoverability-architecture.md`.

*A single, verified reference for taking any project from idea → award-grade site. Written to align the whole pipeline: stack, design language, layout, motion, and the reusable prompts that produce it all.*

*Last verified: July 2026.*

---

## 0. Read this first — how to think about it

You are not "prompting a website." You are directing a studio. The difference between a generic AI page and an Awwwards-grade one is not talent — it's **specification**. Elite sites run on invisible systems: a fixed set of type sizes, a fixed spacing rhythm, a strict color palette, one motion language. When you hand those systems to an AI (or a developer), it stops guessing and starts executing.

This document gives you the four systems that matter, the real tools that power them, and copy-paste master prompts. Everything here is verified against current award galleries and official sources, not vibes.

**The mental model — five layers, built in this order:**

1. **Architecture** — what pages/sections exist and what data they need (sitemap). *You already have this handled.*
2. **Layout** — where things sit and how they reflow (wireframe grid).
3. **Language** — the fixed tokens: type, color, space, motion (style guide).
4. **Motion** — how it moves as you scroll (cinematic layer).
5. **Data** — how the frontend connects to a backend later.

Skip a layer and the site feels amateur. Nail all five and it feels inevitable.

---

## 1. The verified elite stack (2026)

This is the actual combination that recurs across award-winning agency sites — not a theoretical ideal. Each tool earns its place.

| Layer | Tool | What it does | Why it's the standard |
|---|---|---|---|
| **Framework** | **Next.js** (React) or **Nuxt** (Vue) | App structure, routing, SSR | Award galleries are dominated by these two. Next.js for the React ecosystem; Nuxt if you prefer Vue. |
| **Styling** | **Tailwind CSS** | Utility-first styling | Enforces a design system by default. Fast to iterate, hard to make inconsistent. |
| **Animation engine** | **GSAP** + **ScrollTrigger** | The motion + scroll timeline engine | The gold standard. **Now 100% free** including all former paid plugins. This is the single most important tool to learn. |
| **Smooth scroll** | **Lenis** | Buttery inertial scrolling | Made by Studio Freight/Darkroom. The "expensive feel" of premium sites is almost always Lenis under the hood. |
| **3D / WebGL** | **Three.js** + **React Three Fiber** | Real-time 3D, shaders, particles | The layer that separates "nice" from "unforgettable." Optional but high-impact. |
| **Text splitting** | **GSAP SplitText** | Splits headings into lines/words/chars for staggered reveals | Rewritten and free since 2025. The signature "premium headline" effect. |
| **Micro-interactions** | **Framer Motion** (React) | Component-level enter/exit, hover, layout animation | Great for UI polish. Often used alongside GSAP, not instead of it. |
| **Vector animation** | **Lottie** | Plays After Effects animations as JSON | For designed illustrations/icons that move. |
| **Deploy** | **Vercel** or **Netlify** | Hosting + CI | Near-universal in the galleries. |

### The critical 2026 update

**GSAP is now completely free — including everything that used to cost money.** In October 2024 Webflow acquired GreenSock (GSAP's maker). In April 2025, with version 3.13, Webflow released the entire library for free, including the previously paid "Club" plugins (SplitText, ScrollTrigger, ScrollSmoother, MorphSVG, DrawSVG, Physics2D, and more), with the standard license expanded to cover commercial use at no cost.

Practically: **the exact toolset elite studios used to pay for is now free to you.** Learn GSAP + ScrollTrigger + SplitText first. They unlock 80% of what makes premium sites feel premium.

*(Note: GSAP is free-to-use but not open-source — you can't decompile it or build a competing product from its code. For normal site-building this restriction never touches you.)*

### The canonical wiring (how the pieces connect)

Every cinematic site uses roughly this loop — Lenis handles smooth scroll, GSAP's ticker drives it every frame, and ScrollTrigger reads scroll position to animate:

```js
import Lenis from 'lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // exponential ease-out
});

// Let GSAP drive Lenis on every frame
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

Memorize the *shape* of this, not the syntax. When you prompt, you can now say "wire Lenis to GSAP's ticker and drive ScrollTrigger from it" — and the AI will produce exactly this.

---

## 2. The Style Guide — your fixed language (tokens)

This is the layer beginners skip and pros obsess over. A **design token** is a single named decision — one color, one text size, one spacing unit — that you reuse everywhere. Fixed tokens are *why* a site looks coherent across 40 pages.

### 2.1 Typographic scale (pick a ratio, never eyeball sizes)

Every size is mathematically derived from a base by a multiplier. Pick **one** ratio and stick to it. This is the difference between "designed" and "random."

| Ratio | Feel | Use for |
|---|---|---|
| 1.2 (Minor Third) | Calm, editorial | Content-heavy, readable sites |
| 1.25 (Major Third) | Balanced, safe | Most projects — good default |
| 1.333 (Perfect Fourth) | Confident | Marketing / product sites |
| 1.414–1.618 (Aug. Fourth / Golden) | Dramatic, high-contrast | Agency / fashion / hero-driven sites |

**A high-contrast agency scale (Tailwind classes):**

- **Display / hero:** `text-[clamp(2.8rem,8vw,7rem)] font-bold tracking-tight leading-[0.92] uppercase`
- **Section header:** `text-3xl sm:text-5xl font-semibold tracking-tight`
- **Body:** `text-base leading-relaxed text-white/70`
- **Micro-label / eyebrow:** `text-[10px] sm:text-xs uppercase tracking-[0.2em] text-white/40`

The `clamp()` on the display size is the pro move: it scales fluidly between a minimum and maximum based on viewport width, so headings never break at any screen size.

### 2.2 Color system (restraint reads as luxury)

Premium ≠ colorful. Premium = **one canvas, one or two accents, strict transparency tiers.**

- **Canvas (background):** one deep, near-black or one warm off-white. e.g. `#09090B` (dark) or `#FBFBFA` (cream).
- **Ink (text):** never pure `#FFF` on pure `#000` — it vibrates. Use `white/90` for primary, `white/70` for body, `white/40` for labels. These opacity tiers *are* your grey scale.
- **Accent:** exactly one signature color, used sparingly (buttons, hovers, one highlighted word). e.g. electric indigo `#4F46E5`.
- **Borders / dividers:** hairline and semi-transparent — `border-white/10` (dark) or `border-black/5` (light). This gives structure without clutter and is a hallmark of high-end layout.

Rule of thumb: **if you're reaching for a fourth color, you probably need a fourth opacity tier of an existing one instead.**

> **Arika note:** for real Arika builds the canvas/accents are *not* free choices — they are the confirmed Brand Genome (Deep Revenue Navy `#0E1B29`, Champagne Gold `#D4AF37` accent, Alabaster Cream `#F7F5F0` ink, Operator Blush `#F3C1C6` sparing UGC accent). See `12_Branding/BRANDING_OS.md` §2. The ratio-and-tier *method* below is what's reusable; the values are Branding's.

### 2.3 Spacing rhythm

Use a consistent scale (Tailwind's default 4px base is fine: 4, 8, 12, 16, 24, 32, 48, 64, 96...). Never use arbitrary values like `mt-[37px]`. Consistent spacing is invisible when right and screams "amateur" when wrong.

### 2.4 Component & interaction rules

Decide these once, apply everywhere:

- **Corners:** commit to a personality — `rounded-none` (brutalist/editorial), `rounded-lg` (modern-friendly), or `rounded-full` (soft/playful). Mixing them looks accidental.
- **One button formula.** Example premium button:
  ```
  px-6 py-3 border border-white/20 uppercase tracking-widest text-xs
  transition-all duration-300 ease-out hover:bg-white hover:text-black hover:border-white
  ```
- **One transition curve.** Pick a duration (250–350ms) and easing (`ease-out`) and use it for *everything*. Consistency of motion is as important as consistency of color.

---

## 3. The Wireframe — the 12-column grid system

A profound layout is an intentional hierarchy of focus, not "elements on a page." The industry tool for this is the **12-column responsive grid**. Twelve divides cleanly into halves, thirds, quarters, and sixths, giving you every useful proportion.

**In Tailwind:** `grid grid-cols-12 gap-6 md:gap-8`, then assign `col-span-*` to children.

### Layout archetypes (reuse these)

| Archetype | Desktop spec | Best for |
|---|---|---|
| **Premium Editorial** | `col-span-1` gutter + `col-span-7` main + `col-span-4` sidebar | Hero sections, case studies, deep content |
| **Asymmetric Split** | `col-span-5` text pillar + `col-span-7` widget/form | Contact pages, feature showcases |
| **Balance Grid** | 3 cards `col-span-4` each, or 4 cards `col-span-3` each | Portfolios, services, pricing |

**Asymmetry is the secret.** A 7/5 split feels designed; a 6/6 split feels like a spreadsheet. Elite layouts lean off-center on purpose.

### The two responsive rules that prevent 90% of bugs

1. **Mobile-first, stack by default.** On mobile everything is `col-span-12` (full width, stacked). Add complexity *upward* with `md:` and `lg:` prefixes. Never design desktop-first and cram down.
2. **Use dynamic viewport height.** Never use `h-screen` (`100vh`) for full-height sections — mobile browser toolbars clip the bottom. Use **`min-h-[100dvh]`** (dynamic viewport height). This one change fixes the most common mobile bug in AI-generated pages.

---

## 4. The Cinematic Layer — scrolltelling

This is where a site becomes an experience. Direct it like film: each scroll is a camera move. Four techniques cover almost everything, and all four are just GSAP ScrollTrigger + Lenis.

### 4.1 Pinning (the locked camera)

Freeze a section in place while its *internal* content animates, then release. This is how you keep a background video or 3D scene alive while text changes over it.

> **Prompt language:** "Pin this section (`pin: true`) for the duration of a scroll timeline; keep the background media fixed while the foreground text transitions in stages driven by scroll progress."

### 4.2 Scrubbing (scroll = the timeline's playhead)

Instead of animations playing on their own clock, tie them directly to scroll position with `scrub`. Scroll forward, it plays; scroll back, it reverses. This is what makes scroll feel like a physical control.

> **Prompt language:** "Bind this timeline to scroll with `scrub: 1` so progress maps directly to scroll position and reverses on scroll-up."

### 4.3 Staggered reveals (the storyboard)

Elements never appear all at once. They cascade on a timeline: eyebrow at 0ms, headline at 200ms, CTA at 400ms. With **SplitText**, headlines break into individual characters or lines that reveal in sequence — the signature premium effect.

> **Prompt language:** "Use SplitText to split the heading into lines, then stagger each line up from `y: 40, opacity: 0` on a ScrollTrigger, firing once when the section enters view."

### 4.4 Media masking (the lens effect)

Use video/3D as an environment, not decoration. Start a video boxed inside a small centered frame, then expand its mask to full-bleed as the user scrolls into the section.

> **Prompt language:** "Start the video contained in a centered `max-w-4xl scale-95` frame; as the section scrubs, expand it to full-bleed `w-full h-full scale-100`."

**Guardrail — always ask for `prefers-reduced-motion`.** Elite ≠ nauseating. Respect users who disable motion; GSAP's `matchMedia()` handles this cleanly. Add "gate all scroll animation behind `prefers-reduced-motion` using `gsap.matchMedia()`" to every cinematic prompt.

---

## 5. Frontend → Backend (so it's not hardcoded)

Even a static-looking site should be built as if data comes from an API. This costs nothing now and saves a rebuild later.

**The one rule:** never hardcode content inside JSX. Lift it into a config object at the top of the file (or a separate `content.ts`), then map over it. Swapping in a real API later becomes a one-line change.

```ts
// content.config.ts — your "data contract"
export const landing = {
  hero: {
    eyebrow: "World-Class Digital Collective",
    headings: ["Design.", "Disrupt.", "Conquer."],
    subtext: "We build fierce brand identities that lead.",
  },
  metrics: [
    { value: "250+", label: "Brands Transformed" },
    { value: "95%",  label: "Client Retention" },
    { value: "10+",  label: "Years in the Game" },
  ],
  media: { heroVideo: "https://…" },
};
```

The data flow, when you're ready for a real backend:

```
Frontend (Next.js)  ──GET /api/landing──▶  Backend (Node/Express, or Next API routes)
        ▲                                          │
        │  JSON payload                            │ ORM query (Prisma)
        └──────────────────────────────────────────┼
                                            Database (PostgreSQL)
                        holds: hero copy, metrics, project entries, media URLs
```

Fetch it with **TanStack Query** (handles loading/error/caching for you) and fall back to your static config while loading. Same shape, static → dynamic, no refactor.

---

## 6. The reusable Master Prompts

These are the payoff. Fill the brackets, paste, iterate.

### 6.1 The universal shell prompt

```
Act as a Principal Frontend Engineer + Creative Director. Build a mobile-first,
production-grade page shell.

STACK: React (Next.js), Tailwind CSS, GSAP + ScrollTrigger, Lenis smooth scroll,
lucide-react icons. No other animation libraries.

ARCHITECTURE:
- Single config object at the top of the file holding ALL content (nav, hero copy,
  metrics, footer) so I can swap in API data later. Map over it — never hardcode in JSX.

LAYOUT:
- Responsive 12-column grid (grid grid-cols-12 gap-6 md:gap-8).
- Desktop uses ASYMMETRIC splits (e.g. col-span-7 / col-span-5), NOT 6/6.
- Mobile: everything col-span-12, stacked. Build up with md: and lg:.
- Full-height sections use min-h-[100dvh], never h-screen.

STYLE TOKENS:
- Palette: [e.g. deep charcoal #09090B canvas, one electric-indigo accent, white
  opacity tiers (white/90, white/70, white/40) as the grey scale].
- Type: display uses text-[clamp(2.8rem,8vw,7rem)] font-bold tracking-tight
  leading-[0.92]; body text-base leading-relaxed; labels uppercase tracking-[0.2em].
- Corners: [rounded-none / rounded-lg]. Borders: hairline border-white/10.
- ONE transition curve everywhere: duration-300 ease-out.
```

### 6.2 The cinematic add-on (append when you want scrolltelling)

```
MOTION:
- Wire Lenis to GSAP's ticker and drive ScrollTrigger from it.
- Entrance: stagger elements on a timeline (eyebrow 0ms → headline 200ms → CTA 400ms).
- Headlines: use GSAP SplitText, reveal by line from y:40, opacity:0.
- [Optional] Pin the hero and scrub a timeline tied to scroll progress.
- Gate ALL scroll animation behind prefers-reduced-motion via gsap.matchMedia().
```

### 6.3 The self-audit prompt (run it after every build)

```
Review this build against a premium checklist and fix any misses:
1. Any h-screen that should be min-h-[100dvh]?
2. Any hardcoded content that should live in the config object?
3. Any layout that's 6/6 where an asymmetric 7/5 would look more designed?
4. More than one accent color, or colors that should be opacity tiers?
5. Inconsistent transition durations/easings?
6. Missing prefers-reduced-motion handling?
7. Any arbitrary spacing (mt-[37px]) that should snap to the scale?
```

---

## 7. Study these (the real reference set)

To develop taste, reverse-engineer the best. Recurring names in current award galleries:

- **Lusion** — the benchmark for interactive WebGL/3D.
- **Immersive Garden** (France) — cinematic 3D brand experiences.
- **Make Me Pulse** — immersive storytelling.
- **Studio Freight / Darkroom** — makers of Lenis; the "smooth premium" feel.
- **Dennis Snellenberg** — a developer portfolio that's a masterclass in transitions.

Galleries to browse weekly: **Awwwards**, **Orpetron**, **CSS Nectar**, **Codrops** (for tutorials with real code).

---

## 8. The 30-day path (since you're starting fresh)

Don't try to build a WebGL cinematic epic on day one. Layer up:

1. **Week 1 — Tokens + layout.** Build a static shell with the 12-column grid and your token system. No motion. Get it looking coherent and reflowing perfectly on mobile.
2. **Week 2 — GSAP basics.** Add staggered entrance animations and one SplitText headline reveal. This alone will make it feel professional.
3. **Week 3 — Scroll.** Add Lenis, then one ScrollTrigger pin-and-scrub section.
4. **Week 4 — Data.** Move all content into the config object and (optionally) wire one section to a real API route.

Only after all four feel comfortable should you reach for Three.js/WebGL. It's the highest-effort, highest-risk layer — earn it last.

---

*The whole system in one sentence: **fixed tokens, asymmetric grid, one motion language, data-driven from day one — directed, not guessed.***
