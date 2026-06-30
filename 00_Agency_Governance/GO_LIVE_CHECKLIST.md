# Go-Live Checklist

**Status:** Active — created 2026-06-30 in response to the owner's two real platform decisions (Zoho CRM/Zoho Books, Claude as the agency-standard LLM) and the question "what's next for this workspace to be live and start operating."
**Last updated:** 2026-06-30

> Referenced from [`GLOBAL_OS.md`](../GLOBAL_OS.md). This file is the action sequence for turning the now-closed governance/decision layer (`OWNER_INPUT_NEEDED.md`, `OWNER_DECISION_WORKSHEET.md` — both at 0 open [DECISION] items as of this entry) into a running operation. Unlike those two files, this one tracks **build/setup work**, not open decisions — every row below is either an owner action (account creation, credentials, sign-off) or a build task this session can do once approved. Mark items done in place; don't delete rows, same convention as the other governance trackers.

---

## Why this exists now

As of 2026-06-30, every cross-department decision blocking governance is resolved — `OWNER_INPUT_NEEDED.md` has 0 open [DECISION] items, only 4 [WAITING ON DATA] items that close on their own once the agency operates (items 8, 9, 13, 20). The repo's bottleneck has shifted from "what should we decide" to "what's documented but not yet real." This checklist is that punch list.

---

## Phase 1 — Core platform setup (blocks everything downstream)

| # | Item | Type | Status | Notes |
|---|---|---|---|---|
| 1 | Create the real Zoho CRM account/org | **Owner action** | Not started | Needs Zoho org login, billing, and the domain the agency operates under |
| 2 | Create the real Zoho Books account, linked to the same Zoho org as #1 | **Owner action** | Not started | Confirm Zoho Books is available in the agency's billing region (Kenya + global clients, see `03_Marketing/MARKETING_OS.md` §14) |
| 3 | Build out Zoho CRM's object/field model to match `CRM_SCHEMA.md` | Buildable (with Zoho admin access) | Not started | Lead, Opportunity, Client, Engagement/Project, Partner objects — see `00_Agency_Governance/CRM_SCHEMA.md` §"Core Objects" for the exact field list per object |
| 4 | Configure native Zoho CRM ↔ Zoho Books sync | Buildable (with Zoho admin access) | Not started | This is the entire reason Zoho Books was chosen over a third-party accounting tool — confirm the Opportunity-closed-won → Invoice handoff (`CRM_SCHEMA.md` "Handoff Points") actually fires through native sync before relying on it |
| 5 | Get a Zoho CRM + Zoho Books API key/OAuth app for programmatic access | **Owner action** | Not started | Needed before `finos-plugin`'s `integrations/index.ts` connector (item 9 below) can be built — that's currently a confirmed stub with zero real connectors |
| 6 | Get an Anthropic API key for the agency (billing account) | **Owner action** | Not started | Needed before any of the LLM-wiring items below can run against a real model instead of being spec-only |

## Phase 2 — Wire Claude into the two code-backed agent layers

