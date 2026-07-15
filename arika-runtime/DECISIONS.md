# Arika Runtime — Decision Log

Newest first. Records architecture decisions made while building the runtime,
per GLOBAL_OS.md §10.

## 2026-07-15 — The `join` barrier

**Decision:** add a fifth trigger type, `join`, rather than flag the gap a second time.

**Why now.** The gap was found wiring Experience Engineering (20) and documented as
"the real fix is a `waits_for: [A, B]` trigger type". Audits & Diagnostics (14) then
hit the identical wall on its parallel sub-audits. Two departments with genuinely
parallel work is enough evidence that this is a runtime limitation, not a modelling
error in one department.

**Design notes:**
- **Fires once, on the last arrival**, then clears the barrier — a stray late event
  cannot re-fire a completed join.
- **`waits_for` requires 2+ distinct events.** One event is just `type: event`; a
  repeated event can never produce a second arrival. Both are schema errors, so
  neither becomes a silent deadlock.
- **`correlate_on` is a safety property.** Events only satisfy a barrier together when
  they share a correlation value. A missing key means the event is **dropped loudly,
  not guessed** — attributing it to whichever run is waiting would, in 14's case,
  print one client's audit findings on another client's report. Both properties are
  tests, not comments.

**Deliberately NOT built: a counting barrier.** 14's fan-in membership is decided at
runtime (a Lite audit scopes one sub-audit, full-stack scopes seven), which the fixed
barrier cannot express — it would deadlock on Lite or fire early on full-stack. The
fix is a barrier that reads its expected set from an upstream payload. **14 has never
delivered an audit**, so that primitive would be designed entirely against a workflow
no one has ever run. Flagged in `AUDITS_DIAGNOSTICS_OS.md` §12; build it when a real
audit demands it.

**Known limit:** joins are in-memory and per-process. A 7-14 day audit outlives the
runtime. Cross-day barriers need the durable bus `EventBus` was designed to be
swapped for.

**Applied:** `experience-engineering-technical-director` now joins on
`[MOTION_SPEC_READY, CAMERA_SPEC_READY, SCENE_COPY_READY]` correlated on `project`,
resolving 2 of EE's 4 orphaned emits. The other 2 are the launch gates — that join is
a **human**, by design, not by limitation.

## 2026-07-14 — Session 1: runtime scaffold + first 9 agents

**Delivered:** a working `arika-runtime/` — one canonical agent spec format + one
executor that runs agents from manual, cron, event, and webhook triggers, with
governance (Constitution risk classes) and bois-compatible JSONL memory.

**Agents live (9):** `design-storyboard-generator` (prompt), the 7 Finance agents
wrapped from finos-plugin (`finance-{cfo,cashflow,risk,profitability,treasury,
compliance,leakage}-agent`), and `sales-lead-qualification` (prompt). The other 16
`.claude/agents` files are cleanly quarantined as legacy (no `triggers` block) —
they still work as interactive Claude Code subagents and migrate later.

**Verified this session (no API key required):**
- `npm run build` clean; `npm test` → 8/8 pass (governance, schema, registry, memory).
- `arika list` → 9 registered, 16 skipped with reasons.
- Runtime boots: 9 agents, 26 event bindings, 1 cron (`0 9 * * 1-5`), webhook on 8080.
- `POST /webhook/zoho {type:REVENUE_RECEIVED}` fanned out to all 5 finance agents
  that listen for it; each delegated into finos's own `ClaudeAgentRuntime` and
  failed *gracefully* on the missing key — proving the dynamic-import wrapper and
  event fan-out both work end-to-end.
- CLI `run` (prompt + finos paths) and `logs` behave correctly.

**Not verified (needs `ANTHROPIC_API_KEY`):** the live Claude call itself. Set the
key in `arika-runtime/.env`, then `arika run design-storyboard-generator
--input='{"topic":"..."}'` returns the 7-field storyboard JSON and writes a memory
line. This is the only remaining step to close end-to-end.

Decisions taken:

- **Toolchain mirrors finos-plugin** (ESM, `module: NodeNext`, `strict`, Node
  ≥20.11, `node:test`, `tsx`) so the runtime is consistent with the one built
  plugin in the repo. Rejected: a bundler/Jest setup — no reason to diverge.
- **Executor generalizes finos's `ClaudeAgentRuntime.run()`** rather than
  reimplementing the Claude call. Same model default (`claude-opus-4-8`),
  `thinking:{type:"adaptive"}`, `output_config` json_schema structured output.
- **finos is wrapped by dynamic-importing its built `dist/`**, not by adding it
  to arika-runtime's tsc graph (finos sources live outside `rootDir: src`). Keeps
  finos untouched and avoids cross-package compilation. A minimal local interface
  types the seam.
- **Advisory-first:** the executor returns recommendations + writes memory only;
  it performs no state-changing actions. `tools` are declared but not invoked.
- **Constitution Class 0–4 is the supreme risk model;** finos/Sales
  low/medium/high/critical maps onto it. Human approval forced at class ≥ 3.
- **Memory = append-only JSONL** in the bois envelope shape (the only live
  machine-written log format in the repo).
