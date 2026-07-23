# AEIT_07 — Intelligence Operating System (IntOS) Blueprint

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Fills:** the genuinely-absent platform (`AEIT_01 §3`); `REGISTRY_TAXONOMY_REFERENCE.md` future-state
registries **Intelligence / Learning / Feedback**; `GLOBAL_OS.md` §11 item 8 (unified memory protocol).
**Depends on:** `AEIT_06` (canonical model = write target), `AEIT_05` SM4 (Knowledge lifecycle),
`AEIT_08` (source registry), `arika-runtime` (execution substrate).
**Status:** Blueprint — design only. **IntOS is NOT activated in Phase Zero.** Activation is gated
in `AEIT_10` behind the API key, a proven scheduled runtime, and governance rows.

> IntOS is the platform that turns the agency from **produce-strong / validate-weak**
> (`AEIT_03 §2`) into a system that knows what it knows, how sure it is, and when to refresh it.
> It is the one of the four foundational platforms that does not yet exist — EGOS (Governance),
> OrchOS (`arika-runtime`), and RevOS (distributed) already do.

---

## 1. Position in the enterprise

```
        SOURCES ──▶ IntOS ──▶ CANONICAL MODEL / KNOWLEDGE GRAPH ──▶ DEPARTMENTS ──▶ EXECUTION
        (AEIT_08)  (this)        (AEIT_06)                         (via AEIT_09)   (arika-runtime)
                     ▲                                                                    │
                     └──────────────────── LEARNING / FEEDBACK ◀─────────────────────────┘
```

- **Reads from:** the Source Registry (`AEIT_08`) and existing intelligence producers, chiefly
  Sector (01) and Branding's `bois` RAG.
- **Writes to:** the canonical entity model + knowledge graph (`AEIT_06`) — one object model, not
  per-department stores.
- **Distributes via:** the interface-contract standard (`AEIT_09`) to every department.
- **Executes through:** `arika-runtime` (OrchOS) — IntOS defines *what* intelligence work runs;
  the runtime is *how* it runs.

---

## 2. The IntOS pipeline (maps to SM4 Knowledge lifecycle)

Each stage corresponds to a Knowledge-Object state (`AEIT_05` SM4) and to one of the user's eight
engineering phases:

| # | IntOS layer | Knowledge state | Engineering phase | What it does |
|---|---|---|---|---|
| 1 | **Information** | (schema) | Ph.1 Information Eng | Canonical entities/fields to populate (`AEIT_06`) |
| 2 | **Knowledge** | (schema) | Ph.2 Knowledge Eng | Ontology + graph edges (`AEIT_06 §4`) |
| 3 | **Source** | Observed | Ph.3 Source Eng | Registry of every source + trust (`AEIT_08`) |
| 4 | **Collection** | Collected | Ph.4 Collection Eng | Connectors, pipelines, queues, scheduling, rate-limit, retries |
| 5 | **Verification** | Validated → Verified → Normalized | Ph.5 Verification Eng | Validation, dedup, entity resolution, confidence + trust scoring |
| 6 | **Enrichment** | Enriched → Trusted | — | Cross-source corroboration → promote to Trusted |
| 7 | **Distribution** | Distributed → Consumed | Ph.6 Distribution Eng | Department views, agent memory, workflow feeds (`AEIT_09`) |
| 8 | **Execution** | (acts) | Ph.7 Execution Eng | Triggers/actions/skills via `arika-runtime` under the Approval Matrix |
| 9 | **Learning** | Learned → Archived | Ph.8 Learning Eng | Feedback, KPIs, confidence recalibration, optimization |

**Governance wraps all nine** (retention, versioning, deletion, observability) — inherited from
EGOS, not reinvented.

---

## 3. Component design

### 3.1 Collection layer
- **Connectors** defined per source in `AEIT_08` (API / registry / scrape / MCP / manual).
- **Scheduling/queue/retry** run on `arika-runtime`'s trigger system — *the same estate that is
  currently dormant*. IntOS collection therefore **cannot precede runtime activation** (`AEIT_10`).
- **Rate-limit + cost** governed by Tech Stack's `techstack-cost-guardian` (already built) —
  intelligence collection must report runway in units, not credits.

