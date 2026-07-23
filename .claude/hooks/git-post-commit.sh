#!/bin/sh
# Auto-push after every commit (manual OR made by auto-commit.ps1).
#
# This is the TRACKED source of truth. The live hook is a copy at
# .git/hooks/post-commit (git hooks are not version-controlled). Re-install with:
#   cp .claude/hooks/git-post-commit.sh .git/hooks/post-commit && chmod +x .git/hooks/post-commit
#
# Non-fatal by design: a push failure (e.g. offline) never blocks the commit.

root="$(git rev-parse --show-toplevel 2>/dev/null)"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
ts="$(date '+%Y-%m-%d %H:%M:%S')"
log="$root/.claude/hooks/auto-sync.log"

if git push origin "$branch" >/dev/null 2>&1; then
  echo "[$ts] POST-COMMIT push ok: origin/$branch" >> "$log"
else
  echo "[$ts] POST-COMMIT push failed (will retry on next auto-sync): origin/$branch" >> "$log"
fi
exit 0
