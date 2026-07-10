# The Workflow Run-Sheet

> **Repo-alignment header (added 2026-07-09).** Homed under Experience Engineering (20). This is the owner-facing, non-coder run-sheet for a single build. It sits *alongside* the department's canonical 17-step Creative Pipeline (`EXPERIENCE_TECH_STACK.md` §3) — this run-sheet is the four-phase human view; that pipeline is the granular production sequence. Phase 2 ("Design the Spec") of this run-sheet is exactly the 6-station discipline codified in `EXPERIENCE_SPEC_SYSTEM.md`. Companion files: `elite-web-build-system.md`, `vision-to-build-pipeline.md`, `discoverability-architecture.md`.

*The operational detail behind the pipeline. Run this every project. Each stage lists the **trigger** (what starts it), the **skill** you bring, the **tool**, and the **output** you hand forward. When the output is ready, you move to the next stage — that's the trigger for it.*

---

## Phase 1 — Define & Map

| Stage | Trigger | Skill you bring | Tool | Output (hand-off) |
|---|---|---|---|---|
| **Capture** *(always on)* | You see something you love | Recognizing the *moment* | Screen recorder + your library (Design 19 Inspiration Brackets) | A tagged library entry |
| **Define** | You decide to build a thing | Articulating purpose, audience, feeling in one paragraph | A note; pressure-test it | The brief |
| **Sitemap** | Brief is written | Information architecture | A list, or Whimsical | Pages + sections + data each needs |

## Phase 2 — Design the Spec  *(= `EXPERIENCE_SPEC_SYSTEM.md`, the 6 stations)*

| Stage | Trigger | Skill you bring | Tool | Output |
|---|---|---|---|---|
| **Pull references** | Sitemap done | Matching feeling → named technique; honesty about tiers | Your library + tier tagging | 3–6 chosen techniques, each tiered |
| **Wireframe** | References chosen | Layout & focus hierarchy | Whimsical, or Relume | Low-fi layout with techniques placed in zones |
| **Style tokens** | Wireframe done | Taste, restraint | The token system (Elite Web Build System §2) + Brand Genome | Type scale, palette, spacing, one motion curve |

## Phase 3 — Build

| Stage | Trigger | Skill you bring | Tool | Output |
|---|---|---|---|---|
| **Assemble master prompt** | Tokens + wireframe + references ready | Assembling trusted parts | Your prompt fragments + the master shell (Elite Web Build System §6) | One complete build prompt |
| **Build** | Prompt ready | Prompting + visual 3D (if any Tier-2) | Spline (3D) → v0 / Bolt / Lovable, **or** Framer; or hand-build in Next.js (the Arika path) | A working draft |
| **Iterate** | Draft exists | The critical eye — *the real test* | Same build tool | A refined, honest version |

## Phase 4 — Launch & Learn

| Stage | Trigger | Skill you bring | Tool | Output |
|---|---|---|---|---|
| **Launch** | Design is done | Patience with plumbing | Domain/DNS, a form service (Formspree), analytics, an OG share image, Vercel/Netlify/Framer publish | A live URL that actually works |
| **Measure & learn** | Real visitors arrive | Reading data honestly | Analytics (Plausible/GA) | What to change next — back into Capture/Define |

---

## The three things that quietly decide quality

1. **The reference pull (Phase 2) is where "cinematic" becomes concrete.** Skip it and you're prompting a vibe. Do it and you're prompting three named techniques with known tiers.
2. **Iterate (Phase 3) is the real work, not the first generation.** The tool saves you the build, not the thinking. The site that survives your editing is the one worth launching.
3. **The last mile (Phase 4) is where non-coders stall.** Domain, forms, analytics, share image — unglamorous, and exactly where projects die three feet from done. Budget time for it. (See `discoverability-architecture.md` for the findability half of this last mile.)

## The loop

Every finished project drops new entries into your library and teaches you something from real visitors. The next project starts with a fuller library and a sharper eye. The pipeline isn't a line, it's a wheel.

---

*Companion files: **Elite Web Build System** (the stack, tokens, grids, master prompts), **Vision-to-Build Pipeline** (reference library + feasibility tiers), **Discoverability & Architecture** (findability + backend).*
