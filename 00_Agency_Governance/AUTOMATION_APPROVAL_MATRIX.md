# Automation Approval Matrix

**Status:** v0.1-draft — governance framework; no real automations exist yet to apply it to.
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §11 (closes "Required Agency-Wide Closure Systems" item 7). Expands the risk-class table in `AGENCY_OPERATING_CONSTITUTION.md` §5 into a trigger-by-trigger format for actual automations once they're built.

---

## How to use this

When any department builds a real automation (a Triggers/Automation Hooks entry in a `{DEPT}_OS.md` §12 graduates from placeholder to live), add a row here before turning it on. No automation goes live without a row in this matrix and, for Risk Class 3+, explicit human sign-off per the Constitution.

## Matrix

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

These are template rows illustrating the pattern, not live automations — every row should be deleted and replaced with a real entry once the corresponding automation is actually built, not left as a placeholder claiming something exists that doesn't.

## Adding a New Automation

1. Identify which department's Triggers/Automation Hooks section it belongs to.
2. Classify its risk per `AGENCY_OPERATING_CONSTITUTION.md` §5.
3. Define rollback and fallback before activation, not after the first failure.
4. Add a row here.
5. If Risk Class 3+, get the required human sign-off (per Constitution §5) before activation, and log the approval in the department's Decision Log.
6. Reference this row's trigger name in the department's own `{DEPT}_OS.md` §12 entry rather than duplicating the detail there.

## Changelog

- 2026-06-30 — Initial automation approval matrix structure created as part of governance-closure pass, with illustrative template rows across all 4 risk classes. No real automations exist yet. — Claude Code (Sonnet 4.6)
