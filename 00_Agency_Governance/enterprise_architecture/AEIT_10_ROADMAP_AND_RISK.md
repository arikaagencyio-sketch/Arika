# AEIT_10 — Prioritized Roadmap & Enterprise Risk Register (Blueprint)

**Version:** v0.1
**Last updated:** 2026-07-22
**Owner:** Mary Thuo (Agency Governance, 00)
**Consumes:** all of AEIT_01–09. **Sequences:** reconciliation enactment (AEIT_05), gap remediation
(AEIT_04), and the missing-piece builds (AEIT_06–09).
**Status:** Roadmap + risk register. Nothing here is executed in Phase Zero.

> The governing principle is **reality-gating**: a solo, pre-revenue, not-yet-incorporated business
> whose automation has never run does not build a collection platform first. Each phase unlocks only
> when its gate is met. This is what stops the architecture from outrunning the business again.

---

## 1. The reality gates (ordered)

| Gate | Condition | Blocks |
|---|---|---|
| **G0 — Coherence** | Ratified R1–R5 enacted; dead systems cleaned | any new build on a contradictory base |
| **G1 — Legal existence** | Entity incorporated; counsel engaged (`LEGAL_OS.md` §8) | client-facing offers, DPA, AI-Enablement Class-3 gate |
| **G2 — Activation** | `ANTHROPIC_API_KEY` set; runtime boots persistently | every `prompt` agent, all collection |
| **G3 — Proven schedule** | One unattended scheduled job lands end-to-end (`AEIT_04 §C5`) | trusting any cron cadence |
| **G4 — Governance coverage** | Approval-Matrix row per armed automation (`AEIT_04 §C2`) | firing automations safely |
| **G5 — First source** | ≥1 Source registered + verified (`AEIT_08`) | IntOS collection |

---

## 2. Phased roadmap

### Phase 0 — Coherence & cleanup *(gate: none — do now; spec→apply)*
Enact the ratified reconciliation and clear dead weight. **Small, safe, owner-approved edits:**
- Apply **R1**: amend `CRM_SCHEMA.md:23` — `ICP_fit_score` "set by Sector (01), consumed by Sales (05)".
- Apply **R2–R4**: glossary into `AEIT_06`; rename Sector priority bands to P1–P4
  (`SECTOR_OS.md:68,89`); qualify "pipeline" usages opportunistically.
- Apply **R5**: delete the empty ClickUp "Sales CRM" template `901511301824`; keep names separated.
- **Hygiene:** mark phantom `_memory/runtime.jsonl` claims "planned, not written" (`AEIT_04 §C4`);
  archive/rewrite the 2 dead Python scripts (`AEIT_04 §C6`); reconcile the cron count to one verified
  number (`AEIT_04 §C1`).

### Phase A — Activation & governance *(gate: G2, G3, G4)*
- Set `ANTHROPIC_API_KEY`; boot `arika-runtime` persistently.
- Write one Approval-Matrix row per armed automation **before** enabling schedules.
- Prove `automation-reliability-monitor`'s daily cron survives one unattended cycle.
- **Compliance (needs G1):** add Zoho to the DPA sub-processor register; resolve Zoho Books plan;
  register a calendar/transcription tool before the advisory offer sells (`AEIT_04 §D1–D2`).

### Phase B — IntOS minimal slice *(gate: G2–G5)*
- Build the smallest loop end-to-end: **Sector → Company/ICP Knowledge Objects → verified →
  distributed to Sales** (`AEIT_07 §6`). One source, one entity, full SM4 lifecycle once.
- Reuse `bois` for storage/RAG; `arika-runtime` for scheduling; `techstack-cost-guardian` for runway.

### Phase C — IntOS scale-out *(gate: Phase B proven)*
- Populate the Source Registry (`AEIT_08`) beyond the seed; build the **Verification layer**
  (validation, entity resolution, confidence/trust scoring) — the missing capability.
