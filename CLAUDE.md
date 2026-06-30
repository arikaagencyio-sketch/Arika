# Claude Code Entry Point

This repository is Arika Agency's Operating System. The substance lives in plain markdown, not here — this file is intentionally a thin pointer.

## How to operate in this repo

1. Read [`GLOBAL_OS.md`](GLOBAL_OS.md) first — agency identity, department map, operating flow, registry pattern, and open gaps.
2. For department-specific work, read that department's `{DEPT}_OS.md` (linked from the Department Index in `GLOBAL_OS.md` §4).
3. Follow the pointers in those files to workflows, agents, skills, and raw source material as needed — do not read the raw draft archives directly without going through a department's `{DEPT}_OS.md` first.
4. On completing meaningful work, update the relevant department's Decision Log / Changelog per the pattern described in `GLOBAL_OS.md` §10.
5. If this project later defines Claude Code skills/agents under `.claude/`, they should reference department OS files rather than re-stating their content.

## Constraints

- Do not duplicate content here. If it needs to be said, it belongs in `GLOBAL_OS.md` or a department OS file.
- Do not invent agency-specific facts (numbers, client names, pricing, legal terms) when source material is missing — flag the gap instead.
- See [`AGENTS.md`](AGENTS.md) for the platform-neutral version of this same entry point, used by non-Claude agent platforms.
