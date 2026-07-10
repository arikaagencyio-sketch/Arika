# Finance — Department OS

**Department:** Finance (09)
**Position in flow:** Receives billable events/delivery output from Operations (08); reports roll up to Agency Governance (00).
**Mandate:** Own accounting, cash flow, treasury, forecasting, and financial compliance for the agency.
**Owner:** Mary Thuo

> See [`GLOBAL_OS.md`](../GLOBAL_OS.md) for how this file fits into the whole system. Read that first if you haven't.

---

## 1. Identity

Finance accounts for and forecasts the agency's money — revenue, costs, margins, cash flow, treasury, tax compliance. Its `finos-plugin/docs/architecture.md` defines a 10-layer event-driven architecture: Data Ingestion → Event Bus → Core Ledger → Treasury/Allocation → Cashflow/Forecasting → Risk → AI Agent Layer → Governance/Compliance → Reporting/Dashboard → MCP/API Layer.

## 2. Status

**Content migration complete (2026-06-30) — correcting an earlier under-assessment.** This department's code scaffold (`finos-plugin/`) is meaningfully more real than originally characterized in this restructuring's skeleton pass: it is **not** "mostly stub files" — `core-ledger`, `cashflow-engine`, `risk-engine`, and `compliance-engine` all contain working, testable business logic (e.g. `core-ledger` enforces real double-entry balance validation; `cashflow-engine` actually computes a 91-day forecast; `risk-engine` evaluates real threshold logic for DSCR, forecast deficit, and client concentration), and there's a real `tests/engine-smoke.test.mjs`. Only `integrations/index.ts` (and likely a few unsampled engines) remain genuinely stub-level. **Also corrected**: the engine count is **17, not 19** (the original count likely conflated supporting infrastructure folders — `event-bus`, `shared`, `api-layer` — with engines; `module-map.md` and the `src/` folder both confirm 17). **Most significant finding**: `finos-plugin/docs/source-intelligence.md` is a real citation map — it names all 16 source drafts with paragraph counts and a one-line "implementation signal" per document, closer to Sales (05)'s citation-backed model than Marketing (03)'s uncited one. Like every department migrated so far, **all numbers throughout are generic doctrine/thresholds, not real historical figures** — no actual agency revenue, cost, or billing data exists anywhere in the docs, code, or raw drafts.

## 3. Capability Registry

All 17 modules below have real, non-trivial design content in `finos-plugin/docs/` (confirmed, not just folder names with nothing behind them) — code-implementation maturity varies (see §13):

| Capability | Description | Code status |
|---|---|---|
| Core Ledger | Double-entry posting from events, balance assertion, trial balance | Real logic |
| Event Bus | Central event routing fanning out to ledger, allocation, cashflow, risk, AI agents | Infrastructure |
| Cashflow Engine | 91-day rolling forecast, daily inflow/outflow/net/runway calculation | Real logic |
| Allocation Engine | Capital/budget allocation across the agency | Unconfirmed depth |
| Risk Engine | DSCR, forecast deficit, and client concentration risk detection (thresholds: DSCR <1.25x, concentration >20%/critical >35%) | Real logic |
| Forecasting Engine | Longer-horizon financial projection | Unconfirmed depth |
| Treasury System | Reserve management (3-tier: Operating 3-6mo, Emergency 6-12mo, Expansion/Acquisition) | Unconfirmed depth |
| Reporting System | Financial reporting outputs | Unconfirmed depth |
| AI Agents | 7-agent roster (see §5) | Real spec data, no LLM execution wired up |
| Integrations | Connector registry for CRM/payment/banking/accounting/payroll/marketing/ops systems | **First real, verified-live connector (2026-07-07)**: `ZohoBooksConnector` (accounting) — real OAuth client authenticated against the live org, invoice pull/normalize, live USD→KES conversion (see §12). All other domains (CRM/payments/banking/payroll/marketing/ops) remain stub. |
| Workflows | Revenue Received, Expense Approval, Liquidity Alert (see §4) | Unconfirmed depth |
| Financial Governance | Approval tiers, decision rights | Unconfirmed depth |
| Compliance Engine | Tax reserve calculation, audit readiness checklist | Real (small) logic |
| Profitability Engine | CAC, LTV, LTV:CAC, contribution margin, ROIC | Unconfirmed depth |
| Dashboard System | Executive financial dashboard | Unconfirmed depth |
| API Layer | HTTP API, MCP server, application/contracts | Has 4 files, not 1 stub |
| Rules Engine | Cross-cutting business rule evaluation | Unconfirmed depth |
| Audit System | Append-only, hash-chained audit logging | Unconfirmed depth |

