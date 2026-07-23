# Auto-sync hooks

Keeps this repository continuously committed and pushed to `origin`, so no work is
ever left only on disk.

## What runs

| Trigger | Mechanism | What it does |
|---|---|---|
| End of every Claude Code turn | **`Stop` hook** → `auto-commit.ps1` | Stages + commits any changes, then pushes if the branch is ahead of `origin`. |
| Any `git commit` (manual or automated) | **git `post-commit` hook** → `git-post-commit.sh` | Pushes the new commit to `origin` immediately. |

The two cooperate: when `auto-commit.ps1` commits, `post-commit` pushes it, so the
script's own push step becomes a no-op. If either path fails (e.g. offline), the other
retries and the failure is logged.

## Files

- `auto-commit.ps1` — the commit+push script (invoked by the Stop hook).
- `git-post-commit.sh` — tracked source for the git post-commit hook. The live copy
  lives at `.git/hooks/post-commit` (git hooks aren't version-controlled).
- `auto-sync.log` — append-only audit log (git-ignored).
- The Stop hook itself is registered in `.claude/settings.local.json` (machine-local,
  because pushing depends on this machine's git credentials).

## Re-installing after a fresh clone

```sh
cp .claude/hooks/git-post-commit.sh .git/hooks/post-commit
chmod +x .git/hooks/post-commit
```

Then add the Stop hook to `.claude/settings.local.json` (see that file, or the
`hooks.Stop` block, for the exact command).

## Status

- Installed and verified 2026-07-23 (post-commit push + Stop-hook commit/push paths both tested).

## Notes

- Auto-sync commits are labelled `chore(auto-sync): <timestamp> [N changed]` so they're
  easy to distinguish from authored commits in the history.
- To pause auto-sync, remove the `hooks.Stop` block from `.claude/settings.local.json`
  and delete `.git/hooks/post-commit`.
