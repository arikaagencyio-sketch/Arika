# 04_Content/_memory

Tracked placeholder, created 2026-10-09 so the folder exists before anything writes to it.

**What will live here, and only once it is real:**

| File | Written by | Format |
|---|---|---|
| `runtime.jsonl` | `arika-runtime` when a `content-*` agent actually runs (all six declare `memory_stream: 04_Content/_memory/runtime.jsonl`) | Runtime envelope, `arika-runtime/src/memory-writer.ts` |
| `skill_runs.jsonl` | A Content skill (C01–C07) after a real, human-invoked apply | Sector's execution record, `01_Sector/contracts/skill-execution-record.schema.json`, `source: "claude-code"` |

**As of 2026-10-09 neither file exists. No Content agent or skill has run.** That absence is evidence and must not be filled with back-dated or synthetic records. Test fixtures never write here. Under the runtime's approval gate (`arika-runtime/src/approval.ts`), a refused run leaves no record here by design.
