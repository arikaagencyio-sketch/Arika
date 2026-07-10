# Automation Approval Matrix

**Status:** v0.3 — one real automation, live. All other rows below remain illustrative templates.
**Last updated:** 2026-07-04

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 7). Expands the risk-class table in `AGENCY_OPERATING_CONSTITUTION.md` §5 into a trigger-by-trigger format for actual automations once they're built.

---

## How to use this

When any department builds a real automation (a Triggers/Automation Hooks entry in a `{DEPT}_OS.md` §12 graduates from placeholder to live), add a row here before turning it on. No automation goes live without a row in this matrix and, for Risk Class 3+, explicit human sign-off per the Constitution.

## Matrix

**Real row (specified and made live 2026-07-04):**

| Trigger | Action | Risk Class (Constitution §5) | Rollback | Fallback | Log destination | Human gate |
|---|---|---|---|---|---|---|
| Notion content-brief "Publishing Status" reaches the literal value **"Ready for Design"** | Cloud routine drafts a 7-field storyboard + a planning-only Production Engine recommendation, posts both as a Notion comment for owner review | 2 | Disable the routine (`RemoteTrigger` update, `enabled: false`) | Manual invocation of the same agent chain, as documented in `19_Design/DESIGN_OS.md` §4 | `16_Automation/AUTOMATION_OS.md` §8 Decision Log | **Human review required before any OpenArt/Claude Design credit-spending step** — enforced at the infrastructure level, not just by instruction: the routine's cloud session has no OpenArt/Canva MCP connector attached at all, so it is technically incapable of spending credits, not merely instructed not to. It can only draft a storyboard + tool-choice recommendation and leave it for a human to act on. |

**Live as of 2026-07-04** — routine ID `trig_01WyyrXEkFZck1D49tm6BfKv`, hourly cron (`7 * * * *`), repo `https://github.com/arikaagencyio-sketch/Arika`, Notion connector attached (connector_uuid `f957ca4d-bcce-43a2-9f31-9b6954efeee1`), first scheduled run `2026-07-04T14:07:00Z`. Both prior build blockers (`OWNER_INPUT_NEEDED.md` items 54-55) resolved same day. See `16_Automation/AUTOMATION_OS.md` §12.

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
