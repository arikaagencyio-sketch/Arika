# Arika Runtime — Decision Log

Newest first. Records architecture decisions made while building the runtime,
per GLOBAL_OS.md §10.

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