### 3.2 Verification layer (the missing capability)
This is what closes the validate-weak gap. Every Knowledge Object gets:
- **Validation** — schema/format/plausibility checks.
- **Entity resolution** — collapse duplicates to one canonical node (`AEIT_06`).
- **Confidence score** — how certain is this claim? (source count, recency, agreement).
- **Trust score** — how much do we trust the *source* (from `AEIT_08` source trust)?
- Only cross-corroborated objects reach **Trusted**; nothing is distributed as fact from a single
  low-trust source.

### 3.3 Knowledge layer
- **Write target:** the canonical model + graph (`AEIT_06`).
- **Substrate options** (Tech Stack decision, `AEIT_10`): ClickUp relations for structured entities;
  Branding's `bois` vector store for semantic/RAG; a dedicated graph store only if scale demands it.
  **Reuse `bois` before building new** — it already implements RAG + vector memory + scoring.

### 3.4 Distribution layer
- Departments **subscribe** to entity/knowledge views through the `AEIT_09` contract standard.
- Agent memory (`_memory/runtime.jsonl`) becomes a *consumer* of IntOS, not an independent store —
  resolving the phantom-stream problem (`AEIT_04 §C4`).

### 3.5 Learning layer & the unified memory protocol *(closes GLOBAL_OS §11 item 8)*
- **One memory protocol** across the agency, replacing today's fragmented, mostly-fictional streams:
  | Memory type | Contents | Substrate |
  |---|---|---|
  | Historical | what was observed/collected | Knowledge graph, versioned |
  | Operational | what ran, when, outcome | `runtime.jsonl` (bois envelope, already used) |
  | Decision | choices + rationale | department §8 Decision Logs |
  | Execution | actions taken + results | Approval-Matrix-linked logs |
  | Learning | feedback → recalibration | IntOS Learning layer |
- **Feedback loop:** consumed knowledge that proves right/wrong recalibrates source trust and object
  confidence — the "last-verified, not activation-date" discipline (`TECHSTACK_OS.md:152`) made
  systemic.

---

## 4. How IntOS reuses what already exists (build-less wins)

| Need | Reuse (don't rebuild) |
|---|---|
| Execution/scheduling | `arika-runtime` triggers |
| Cost/runway guarding | `techstack-cost-guardian` |
| RAG / vector / scoring | `12_Branding/bois/` |
| First intelligence producer | Sector (01) agents (`sector-*`) |
| Governance / risk class | EGOS (`AUTOMATION_APPROVAL_MATRIX.md`, `governance.ts`) |
| Object model | `CRM_SCHEMA.md` + `AEIT_06` |
| Calendars for refresh | the 7 Cognitive Calendars + `AEIT_08` Intelligence Calendar |

IntOS is therefore **~70% integration of existing parts** + ~30% genuinely new (the Verification
layer and the unified memory protocol). That is the right ratio for a solo agency.

---

## 5. Activation gates (why IntOS is not built now)

IntOS **cannot** be stood up until — in order (`AEIT_10`):
1. `ANTHROPIC_API_KEY` is set (`AEIT_04 §C3`).
2. `arika-runtime` is proven to run **one** unattended scheduled job end-to-end (`AEIT_04 §C5`).
3. Approval-Matrix rows exist for every collection/execution automation (`AEIT_04 §C2`).
4. At least one real Source is registered and verified (`AEIT_08`).

Standing up collectors before these is exactly the "structure ahead of content / automation that
never runs" failure the audit found. IntOS is designed now, **built after activation**.

---

## 6. Minimal first slice (when unblocked)
The smallest useful IntOS: **Sector → Company/ICP knowledge objects → verified → distributed to
Sales**. One source, one entity type, the full lifecycle once. Prove the loop before scaling to the
source registry's full breadth.

## 7. Decision Log
- **2026-07-22 — IntOS blueprinted.** Nine-layer pipeline mapped to SM4 + the user's 8 engineering
  phases; ~70% reuse of `arika-runtime`/`bois`/Sector/EGOS; activation gated; minimal first slice
  defined (Sector→Sales). — Claude Code (Opus 4.8)

## 8. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
