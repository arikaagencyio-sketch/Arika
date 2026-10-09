# -*- coding: utf-8 -*-
"""
Tests for the proposed Creative Pipeline v2 decision table, and for the prompt
and test protocol that describe it.

    python -m unittest discover -s 16_Automation/routines/creative-pipeline -p "test_*.py"

Synthetic data only (`fx-`). Nothing touches Notion, the routine or any _memory stream.
"""
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import disposition as d  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


def prompt_block():
    text = read("prompt-v2-proposed.md")
    return re.search(r"```text\n(.*?)```", text, re.S).group(1)


def page(**over):
    p = {"Surface": "LinkedIn - Company Page", "Editorial DRAGON": "Complete", "Strategic DRAGON": "Complete"}
    p.update(over)
    return p


def ctx(version=2, comments=(), comments_readable=True, brief_readable=True, **rels):
    relations = {
        "opportunity": {"linked": True, "readable": True, "page": page()},
        "translation": {"linked": True, "readable": True, "page": page()},
        "narrative_position": {"linked": True, "readable": True, "page": {}},
        "campaign": {"linked": False},
    }
    relations.update(rels)
    return {"brief_id": "fx-brief-1", "brief": {"readable": brief_readable, "version": version},
            "relations": relations, "comments": {"readable": comments_readable, "texts": list(comments)}}


class Completed(unittest.TestCase):
    def test_ready_brief_without_campaign_completes(self):
        r = d.disposition(ctx())
        self.assertEqual((r["outcome"], r["post"]), ("completed", "storyboard"))
        self.assertEqual(r["marker"], "[creative-pipeline v2 | completed | brief=fx-brief-1 | rev=2]")

    def test_notion_float_version_is_the_same_revision(self):
        self.assertEqual(d.disposition(ctx(version=2.0))["marker"], d.completed_marker("fx-brief-1", 2))

    def test_linked_readable_campaign_is_used(self):
        r = d.disposition(ctx(campaign={"linked": True, "readable": True, "page": {}}))
        self.assertEqual(r["outcome"], "completed")


class Blocked(unittest.TestCase):
    def assertBlocked(self, c, reason):
        r = d.disposition(c)
        self.assertEqual(r["outcome"], "blocked", r)
        self.assertIn(reason, r["reasons"])
        self.assertNotIn("| completed |", r["marker"] or "")
        return r

    def test_missing_required_context_blocks(self):
        for name in ("opportunity", "translation", "narrative_position"):
            self.assertBlocked(ctx(**{name: {"linked": False}}), "MISSING_" + name.upper())

    def test_invalid_revisions_block_and_never_default(self):
        for bad in (None, 0, -1, 1.5, "1", True):
            r = self.assertBlocked(ctx(version=bad), "REV_INVALID")
            self.assertIn("rev=invalid", r["marker"])

    def test_unassigned_surface_blocks(self):
        for s in ("Not yet assigned", None, ""):
            self.assertBlocked(ctx(translation={"linked": True, "readable": True, "page": page(Surface=s)}),
                               "SURFACE_UNASSIGNED")

    def test_unknown_surface_blocks(self):
        for s in ("Company Page", "linkedin_company_page", "LinkedIn — Company Page"):
            self.assertBlocked(ctx(translation={"linked": True, "readable": True, "page": page(Surface=s)}),
                               "SURFACE_UNKNOWN")

    def test_unrun_dragon_passes_block(self):
        self.assertBlocked(ctx(opportunity={"linked": True, "readable": True,
                                            "page": page(**{"Strategic DRAGON": "Not yet run"})}),
                           "STRATEGIC_DRAGON_NOT_RUN")
        self.assertBlocked(ctx(translation={"linked": True, "readable": True,
                                            "page": page(**{"Editorial DRAGON": None})}),
                           "EDITORIAL_DRAGON_NOT_RUN")

    def test_blocked_notice_is_posted_once_per_reason_set(self):
        first = d.disposition(ctx(version=None))
        self.assertEqual(first["post"], "blocked_notice")
        again = d.disposition(ctx(version=None, comments=[first["marker"] + "\nREV_INVALID: ..."]))
        self.assertEqual((again["outcome"], again["post"]), ("blocked", None))

    def test_blocked_marker_never_counts_as_completed(self):
        blocked = d.disposition(ctx(version=None))["marker"]
        fixed = d.disposition(ctx(version=2, comments=[blocked]))
        self.assertEqual(fixed["outcome"], "completed")


