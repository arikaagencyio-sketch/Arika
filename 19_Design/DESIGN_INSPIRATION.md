# Design Inspiration — Reference Archive

**Status:** North-star reference only, not a finalized spec. Exact hex/type-weight values are **not** confirmed here — those live in [`12_Branding/BRANDING_OS.md`](../12_Branding/BRANDING_OS.md) §2 once the owner finalizes them. This file exists so the visual direction shared during the Design department's founding planning session has a durable, citable home instead of living only in conversation history, per the repo-wide "log it, don't just say it" convention (`GLOBAL_OS.md` §2 item 4). **As of 2026-07-03**, this file also holds the **Inspiration Brackets** system (below) — a structured, per-format intake for ongoing design references the owner wants to build taste/direction from, not just the one-time founding moodboard capture.

---

## Direction confirmed from owner-supplied moodboard imagery (2026-07-01)

- **Palette direction**: Deep Navy, Charcoal Gray, Silver Mist, Accent Gold — names as labeled on the shared brand-kit color-palette reference page. Exact hex values were not legible/confirmed in the source imagery and are not invented here.
- **Typography direction**: Space Grotesk / Satoshi / Neue Montreal for display/headline use; Inter / Manrope for body use — as labeled on the shared typography reference page.
- **Aesthetic direction**: premium enterprise/executive environment — glass and brushed-metal surfaces, gold-on-navy contrast, cinematic lighting, data-visualization motifs (growing bar/line charts, revenue dashboards), architectural grid systems. Physical brand-collateral mockups (notebook, cap, bottle, business cards) shown alongside digital surfaces (dashboards, presentation decks, social carousels).
- **Explicit environment referenced**: an "Executive/Revenue Operations" control-room scene — two figures interacting with a holographic revenue-pipeline visualization — the direct visual ancestor of the "Creative Digital Twin" room doctrine in `19_Design/DESIGN_OS.md` §10 (this scene maps most closely to the "Revenue Operations Center" room).
- **Explicit owner correction**: the imagery shared reads as visibly AI-generated and needs to be elevated to a "non-AI, very human realistic" standard before any real production use — see the corresponding Standards entry in `19_Design/DESIGN_OS.md` §10.

## What this file is not