## 4. Workflow Index

| Workflow | Trigger | Steps | Output | Owner | Source |
|---|---|---|---|---|---|
| Revenue Received | Payment event | Payment → Event Bus → Ledger → Allocation → Treasury → Compliance → Risk → Report | Posted, allocated revenue | Mary Thuo | `finos-plugin/docs/workflows.md` |
| Expense Approval | New expense | Tiered approval: ≤$500 auto/dept owner, $500-5K manager, $5K-25K CFO, >$25K executive/board | Approved/rejected expense | Mary Thuo | same |
| Liquidity Alert | Trigger condition met | Fires on: runway <60 days, negative net liquidity, negative 13-week forecast, reserve breach | Escalation to Treasury/CFO Agent | Mary Thuo | same |
| Operating rhythm | Time-based | Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly reviews, each with specific documented content | Maintained financial oversight | Mary Thuo | same |

## 5. Agent Roster

**7 agents**, each with a full system prompt in `finos-plugin/docs/agent-prompts.md`, mirrored in code at `finos-plugin/src/ai-agents/index.ts` (`financialAgentSpecs`) — docs and code are in sync, including `humanApprovalRequiredFor` escalation lists per agent: **CFO Agent**, **Cashflow Agent**, **Risk Agent**, **Profitability Agent**, **Treasury Agent**, **Compliance Agent**, **Leakage Detection Agent**. All share a common doctrine: *"Operate liquidity-first... Never treat restricted cash, tax reserves, payroll reserves, or emergency reserves as discretionary cash."*

**Wired to a real LLM and verified live (2026-07-01).** `package.json` now depends on `@anthropic-ai/sdk` (`^0.109.0`). New `src/ai-agents/runtime.ts` (`ClaudeAgentRuntime`) calls `claude-opus-4-8` per agent, using the real `systemPrompt` above as the system message, adaptive thinking, and a `json_schema` structured-output format that forces a `{summary, recommendedActions, requiresHumanApproval, approvalReasons, riskLevel}` shape — so `humanApprovalRequiredFor` isn't just spec metadata anymore, the model is asked to flag it per-recommendation. Wired into `src/workflows/index.ts`'s `FinancialWorkflowOrchestrator`, which — discovered during this wiring — **existed in code but was never instantiated anywhere in the app**; fixed by constructing it (with the new runtime + the pre-existing but likewise-unused `AuditSystem`) and calling `.register()` inside `createFinOsApplication()`. **Advisory only**: recommendations are written to the hash-chained audit trail, nothing auto-executes — matches `AGENCY_OPERATING_CONSTITUTION.md`'s human-approval rule; real automation still needs `AUTOMATION_APPROVAL_MATRIX.md` rows (`GO_LIVE_CHECKLIST.md` item 11).

**Live verification, not just a compile check**: publishing a real `REVENUE_RECEIVED` event through the running app produced 5 real, distinct, domain-correct recommendations (from the 5 agents whose `listensTo` includes that event — CFO, Cashflow, Profitability, Treasury, Compliance), each written to the audit log with the hash chain verified intact afterward.

**Bonus finding**: `node_modules/` didn't exist anywhere in this codebase before this session — `npm run build` had apparently never actually been run. Running it for the first time surfaced 2 unrelated pre-existing TypeScript compile errors (in `financial-governance/index.ts` and `risk-engine/index.ts`, both now fixed) that had been sitting undetected in "working" code.

## 6. Skill Library Index