- Decide the knowledge-graph substrate (ClickUp relations vs `bois` vs graph DB) — a Tech Stack call.

### Phase D — Distribution & unified memory *(gate: Phase C)*
- Roll out `AEIT_09` handoff contracts pair-by-pair as pairs go live.
- Implement the unified memory protocol (`AEIT_07 §3.5`); agent memory becomes an IntOS consumer.

### Phase E — Learning, optimization & platform formalization *(gate: revenue + real content)*
- Turn on the Learning loop (trust recalibration, KPI feedback).
- **Now — and only now — formalize the four platforms** (EGOS/OrchOS/RevOS/IntOS) and the 15-chapter
  EDS (deferred in `AEIT_00 §6`). Trigger met: legal existence + proven automation + real content.

---

## 3. Four-platform target framing (describe, don't rename yet)

```
                 ┌───────────────── EGOS (Governance) ─────────────────┐
                 │  Constitution · RACI · Approval Matrix · risk class  │  ← 00_Agency_Governance (exists)
                 └──────────────────────────────────────────────────────┘
   RevOS (Revenue)          IntOS (Intelligence)          OrchOS (Orchestration)
   Sales/Offer/Finance      AEIT_06–09 (to build)         arika-runtime (exists)
   (distributed, exists)    the one genuinely-new platform (executes all)
```

**Do not rebrand or re-fold** the existing Governance folder or `arika-runtime` into new "platform"
files now — that is churn without value (`AEIT_01 §3`). The four-platform model is the *target map*;
formalization is a Phase E deliverable, triggered, not immediate.

---

## 4. Enterprise Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| RK-1 | Activation without governance → automations fire uncontrolled | Med (one command away) | High | G4 hard gate before G2/G3; Approval-Matrix rows first | Governance/Automation |
| RK-2 | Architecture keeps outrunning reality (more structure, no runs) | High (the documented pattern) | High | Reality gates §1; Architecture Review Checklist; label structure-vs-real honestly | Governance |
| RK-3 | Legal non-existence blocks revenue + exposes IP | High (currently true) | High | G1: incorporation + counsel (in motion, `LEGAL_OS.md` §8) | Legal |
| RK-4 | Silent automation death recurs (cf. 11-day outage) | Med | Med | `automation-reliability-monitor` proven on G3; last-verified discipline | Automation |
| RK-5 | Single-vendor concentration (Zoho load-bearing, off DPA register, trial expired) | Med | Med | Phase A compliance; fallback sources in `AEIT_08` | Tech Stack/Legal |
| RK-6 | Cost/runway exhaustion (Design ~2 images left; API metering) | Med | Med | `techstack-cost-guardian`; runway-in-units reporting | Tech Stack |
| RK-7 | IntOS over-build (collectors before proven loop) | Med | Med | Minimal-slice-first (Phase B); ~70% reuse mandate (`AEIT_07 §4`) | Governance |
| RK-8 | Reconciliation not enacted → contradictions persist into IntOS | Low (ratified) | Med | Phase 0 enactment tracked; `AEIT_05` audit trail | Governance |

---

## 5. What "done" looks like for Phase Zero
Phase Zero is complete when: the 11 AEIT artifacts exist and are internally consistent; R1–R5 are
ratified (✅); the roadmap is reality-gated; and every `GLOBAL_OS.md` §11 Open gap is either
addressed by an AEIT artifact or explicitly deferred with a trigger. **Implementation (Phase 0
enactment onward) is a separate, post-approval activity** — the Implementation Protocol, deferred
per the Owner's right-sized scope.

## 6. Decision Log
- **2026-07-22 — Roadmap + risk register set.** Six reality gates defined; six phases sequenced
  behind them; four-platform formalization + EDS deferred to Phase E (triggered); 8-risk register
  compiled. — Claude Code (Opus 4.8)

## 7. Changelog
- **v0.1 (2026-07-22):** Created. — Claude Code (Opus 4.8)
