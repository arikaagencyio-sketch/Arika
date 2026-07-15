# Automation Approval Matrix

**Status:** v0.4 — one real automation, **restored 2026-07-15 after an 11-day undetected outage**. All other rows below remain illustrative templates.
**Last updated:** 2026-07-15

> **🔴 This document asserted an automation was live while it was dead, for 11 days.** The row below said *"made live 2026-07-04"* — true for 3 hours and 41 minutes. See `16_Automation/AUTOMATION_OS.md` §9 for the incident.
>
> **Two rules added as a result:**
> 1. **A row carries a `Last verified` date, not just an activation date.** "We turned it on" and "it is on" are different claims. Only the second one matters, and only the recent one is credible.
> 2. **A row must answer "how will anyone know this stopped?"** The columns below require rollback and fallback before activation — both existed here and both worked. **The gap was never rollback; it was detection.** `automation-reliability-monitor` (16) is now that control.

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 7). Expands the risk-class table in `AGENCY_OPERATING_CONSTITUTION.md` §5 into a trigger-by-trigger format for actual automations once they're built.

---

## How to use this

When any department builds a real automation (a Triggers/Automation Hooks entry in a `{DEPT}_OS.md` §12 graduates from placeholder to live), add a row here before turning it on. No automation goes live without a row in this matrix and, for Risk Class 3+, explicit human sign-off per the Constitution.

## Matrix

**Real row (specified and made live 2026-07-04):**

| Trigger | Action | Risk Class (Constitution §5) | Rollback | Fallback | Log destination | Human gate |
|---|---|---|---|---|---|---|
| Notion content-brief "Publishing Status" reaches the literal value **"Ready for Design"** | Cloud routine drafts a 7-field storyboard + a planning-only Production Engine recommendation, posts both as a Notion comment for owner review | 2 | Disable the routine (`RemoteTrigger` update, `enabled: false`) | Manual invocation of the same agent chain, as documented in `19_Design/DESIGN_OS.md` §4 | `16_Automation/AUTOMATION_OS.md` §8 Decision Log | **Human review required before any OpenArt/Claude Design credit-spending step** — enforced at the infrastructure level, not just by instruction: the routine's cloud session has no OpenArt/Canva MCP connector attached at all, so it is technically incapable of spending credits, not merely instructed not to. It can only draft a storyboard + tool-choice recommendation and leave it for a human to act on. |

**Activated 2026-07-04 · Died 2026-07-04T17:07Z · Restored 2026-07-15 · Last verified 2026-07-15T09:36:46Z (forced run).** Routine ID `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron (`7 * * * *`), repo `https://github.com/arikaagencyio-sketch/Arika`, Notion connector attached (connector_uuid `f957ca4d-bcce-43a2-9f31-9b6954efeee1`).

