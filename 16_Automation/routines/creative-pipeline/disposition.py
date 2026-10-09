# -*- coding: utf-8 -*-
"""
Creative Pipeline routine, prompt v2 (PROPOSED, not applied): the per-brief
decision table as code.

    python -m unittest discover -s 16_Automation/routines/creative-pipeline -p "test_*.py"

The live routine is an LLM following prompt-v2-proposed.md, so this module does
not run in production. It is the same decision table in a form that can be
tested, and test_disposition.py checks the prompt text against it so the two
cannot drift apart silently. The Surface and DRAGON vocabularies and the
revision rule come from Content's contract (04_Content/contracts), so there is
one definition of each. Pure: no Notion, no network, no file writes.

Outcomes (exactly one per brief per run):
    completed          post the storyboard comment; its first line is the COMPLETED marker
    skipped_duplicate  a COMPLETED marker for this revision already exists
    blocked            the brief's own data is not ready; post one BLOCKED notice at most
    failed             something could not be read or written; post nothing, retry next run
Only `completed` ever writes the COMPLETED marker.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "04_Content", "contracts"))
import content_write_gate as gate  # noqa: E402

PROMPT_VERSION = "creative-pipeline v2"
COMPLETED = "[creative-pipeline v2 | completed | brief={brief} | rev={rev}]"
BLOCKED = "[creative-pipeline v2 | blocked | brief={brief} | rev={rev} | reasons={reasons}]"
REQUIRED = ("opportunity", "translation", "narrative_position")
OPTIONAL = ("campaign",)

_CONTRACT = gate.load_contract()
ASSIGNED_SURFACES = [o["notion"] for o in _CONTRACT["vocabularies"]["surface"]["options"] if o["assigned"]]
UNASSIGNED_SURFACES = [o["notion"] for o in _CONTRACT["vocabularies"]["surface"]["options"] if not o["assigned"]]
DRAGON_DONE = list(_CONTRACT["vocabularies"]["dragon_status"]["done"])


def completed_marker(brief_id, rev):
    return COMPLETED.format(brief=brief_id, rev=rev)


def blocked_marker(brief_id, rev, reasons):
    return BLOCKED.format(brief=brief_id, rev=rev if rev is not None else "invalid",
                          reasons=",".join(sorted(reasons)))


def disposition(ctx):
    """ctx = {
        "brief_id": str,
        "brief": {"readable": bool, "version": <raw Version>},
        "relations": {name: {"linked": bool, "readable": bool, "page": {...}}},
        "comments": {"readable": bool, "texts": [str]},
    }
    Returns {"outcome", "reasons", "post": None | "storyboard" | "blocked_notice", "marker"}."""
    bid = ctx["brief_id"]
    if not (ctx.get("brief") or {}).get("readable"):
        return _result("failed", ["UNREADABLE_BRIEF"])
    rels = ctx.get("relations") or {}
    blocked, failed = [], []
    rev = gate.revision_value(ctx["brief"].get("version"))
    if rev is None:
        blocked.append("REV_INVALID")
    for name in REQUIRED + OPTIONAL:
        r = rels.get(name) or {"linked": False}
        if not r.get("linked"):
            if name in REQUIRED:
                blocked.append("MISSING_" + name.upper())
            continue
        if not r.get("readable"):
            failed.append("UNREADABLE_" + name.upper())
    if failed:
        return _result("failed", failed)
    tr = ((rels.get("translation") or {}).get("page") or {}) if "MISSING_TRANSLATION" not in blocked else None
    opp = ((rels.get("opportunity") or {}).get("page") or {}) if "MISSING_OPPORTUNITY" not in blocked else None
    if tr is not None:
        surface = tr.get("Surface")
        if surface in ASSIGNED_SURFACES:
            pass
        elif surface in UNASSIGNED_SURFACES or surface in (None, ""):
            blocked.append("SURFACE_UNASSIGNED")
        else:
            blocked.append("SURFACE_UNKNOWN")
        if tr.get("Editorial DRAGON") not in DRAGON_DONE:
            blocked.append("EDITORIAL_DRAGON_NOT_RUN")
    if opp is not None and opp.get("Strategic DRAGON") not in DRAGON_DONE:
        blocked.append("STRATEGIC_DRAGON_NOT_RUN")
    comments = ctx.get("comments") or {}
    if not comments.get("readable"):
        return _result("failed", ["COMMENTS_UNREADABLE"])
    texts = comments.get("texts") or []
    if blocked:
        marker = blocked_marker(bid, rev, blocked)
        already = any(marker in t for t in texts)
        return _result("blocked", sorted(blocked), post=None if already else "blocked_notice", marker=marker)
    marker = completed_marker(bid, rev)
    if any(marker in t for t in texts):
        return _result("skipped_duplicate", [], marker=marker)
    return _result("completed", [], post="storyboard", marker=marker)


def after_post(marker, comments_after):
    """Read-after-write. A post that cannot be seen is FAILED; the next run's
    duplicate check finds it if it did land, and retries if it did not."""
    if not (comments_after or {}).get("readable"):
        return "failed"
    return "completed" if any(marker in t for t in comments_after.get("texts") or []) else "failed"


def _result(outcome, reasons, post=None, marker=None):
    return {"outcome": outcome, "reasons": reasons, "post": post, "marker": marker}
