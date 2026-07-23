# Platform Intelligence Layer (PIL) — Enterprise Integration & Migration Report

**Version:** v0.1
**Last updated:** 2026-07-23
**Owner:** Mary Thuo (Agency Governance, 00)
**Author of this pass:** Claude Code (Opus 4.8)
**Status:** Report complete. Canonical registry **established** (`04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md`); all cross-department edits **staged as a reviewable roadmap here, not applied** (owner decision, 2026-07-23 — clean decide→apply trail, like AEIT Phase Zero).

> This is an enterprise-architecture integration report. It sits beside the AEIT package and is governed by the same review checklist (`AEIT_00 §5`) and reality gates (`AEIT_10`). It is **not** a numbered AEIT artifact.

---

## 1. Executive Summary

A new capability — the **Platform Intelligence Layer (PIL)** — has been introduced: upstream *behavioral* intelligence about how each digital platform works (psychology, trust, discovery, communication/visual/motion language), consumed **before** assets are produced. PIL is explicitly **not** a distribution channel and **not** a social-media document.

The source brief requested a standalone department, a 28-department migration, and a new folder tree. Owner decisions (2026-07-23) resolved that against the agency's own ratified governance (`AEIT_00 §4–5`: right-sized, reconcile-before-build, no structure ahead of content, propose-then-enact) on a solo, 0-client, $0-revenue business:

