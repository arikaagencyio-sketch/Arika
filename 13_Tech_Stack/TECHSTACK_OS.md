# Tech Stack — Department OS

**Department:** Tech Stack (13)
**Position in flow:** Horizontal support layer — provides tooling/infrastructure to all other departments; reports into Agency Governance (00).
**Mandate:** Own the canonical inventory of tools/software the agency actually uses (CRM, project management, hosting, email, AI platforms, APIs), plus integration and access records for them.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Tech Stack is a **newly created department** — confirmed as a real gap during workspace exploration. The repo contains two aspirational software builds (Finance's `finos-plugin/` and Branding's `bois/`) but no canonical list of what tools the agency actually runs on day-to-day.

## 2. Status

**Skeleton, with its first 3 real confirmed tools (2026-06-30).** No raw draft archive exists for this department specifically. Note: the two code scaffolds (`09_Finance/finos-plugin/`, `12_Branding/bois/`) are aspirational software the agency is building, not a record of tools it currently uses — do not conflate the two when this department's content gets built out. None of the 3 tools below are implemented yet — confirmed as the real platform decisions, not yet wired up. See `00_Agency_Governance/GO_LIVE_CHECKLIST.md` for the implementation sequence.

## 3. Capability Registry

| Capability | Description | Status |
|---|---|---|
| Zoho CRM | CRM platform — implements the Lead/Opportunity/Client/Partner pipeline defined in `00_Agency_Governance/CRM_SCHEMA.md` | **Confirmed real (2026-06-30)**, not yet implemented |
| Zoho Books | Accounting/invoicing platform for Finance (09); selected specifically to pair with Zoho CRM for native CRM↔Books sync | **Confirmed real (2026-06-30)**, not yet implemented — closes Finance's tracker item 25 integration gap |
| Claude (Anthropic API) | Agency-standard LLM backing AI agent execution — confirmed for Finance (09)'s 7-agent roster and Branding (12)'s 20-agent roster; the default choice once Sales (05)/Marketing (03)'s markdown-defined agent rosters get executable runtimes | **Confirmed real (2026-06-30)**, not yet wired — `finos-plugin` and `bois` both still have zero LLM SDK dependency as of this entry |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 5. Agent Roster

*(placeholder — none yet)*

## 6. Skill Library Index

*(placeholder — none yet)*

## 7. KPI Dictionary (department-local)

| Metric | Formula | Source | Owner | Cadence | Threshold |
|---|---|---|---|---|---|
| *(placeholder)* | | | | | |

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty; e.g. vendor lock-in, API deprecation risk, once real content exists)*

## 10. Standards & SOPs Index

*(placeholder — canonical tool inventory, access/credential management process, integration documentation)*

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder)* | | | | |

## 12. Triggers / Automation Hooks

*(placeholder — structure only)*

## 13. Existing OS Sub-Layer

None yet. (Note: `09_Finance/finos-plugin/` and `12_Branding/bois/` are department-specific aspirational software builds, not Tech Stack inventory — see those departments' own §13 sections.)

## 14. Raw Archive Pointer

None. This is a genuinely new department with no inherited backlog.

## 15. Changelog

- 2026-06-30 — Department created as part of v0.1 skeleton restructuring, addressing a confirmed gap. — Claude Code (Sonnet 4.6)
- 2026-06-30 — First 3 real tool decisions recorded: **Zoho CRM** (supersedes the earlier HubSpot selection, `CRM_SCHEMA.md`), **Zoho Books** (Finance's accounting platform, closes tracker item 25), and **Claude (Anthropic API)** as the agency-standard LLM for AI agent execution (Finance's 7 agents + Branding's 20 agents). All 3 are real decisions, none implemented yet — see `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 4.6)