**Outage history (do not delete — this row's credibility depends on it):** fired once at `2026-07-04T14:07:35Z`, auto-disabled at `17:07:19Z` with `ended_reason: auto_disabled_repo_access`, and sat dead **11 days** with `next_run_at` frozen in the past while this matrix and 4 OS files asserted it was live. Restored by pushing the repo (origin was 5 days stale) and re-enabling; a forced run succeeded without re-tripping the disable. **The hourly cadence is not yet proven post-restoration** — one forced run is not a restored cron. Full incident: `16_Automation/AUTOMATION_OS.md` §9.

**Detection control (added 2026-07-15):** `automation-reliability-monitor` (16) — daily, checks `enabled` / `ended_reason` / `last_fired_at` vs. cron across the estate. It did not exist during the outage, which is why the outage lasted 11 days. **Caveat:** it is itself a runtime cron trigger, so it only runs if the runtime is booted — see the standing gap below.

---

### 🔴 Standing gap: 21 runtime cron triggers, 1 matrix row

`arika-runtime` declares **21 `schedule` triggers**. This matrix has **one** real row — the one above.

**Not a live breach only because the runtime is not running.** It is a local Node process with no `ANTHROPIC_API_KEY` and no daemon; its cron triggers are **declared, not scheduled**. One `npx tsx src/index.ts` with a key turns 21 undocumented automations on at once — no rows, no rollback, no fallback, in direct violation of this document's own rule.

**Rows are deliberately not written yet.** Whether this is 21 rows or one covering row (shared rollback: disable the scheduler; shared fallback: `arika run <name>` manually) is an **owner decision**, and writing 21 rows for agents that have never run once would document an intention as a fact — the exact error that made the row above unreliable.

**Until then:** `automation-approval-gate` (16) returns `blocked` on any request to run the runtime as a persistent service. **Manual `arika run` is fine and needs no row** — a human invoking an advisory agent is not an automation.

**Template rows below** (illustrative, not live automations — none of these have been built yet either):

| Trigger | Action | Risk Class (Constitution §5) | Rollback | Fallback | Log destination | Human gate |
|---|---|---|---|---|---|---|
| *(template row)* New lead captured | Auto-tag source + add to CRM | 1 | Delete/edit tag | Manual tagging | Department Decision Log | None |
| *(template row)* Lead reaches qualification threshold | Auto-route to Sales queue | 1 | Re-route manually | Manual triage | Sales (05) Decision Log | None |
| *(template row)* Outbound message sequence to a lead | Send automated email/message | 2 | Pause sequence | Manual send | Department Decision Log | Department owner reviews sequence templates before activation, not per-send |
| *(template row)* Deal marked closed-won | Auto-generate client record + notify Client Success | 2 | Manual record correction | Manual handoff | Sales (05) + Client Success (07) Decision Logs | None |
| *(template row)* Invoice generation | Auto-create draft invoice from completed milestone | 3 | Void draft | Manual invoice creation | Finance (09) Decision Log | **Human sign-off before sending to client** |
| *(template row)* Client-facing communication (any) | Send email/message visible to client | 3 | N/A — already sent | Manual review before send | Relevant department Decision Log | **Human review before send**, unless pre-approved template explicitly exempted in writing |
| *(template row)* Contract generation/modification | Auto-draft contract terms | 4 | N/A — must not auto-send | Manual drafting | Legal (10) Decision Log | **Agency owner sign-off required**, no exceptions |
| *(template row)* Payment/fund movement | Initiate transfer | 4 | Reverse if possible, else manual correction | Manual transfer | Finance (09) Decision Log | **Agency owner sign-off required**, no exceptions |

The 8 rows immediately above (marked *template row*) illustrate the pattern only — not live automations — and should each be deleted and replaced with a real entry once the corresponding automation is actually built, not left as a placeholder claiming something exists that doesn't. The Creative Pipeline Automation row above them is real and live — update its Human gate/Risk Class in place if either changes, don't delete and re-add.

## Adding a New Automation

1. Identify which department's Triggers/Automation Hooks section it belongs to.
2. Classify its risk per `AGENCY_OPERATING_CONSTITUTION.md` §5.
3. Define rollback and fallback before activation, not after the first failure.
4. Add a row here.
5. If Risk Class 3+, get the required human sign-off (per Constitution §5) before activation, and log the approval in the department's Decision Log.
6. Reference this row's trigger name in the department's own `{DEPT}_OS.md` §12 entry rather than duplicating the detail there.

## Changelog

- 2026-07-04 — **Creative Pipeline Automation went live.** Both build blockers resolved same day (Notion cloud-routines connector confirmed already attached; "Publishing Status" given a real "Ready for Design" trigger value). Real routine created via `RemoteTrigger` (`trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron `7 * * * *`, Notion connector only — deliberately no OpenArt/Canva connector attached, making the credit-spend gate infrastructural rather than instruction-only). Closes `OWNER_INPUT_NEEDED.md` items 54-55 and `GO_LIVE_CHECKLIST.md` Phase 9 items 41-43. — Claude Code (Sonnet 5)
- 2026-07-04 — **First real (non-template) row added**: Creative Pipeline Automation for Design (19) — a Notion-status-triggered cloud routine invoking Design's real agent chain, Risk Class 2, with a human gate before any credit-spending step (stricter than the class requires, given OpenArt's scarce Free-plan credit pool). Specified in full but not yet live — 2 real prerequisites tracked as `OWNER_INPUT_NEEDED.md` items 54-55. Full detail: `16_Automation/AUTOMATION_OS.md` §3, §4, §9, §12. — Claude Code (Sonnet 5)
- 2026-06-30 — Initial automation approval matrix structure created as part of governance-closure pass, with illustrative template rows across all 4 risk classes. No real automations exist yet. — Claude Code (Sonnet 4.6)
