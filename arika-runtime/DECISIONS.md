# Arika Runtime — Decision Log

Newest first. Records architecture decisions made while building the runtime,
per GLOBAL_OS.md §10.

## 2026-09-22 — The fixture lane becomes an authorisation registry (prepared, closed)

**Why:** the lane was hard-wired to one authorisation — A001 D21's agent, stream and
unit as single constants. A second, separately authorised fixture (draft Offer decision
OFFER-F2) could not be expressed without either overwriting D21's pins or loosening them.

**Decision:** `FIXTURE_AUTHORISATIONS` in `src/fixture.ts` lists every fixture authorisation
ever made; entries are never deleted. Each pins one `agent`, one repo-relative `stream`,
required markers, forbidden patterns, optionally an exact `inputSha256`, and a `status` of
`draft` / `approved` / `spent`.

- **Two locks to run:** the master switch **and** an `approved` authorisation. D21 is
  `spent`; OFFER-F2 is `draft`; the switch is `false`.
- **Destination resolves to exactly one authorisation.** Absolute paths, traversals and
  unregistered `sandbox*.jsonl` names are refused, and each authorisation is pinned to its
  own agent, so neither can run on the other's stream.
- **Exact input where pinned.** OFFER-F2 carries a sha256 of its `seed_brief`, which turns
  D21's documented weakness (a text check on free text) into an exact match for this one.
- **Reserved names widened, deliberately:** any `sandbox.jsonl` or `sandbox-<id>.jsonl` is a
  fixture stream, so an ordinary run is refused from all of them.
- **The registry is validated at load** (repo-relative, sandbox-named, unique ids and
  streams, global regexes), so a malformed entry fails closed.

**Not changed:** the pre-model gate still runs first in `runAgent`; `writeMemory`'s coarse
guard is unchanged in shape; ordinary runs are unaffected; D21's `sandbox.jsonl` and
`runtime.jsonl` are untouched. **Fixture runs still advertise their spec's emits** — not in
scope here, and recorded as a limit in the OFFER-F2 draft.

**Verified:** see the OFFER-F2 entry in `02_Offer/OFFER_OS.md` §15 and `npm test`.

## 2026-09-22 — A rejected brief withholds `OFFER_BRIEF_RECEIVED`

**Found by:** the A001 D21 `TEST_FIXTURE` run (one `offer-orchestrator` attempt,
2026-09-21). It returned `registry_action: reject`, yet the result reported
`emitted: ["OFFER_BRIEF_RECEIVED"]` — the event `offer-oeos-engineer` subscribes to.
`emitted` was `spec.emits` verbatim, so a stopped brief advertised the event that would
advance it. Nothing chained only because no path sends agent emits: the CLI has no bus,
and the booted runtime's event handler discards `result.emitted`.

**Decision:** `finalizeRun` returns `advertisedEmits(spec.emits, recommendation)`. A small
table, `WITHHELD_EMITS`, withholds `OFFER_BRIEF_RECEIVED` when `registry_action` is
`reject`. Nothing else is filtered.

- **Only `reject`.** It is the one value with no path forward (readiness packet
  PG3 / R5 / RD7). `needs_more_seed_data`, `add_new_offer` and `update_existing_offer`
  each have a human-reviewed path, so the control for them is review, not suppression.
- **Recommendation and memory line untouched.** `emitted` was never in the memory
  payload, so the log format is unchanged.
- **Kept inside `executor.ts`**, where the estate gate's runtime-reality check watches.
  The change adds no event sending, so that check still passes.

**Not changed:** the spec still declares `emits: [OFFER_BRIEF_RECEIVED]`; no registry
behaviour; no approval logic. The one line in `02_Offer/_memory/sandbox.jsonl` is
append-only history and stays as written.

**Residual, recorded rather than fixed:** if emits are ever sent, the three non-reject
values would reach OEOS without PG3's human review — the orchestrator's top-level
approval flag can be `false` at class 1. See `02_Offer/OFFER_OS.md` §12.

**Verified:** `npm test` → 40/40. Three new cases: the table withholds only the named
event on `reject`; the **real** orchestrator spec through `finalizeRun` returns no
`OFFER_BRIEF_RECEIVED` on `reject` while its memory line keeps the reject; and the other
three actions are unchanged, with no approval invented.

## 2026-09-13 — The agent's own approval flag raises the gate

**Found by:** three consecutive Sector → Offer test runs (`offer-orchestrator` ×2,
`offer-oeos-engineer` ×1). Each recommendation returned `requiresHumanApproval: true`;
each top-level result — and each memory line — said `false`. The gate was computed
*before* the agent ran, from `risk_class` and the spec flag alone, so the agent's
answer could never reach it. For Offer that is the dangerous direction: pricing,
claims, and registry changes reported as needing no sign-off.

**Decision:** the gate is now decided in `finalizeRun`, after the agent answers:

`requiresHumanApproval = risk_class >= 3 || spec.requires_human_approval || recommendation.requiresHumanApproval === true`

- The agent can **raise** the gate for its run, never lower it; class 3+ still forces it.
- Only a literal `true` counts. All three execution paths (prompt, finos-plugin via its
  `recommendationSchema`, bois via `run_brand_task.py`) return this camelCase key, so
  one rule covers every department.
- The result and the memory line get the same value.

**Not changed:** the three existing lines in `02_Offer/_memory/runtime.jsonl` still say
`false` — the log is append-only. Their `payload.recommendation.requiresHumanApproval`
carries the true value.

**Verified:** `npm test` → 18/18, including the three approval cases (low-risk + agent
true → true; low-risk + agent false or absent → false; class 3/4 + agent false → true),
each asserted on both the top-level result and the logged line.

## 2026-09-13 — Prompt-agent response budget + truncation handling

**Found by:** the first live Sector → Offer test. `offer-orchestrator` reached Claude
but failed with `Unterminated string in JSON at position 4758` — the reply was cut
off at `max_tokens: 2048`, which thinking and a 12-field `output_schema` share. The
2048 was inherited from finos's call shape, sized for the 5-field base envelope.

**Decision:**
- **Default raised to 16000** (`DEFAULT_MAX_TOKENS`, `src/executor.ts`).
- **Specs may declare `max_tokens`**, validated as a positive integer capped at
  21333 (`MAX_NONSTREAMING_TOKENS`) — the SDK refuses any larger non-streaming call,
  so an over-budget spec fails at load, not mid-run.
- **A `stop_reason: "max_tokens"` reply now throws "output was truncated"** naming the
  budget, instead of a JSON parse error. Both are tests, not comments.

**Deliberately NOT changed:** streaming (not needed under the ceiling), and
finos-plugin's own `max_tokens: 2048` (`09_Finance/finos-plugin/src/ai-agents/runtime.ts`)
— its agents return the small base envelope; revisit if a finance agent truncates.

**Verified:** `npm test` → 15/15. Re-run of the same manual `offer-orchestrator` call
succeeded (`registry_action: needs_more_seed_data`) and wrote the first line of
`02_Offer/_memory/runtime.jsonl` — the live Claude call, unverified since Session 1,
is now closed end-to-end for a prompt agent.

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