class Failed(unittest.TestCase):
    def test_unreadable_required_or_optional_context_fails_without_posting(self):
        for name in ("opportunity", "translation", "narrative_position", "campaign"):
            r = d.disposition(ctx(**{name: {"linked": True, "readable": False}}))
            self.assertEqual((r["outcome"], r["post"], r["marker"]), ("failed", None, None), name)
            self.assertIn("UNREADABLE_" + name.upper(), r["reasons"])

    def test_unreadable_comments_fail_even_when_blocked(self):
        for c in (ctx(comments_readable=False), ctx(version=None, comments_readable=False)):
            r = d.disposition(c)
            self.assertEqual((r["outcome"], r["post"]), ("failed", None))

    def test_unreadable_brief_fails(self):
        self.assertEqual(d.disposition(ctx(brief_readable=False))["outcome"], "failed")

    def test_retry_after_transient_failure_completes(self):
        down = d.disposition(ctx(translation={"linked": True, "readable": False}))
        self.assertEqual(down["outcome"], "failed")
        self.assertEqual(d.disposition(ctx())["outcome"], "completed")

    def test_unverified_post_is_failed_and_retryable(self):
        marker = d.completed_marker("fx-brief-1", 2)
        self.assertEqual(d.after_post(marker, {"readable": True, "texts": []}), "failed")
        self.assertEqual(d.after_post(marker, {"readable": False}), "failed")
        self.assertEqual(d.after_post(marker, {"readable": True, "texts": [marker + "\n..."]}), "completed")


class Duplicates(unittest.TestCase):
    def test_same_revision_is_skipped(self):
        marker = d.completed_marker("fx-brief-1", 2)
        r = d.disposition(ctx(comments=[marker + "\nstoryboard ..."]))
        self.assertEqual((r["outcome"], r["post"]), ("skipped_duplicate", None))

    def test_new_revision_is_processed(self):
        r = d.disposition(ctx(version=3, comments=[d.completed_marker("fx-brief-1", 2)]))
        self.assertEqual(r["outcome"], "completed")


class PromptMatchesTable(unittest.TestCase):
    """The live routine follows prose; these keep the prose and the table aligned."""

    def test_markers_in_prompt_match_code(self):
        block = prompt_block()
        self.assertIn(d.COMPLETED.format(brief="<brief page id>", rev="<REV>"), block)
        self.assertIn(d.BLOCKED.format(brief="<brief page id>", rev="<REV or invalid>", reasons="<CODES>"), block)

    def test_prompt_lists_exactly_the_assigned_surfaces_from_the_vocabulary(self):
        block = prompt_block()
        line = next(l for l in block.splitlines() if "Surface must be exactly one of" in l)
        self.assertEqual(re.findall(r'"([^"]+)"', line.split("exactly one of")[1].split(".")[0]), d.ASSIGNED_SURFACES)

    def test_prompt_names_every_reason_code_the_table_can_return(self):
        block = prompt_block()
        for code in ("REV_INVALID", "MISSING_OPPORTUNITY", "MISSING_TRANSLATION", "MISSING_NARRATIVE_POSITION",
                     "SURFACE_UNASSIGNED", "SURFACE_UNKNOWN", "STRATEGIC_DRAGON_NOT_RUN", "EDITORIAL_DRAGON_NOT_RUN",
                     "UNREADABLE_BRIEF", "UNREADABLE_OPPORTUNITY", "UNREADABLE_TRANSLATION",
                     "UNREADABLE_NARRATIVE_POSITION", "UNREADABLE_CAMPAIGN", "COMMENTS_UNREADABLE", "POST_UNVERIFIED"):
            self.assertIn(code, block)

    def test_prompt_never_defaults_the_revision(self):
        block = prompt_block()
        self.assertNotIn('"none" if Version is empty', block)
        self.assertIn("Never substitute a default revision", block)

    def test_campaign_is_optional_in_the_prompt(self):
        self.assertIn("Campaign (optional)", prompt_block())

    def test_prompt_requests_spend_approval_not_generation(self):
        block = prompt_block()
        self.assertIn("SPEND APPROVAL", block)
        self.assertIn("Call no generation tool", block)


class ProtocolAmended(unittest.TestCase):
    def section(self, n):
        text = read("CHANGE_PROPOSAL.md")
        return re.search(r"## %d\..*?(?=\n## %d\.)" % (n, n + 1), text, re.S).group(0)

    def test_readiness_checkpoint_precedes_the_human_flip(self):
        s = self.section(5)
        self.assertLess(s.index("T2a"), s.index("T2b"))
        self.assertIn("content_write_gate.py readiness", s)

    def test_revision_is_captured_not_hard_coded(self):
        s = self.section(5)
        self.assertNotRegex(s, r"rev=\d")
        self.assertIn("REV = the brief's live Version", s)

    def test_scheduled_duplicate_concurrency_and_retirement_retained(self):
        text = read("CHANGE_PROPOSAL.md")
        self.assertIn("Forced-run proof is not scheduled-run proof", text)
        self.assertIn("skipped-duplicate 1", text)
        self.assertIn("never force a run between :05 and :10", text)
        self.assertIn("separate** owner approval", text)


if __name__ == "__main__":
    unittest.main()