- Not a finalized brand kit (see `12_Branding/BRANDING_OS.md` §2 for that gap and its closure status)
- Not a set of production-ready hex codes, font license confirmations, or logo lockup specs
- Not a Canva asset — nothing here has been uploaded/created in Canva yet (that's a follow-up execution step, out of scope for this documentation pass)

---

## Inspiration Brackets (added 2026-07-03)

**Purpose.** Per owner direction: when the owner sees a piece of design (a website, a carousel, a reel, a poster, a motion graphic) that captures a direction they want to move toward, it needs a durable, structured home — not just conversation history — so Claude/other agents can read the owner's actual taste before generating new work, and can point back at a concrete reference instead of guessing at "premium" or "cinematic." This is the taste/direction-building system the owner asked for, distinct from the finalized Brand Genome (`12_Branding/BRANDING_OS.md` §2) — inspiration can be broader and more exploratory than the locked brand kit.

**Structure: format-first folders, style tags cross-cutting.** Each bracket below is a real, named category an inspiration reference gets filed under by *output format*. Every entry inside a bracket also carries one or more **style/mood tags** (free-text, lowercase-hyphenated, e.g. `cinematic-gold`, `minimal-glass`, `architectural-grid`) so references can be pulled either by format ("show me Carousel inspiration") or by taste across formats ("show me everything tagged `light-sweep`"). Tags are not a fixed enum — they accumulate organically as real references come in; don't pre-invent a taxonomy before real entries exist.

**Entry template** (one row per reference, inside the relevant bracket's table):

| Field | What goes here |
|---|---|
| Reference | Link (URL) or a precise description if no link exists (e.g. a screenshot description, a named campaign) |
| Style/Mood Tags | One or more hyphenated tags, comma-separated |
| What to extract | The specific, nameable thing about this reference worth reusing — a transition style, a layout rhythm, a color-contrast move, a typographic pairing, a camera move. Not "I like this," but *what* about it is the direction |
| Added | Date |

**Intake process.** When the owner shares a piece of inspiration (a link, an image, a description), file it under the format bracket it matches, tag it, and fill in "What to extract" — the one-line reason it's useful, so future generation prompts can cite it concretely instead of vaguely. If it doesn't fit an existing bracket cleanly, add a new bracket rather than forcing it — the list below is a starting set, not a closed list.

### Website

*(empty — no entries yet; add real references here as the owner supplies them)*

### Carousel (Instagram / social)

*(empty — no entries yet)*

### Reel / Motion Graphic / Video

*(empty — no entries yet)*

### Poster / Static Graphic

*(empty — no entries yet)*

### Cross-format baseline direction (pre-dates the bracket system)

The moodboard direction captured in "Direction confirmed from owner-supplied moodboard imagery (2026-07-01)" above applies across all formats rather than one — it's the aesthetic floor (premium enterprise, gold-on-navy, glass/brushed-metal, cinematic lighting, data-viz motifs) every bracket entry should be read against, not a bracket itself. Treat it as tag `arika-baseline` implicitly applied everywhere until superseded.

## Tool & Reference-Source List (owner-supplied, 2026-07-04)

**Purpose.** Owner shared a raw list of design/UI/3D/motion tools and inspiration sources as direction for Design (19) and Experience Engineering (20) — several of these fill open slots in `DESIGN_LANGUAGE_SYSTEM.md` §2a's Motion/VFX/SFX/3D-5D Tool Registry (`OWNER_INPUT_NEEDED.md` item 48) and Experience Engineering's tech-stack candidate list (item 49). Per the no-silent-invention rule: only names Claude can confidently identify from general public knowledge get a purpose note below; the rest are flagged unverified rather than guessed at. **Naming here is not an adoption decision** — same "named, not connected" status every other candidate tool in this repo carries until the owner confirms otherwise.

| Owner-supplied name (as typed) | Likely identity / purpose | Confidence | Distilled to |
|---|---|---|---|
| flair.ai | AI-generated branded product/scene photography tool | Medium — general knowledge, not independently verified this session | Production Engine candidate note, `DESIGN_OS.md` §3 |
| Khroma | AI color-palette generator trained on liked/disliked colors | Medium | `DESIGN_LANGUAGE_SYSTEM.md` §2a |
| Designspells | Curated design/motion/branding inspiration gallery | Medium | Reference-gallery list below |
| Posterlad | **Confirmed via owner-supplied URL `https://posterlad.com/`** — an e-commerce platform selling abstract art prints/posters ('90s-inspired aesthetic, 100+ designs across minimalist/geometric/typography/organic styles, standard + limited-edition lenticular), for interior-design/art buyers | Confirmed (owner-supplied link, fetched 2026-07-04) | Reference-gallery list below (visual-style reference for Poster/Static Graphic bracket, not a tool/gallery in the browsing sense) |
| Threatr.JS | Likely "Theatre.js" — JS animation/keyframe-sequencing library, commonly paired with Three.js for cinematic camera work | Medium, typo-corrected | `EXPERIENCE_TECH_STACK.md` §2 |
| Spine.desgins | Likely "Spline" — browser-based real-time 3D design tool, already registered | Medium, typo-corrected duplicate | Already in `DESIGN_LANGUAGE_SYSTEM.md` §2a / `EXPERIENCE_TECH_STACK.md` §2 |
| Threlte.xyz | Svelte component framework built on Three.js for 3D web scenes | Medium | `EXPERIENCE_TECH_STACK.md` §2 |
| Peachweb.io | **Confirmed via owner-supplied URL `https://www.peachweb.io/`** (cross-checked via web search) — "PeachWeb: Stunning Interactive 3D Websites Without Code," a no-code builder for interactive 3D websites (or hire-an-expert option), aimed at designers/brands | Confirmed (owner-supplied link + web search, 2026-07-04) | `DESIGN_LANGUAGE_SYSTEM.md` §2a (3D/5D Motion) — a tool, not just an inspiration source |
| Three.JZ | Likely "Three.js" — core WebGL/3D library, already registered | High, typo-corrected duplicate | Already in `EXPERIENCE_TECH_STACK.md` §2 |
| Motionsite | **Confirmed via owner-supplied URL `https://motionsites.ai/`** — a gallery of pre-built, animated landing-page templates/hero sections (copy-and-deploy design prompts/components), free + premium tiers, aimed at designers/agencies/entrepreneurs launching sites quickly with AI-assisted design | Confirmed (owner-supplied link, fetched 2026-07-04) | Reference-gallery list below |
| 21stDEv | "21st.dev" — AI-curated/generated React UI component marketplace, a common design-engineering reference | Medium | `DESIGN_LANGUAGE_SYSTEM.md` §2a |
| npm i framer motion | Confirms the Framer Motion React animation library, already registered | High | Already in `EXPERIENCE_TECH_STACK.md` §2 |
| unsection.com | **Confirmed via owner-supplied URL `https://www.unsection.com/`** — a curated design library of "4,000+ website sections" (heroes, CTAs, pricing, footers), pre-made component designs/hover effects/SVG assets, updated weekly, for web designers/developers wanting ready-made patterns | Confirmed (owner-supplied link, fetched 2026-07-04) | Reference-gallery list below |
| screendesgin | Likely "screendesign"/"screensdesign" — a mobile/UI screen-design inspiration gallery | Low-medium, typo-corrected, unverified | Reference-gallery list below |
| jitter.video | Browser-based motion-graphics design tool | Medium | `DESIGN_LANGUAGE_SYSTEM.md` §2a |
| toolfolio.io | **Confirmed via owner-supplied URL (given as `https://toolfolio.com/`; owner originally typed `.io`, both appear to resolve to the same "Toolfolio" product)** — "All the Tools You Need in One Place," a curated tool-discovery directory spanning brainstorming/diagramming, social schedulers, mockup sites, screen recording, icon libraries, AI meeting assistants, note apps, to-do apps — broader than design-specific, 1M+ claimed users | Confirmed (owner-supplied link + web search, 2026-07-04; direct fetch rate-limited, 429) | Reference-gallery list below |
| getlayers.ai | **Confirmed via owner-supplied URL `https://www.getlayers.ai/`** — "GetLayers," an AI-native template library: copy-paste prompts + design components (99+ templates, 3D scenes, backgrounds, updated weekly) for building landing pages that "don't look AI-made" | Confirmed (owner-supplied link, fetched 2026-07-04) | Reference-gallery list below (a prompt/template library, not a generation engine — reclassified out of `DESIGN_OS.md` §3's Production Engine note) |

### Reference Galleries & Tool Directories (owner-named, not yet mined)

Distinct from the per-item Inspiration Brackets above (which hold *specific pieces* of inspiration with a "what to extract" note): these are named *sources to browse* for future bracket entries, not entries themselves.

- Designspells
- Posterlad — **confirmed**: `https://posterlad.com/`, abstract art-print/poster e-commerce site ('90s-inspired, minimalist/geometric/typography/organic styles) — a visual-style reference for the Poster/Static Graphic bracket, not a browsable design gallery
- ~~Peachweb.io~~ — **confirmed as a tool, not a gallery**: moved to `DESIGN_LANGUAGE_SYSTEM.md` §2a (see table above)
- Motionsite — **confirmed**: `https://motionsites.ai/`, animated landing-page/hero template gallery
- unsection.com — **confirmed**: `https://www.unsection.com/`, curated library of 4,000+ ready-made website section designs (heroes/CTAs/pricing/footers) + hover effects/SVG assets
- screendesign (as typed: "screendesgin")
- toolfolio.io — **confirmed**: "Toolfolio," a broad tool-discovery directory (design mockup sites, icon libraries, social schedulers, and more — not design-only)
- getlayers.ai — **confirmed**: `https://www.getlayers.ai/`, AI-native prompt/template library for landing pages, 3D scenes, and backgrounds (99+ templates, updated weekly) — notably aligned with Design's own "no visible AI artifacts" standard (`DESIGN_OS.md` §10), worth reviewing for the Prompting System (`20_Experience_Engineering/PROMPTING_SYSTEM.md`)

**Status:** owner-named 2026-07-04, none browsed or mined into real Bracket entries yet. When a specific reference gets pulled from one of these, file it into the correct format Bracket above with its own tags and "what to extract" note — the gallery name itself doesn't go in a Bracket row.

## What the Inspiration Brackets are not

- Not populated yet — every bracket above is a real, ready-to-fill structure with zero real entries. Per the no-silent-invention rule, no placeholder references were fabricated to make brackets look complete.
- Not a replacement for the Brand Genome — brackets can hold exploratory/aspirational direction that never becomes brand-official.

## Changelog

- 2026-07-01 — Created alongside the Design department (19) to capture the owner-supplied moodboard direction from this planning session as a durable reference. — Claude Code (Sonnet 5)
- 2026-07-03 — Added the Inspiration Brackets system (format-first folders — Website/Carousel/Reel/Poster — with cross-cutting style/mood tags), per owner request for a structured way to capture design taste/direction so future generation work can cite concrete references instead of vague style words. All brackets currently empty — real entries get added as the owner supplies them, not fabricated here. — Claude Code (Sonnet 5)
- 2026-07-04 — Added the Tool & Reference-Source List: a raw, owner-supplied list of 18 design/UI/3D/motion tools and inspiration galleries, triaged honestly by confidence rather than guessed at uniformly — confidently-identified tools distilled into `DESIGN_LANGUAGE_SYSTEM.md` §2a (Khroma, 21st.dev, Jitter) and `EXPERIENCE_TECH_STACK.md` §2 (Threlte, Theatre.js), likely-typo'd duplicates of already-registered tools flagged (Spline, Three.js, Framer Motion), and low-confidence names left explicitly unverified (GTA.Gallery, Posterlad, Peachweb.io, Motionsite, unsection.com, toolfolio.io, getlayers.ai) rather than fabricated. Also added the Reference Galleries & Tool Directories list, distinct from real Bracket entries — named sources to browse later, not inspiration entries themselves. — Claude Code (Sonnet 5)
- 2026-07-04 — **Motionsite confirmed**: owner supplied the real URL (`https://motionsites.ai/`), fetched and verified — a gallery of pre-built, animated landing-page templates/hero sections (copy-and-deploy, free + premium), aimed at designers/agencies/entrepreneurs. Upgraded from "low confidence, unverified" to confirmed in both the Tool & Reference-Source table and the Reference Galleries list above. — Claude Code (Sonnet 5)
- 2026-07-04 — **Posterlad confirmed**: owner supplied the real URL (`https://posterlad.com/`), fetched and verified — not a browsable design-inspiration gallery as originally guessed, but an e-commerce site selling abstract art prints/posters ('90s-inspired aesthetic, minimalist/geometric/typography/organic styles). Reclassified as a visual-style reference for the Poster/Static Graphic bracket rather than a tool-directory-style gallery. — Claude Code (Sonnet 5)
- 2026-07-04 — **Peachweb.io confirmed**: owner supplied the real URL (`https://www.peachweb.io/`); direct fetch was blocked (403), cross-checked via web search instead — "PeachWeb: Stunning Interactive 3D Websites Without Code," a no-code 3D-website builder. Reclassified out of the Reference-Gallery list (it's a tool, not a browsable inspiration source) and distilled into `DESIGN_LANGUAGE_SYSTEM.md` §2a's 3D/5D Motion category as an alternative/adjacent candidate to Spline. — Claude Code (Sonnet 5)
- 2026-07-04 — **unsection.com confirmed**: owner supplied the real URL (`https://www.unsection.com/`), fetched and verified — a curated library of 4,000+ ready-made website section designs (heroes/CTAs/pricing/footers) plus hover effects and SVG assets, updated weekly. Upgraded from "not confidently identified" to confirmed in both the Tool & Reference-Source table and the Reference Galleries list. — Claude Code (Sonnet 5)
- 2026-07-04 — **toolfolio confirmed**: owner supplied `https://toolfolio.com/` (originally typed as "toolfolio.io" in the raw list; both names appear to resolve to the same product per web search — direct fetch was rate-limited, 429, so identity confirmed via search instead). "Toolfolio: All the Tools You Need in One Place" — a broad tool-discovery directory, not design-specific (also covers social schedulers, icon libraries, meeting assistants, etc.). Upgraded from "not confidently identified" to confirmed. — Claude Code (Sonnet 5)
- 2026-07-04 — **getlayers.ai confirmed**: owner supplied the real URL (`https://www.getlayers.ai/`), fetched and verified — "GetLayers," an AI-native prompt/template library (99+ templates, 3D scenes, backgrounds) for landing pages designed to not "look AI-made." Originally mis-triaged as a possible Production Engine generation-tool candidate in `DESIGN_OS.md` §3 — corrected there and reclassified here into the Reference Galleries list, since it's a template/prompt library rather than a generation engine. Flagged as a useful reference for the Prompting System (`20_Experience_Engineering/PROMPTING_SYSTEM.md`) given its explicit anti-"AI-made-look" framing, which mirrors Design's own §10 standard. — Claude Code (Sonnet 5)
- 2026-07-04 — **GTA.Gallery removed** per explicit owner direction — could not be identified/verified and the owner chose to drop it rather than keep chasing it. Removed from the Tool & Reference-Source table and the Reference Galleries list; the name remains visible only in the 2026-07-04 changelog entry recording the original raw list, as a historical record. — Claude Code (Sonnet 5)