Both `09_Finance/finos-plugin/` and `12_Branding/bois/` are real, working codebases with zero LLM SDK dependency today (confirmed by direct code inspection — see each department's §5/§13). This is genuine build work, not a config flag.

| # | Item | Type | Status | Notes |
|---|---|---|---|---|
| 7 | Add the Anthropic SDK to `finos-plugin/package.json` and implement the actual model call for the 7-agent roster | Buildable | Not started | Specs already exist at `finos-plugin/docs/agent-prompts.md`, mirrored in `src/ai-agents/index.ts`'s `financialAgentSpecs` — the prompts are real, only the execution call is missing |
| 8 | Add Claude wiring to `bois/` for the 20-agent roster | Buildable | Not started | `bois/agents/AGENT_SYSTEM.md` + `core/orchestration/registry.py`'s `agent_prompt()` already generate the prompt string per agent — needs the actual API call added where the prompt is currently just returned |
| 9 | Build the real Zoho Books connector in `finos-plugin/src/integrations/` | Buildable (needs API key, item 5) | Not started | Closes the one confirmed-stub module in Finance's capability registry (`FINANCE_OS.md` §3) |
| 10 | Decide and document per-agent `humanApprovalRequiredFor` behavior once agents are live | **Owner decision, when reached** | Not started | The escalation lists already exist in spec (`finos-plugin/docs/agent-prompts.md`) — confirm they still hold once agents can actually act, not just recommend |
| 11 | Add real rows to `AUTOMATION_APPROVAL_MATRIX.md` for any agent action that crosses Risk Class 2+ (per `AGENCY_OPERATING_CONSTITUTION.md` §5) | Buildable, needs owner sign-off for Class 3+ | Not started | No automation goes live without a row here first — this is a hard repo rule, not a suggestion |

## Phase 3 — Operational launch (uses the now-real platforms)

| # | Item | Type | Status | Notes |
|---|---|---|---|---|
| 12 | Run the first real Lead → Opportunity → Client through Zoho CRM | **Owner action** (real selling) | Not started | This is what actually starts closing items 8/9/13/20 in `OWNER_INPUT_NEEDED.md` — they resolve themselves through real operating history, not more documentation |
| 13 | Issue the first real invoice through Zoho Books | **Owner action** | Not started | First real test of the CRM↔Books handoff built in Phase 1 |
| 14 | Confirm LinkedIn/Instagram launch date for Content (04) | **Owner decision** | Not started — currently "not launched yet, no date set" (`04_Content/CONTENT_OS.md` §7, tracker item 18 resolved as "no date yet") | Content pillars and the LinkedIn DRAGON post series are already built (`CONTENT_OS.md` §10) — this is a timing decision, not a content gap |
| 15 | Fill in the empty per-function RACI rows now that the owner (Mary Thuo, sole owner) is confirmed | Buildable | Not started | Every department's §11 RACI table is still a placeholder row despite owner/ownership being resolved (tracker items 2, 3) — quick mechanical fill-in once you confirm you want it done agency-wide in one pass |

## Phase 4 — Structural gaps still open per `GLOBAL_OS.md` §11

These predate today's decisions and aren't blocking Phase 1-3, but are worth sequencing once the core platform is live:

| # | Item | Type | Status |
|---|---|---|---|
| 16 | Dashboard spine (`GLOBAL_OS.md` §11 item 9) | Buildable, needs design input | Not started — no work done yet |
| 17 | Formal handoff packet spec per department pair (`CRM_SCHEMA.md` "Handoff Points" is the seed) | Buildable | Partially open — seed exists, full spec doesn't |
| 18 | Agency Global Source Registry (`GLOBAL_OS.md` §11 item 1) | Buildable | Not started |
| 19 | Unified memory protocol doc (`GLOBAL_OS.md` §11 item 8) | Buildable | Partially open — Decision Log/Changelog pattern exists per department, no unified spec |

---

## How to use this

- Phase 1 and 2 are the actual blockers for "live." Everything in Phase 3 depends on Phase 1 being real (you can't run a real deal through a CRM that doesn't exist yet).
- Items marked **Owner action** need credentials, billing, or a real-world decision only the owner can make — flag these back to the owner rather than attempting to fabricate them.
- Items marked **Buildable** can be done in a Claude Code session once the prerequisite owner action (API keys, account creation) is in place — say which item to start and it can be built directly into the relevant codebase (`finos-plugin/`, `bois/`) or governance file.
- Update each row's Status column in place as work completes, and log the real outcome in the relevant department's own Decision Log/Changelog (per `GLOBAL_OS.md` §10's rule) — don't let this file become the only record.

## Changelog

- 2026-06-30 — Created in response to the owner's two real decisions (Zoho CRM + Zoho Books replacing HubSpot/no-platform; Claude as the agency-standard LLM replacing "spec/routing-only"). Sequenced into 4 phases: core platform setup, Claude wiring into Finance/Branding's code-backed agent layers, operational launch, and pre-existing structural gaps from `GLOBAL_OS.md` §11. — Claude Code (Sonnet 4.6)
