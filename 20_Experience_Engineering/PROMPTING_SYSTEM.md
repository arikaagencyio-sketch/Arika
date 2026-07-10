# Prompting System — Structured, ID'd, Stateful Generative Architecture

**Status:** Proposed, not built. Added 2026-07-03 per direct owner request during this department's founding session: not just a named "AI" capability, but a real, structured, navigable system for *how* the AI actually generates assets — reference-photo-driven or text-only — with the right sequence, right flow, and a "hyper-realistic, hyper-efficient" quality bar, where every generated thing is IDed, stateful, and navigable. Cross-referenced from [`EXPERIENCE_ENGINEERING_OS.md`](EXPERIENCE_ENGINEERING_OS.md) §3 (Prompting System capability) and §6 (Structured Prompt Generation skill).

---

## 1. Why this exists

Two things ground this system so it isn't invented from nothing:

1. **Design (19) already has a real, owner-set quality standard**: "No visible AI artifacts — human-realistic production" (`19_Design/DESIGN_OS.md` §10) — directly from owner feedback that AI-mockup drafts needed to be elevated to a premium, human-realistic standard before real use. That standard currently lives at the *review* stage. This system exists to push it earlier, into *prompt construction*, so quality is a property of how a prompt is built, not just something caught (or missed) at review.
2. **The source material's own "AI's Role Today" scope** (`EXPERIENCE_ENGINEERING_VISION.md` §2): generating concept art and moodboards, creating background imagery and textures, assisting with copy and storytelling, generating initial 3D concepts, helping developers write animation logic, optimizing assets and performance. This is the scope of what actually needs structured prompting — not "AI generation" as a vague, unbounded capability.

The goal: "hyper-realistic, hyper-efficient" becomes a repeatable, checkable property of every generated asset — not a skill that lives only in whoever happens to be prompting that day.

## 2. Prompt Record — the ID'd, stateful unit

Every generative step (one image, one video clip, one 3D asset, one motion sequence) gets a real record, not a one-off chat prompt that disappears. Proposed fields:

| Field | Purpose |
|---|---|
| **ID** | Stable identifier: `EXP-{project-slug}-{scene-#}-{asset-type}-v{n}`. Every generated asset is individually addressable, versionable, and referenceable from the Experience Pattern Library's "AI prompts" field (`EXPERIENCE_ENGINEERING_OS.md` §3) or from Design's own Production Engine work. |
| **Asset Type** | image / video / 3D model / motion clip / voice / music — mirrors Design's existing Production Engine chain (Story → Image → Video → Voice → Animation → Music → Enhancement/Upscale → Assembly, `19_Design/DESIGN_OS.md` §3). |
| **Reference Input** | A real source, never invented: a linked entry from Design's Inspiration Brackets (`19_Design/DESIGN_INSPIRATION.md`), an owner-supplied reference photo, or explicitly "none (text-only)." No Prompt Record should claim a reference that doesn't exist. |
| **Prompt Template** | Parameterized text — pulls brand tokens (color/type/motion values) from Branding's Brand Genome once the Design Language System's token surface (`19_Design/DESIGN_LANGUAGE_SYSTEM.md` §1) is queryable, rather than hardcoding brand values per-asset. Until that surface is real, tokens are inserted manually from `12_Branding/BRANDING_OS.md` §2. |
| **Quality Bar** | Reference to §3 below — the checklist a record must pass. |
| **Sequence Position** | Which Creative Pipeline step (Draft A or Draft B, `EXPERIENCE_TECH_STACK.md` §3) and which of the 9 Storyboard fields (Scene/Camera/Lighting/Object/Text/Narration/Motion/Interaction/Goal, `EXPERIENCE_ENGINEERING_OS.md` §3) this record fulfills. |
| **Target Tool** | Which real or proposed tool executes it — e.g. OpenArt or Claude Design (both real, connected, `19_Design/DESIGN_OS.md` §3) for image/video; a named-not-connected candidate from `EXPERIENCE_TECH_STACK.md` §2 for code-driven motion/3D. |
| **State** | `Draft → Generated → Enhanced → Reviewed → Approved → Final`. Directly extends Design's existing doctrine that "the storyboard is the durable asset, not the generated output" (`19_Design/DESIGN_OS.md` §10) — when generation tooling improves, regenerate from the Prompt Record, don't start over from a blank prompt. |

