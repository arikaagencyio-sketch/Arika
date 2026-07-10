# The Vision-to-Build Pipeline

> **Repo-alignment header (added 2026-07-09).** Homed under Experience Engineering (20). This is the **feasibility-tier engine** (Tier 1 / 2 / 3) and the **Reference Library** template that Station 3 of `EXPERIENCE_SPEC_SYSTEM.md` runs, and that the `sitemap-and-refs` skill applies. The tier vocabulary maps onto EE's real agents: Tier 1 → Technical Director builds directly; Tier 2 → Design (19)'s Spline/3D authoring + Technical Director embed; Tier 3 → flagged for a creative developer (or the 3D Director's scope call). Companion files: `elite-web-build-system.md`, `workflow-run-sheet.md`, `discoverability-architecture.md`.

*The companion to the Elite Web Build System. This is the operational machine: how a feeling in your head — or a clip you saved — becomes a live website, without you writing code.*

*Last verified: July 2026.*

---

## The one idea that makes all of this work

You cannot prompt a feeling. "Make it cinematic like Lusion" gives the AI nothing. But every feeling is made of **named techniques**, and every technique has a **build tier** that tells you exactly how to produce it.

So the pipeline is really one loop, repeated:

> **See something you love → name the technique → check its tier → grab the prompt fragment → assemble.**

Your reference library is where you store the results of that loop so you never start from zero again. This document gives you the library template, the tier system that powers it, and the full idea-to-live workflow.

---

## Part 1 — The three feasibility tiers (your honest map)

Every effect you'll ever want falls into one of these. Knowing the tier *before* you start saves you from chasing something that needs a specialist — or paying for one when you didn't need to.

### Tier 1 — The AI writes it directly
The elite motion layer. An AI code generator (v0, Bolt, Lovable) produces this from a good prompt, or Framer/Webflow does it visually. **This is 80% of what makes sites feel premium.** You can do all of it yourself.

- Smooth inertial scroll (Lenis)
- Staggered entrance reveals; headline text splitting into lines/letters (SplitText)
- Scroll-pinned sections with scrub (zoom in/out, freeze-and-transition)
- Horizontal scroll galleries
- Full-bleed video that masks/expands on scroll
- Custom cursors, hover micro-interactions
- Page-to-page transitions

### Tier 2 — Visual 3D tool + no-code (the "Lusion-lite" zone)
Real 3D and depth, produced in a **visual tool (Spline)** and dropped into your site. No JavaScript. This is where you reach effects that *feel* bespoke.

- A 3D object in the hero that follows the cursor or rotates on scroll
- A product that unfolds/assembles as you scroll
- Scroll-driven camera pushes through a scene
- Physics-based interactions (objects that bounce, collide, react)
- Shader gradients / animated 3D backgrounds

**How:** design the scene in Spline → embed it in Framer/Webflow with one drop-in, or export as a React component for the v0/Bolt lane. Spline handles scroll events, cursor-follow, camera states, and physics visually. (Model complex shapes in Blender first if needed, then make them interactive in Spline — that's the standard 2026 workflow.)

### Tier 3 — Needs a creative developer
Genuinely custom, and worth knowing so you brief it correctly (or skip it).

- Fully navigable 3D worlds (walking through a 3D space, like Lusion's museum)
- Bespoke custom shaders / generative WebGL art
- Complex real-time 3D games or simulations in the browser

**When you hit Tier 3:** your reference library is now a *brief* — you hand the developer the exact reference and named technique, and you've done 90% of their thinking for them. That's leverage, not defeat.

---

## Part 2 — The Reference Library (fill this in)

Not a mood board. Each row turns a feeling into something buildable. Capture entries whenever you see something you love — Awwwards, Lusion, Pinterest, a competitor.

> **Arika note:** for Arika, the reference library and this loop share intake with Design (19)'s **Inspiration Brackets** (`19_Design/DESIGN_INSPIRATION.md`, format-first: Website/Carousel/Reel/Poster). A Website-bracket entry that names an interactive technique *is* a Reference Library row — file it once, tag it both ways.

**Each entry has six columns:**

| Field | What goes here |
|---|---|
| **Source** | Link + a screen-recording of the *exact moment* you love (10 sec is enough) |
| **What I love** | Plain language, no jargon. "The way the letters fall apart as you scroll past." |
| **Technique** | The named move |
| **Tier** | 1 / 2 / 3 — tells you how it gets built |
| **Prompt fragment** | The 1–2 sentences that recreate it, ready to paste |
| **Used on** | Which of your projects you've applied it to |

### Pre-seeded starter entries

Copy these in. They cover the cinematic vocabulary worth admiring.

| Technique | Tier | Prompt fragment (paste-ready) |
|---|---|---|
| **Smooth inertial scroll** | 1 | "Add Lenis smooth scroll wired to GSAP's ticker; give it a slow, weighted inertial feel." |
| **Headline shatter/reveal** | 1 | "Use GSAP SplitText to split each heading into lines; reveal them one by one from y:40, opacity:0 on scroll-in." |
| **Pinned hero, zoom-out on scroll** | 1 | "Pin the hero section and scrub a timeline tied to scroll: the hero content scales down and blurs out as the next section rises up underneath." |
| **Video mask expansion** | 1 | "Start the hero video contained in a centered small frame; as the user scrolls, expand it to full-bleed." |
| **Horizontal scroll gallery** | 1 | "Make this project row scroll horizontally as the user scrolls vertically, using GSAP ScrollTrigger." |
| **Custom cursor** | 1 | "Replace the default cursor with a small circle that scales up and shows a label on hover over links." |
| **3D hero object, cursor-reactive** | 2 | "Embed a Spline scene in the hero: a [object] that rotates toward the cursor and drifts subtly. Design it in Spline, embed via the Framer Spline component." |
| **Product unfolds on scroll** | 2 | "Spline scene of the [product] that assembles/unfolds as the user scrolls, driven by Spline scroll events tied to camera states." |
| **Navigable 3D world** | 3 | *(Brief a creative developer — hand them the reference + 'React Three Fiber, scroll or drag to move a camera between anchor points in a 3D scene.')* |

---

## Part 3 — The full pipeline: idea → live site

Six steps. You already own steps 1–3.

### Step 1 — Define the idea
One paragraph: what is it, who's it for, what feeling. e.g. "An ecommerce store for a small-batch fragrance brand; feels quiet, luxurious, slow; the product should feel like an object in space."

### Step 2 — Sitemap
The pages/sections and the data each needs. (See the Elite Web Build System, Phase 1.)

### Step 3 — Pull references *before* wireframing
This is the step people skip. **Go to your library and your saved clips, and pick 3–6 reference moments that match the feeling.** Tag each with its tier. This is where "cinematic" becomes concrete: three named techniques, not a vibe.

### Step 4 — Wireframe with the references baked in
Now the layout isn't abstract — it's "12-column asymmetric grid, hero uses the *pinned zoom-out* (Tier 1) with a *cursor-reactive 3D bottle* (Tier 2), product grid uses *horizontal scroll* (Tier 1)." The references tell the layout what each zone *does*. (Grid system: Elite Web Build System, Section 3.)

### Step 5 — Assemble the master prompt
Stack it: the universal shell prompt + your style tokens + the prompt fragments for each chosen technique. You're no longer writing prose — you're assembling parts you already trust. (Master prompts: Elite Web Build System, Section 6.)

### Step 6 — Build in the right lane, then go live
- **Tier 1 only** → Framer (stay visual, publish live in-app) **or** v0/Bolt (real code, deploy to Vercel).
- **Tier 1 + 2** → build the 3D in Spline first, then embed it (Framer drop-in) or generate the page in v0/Bolt with the Spline React component.
- **Tier 3 present** → build everything else yourself; brief a developer for the one 3D piece using your reference as the spec.

Then iterate by *editing* — the honest test of any tool is whether the site survives your edits, not the first generation.

---

## Part 4 — What changes by site type

The pipeline is identical; only the emphasis shifts.

| | **Landing page** | **Ecommerce store** | **Portfolio / brand site** |
|---|---|---|---|
| **Goal** | One message, one action | Browse → trust → buy | Feeling + credibility |
| **Where 3D earns its place** | Hero object (Tier 2) — high impact, one scene | Product viewer (Tier 2) — 3D product you rotate | Signature moment (Tier 2–3) |
| **Motion focus** | Strong hero reveal + one scroll moment | Restraint — motion must not slow the path to buy | Cinematic throughout; transitions matter most |
| **Best lane** | Framer or v0 | Shopify (for real commerce) + Spline product embeds; or Framer for a simpler catalog | Framer, or v0/Bolt for max cinematic control |
| **Watch out** | Don't over-animate the CTA | 3D must be lightweight — heavy scenes kill load speed & sales | Don't let effects bury the work itself |

*(Note on ecommerce: real stores with carts, inventory, and payments are usually better on Shopify than on a hand-built site. You can still embed Spline 3D product views into Shopify.)*

---

## Part 5 — The 3D bridge: Spline, specifically

Since this is the piece that unlocks the look you're chasing:

- **What it is:** a browser-based, visual 3D editor for designers with no code or 3D background.
- **What you can wire up visually:** scroll position → camera moves; cursor → object follow/look-at; hover, click, collision, physics (gravity, bounce); even live data via variables/webhooks.
- **How it gets onto your site:** native drop-in for **Framer, Webflow, Wix Studio** (scroll triggers and events stay intact), or `@splinetool/react-spline` as a **React component** for Next.js / v0 / Bolt. There's even an experimental export to react-three-fiber if you later want a developer to take it further.
- **Cost:** free to start (with a watermark on free); paid tiers remove it and unlock advanced export.
- **The workflow for a complex object:** model in **Blender** (free) → import to **Spline** → make it interactive → embed.

**The Lusion-lite recipe:** Spline hero object + Lenis smooth scroll + one SplitText headline + a pinned scroll moment. That combination reads as "expensive and cinematic" to 95% of visitors — and every piece of it is within reach.

---

## The whole thing in one line

**Collect references → name the technique → check the tier → assemble the prompt → build in the matching lane.** Do that repeatedly and your library compounds: every project makes the next one faster, and "I have a vision" becomes "I have a live site" on a path you control.
