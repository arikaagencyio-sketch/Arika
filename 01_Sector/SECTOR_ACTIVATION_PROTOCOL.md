# Sector Activation Protocol — Sector #002 onward

**Department:** Sector (01) · **Status:** 🔲 **SKELETON — provisional.** Completed only at Gate 9, after Hospitality #001 is validated.
**Version:** v0.1 (2026-08-20)

**Purpose.** The repeatable procedure for activating any new sector, so that Sector #002 is authored as a **plugin** rather than re-derived as an architecture.
**Authority.** Subordinate to [`SECTOR_ACTIVATION_CONTRACT.md`](SECTOR_ACTIVATION_CONTRACT.md) and [`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md). Authoritative for activation sequencing only.
**Inputs.** The 14-slot Plugin Interface · the Lifecycle State machine · the validated Hospitality plugin.
**Outputs.** A completed sector plugin pack · a sector promoted through the Lifecycle State machine on evidence.

> ⚠️ **Why this file is deliberately incomplete.** A protocol extracted before its first implementation is validated is a guess dressed as a standard. The gates below are stable; **the slot classification in §4 is provisional and will change** where Hospitality proves something is not universal after all.

---

## 1. The one rule that governs everything else

> **Do not replicate Hospitality. Extract the pattern.**

Copying a sector's database is how a general engine becomes a hospitality engine with other sectors bolted on. Activation means **authoring 14 slots**, not cloning 14 tables. What changes per sector is *which sources are T1, which signal types dominate, what the timing table says, and what the words are.* What never changes is the schema, the engines, the doctrine and the event bus.

---

## 2. No third loop

Three constructs already exist and are **not** replaced by this file:

| Construct | Where | What it does |
|---|---|---|
| **Cognition Runtime Loop** (14 steps) | `SECTOR_ACTIVATION_CONTRACT.md` §6 | how a single Sector *task* executes |
| **Per-sector Cross-Loop** (7 links: WHEN → WHY → HOW → WHO → WHICH → WHAT → WHERE) | `SECTOR_ACTIVATION_CONTRACT.md` §14.2 | how a sector's *commercial content* is authored |
| **Lifecycle State machine** (11 evidence-gated states) | `SECTOR_NOTION_SCHEMA.md` DB 1 | how a sector's *maturity* is tracked |

**This protocol sequences them into gates.** It introduces no new loop, no new state, and no new vocabulary.

---

## 3. The gates

Each gate names its **entry condition**, its **work**, its **exit evidence**, and the **Lifecycle State** it can justify. Promotion is evidence-gated — *no self-promotion without the underlying rows.*

| Gate | Entry condition | Work | Exit evidence | Lifecycle State |
|---|---|---|---|---|
| **A · Qualify** | A vertical exists in DB 1 with a `Sector Priority Score` | Confirm the score's band; confirm capability fit; confirm no Legal (10) blocker | `Priority Band = P1/P2`; regulated verticals flagged | `Discovered` |
| **B · Scope** | Gate A passed | Choose **one** sub-sector. Set `Status = Target`. Define geography scope + validation places (each must demonstrate a *different* demand relationship) | One `Target` sub-sector; geography scope named | `Mapped` |
| **C · Author the plugin** | Gate B passed | Fill the 14 slots (`SECTOR_OS_ARCHITECTURE.md` §3). Run the 7-link Cross-Loop to generate the content. Leave unresearched slots **empty** | A plugin pack with every slot either filled-and-cited or explicitly ⬜ | `Intelligence-Rich` |
| **D · Register sources** | Slot P8 authored | Web-verify each candidate publisher. Record real `Feed Type`, and an endpoint **only if one genuinely exists**. Promote `candidate → active` | Zero `active` sources without a verification call; every source names a `consumers` DB | — |
| **E · Load** | Gates C+D passed | Write plugin values into core fields: signals, geography, routes, destination profiles, findings, linguistics, audience, DM titles, offer matrix | Rows exist, cited, `Confidence` set to match evidence | `Validated` |
| **F · Resolve** | Gate E passed | Run the Resolution Engine (`SECTOR_OS_ARCHITECTURE.md` §4) for each validation place | **The outputs are structurally different per place.** If identical, the model is wrong — stop | `Offer-Ready` |
| **G · Route** | Gate F passed | Emit the packet: Content Opportunities (04), offer match / `GAP — needs OEOS` (02), the CRM bridge mapping (ClickUp) | Downstream rows exist and resolve upstream | `Content-Ready` / `Acquisition-Ready` |
| **H · Live-loop** | Gate G passed | Move one real signal date. Confirm the change versions rather than overwrites, **names what it invalidates**, and emits its event | A change record with a named invalidation set | `Campaign-Ready` |
| **I · Generalize** | Gate H passed | Reclassify every slot (§4). Run the plugin-removal test. Record what this sector proved *not* universal | Updated §4 classification + a decision-log entry | — |

**Gates F and I are the falsification gates.** Everything else can succeed while the architecture is still wrong; those two cannot.

---

## 4. Slot classification — PROVISIONAL

Every element is **universal** (core, never re-authored), **plugin** (re-authored per sector), or **configurable rule** (core field, plugin-supplied value). **This table is a hypothesis until Gate I of Hospitality #001 confirms it.**

| Slot | Provisional class | Confidence | Note |
|---|---|---|---|
| P1 Ontology | **plugin** | high | Every sector has a different taxonomy; the *shape* (vertical → industry → model → archetype) is universal |
| P2 Entity/asset typology + rules | **plugin** | high | The rule *mechanism* (signal→archetype filter) is universal; the archetypes are not |
| P3 Demand model | **plugin** | high | The `Demand Pattern` category is universal |
| P4 Geography scope | **configurable rule** | medium | The place-tree is universal and shared; the *scope* is per sector. Whether `Destination` is a universal level or travel-specific is **open** |
| P5 Destination themes | **plugin** | ⚠️ **low** | **Is a destination profile universal at all?** It is obviously right for travel-driven sectors. For B2B SaaS, geography may carry no demand-theme meaning — in which case DB 16 is a *travel-family* object, not a core one. **Gate I must rule.** |
| P6 Signal-type profile | **configurable rule** | high | The 21 values are universal; the weighting is per sector |
| P7 Timing rules | **configurable rule** | high | The six activation date fields are universal; the offsets are per sector. The `Any sector · Regulatory` row is genuinely universal |
| P8 Source pack | **plugin** | high | The source *schema* and tier hierarchy are universal |
| P9 Audience + DMs | **plugin** | high | The `Operator/Buyer/Amplifier/Enabler` lens is universal |
| P10 Linguistics | **plugin** | high | The 5-layer model is universal |
| P11 Offer ladder | **plugin** | high | Entry→Expansion→Transformation + the 12 capability families are universal |
| P12 Content pillars | **plugin** | high | ACCOS, the atomic unit, and the scoring model are universal |
| P13 Seasonality + compression | **configurable rule** | medium | The compression *rule* is universal; the threshold is per sector. Whether every sector has "seasonality" is **open** |
| P14 KPI semantics | **configurable rule** | high | DB 12's fields are deliberately named sector-neutrally |

**Open architecture questions Gate I must answer:**

1. **Is DB 16 Destination Profile universal, or travel-family?** If a non-travel sector cannot fill it, it is a family-level object and the interface has a conditional slot — which is a real architectural finding, not a failure.
2. **Is DB 15 Market Routes universal?** The *concept* (a directed origin→destination market pair with its own clock) plausibly generalizes to expansion markets. The *fields* (`Air Connectivity`, `Visa Friction`, `Booking Lead Time`) do not. Either they become plugin-declared extensions, or DB 15 is also travel-family.
3. **Does any sector need a store the core does not have?** If yes, that is a Tier-1 architecture change requiring owner ratification and an `AEIT_06` entry — **never** a plugin edit.

---

## 5. Candidate Sector #002

Not chosen. Data-derived from `Sector Priority Score` when the owner activates it:

- **B2B SaaS** (88, P1) — the strongest generalization test: trigger-led, no seasonality, no geography-as-demand, buyer = CRO/founder. **If the engine works here, DB 15/16 universality is settled.**
- **Professional Services → Legal & Accounting** (76, P1) — tax-season-led, buyer = Managing Partner. Tests whether "seasonality" generalizes beyond travel.

Choosing the *most different* sector for #002 is deliberate. Choosing another travel-adjacent sector would prove nothing.

---

## 6. Failure conditions

- A gate's exit evidence does not exist → **do not promote.** State the missing evidence.
- Gate F returns identical calendar shapes across validation places → **stop.** The destination/property-type layers are not doing work.
- A sector appears to need a new store → **ESCALATE.** Architecture change, not a plugin edit.
- A slot is filled with a plausible value that has no source → **constitutional breach.** Empty is a valid state; guessed is not.

## 7. Cross-references

[`SECTOR_OS_ARCHITECTURE.md`](SECTOR_OS_ARCHITECTURE.md) (the interface + engine) · [`SECTOR_ACTIVATION_CONTRACT.md`](SECTOR_ACTIVATION_CONTRACT.md) §6, §14, §16 · [`SECTOR_NOTION_SCHEMA.md`](SECTOR_NOTION_SCHEMA.md) DB 1 (Lifecycle State) · [`sector_plugins/hospitality/HOSPITALITY_PLUGIN.md`](sector_plugins/hospitality/HOSPITALITY_PLUGIN.md) (the worked reference).

## 8. Changelog

- **v0.1 (2026-08-20, Gate 1 — DECIDE):** Created as a **skeleton**. Establishes the one rule (extract the pattern, do not replicate the sector), the no-third-loop constraint, the nine activation gates mapped to the existing 11-state Lifecycle machine, and a **provisional** universal/plugin/configurable classification of all 14 slots — with three open architecture questions (is DB 16 universal or travel-family; is DB 15 universal; does any sector need a new store) that only Gate I can answer. Names B2B SaaS as the strongest candidate for Sector #002 precisely because it is the most different. **Completion is deferred to Gate 9 by design.** — Claude Code (Opus 5)