**Nothing here is wired to a real system yet.** No real Prompt Record exists in this repo as of this pass — this section defines the structure, not a populated table.

## 3. Quality bar — what "hyper-realistic, hyper-efficient" actually checks

Built from three things already established or captured elsewhere in this repo, rather than invented fresh for this file:

1. **Design's no-visible-AI-artifacts standard** (`19_Design/DESIGN_OS.md` §10) — the human-realism floor. A Prompt Record cannot reach "Approved" if its output reads as visibly AI-generated.
2. **Creative DNA** (7 questions, `EXPERIENCE_ENGINEERING_OS.md` §10 / `EXPERIENCE_ENGINEERING_VISION.md` §2) — the creative/story-level check: does it tell a compelling story, does the motion have purpose, does it reinforce the brand, does it support a business objective, does it end with a clear action.
3. **Quality Assurance Framework** (11 items, `EXPERIENCE_ENGINEERING_OS.md` §3 / `EXPERIENCE_ENGINEERING_VISION.md` §3) — the technical/production-level check, specifically the items relevant to a single generated asset: Animation quality, Performance, Accessibility, Browser compatibility.

"Hyper-efficient" (the owner's second criterion, alongside "hyper-realistic") means: no Prompt Record gets regenerated from scratch when it can instead be re-run from its existing template with an updated Target Tool or an incremental parameter change — the ID + State fields exist specifically to make this possible instead of re-prompting blind each time.

A Prompt Record cannot move to **Approved** state without passing all three checks above.

## 4. Sequencing doctrine

No Prompt Record gets created before its scene's Storyboard Library entry (the 9-field template) is filled in. This formalizes "storyboard-before-generation" — already real Design doctrine for video assets (`19_Design/DESIGN_OS.md` §10) — at the level of *every* generated asset in an experience, not just video.

## 5. Reference-image workflow

When a real reference exists (a photo, a moodboard image, a piece of inspiration the owner points at), it becomes a Prompt Record's Reference Input via Design's existing Inspiration Brackets structure (`19_Design/DESIGN_INSPIRATION.md`), which already has a real entry template: Reference (link or description) / Style-Mood Tags / What to extract / Added date. A Prompt Record's Reference Input field should link to a real Inspiration Bracket entry rather than re-describing the reference inline — one source of truth for "what does this look like," not two.

When no reference exists, the Prompt Record explicitly states "none (text-only)" rather than silently omitting the field — the field's presence-or-explicit-absence is itself part of the record.

## 6. Relationship to Design (19)

This is a **shared system**, not exclusive to Experience Engineering. Design (19) already has two live, connected generative tools — OpenArt and Claude Design (`19_Design/DESIGN_OS.md` §3) — that need prompting discipline *today*, independent of whether Experience Engineering ever ships a real interactive experience. Primary ownership of this file stays in Experience Engineering (20) because the multi-scene sequencing need (many Prompt Records chained across a Storyboard Library) is most complex there, but it's cross-referenced both ways: `19_Design/DESIGN_OS.md` §3's Production Engine row and `19_Design/DESIGN_LANGUAGE_SYSTEM.md` §4's Skill Catalog both point here.

## 7. Status

Proposed, not built. Zero real Prompt Records exist. No ID convention, state machine, or reference-linking has been implemented in any real tool (not Notion, not ClickUp, not a database) — see `00_Agency_Governance/OWNER_INPUT_NEEDED.md` item 53 for the open decision on where Prompt Records would actually live once this becomes real. Sourced from the pasted "AI's Role Today" scope plus this session's direct owner request for a formal ID'd/stateful system — this file is architecture, not an operating system that exists yet.

## Changelog

- 2026-07-03 — File created per direct owner request, after reviewing the first draft of Experience Engineering (20)'s founding plan, for a structured prompting/ID/state system rather than leaving generative-AI use as a vague capability name. Built from Design's existing no-visible-AI-artifacts standard, the source's Creative DNA and QA Framework checklists, and Design's existing Inspiration Brackets/storyboard-before-generation doctrine — cross-referenced rather than duplicated. Explicitly flagged as a shared system serving both Design (19)'s live Production Engine and Experience Engineering (20)'s future builds. — Claude Code (Sonnet 5)
