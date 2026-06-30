# Agency Operating Constitution

**Status:** v0.1-draft — process/structure sections are load-bearing now; mission/objective content is placeholder pending owner input.
**Owner:** *(unassigned — placeholder)*
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md) §3. This is the full version; that file carries only a compressed summary.

---

## 1. Purpose of This Document

This constitution governs how the agency operates as a system — who decides what, what risk classes require human sign-off, how the constitution itself changes, and what every department and agent (human or AI) is bound by regardless of which department they sit in. It does not replace department-level Standards & SOPs (those live in each `{DEPT}_OS.md` §10); it sets the rules those SOPs must operate within.

## 2. Mission & Objectives

*(Placeholder — pending owner input.)* A real mission statement, annual objectives, and quarterly goals belong here once defined by the agency owner. Until then, the only binding mission-level statement is the working description already used in `GLOBAL_OS.md` §1: operate as an AI-native agency that runs its own departments and client engagements through documented, repeatable, auditable systems rather than ad hoc effort.

**Do not backfill this section with invented numbers, targets, or dates.** Leave it placeholder until real objectives are supplied.

## 3. Non-Negotiables

These apply across every department, regardless of what any department-local Standards & SOPs document says:

1. **No silent invention.** When source material or real data is missing, say so. Never fabricate agency-specific facts: client names, numbers, pricing, contract terms, legal claims, or performance results.
2. **Department ownership is local; the constitution is supreme.** A department's `{DEPT}_OS.md` is authoritative for its own domain, but cannot override a rule set here.
3. **Structure before content.** Registries may exist as empty/placeholder structure without being treated as failures — but they may not be filled with guessed values to look complete.
4. **Every significant decision is logged**, not just stated in conversation (see §6 — Decision Rights, and each department's Decision Log).
5. **Human sign-off is required** for anything in Risk Class 3 or above (§5), with no exceptions carved out by convenience or urgency.

## 4. Decision Rights

| Decision type | Who decides | Escalation path |
|---|---|---|
| Department-local operational decisions (workflow tweaks, content drafts, internal tooling choices within an approved budget/tool list) | Department owner *(once assigned)* | None required — log in department Decision Log |
| Cross-department workflow changes (anything touching the handoff points in `GLOBAL_OS.md` §5) | Department owners of both sides, jointly | Agency owner if they disagree |
| New department creation, department merge/split, or structural changes to this repo's top-level layout | Agency owner | — |
| Anything in Risk Class 3+ (§5) | Agency owner (human) | — |
| Amendments to this constitution | Agency owner | — |

This table is intentionally light on named individuals because none are assigned yet (see `GLOBAL_OS.md` §4, Department Index — all owners are placeholders). Update the "Who decides" column with real names as soon as ownership is assigned; until then, default every decision above "department-local operational" to the agency owner.

## 5. Risk Classes

Every action — whether taken by a human, an AI agent, or an automation — falls into one of these classes. Higher classes require more sign-off, regardless of which department or tool is taking the action.

| Class | Description | Examples | Approval required |
|---|---|---|---|
| **0 — Informational** | Read-only, no state change | Reading files, generating a draft for internal review, research | None |
| **1 — Reversible internal** | Changes internal-only state, easily undone | Editing a department OS file, updating an internal doc, organizing files | None, but log in Decision Log if non-trivial |
| **2 — Reversible external-facing** | Visible outside the agency but correctable without lasting harm | Draft social posts before publishing, internal-only client communications drafts | Department owner review |
| **3 — Hard to reverse or client/money-facing** | Touches real client commitments, money movement, or public claims | Sending a client-facing email, creating an invoice, publishing content externally, signing off on a deliverable | **Human sign-off required**, logged in the relevant department's Decision Log |
| **4 — Legal, contractual, or irreversible** | Contracts, money transfers above a threshold, anything legally binding, deleting client data, public legal/financial claims | Signing a contract, wiring funds, making compliance representations | **Human sign-off required from agency owner specifically**, not just a department owner |

This table is the seed of the agency-wide automation approval matrix (`GLOBAL_OS.md` §11, item 7) — see `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` for the expanded trigger-by-trigger version.

## 6. Amendment Process

1. Propose a change as an edit to this file with a clear rationale.
2. Log the proposed change in the Changelog (§8) with status "proposed."
3. Agency owner approves or rejects.
4. On approval, update status to "adopted" in the Changelog and bump the document version if the change is structural (decision rights, risk classes) rather than just clarifying wording.

No department, agent, or automation may bypass this process to self-amend the constitution, even temporarily.

## 7. Cross-References

- Compressed summary: `GLOBAL_OS.md` §3
- Cross-department RACI: `00_Agency_Governance/AGENCY_RACI.md`
- Automation approval matrix (expanded): `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md`
- Agency-wide KPI dictionary: `00_Agency_Governance/AGENCY_KPI_DICTIONARY.md`
- CRM schema: `00_Agency_Governance/CRM_SCHEMA.md`
- Department-local standards: each `{DEPT}_OS.md` §10
- Consolidated list of every gap that needs a real fact from the agency owner (not more reading/writing): `00_Agency_Governance/OWNER_INPUT_NEEDED.md`

## 8. Changelog

- **2026-06-30 — v0.1-draft adopted** — Initial constitution written as part of the governance-closure pass: non-negotiables, decision rights framework, 5-tier risk classification, and amendment process established. Mission/objectives left as placeholder pending agency owner input. — Claude Code (Sonnet 4.6)
