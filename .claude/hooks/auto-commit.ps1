# Auto-sync: stage + commit any working-tree changes, then push to origin.
#
# Wired to the Claude Code "Stop" hook (see .claude/settings.local.json), so it
# runs at the end of every turn. Also safe to run by hand:
#   powershell -NoProfile -ExecutionPolicy Bypass -File .claude/hooks/auto-commit.ps1
#
# Design notes:
#   * Never throws and always exits 0 - a failing Stop hook must not disrupt the session.
#   * Commits only when the tree is dirty; pushes whenever the branch is ahead of upstream
#     (so it also flushes manual commits that were never pushed).
#   * All actions and errors are appended to auto-sync.log (git-ignored) for auditing.
#   * On push failure it emits a systemMessage so the user is told the work is only local.

$ErrorActionPreference = 'Continue'

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$log  = Join-Path $PSScriptRoot 'auto-sync.log'

function Write-Log($msg) {
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Add-Content -Path $log -Value "[$ts] $msg" -Encoding utf8
}

# Guard: only operate inside a real git work tree.
$inside = (& git -C $repo rev-parse --is-inside-work-tree 2>$null)
if ($LASTEXITCODE -ne 0 -or "$inside".Trim() -ne 'true') {
    Write-Log "SKIP: not a git work tree ($repo)"
    exit 0
}

$didCommit = $false

# 1) Commit pending changes, if any.
$status = & git -C $repo status --porcelain
if ($status) {
    $count = ($status | Measure-Object -Line).Lines
    & git -C $repo add -A 2>&1 | Out-Null
    $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    $msg = "chore(auto-sync): $stamp [$count changed]"
    $commitOut = & git -C $repo commit -m $msg 2>&1
    if ($LASTEXITCODE -eq 0) {
        $didCommit = $true
        Write-Log "COMMIT ok: $msg"
    } else {
        Write-Log "COMMIT failed: $commitOut"
    }
} else {
    Write-Log "clean tree - nothing to commit"
}

# 2) Push if the branch is ahead of (or has no) upstream.
#    (If a git post-commit hook already pushed, ahead is now 0 and this is a no-op.)
$branch = (& git -C $repo rev-parse --abbrev-ref HEAD).Trim()
$pushNeeded = $false
$pushArgs = $null

$null = (& git -C $repo rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>$null)
if ($LASTEXITCODE -ne 0) {
    $pushNeeded = $true
    $pushArgs = @('-C', $repo, 'push', '-u', 'origin', $branch)
} else {
    $ahead = (& git -C $repo rev-list --count '@{u}..HEAD' 2>$null)
    if ("$ahead".Trim() -and [int]("$ahead".Trim()) -gt 0) {
        $pushNeeded = $true
        $pushArgs = @('-C', $repo, 'push', 'origin', $branch)
    }
}

if ($pushNeeded) {
    $pushOut = & git @pushArgs 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Log "PUSH ok: origin/$branch"
    } else {
        Write-Log "PUSH failed: $pushOut"
        $obj = @{ systemMessage = "Auto-sync: changes are committed locally but the PUSH to origin/$branch FAILED. Run 'git push' when back online. Details: " + (($pushOut | Out-String).Trim()) }
        Write-Output ($obj | ConvertTo-Json -Compress)
        exit 0
    }
} else {
    Write-Log "up to date with upstream - no push"
}

if ($didCommit) { Write-Output '{"suppressOutput": true}' }
exit 0