1. **Scope** → right-sized, reconcile-first: PIL is **one canonical registry**, not a department.
2. **Owner** → **Content (04)** owns it (home of ACCOS, PIL's primary consumer); Marketing (03) keeps the downstream distribution view.
3. **Deliverable** → establish the registry + this report now; **stage** all cross-department edits.

**Net effect:** PIL becomes native by *extending* three artifacts that already describe platform objects (Marketing §10, Content's Notion `Platform` field, Sector's Social Media Sector Layering draft) rather than adding a parallel structure. **One new registry, one report. Zero new departments, folders, agents, or schema columns.**

---

## 2. Architecture Impact Assessment

**Key architectural insight:** PIL is *not* a new free-floating "intelligence layer." The repo models intelligence as **departments that produce it** + the single **IntOS pipeline** (`AEIT_07`). PIL maps onto that as **one Intelligence knowledge-object type — the Platform** — an instance of the *Intelligence* registry already anticipated in `REGISTRY_TAXONOMY_REFERENCE.md` and blueprinted in IntOS. The author's "stack of layers (Sector/Audience/Brand/Revenue)" mental model is **not** imported.

| Architecture element | Impact |
|---|---|
| **Intelligence Layer hierarchy** | No new hierarchy. PIL = one Intelligence object type, owned by Content, consumed via `AEIT_09` contracts / IntOS Distribution (`AEIT_07` layer 7) once activated. |
| **IntOS (`AEIT_07`)** | "Platform" registered as an Intelligence knowledge-object type and, on activation, an `AEIT_08` Source. Reality-gated — design only. |
| **ACCOS (Content)** | PIL enters as an **upstream design constraint** at Stages 2/5/7/10/11 (not a new stage). |
| **Design / Motion / Production (19), Experience Engineering (20)** | Visual & motion language become platform-conditioned; format/aspect ratio derive from the profile. |
| **Distribution Engineering (Marketing 03)** | Marketing §10 platform-role table reframed as the **downstream twin** of the canonical registry; ownership of distribution unchanged. |
| **Knowledge graph / canonical model (`AEIT_06`)** | "Platform" is a role-modeled entity consumed by many; no per-department copies. |
| **Prompt / AI orchestration** | Existing agents gain a *consumption reference*; **no new agent** (honors the deliberate no-platform-agent decision). |

**Passes the `AEIT_00 §5` gate:** single owner (Content); canonical fit (extends, does not reinvent); contract (IntOS/`AEIT_09`); no circular dependency; reality label (design-only, reality-gated); logged.

---

## 3. Department Impact Matrix

| # | Department | Role re: PIL | Change required |
|---|---|---|---|
| 04 | **Content** | **Owner** | Registry (done) + ACCOS/agent cross-refs (§8, §10) |
| 03 | Marketing | Consumer — downstream distribution view | Reframe §10 table to cite registry |
| 01 | Sector | Consumer + supplies per-sector overlay | Surface Social Media Sector Layering draft into `SECTOR_OS.md` |
| 19 | Design | Consumer — visual/motion language, format per platform | Cross-ref in storyboard + production-engine reasoning |
| 20 | Experience Engineering | Consumer — Website = owned hub; motion language | Light cross-ref |
| 12 | Branding | **Input provider** (identity/voice) + consumer | Cross-ref (PIL consumes brand genome; brand tolerance per platform) |
| 05 | Sales | Minor — social-selling / platform trust context | One-line optional cross-ref |
| 07 | Client Success | Minor — advocacy captured on platforms | One-line optional cross-ref |
| 16 | Automation | Minor — engagement-layer DM automation per platform | One-line optional cross-ref |
| 21 | **Presence** | **Downstream operational owner** — consumes PIL's platform behavior to run presence across layers | Cross-ref: PIL = upstream *behavioral intelligence* (Content/IntOS-owned); Presence 21 = downstream *operational* owner (added 2026-07-23) |
| 00 | Governance / IntOS | Registers "Platform" as an Intelligence source | `AEIT_07`/`AEIT_08` note; `GLOBAL_OS` §6/§11 + changelog; `REGISTRY_TAXONOMY` note |
| 02, 06, 08, 09, 10, 11, 13, 14, 15, 17 | Offer, ClientPartner, Ops, Finance, Legal, HR, Tech Stack, Audits, Consulting, AI Enablement | **Not a consumer** | **No change.** Stated explicitly — honest "no change" is the right-sizing. |

### Per-department analysis (consumers only; the source brief's 9-part template, at right altitude)

- **Content (04) — Owner.** *Current:* owns ACCOS + the Notion `Platform` tag. *Impact:* PIL becomes the upstream constraint the tag already implies. *New responsibilities:* maintain the registry; keep it reconciled with Marketing §10. *Dependencies:* Branding (identity), Sector (overlay), Audience. *Outputs:* the registry; platform-native briefs. *Workflows:* ACCOS 2/5/7/10/11. *Agents:* opportunity-mapper, brief-builder, multiplication-engine, publishing-gate (consumption edits). *Knowledge objects:* the registry. *Validation:* platform-native filter folded into publishing-gate.
- **Marketing (03) — Consumer.** *Current:* §10 platform-role table (role+KPI), owns distribution. *Impact:* table becomes the downstream view of the registry; ownership unchanged. *New responsibilities:* none new — cite the registry. *Validation:* distribution sequencing respects behavioral fit.
- **Sector (01) — Consumer + overlay provider.** *Current:* unmigrated Social Media Sector Layering draft. *Impact:* becomes the per-sector overlay on the platform baseline. *Outputs:* sector overlay notes. *Knowledge objects:* draft surfaced into `SECTOR_OS.md`.
- **Design (19) / EE (20) — Consumers.** *Impact:* visual & motion language conditioned on target platform; format/aspect ratio from the profile. *Validation:* brand/environment checks include platform-native fit.
- **Branding (12) — Input + consumer.** *Impact:* PIL consumes the brand genome/voice; brand-tolerance-per-platform noted. No brand redefinition.

---

## 4. Workflow Impact Matrix

| Workflow | Dept | Modification |
|---|---|---|
| ACCOS Stage 2 (Audience Mapping) | 04 | Map audience by platform behavior, not only role |
| ACCOS Stage 5 (Opportunity Mapping) | 04 | Platform-fit as a scoring input |
| ACCOS Stage 7 (System Design) | 04 | Platform-native copy/visual/motion templates |
| ACCOS Stage 10 (Multiplication) | 04 | Native executions per platform, not resizes |
| ACCOS Stage 11 (Distribution Engineering) | 04→03 | Sequence per behavioral fit + buyer journey |
| Social Ecosystem repurposing flow | 03 | Each format targets its platform's behavioral profile |
| Sector mapping | 01 | Emit per-sector platform overlay |
| Creative Pipeline (Design production) | 19 | Storyboard format/motion conditioned on `Platform` |

**No workflow is removed or re-owned.** The Content→Design→Marketing handoff chain (`CONTENT_OS.md` §12) is unchanged.

---

## 5. Knowledge Base Changes

- **New:** `04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md` (canonical) — **created.**
- **Surfaced:** `01_Sector/Social Media Sector Layering. Draft 14.md` → migrate into `SECTOR_OS.md` as the per-sector overlay (staged).
- **Reframed (annotation only):** `MARKETING_OS.md` §10 platform table → downstream twin (staged).
- **No knowledge base is deleted or rewritten.**

---

## 6. New Folder Structure

**None.** PIL is a registry, not a plugin. Per `REGISTRY_TAXONOMY_REFERENCE.md`: *"Promoting a registry means adding it as a section/doc, not necessarily creating a new top-level folder."* The registry lives in the owning department's folder (`04_Content/`).

---

## 7. New Documents Required

Exactly two, both in this pass:
1. `04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md` — the canonical registry (**created**).
2. `00_Agency_Governance/enterprise_architecture/PIL_INTEGRATION_REPORT.md` — this report (**created**).

No further new documents. The Watchlist (registry §4.3) prevents empty per-platform stub docs.

---

## 8. Existing Documents to Modify (staged — NOT applied this pass)

| # | File | Edit | Applied? |
|---|---|---|---|
| E1 | `04_Content/CONTENT_OS.md` | §3/§10: note PIL as upstream ACCOS constraint (Stages 2/5/7/10/11); `Platform` Notion field implies the registry; §8 Decision Log entry | ☐ staged |
| E2 | `03_Marketing/MARKETING_OS.md` §10 | Annotate platform table as downstream twin of the registry; cross-ref | ☐ staged |
| E3 | `01_Sector/SECTOR_OS.md` | Surface Social Media Sector Layering draft as per-sector overlay; baseline-vs-overlay note | ☐ staged |
| E4 | `19_Design/DESIGN_OS.md` | Cross-ref: visual/motion language + format per platform from the registry | ☐ staged |
| E5 | `20_Experience_Engineering/EXPERIENCE_ENGINEERING_OS.md` | Light cross-ref (Website = owned hub; motion language) | ☐ staged |
| E6 | `12_Branding/BRANDING_OS.md` | Cross-ref: PIL consumes brand genome; brand tolerance per platform | ☐ staged |
| E7 | `GLOBAL_OS.md` | §6 registry index (note Platform registry) + §11 (Intelligence registry instance) + changelog entry | ☐ staged |
| E8 | `REGISTRY_TAXONOMY_REFERENCE.md` | One line: Platform = first populated instance of the Intelligence registry | ☐ staged |
| E9 | `00_Agency_Governance/enterprise_architecture/AEIT_07` + `AEIT_08` | Note Platform as an Intelligence object type / future Source (reality-gated) | ☐ staged |

Each edit is small, additive, and carries the `AEIT_00 §5` verdict.

---

## 9. Prompt Updates (staged — NOT applied this pass)

Consumption references only — no behavior rewrite, no new prompt files:

| Agent prompt | Addition |
|---|---|
| `.claude/agents/content-opportunity-mapper.md` | Platform-fit as a scoring input; cite registry |
| `.claude/agents/content-brief-builder.md` | Derive `Platform` tag + platform-native Visual Direction from the profile |
| `.claude/agents/content-multiplication-engine.md` | Native executions per platform, not resizes |
| `.claude/agents/content-publishing-gate.md` | Sharpen the existing **Distribution** governance alignment: "does it fit the target platform's behavioral profile?" (a fold, not a 9th gate) |
| `.claude/agents/marketing-demand-generation.md`, `marketing-seo-aeo-geo.md` | Cite registry for channel execution / discoverability |
| `.claude/agents/design-storyboard-generator.md`, `design-production-engine-coordinator.md` | Format/aspect ratio + motion language per target platform |

---

## 10. AI Agent Updates

**Zero new agents.** This is the load-bearing right-sizing decision: the agency already declined a distribution/platform agent (`CONTENT_OS.md` §5, `MARKETING_OS.md` §10). PIL is consumed by the agents in §9 via prompt references. No new memory streams, tools, or triggers are added; agent files are **not** touched in this pass (so `arika list` / `npm test` stay green).

---

## 11. Database / Schema Changes

**None.** The Notion content-brief database already has a `Platform` multi-select field (`CONTENT_OS.md` §10). PIL adds *meaning* to that field (it now implies consulting the registry), not columns. **One data note, not a schema change:** the field's option set (Instagram/LinkedIn/Facebook/X/Pinterest/Tumblr/Newsletter/Website) diverges from Marketing §10's set — see the reconciliation flag (§14 risk R3). No IntOS/`AEIT_06` schema change; "Platform" reuses the role-modeled entity pattern.

---

## 12. Cross-Reference Updates

Bidirectional links to establish (staged): registry ⇄ `CONTENT_OS.md`, registry ⇄ `MARKETING_OS.md` §10, registry ⇄ `SECTOR_OS.md`, registry ⇄ `DESIGN_OS.md` / `EXPERIENCE_ENGINEERING_OS.md` / `BRANDING_OS.md`, registry ⇄ `AEIT_07`/`AEIT_08`, and `GLOBAL_OS.md` §6/§11. Coherence target: `grep -ri "Platform Intelligence"` resolves to the one canonical registry; no second competing platform list exists.

---

## 13. Validation Rules

Folded into the **existing** `content-publishing-gate`, not a new gate:
- **Platform-native?** Asset matches the target platform's behavioral profile (comm/visual/motion). → sharpens the existing *Distribution* alignment.
- **Narrative preserved?** Native execution must not alter the strategic narrative.
- **Journey-stage fit?** Platform revenue function matches the intended buyer-journey stage.
The 8 validation filters, 3 never-publish rules, 4-layer approval, and `unevidenced_claims` are unchanged.

---

## 14. Repository Migration Plan + Risk Assessment

**Migration = the registry (done) + the 9 staged edits (E1–E9) applied on owner approval.** No data migration; no folder moves; no agent-file changes in this pass.

| Risk | Assessment | Mitigation |
|---|---|---|
| R1 — PIL duplicates Marketing's distribution ownership | Real if framed as "distribution" | Registry §1 states PIL is *not* distribution; §10 is the downstream twin |
| R2 — Structure ahead of content (audit's #1 failure) | Behavioral baselines are real; measured data is not | Reality-gated; Watchlist over empty stubs; no accounts assumed |
| R3 — Platform-set divergence (Marketing §10 vs. Notion field) | Live coherence gap | Flagged in registry §4; `[OWNER: confirm in-scope set]`; not resolved by invention |
| R4 — Scope creep back to a new department | The brief pushes maximal | Owner ratified right-sized; guardrails in registry §1 + report §6/§10 |
| R5 — Invented platform metrics | Would breach the no-invention rule | Behavioral fields only; zero numeric claims |

---

## 15. Implementation Order (when owner approves the staged edits)

1. **E7/E8/E9** — governance anchors (GLOBAL_OS §6/§11 + changelog, registry taxonomy, AEIT notes) so the registry is discoverable.
2. **E1** — Content OS (ACCOS constraint + Decision Log).
3. **E2** — Marketing §10 reframe (the primary reconciliation).
4. **E3** — Sector overlay surfaced.
5. **E4/E5/E6** — Design / EE / Branding cross-refs.
6. **§9 prompt edits** — only after the OS edits land (agents point at settled docs). Re-run `arika list` / `npm test` after.
7. **Owner reconciliation** — resolve R3 (canonical platform set) before prompt edits harden the set.

---

## 16. (folded into §14) Risk Assessment

See §14.

---

## 17. Completion Checklist

- [x] Canonical registry established (`04_Content/PLATFORM_INTELLIGENCE_REGISTRY.md`)
- [x] Migration report written (this file, all 17 sections)
- [x] Reconciled with Marketing §10, Content Notion field, Sector draft — no duplicate list
- [x] No new department / folder / agent / schema column
- [x] No invented metrics; platform-set divergence flagged to owner
- [x] Passes `AEIT_00 §5` review gate (single owner, canonical fit, contract, reality label)
- [ ] Owner approves staged edits E1–E9 + §9 prompt edits
- [ ] Owner resolves R3 (canonical in-scope platform set)
- [ ] Staged edits applied in the §15 order; `arika list` / `npm test` green
- [ ] `GLOBAL_OS.md` changelog + Content §8 Decision Log entries recorded on apply

## Decision Log
- **2026-07-23 — PIL integration reported and registry established, right-sized/reconcile-first.** Registry created; all cross-department edits staged (E1–E9 + prompts), not applied — clean decide→apply trail. No new department/folder/agent/schema. Platform-set divergence (Marketing §10 vs. Notion field) flagged to owner, not invented. — Claude Code (Opus 4.8)

## Changelog
- **v0.1 (2026-07-23):** Created. — Claude Code (Opus 4.8)