*(placeholder — no separate skill library exists; agent capabilities are defined directly in the Agent Roster's system prompts above)*

## 7. KPI Dictionary (department-local)

**All thresholds below are generic doctrine baked into the code/docs, not real measured figures** — same caveat as every other department, though here the numbers double as actual code logic (risk-engine genuinely evaluates these thresholds), not just narrative targets.

| Metric | Formula | Threshold found | Source | Owner | Cadence |
|---|---|---|---|---|---|
| Runway | Cash ÷ average daily burn | Alert if <60 days | `workflows.md`; implemented in `cashflow-engine` | Mary Thuo | Continuous |
| DSCR (Debt Service Coverage Ratio) | Operating income ÷ debt service | Alert if <1.25x | `risk-engine/index.ts` | Mary Thuo | Continuous |
| Client concentration | Largest client revenue ÷ total revenue | Alert >20%, critical >35% | same; matches `concentration_limit_pct` default in `database/schema.sql` | Mary Thuo | Continuous |
| LTV:CAC ratio | See `AGENCY_KPI_DICTIONARY.md` | Doctrine target 3:1 (i.e. 1:3 CAC:LTV) | Draft 5 ("Elite Unit Economics") | Mary Thuo | *(unset)* |
| Reserve tiers | Months of operating cost held | Operating 3-6mo, Emergency 6-12mo, plus Expansion/Acquisition reserves | `cashflow-engine`, `workflows.md` | Mary Thuo | *(unset)* |
| Forecast horizon | Rolling forward-looking window | 13-week / 91-day | `cashflow-engine` | Mary Thuo | Weekly |
| Expense approval tiers | Dollar thresholds | ≤$500 auto, $500-5K manager, $5K-25K CFO, >$25K executive/board | `workflows.md` | Mary Thuo | Per-transaction |
| Revenue target (monthly) | Real, owner-confirmed | $1,000,000/month, $35,000/day, non-negotiable | `AGENCY_REVENUE_TARGETS.md` | Mary Thuo | Daily/Monthly |

These are real, implemented thresholds in working code — closer to "configured business rules awaiting real values" than pure narrative aspiration. Cross-reference `00_Agency_Governance/AGENCY_KPI_DICTIONARY.md` for the agency-wide version of LTV:CAC, and `00_Agency_Governance/AGENCY_REVENUE_TARGETS.md` for the full revenue-target derivation, the 7-calendar cognitive operating system, and cash-flow discipline principle (revenue closed ≠ cash collected) that directly extends this department's own Cashflow Engine/forecasting mandate (§3, §13).

**Owner decision (2026-06-30): keep all the generic doctrine thresholds above as-is for now** (runway <60 days, DSCR <1.25x, concentration >20%/critical >35%, expense approval $500/$5K/$25K tiers). No real cash-flow/expense history exists yet to calibrate against — revisit once real data accumulates rather than guess at real numbers prematurely.

## 8. Decision Log

*(placeholder — empty)*

## 9. Risk / Incident Log

*(placeholder — empty. Note: `risk-engine` and `compliance-engine` are NOT stub-level as originally assumed — they contain real threshold-evaluation logic (DSCR, concentration, tax reserve, audit readiness) — but no real incidents have been logged because no real financial data has ever been run through them.)*

## 10. Standards & SOPs Index

**Security/compliance** (`finos-plugin/docs/security.md`) — real, specific policy design, not boilerplate:
- RBAC roles: founder, CEO, CFO, controller, treasury, operations lead, department owner, accountant, auditor, read-only investor
- Separation-of-duties requirement; JWT/mTLS auth; webhook signature verification; TLS + secret-store encryption
- **Append-only, hash-chained audit logs** with a compensating-event correction policy (errors are corrected via new offsetting events, never edited/deleted) — this is a real architectural decision specific to FinOS's event-sourced model, not generic security boilerplate.

**Agent doctrine** (common to all 7 agents in `agent-prompts.md`): *"Operate liquidity-first... Never treat restricted cash, tax reserves, payroll reserves, or emergency reserves as discretionary cash."*

`finos-plugin/docs/` (11 files total: `architecture.md`, `module-map.md`, `workflows.md`, `integrations.md`, `source-intelligence.md`, `agent-prompts.md`, `api-contracts.md`, `security.md`, `observability.md`, `deployment.md`, `automation-catalog.md`) is the canonical design reference for this department per the earlier grandfathered-exception decision (§13).

## 11. RACI / Ownership

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| *(placeholder — but real RBAC role names already exist to map against once owners are named: founder, CEO, CFO, controller, treasury, operations lead, department owner, accountant, auditor, read-only investor — see `finos-plugin/docs/security.md`)* | | | | |

## 12. Triggers / Automation Hooks

`finos-plugin/docs/automation-catalog.md` documents real trigger logic that already exists in code: the Liquidity Alert workflow (§4) and the risk-engine's threshold evaluations (DSCR, concentration, forecast deficit) ARE implemented automation, not just a wishlist — unlike most other departments' Triggers sections. `integrations/index.ts` remains the genuine gap: the connector registry interface exists but has zero real connector implementations (no Stripe/QuickBooks/Plaid/banking API actually wired up), so none of this can fire against real financial data yet. **Original owner confirmation (2026-06-30): no payment/accounting platform is in real use yet**, so this stayed a documented gap rather than a connector built against nothing. **Platform decision, flipped twice then confirmed real on 2026-07-01:** Zoho Books was confirmed 2026-06-30 as the accounting platform, selected specifically to pair with Zoho CRM for native CRM↔Books sync. That rationale no longer held once Zoho CRM was superseded by **ClickUp** (2026-07-01), so the owner picked **QuickBooks** as the replacement the same day — but attempting the real QuickBooks connection confirmed a paid subscription/business registration is required before any integration can even authenticate, with no free tier. The owner reverted back to **Zoho Books** the same day and connected it via claude.ai's Zoho Books connector: `list_organizations` confirmed a **real, pre-existing organization** (created 2026-06-26) — ID `929138528`, "Arika Agency," Kenya, base currency **KES**, Premium Trial plan. `integrations/index.ts`'s connector registry still has zero real connector implementation — building the Zoho Books connector is `00_Agency_Governance/GO_LIVE_CHECKLIST.md` item 9. **New real requirement surfaced by the currency mismatch**: `02_Offer/OFFER_OS.md`'s entire pricing catalog is in USD, but Zoho Books' org currency is KES — owner decided offers stay priced in USD while invoices are issued in KES via a conversion calculator (exchange-rate source not yet decided) — this is now part of the connector's scope, not a side detail. Map the documented thresholds in §7 directly into `00_Agency_Governance/AUTOMATION_APPROVAL_MATRIX.md` once that real integration exists to trigger them.

**2026-07-07 — the Zoho Books connector is now real code, not a shell.** `src/integrations/zoho-books.ts`'s `ZohoBooksConnector` implements the full `IntegrationConnector` contract against Zoho Books' real REST API (OAuth refresh-token client, independent of the claude.ai session connector): `pull(since)` normalizes invoices into idempotent `INVOICE_CREATED`/`REVENUE_RECEIVED` events, `health()` verifies the credentials work, and `createInvoiceFromUsdAmount(...)` closes the exchange-rate gap noted above — it fetches a **live** USD→KES rate from `open.er-api.com` (free, keyless, daily-refreshed; ECB-based `frankfurter.dev` was tried first and confirmed live to not publish a KES rate at all) and creates the invoice in KES with the original USD amount, rate, and source recorded in the invoice notes for audit. 8 real tests pass (pure conversion math + normalization, no network mocking needed) and the live exchange-rate fetch was verified end-to-end (real rate returned: 129.22 KES/USD on 2026-07-07). **Verified live the same day**: the owner walked through the Zoho API Console (Self Client → scoped grant code → exchanged for a real access/refresh token pair, US data center confirmed by the token response), credentials landed in `.env`, and the standalone connector — independent of the claude.ai session connector, whose authorization doesn't extend to a standalone server process — authenticated for real: `health()` confirmed the live org (`"Connected to Zoho Books org Arika Agency (929138528)"`), `pull()` correctly returned 0 events (no invoices exist yet). Deliberately does not auto-wire `push()` to fire off internal events — invoice creation is a real financial action requiring an `AUTOMATION_APPROVAL_MATRIX.md` row first (item 11), so it's exposed as an explicit method for a human-gated caller instead. No test invoice was created — issuing the first real invoice is `GO_LIVE_CHECKLIST.md` item 13's milestone, an owner decision, not a dry run.

## 13. Existing OS Sub-Layer

**Yes — code-based, and more mature than originally assessed (corrected 2026-06-30).** `09_Finance/finos-plugin/` is a TypeScript application: `src/` with **17 engine folders** (not 19 as originally stated — `event-bus`, `shared`, and `api-layer` are supporting infrastructure, not engines), `docs/` (11 markdown design docs, all with real content), `database/schema.sql` (a real, normalized Postgres schema with enums, concentration limits, journal entries), `tests/engine-smoke.test.mjs`, and a `.codex-plugin/` config.

**Correcting the original "mostly stub" characterization**: spot-checking `core-ledger`, `cashflow-engine`, `risk-engine`, and `compliance-engine` found real, working business logic — double-entry balance enforcement, actual 91-day cashflow forecasting math, real DSCR/concentration risk threshold evaluation, tax reserve calculation. Only `integrations/index.ts` is confirmed genuinely stub-level (interface only, no real connectors); a few other engines (forecasting, treasury, reporting, dashboard, workflows, financial-governance, audit) remain unverified at the code level but have real design content in `docs/`.

**Citation system found, comparable to Sales (05)**: `finos-plugin/docs/source-intelligence.md` names all 16 source drafts with paragraph counts and a one-line "implementation signal" per document (e.g. "Elite Unit Economics. Draft 5.docx — 660 paragraphs — CAC, LTV, LTV:CAC, contribution margin, break-even, ROIC..."), plus 9 "Preserved System Doctrines," 8 "Architecture Decisions Derived From The Corpus," and 7 "Non-Negotiable Implementation Invariants." This is a real, auditable source map — meaningfully more rigorous than Marketing's uncited equivalent layer, though the underlying raw drafts are themselves AI-generated strategy documents, not primary business records.

**Decision (2026-06-30, reaffirmed):** `finos-plugin/` stays a grandfathered code-backed exception to the markdown-first standard — and given this migration found it's more functional than assumed, that decision looks stronger in hindsight, not weaker. `finos-plugin/docs/` remains the canonical spec; code is the implementation.

## 14. Raw Archive Pointer

~16 root-level "Draft N.md" files, sampled for the 2026-06-30 content migration (`Financial Execution Mapping.v1.md`, `Elite Unit Economics. Draft 5.md`, `Cash Flow Engineering Sytem. Draft 4.md`, `Financial Vision. Finance v1.md`, plus others). Existing gap backlog: `09_Finance/00_Workspace_Intelligence_Inventory/` (governance/process gaps about the surrounding markdown layer — not gaps in finos-plugin's docs/code itself, which are confirmed substantive).

**Grounding confirmed**: `Financial Execution Mapping.v1.md` contains the literal prompt that produced the FinOS plugin concept — its 6-layer architecture is the direct ancestor of `architecture.md`'s 10-layer system, and it lists nearly the same 7-agent roster that became `agent-prompts.md`. `Elite Unit Economics. Draft 5.md` is the clear source for the profitability-engine's CAC/LTV/ROIC concepts. `Cash Flow Engineering Sytem. Draft 4.md` is the clear source for the 13-week forecast window and 3-tier reserve system. The raw drafts are themselves AI-generated "elite system" prompts/outputs, not primary records of real agency financial history.

## 15. Changelog

- 2026-06-30 — File created as part of v0.1 skeleton restructuring.
- 2026-06-30 — Content migration: `finos-plugin/docs/` (all 11 files) and a sample of code/raw drafts read. **Corrected** the original "19 engines, mostly stub" characterization — confirmed 17 engines, several with real working logic (core-ledger, cashflow-engine, risk-engine, compliance-engine), and a real source-citation system in `source-intelligence.md` comparable to Sales's. Populated Capability Registry, Workflow Index, Agent Roster, KPI Dictionary, Standards & SOPs Index, and Triggers/Automation Hooks. All financial thresholds confirmed generic doctrine, not real agency figures.
- 2026-06-30 — Added the real, owner-confirmed monthly/daily revenue target to §7, cross-referencing the new `AGENCY_REVENUE_TARGETS.md`. — Claude Code (Sonnet 4.6)
- 2026-06-30 — Confirmed by direct code inspection that the AI agent layer has zero LLM SDK dependency (no Anthropic/OpenAI package in `package.json`, no API-call code anywhere in `src/`) — matches the doc's existing "spec only" characterization exactly. Owner made 3 real decisions: (1) no payment/accounting platform is in real use yet, so the integrations gap stays documented rather than built against nothing; (2) AI agents stay spec/routing-only, not wired to a live LLM, until a real integration exists to feed them real data; (3) all generic risk/expense thresholds stay as-is until real cash-flow history exists to calibrate against. Resolves tracker items 25, 26, 27. — Claude Code (Sonnet 4.6)
- 2026-06-30 — **Items 25 and 27 superseded the same day.** Owner confirmed real decisions that close both gaps these items were waiting on: **Zoho Books** as the real accounting platform (closes item 25's "nothing real to connect to" blocker), and **Claude (Anthropic API)** as the LLM to wire into the 7-agent roster (closes item 27's "no real data to feed it" blocker, now that Zoho Books exists). Neither the Zoho Books connector nor the Claude API wiring is built yet — both added to `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. Item 26 (risk/expense thresholds) is unaffected, still genuinely waiting on real cash-flow history. — Claude Code (Sonnet 4.6)
- 2026-07-01 — Added §16 Memory/Feedback Loop/Cadence per the go-live plan in `00_Agency_Governance/GO_LIVE_CHECKLIST.md`. — Claude Code (Sonnet 5)
- 2026-07-01 — **QuickBooks abandoned, reverted to Zoho Books** as the accounting platform (§12) — real QuickBooks account creation confirmed a paid subscription/business registration is required before authentication, no free tier. Item 9 in `GO_LIVE_CHECKLIST.md` retargeted to a Zoho Books connector. — Claude Code (Sonnet 5)
- 2026-07-01 — **7-agent roster wired to a real LLM and verified live** (§5) — `@anthropic-ai/sdk` added, new `src/ai-agents/runtime.ts` calls `claude-opus-4-8` with structured-output enforcement. Discovered and fixed `FinancialWorkflowOrchestrator` was defined but never instantiated. Real `REVENUE_RECEIVED` test event produced 5 verified agent recommendations in the audit trail. Also fixed 2 unrelated pre-existing compile errors surfaced by running the build for the first time. Closes `GO_LIVE_CHECKLIST.md` item 7. — Claude Code (Sonnet 5)
- 2026-07-01 — **Zoho Books confirmed real and connected** — pre-existing org (ID `929138528`, Kenya, KES base currency, Premium Trial). Real decision: USD offer pricing, KES invoicing via a not-yet-built conversion calculator — added to item 9's scope. — Claude Code (Sonnet 5)
- 2026-07-07 — **Real Zoho Books connector built** (§3, §12), closing the "confirmed stub" characterization for the accounting domain. `ZohoBooksConnector` implements the full connector contract with a real OAuth client, invoice pull/normalization (idempotent event ids), a health check, and `createInvoiceFromUsdAmount(...)` — the USD→KES conversion calculator scoped under item 9, using a live, free, keyless rate source (`open.er-api.com`; ECB-based `frankfurter.dev` was tried and confirmed live to not cover KES). 8 new tests pass; the live rate fetch and full app boot were both verified end-to-end. Registered in `application.ts`'s `IntegrationRegistry`.
- 2026-07-07 — **Default invoice terms/notes and receipt-email preference set, real and verified live.** Owner approved standard boilerplate text (payment-due terms, thank-you note; quotation equivalents drafted but not yet wireable — see below) and turned on the Payment Received acknowledgement email (`send_payment_receipt_acknowledgement`, confirmed persisted via a live toggle + reread). **Confirmed a real platform limitation**: Zoho Books' org-wide default Terms & Conditions preference (`settings/preferences` → `terms.invoice_terms`/`estimate_terms`) returns success on write but silently never persists — tested with two different payload shapes, both no-ops, confirmed via reread. This is UI-only (Settings → Invoices/Estimates → Terms & Conditions), same class of limitation as ClickUp's status-write no-op found earlier. Since the org-wide default can't be set via API, wired the approved text directly into `ZohoBooksConnector.createInvoiceFromUsdAmount` instead (`DEFAULT_INVOICE_TERMS`, `DEFAULT_INVOICE_THANK_YOU_NOTE` constants in `zoho-books.ts`) — verified live with a real test invoice showing both fields correctly, then deleted. **Real scope gap surfaced**: the connector only creates invoices, not estimates/quotations — the approved quotation terms/notes text has nowhere to attach yet; building a `createEstimate` method is unscoped, separate future work. — Claude Code (Sonnet 5)
- 2026-07-07 — **Zoho Books organization profile set for real (phone).** Owner gave the real business phone (`+254142324624`); set live via a raw `PUT /organizations/{id}` REST call using the same refresh-token credentials as the connector — confirmed persisted via an independent `get_organization` read. **Corrects an initial assumption**: no `update_organization` tool is exposed via the claude.ai session connector (only reads), which looked like a UI-only limitation similar to Canva's Brand Kit — but Zoho's actual REST API does accept profile writes; it's just not wrapped as a tool in this session. Address and payment/bank footer details were deliberately left blank — real values not yet given by the owner (not fabricated). Tax registration left off, matching the org's real `is_registered_for_tax: false` state. — Claude Code (Sonnet 5)
- 2026-07-07 — **First real test invoice created end-to-end, then cleaned up.** A real contact ("Jane Don") plus a real $10 USD → KES 1,292.24 invoice (`INV000001`) were created through the standalone connector and confirmed via `get_invoice`. Surfaced and fixed one real bug: the invoice notes text contained a literal `>` (from `USD->KES`), which Zoho Books' API rejects outright (error code 18) — fixed the wording, rebuilt, retried successfully. Both the invoice and contact were deleted afterward per the owner's cleanup choice (no void endpoint is exposed via the available tools; delete is clean for a payment-free draft). First real invoice this system has ever produced. — Claude Code (Sonnet 5)
- 2026-07-07 — **Zoho Books connector verified live end-to-end, same day.** Owner created a Zoho API Console Self Client, generated a scoped grant code, and it was exchanged for a real access/refresh token pair (US data center confirmed). Real credentials written to `.env`; the standalone connector then authenticated against the live org on its own — `health()` confirmed it, `pull()` correctly returned 0 events (no invoices exist yet, see `GO_LIVE_CHECKLIST.md` item 13). Fully closes item 9. — Claude Code (Sonnet 5)

## 16. Memory / Feedback Loop / Cadence

**Memory**: No dedicated memory-log files exist yet (§8 Decision Log is an empty placeholder, unlike Sales' instantiated-but-empty `06_AI_Memory_Logs/`, `05_Sales/SALES_OS.md` §16). Gap — recommend a parallel `09_Finance/06_AI_Memory_Logs/` (or a `finos-plugin/docs/memory/` equivalent) once the 7-agent roster is wired to Claude (`GO_LIVE_CHECKLIST.md` Phase 2), so agent decisions/escalations have somewhere real to land.

**Feedback Loop**: Already real and implemented in code — the Liquidity Alert workflow (§4, §12) fires on runway <60 days, negative net liquidity, negative 13-week forecast, or reserve breach, escalating to the Treasury/CFO Agent; risk-engine's DSCR (<1.25x) and concentration (>20%/critical >35%) threshold evaluations (§7) are the same pattern. This is the most mature feedback loop of any department — code-enforced, not just documented — but has never fired against real financial data (§9).

**Cadence**: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly operating rhythm already documented in `workflows.md` (§4) — maps to the Cash Flow Calendar (weekly forecast refresh, §7's 13-week/91-day horizon) and Capacity Calendar (reserve-tier review). Risk-engine threshold checks (§7) run continuously, not on a calendar tick.
