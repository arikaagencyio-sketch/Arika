# -*- coding: utf-8 -*-
"""
Tests for the Content (04) write gate.

    python -m unittest discover -s 04_Content/contracts -p "test_*.py"

Every record here is synthetic: `fx-` tokens, or Notion-shaped page IDs whose
bodies are zeros (b1… briefs, c1… translations, d1… platforms, e1… offers).
Nothing is read from or written to Notion, the runtime, or any _memory stream;
ProductionMemoryUntouched checks that last point on every run.
"""
import copy
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_write_gate as g  # noqa: E402

CONTRACT = g.load_contract()
MEMORY_DIR = os.path.join(g.REPO, "04_Content", "_memory")
AGENTS_DIR = os.path.join(g.REPO, ".claude", "agents")

# Live field counts read from the Notion schemas on 2026-10-09; DB7 re-read on
# 2026-10-10 before and after the storage unit added six properties (49 -> 55).
# If a field is added in Notion, the contract must gain an owner for it in the
# same change.
LIVE_FIELD_COUNTS = {"DB1": 34, "DB2": 44, "DB3": 51, "DB4": 45,
                     "DB5": 54, "DB6": 52, "DB7": 55, "DB8": 32}

# Option names and IDs as returned by a read-only notion-fetch of DB6 and DB7 on
# 2026-10-09 (correction unit). Pinned here so a rename in the contract, or a
# contract edit that drifts from Notion, fails a test.
LIVE_SURFACE = {"LinkedIn - Founder profile": "016f7eea-b42e-4485-8b26-120eebbd5e24",
                "LinkedIn - Company Page": "18754c3f-6008-4447-a13e-022a11119d2e",
                "Single-identity channel": "e06665b3-559b-497c-8c52-918b9ccf7443",
                "Not yet assigned": "7ceba672-abc1-44eb-b4ec-8db1eda6b23d"}
LIVE_AUDIENCE = {"CEO": "626a011a-86e7-4bce-8a4b-dcf4fd469388",
                 "CMO": "22499767-45ee-4674-8469-0f78686fc8a2",
                 "Sales Leader": "082ff05c-3ee2-4687-a780-6db4212d63ed",
                 "COO": "3e4c73f8-f8af-4e62-a664-88b37759254c",
                 "Investor": "9e3e21e5-85e0-4271-9706-b50209e9b936",
                 "Founder": "ebd7e1a1-14db-4c37-8ff8-4f166457b3d4",
                 "General Manager / Owner": "544696bf-740c-421c-9737-522b6b15de9b",
                 "Revenue / Reservations Manager": "490c08ad-6d9a-4389-b06a-a85fa4f57e12"}
LIVE_PUBLISHING_STATUS = {"Not started": "e552621d-0910-4dd1-8853-fcee1b0d1536",
                          "In progress": "5d53abab-a8ad-433e-bba9-390b4c493c3f",
                          "Ready for Design": "2502a443-7515-4272-ac7d-187d47728d97",
                          "Done": "e34ae6e7-4240-4d5c-8699-722b4eb4eb95"}

FOUNDER, PAGE, CHANNEL, UNASSIGNED = list(LIVE_SURFACE)


# --------------------------------------------------------------------------- fixtures

def lookup(db, records=(), status="complete"):
    return {"lookups": {db: {"status": status, "checked_at": "2026-10-09T10:00:00Z", "records": list(records)}}}


def opportunity(strategic="Complete"):
    return {"id": "fx-opp-001", "strategic_dragon": strategic}


def translation(surface=FOUNDER, editorial="Complete", platform="LinkedIn", family="nar-fx-belief", fmt="Carousel"):
    return {"id": "fx-tr-001", "family_id": family, "surface": surface,
            "editorial_dragon": editorial, "platform": platform, "format": fmt}


def verified_fact(tier="T3 Commercial-intel"):
    return {"text": "OTA effective commission runs 15-30% against about 9% direct",
            "kind": "fact",
            "sources": [{"id": "fx-sector-finding-ota", "tier": tier, "verified_at": "2026-08-19"}]}


def brief(**over):
    p = {
        "db": "DB7", "mode": "CREATE", "actor": "C04",
        "fields": {"Title": "fx brief", "Caption": "I keep seeing the same pattern.",
                   "Script": "S1 ...", "Publishing Status": "In progress", "Version": 1},
        "links": {"opportunity": opportunity(), "translation": translation(),
                  "narrative_position_ids": ["nar-fx-belief"]},
        "claims": [verified_fact(), {"text": "Most stacks are under-decided", "kind": "opinion"}],
        "key_values": {"Translation": "fx-tr-001"},
    }
    p.update(over)
    return p


def prior_brief(**over):
    b = {"Title": "fx brief", "Caption": "Original caption.", "Script": "S1 ...",
         "Visual Direction": "Navy, one chart per frame", "Canva Instructions": "1080x1350, 6 frames",
         "Version": 2.0, "Confidence": "Working Hypothesis"}
    b.update(over)
    return b


def translation_create(audience="General Manager / Owner", surface=PAGE, **over):
    key = {"Translation Family ID": "nar-a", "Platform": "LinkedIn", "Audience Role": audience,
           "Surface": surface, "Format": "Carousel"}
    p = {"db": "DB6", "mode": "CREATE", "actor": "C03",
         "fields": {"Translation": "fx", "Translation Family ID": "nar-a", "Surface": surface,
                    "Audience Role": audience, "Format": "Carousel", "Editorial DRAGON": "Not yet run"},
         "links": {"opportunity": opportunity(), "platform": "LinkedIn", "source_truth": {"position_id": "nar-a"}},
         "key_values": key}
    p.update(over)
    return p, key


def readiness_ctx(**over):
    ctx = {"brief": {"id": BRIEF_ID, "version": 2, "caption": "Copy", "script": "S1 ...",
                     "visual_direction": "Navy, one chart per frame", "canva_instructions": "1080x1350, 6 frames"},
           "links": {"opportunity": "fx-opp-001", "translation": "fx-tr-001", "narrative_position_ids": ["nar-fx-belief"]},
           "opportunity": opportunity(),
           "translation": translation(),
           "g1": g1()}
    ctx.update(over)
    return ctx


BRIEF_ID, OTHER_BRIEF = "b1000000000040008000000000000001", "b1000000000040008000000000000002"
TRANSLATION_ID = "c1000000000040008000000000000001"
PLATFORM_ID, OTHER_PLATFORM_ID = "d1000000000040008000000000000001", "d1000000000040008000000000000002"
OFFER_ID = "e1000000000040008000000000000001"
SESSION, CHECKED_AT, READ_AT = "fx-session-1", "2026-10-10T12:00:00Z", "2026-10-10T11:58:00Z"
OWNER = "Mary Thuo"


def fresh_ctx(brief_id=BRIEF_ID, version=2, caption="Final copy", script="S1 ...", vd="Navy", ci="6 frames",
              platform=("LinkedIn",), translation_ids=(TRANSLATION_ID,), translation_page=TRANSLATION_ID,
              surface=FOUNDER, audience="Founder", fmt="Carousel", platform_ids=(PLATFORM_ID,),
              offer_ids=(), offer_status="Active", session=SESSION, checked_at=CHECKED_AT, read_at=READ_AT,
              translation_status="complete"):
    """A synthetic FRESH read-back: the brief, its one translation and its offers, one session."""
    def part(page_id, properties, status="complete"):
        return {"status": status, "session": session, "read_at": read_at, "page_id": page_id, "properties": properties}
    return {"session": session, "checked_at": checked_at,
            "brief": part(brief_id, {"Script": script, "Caption": caption, "Visual Direction": vd,
                                     "Canva Instructions": ci, "Engagement Follow-up": "", "Evidence": "",
                                     "Platform": list(platform), "Translation": list(translation_ids),
                                     "Offer": list(offer_ids), "Version": version}),
            "translation": part(translation_page, {"Surface": surface, "Audience Role": audience, "Format": fmt,
                                                   "Platform": list(platform_ids)}, status=translation_status),
            "offers": [part(o, {"Offer Status": offer_status}) for o in offer_ids]}


def evidence(fresh, assets=()):
    v, ev = g.build_evidence(fresh, list(assets), CONTRACT)
    assert ev is not None, v
    return ev


def g1(path="design", **over):
    r = {"decision": "passed", "path": path, "by": "human:Mary Thuo", "at": "2026-10-20",
         "brief_id": BRIEF_ID, "revision": 2}
    r.update(over)
    return r


def asset(asset_id="fx-asset-1", version=1, brief_id=BRIEF_ID, brief_revision=2, rights="owned"):
    return {"asset_id": asset_id, "version": version, "rights": rights,
            "provenance": {"brief_id": brief_id, "brief_revision": brief_revision}}


def submission_ctx(fmt="Carousel", artifacts="default", **over):
    b = {"id": BRIEF_ID, "version": 2, "caption": "Final copy", "script": "S1 ...",
         "visual_direction": "Navy", "canva_instructions": "6 frames"}
    text_only = fmt in ("Text post", "Newsletter issue")
    if text_only:
        b.update(visual_direction="", canva_instructions="text-only")
    if artifacts == "default":
        artifacts = [] if text_only else [asset()]
    ctx = {"brief": b, "revision": 2, "opportunity": opportunity(),
           "translation": translation(fmt=fmt, surface=CHANNEL if fmt == "Newsletter issue" else FOUNDER,
                                      platform="Newsletter" if fmt == "Newsletter issue" else "LinkedIn"),
           "g1": g1(path="text_only" if text_only else "design"),
           "claim_review": {"verdict": "pass", "brief_id": BRIEF_ID, "revision": 2}, "artifacts": artifacts}
    ctx.update(over)
    return ctx


def generation_ctx(**over):
    ctx = {"brief": {"id": BRIEF_ID, "version": 2, "publishing_status": "Ready for Design"},
           "storyboard": {"brief_id": BRIEF_ID, "revision": 2},
           "spend_approval": {"by": "human:Mary Thuo", "at": "2026-10-21", "brief_id": BRIEF_ID, "revision": 2,
                              "scope": "6 carousel frames, image model only"}}
    ctx.update(over)
    return ctx


def fresh_for_submission(sub, **over):
    """The fresh read-back that matches a submission packet, unless overridden."""
    b, tr = sub.get("brief") or {}, sub.get("translation") or {}
    entry = g.resolve_surface(CONTRACT, tr.get("surface"))
    kw = dict(brief_id=b.get("id"), version=b.get("version"), caption=b.get("caption") or "",
              script=b.get("script") or "", vd=b.get("visual_direction") or "", ci=b.get("canva_instructions") or "",
              surface=entry["notion"] if entry else tr.get("surface"), fmt=tr.get("format"))
    kw.update(over)
    return fresh_ctx(**kw)


def c06_submit(sub=None, target=BRIEF_ID, prior="default", fresh="default", fields="computed"):
    """A C06 'Submitted for review' write, with the read-back and gate-computed evidence."""
    sub = submission_ctx() if sub is None else sub
    fresh = fresh_for_submission(sub) if fresh == "default" else fresh
    written = {"G2 Decision": "Submitted for review"}
    if fields == "computed":
        _, ev = g.build_evidence(fresh, sub.get("artifacts") or [], CONTRACT)
        if ev is not None:
            written.update({"G2 Packet Manifest": ev["manifest_text"], "G2 Submitted Fingerprint": ev["fingerprint"]})
    elif isinstance(fields, dict):
        written.update(fields)
    p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": written, "g2_submission": sub}
    if target is not None:
        p["target"] = target
    prior = {"id": BRIEF_ID, "Version": 2.0} if prior == "default" else prior
    state = {"fresh": fresh}
    if prior:
        state["prior"] = prior
    return g.validate_write(p, CONTRACT, state=state)


def approval(surface=FOUNDER, fmt="Text post", vd="", ci="", assets=(), offer_ids=(), offer_status="Active",
             audience="Founder", caption="Final copy", script="", **brief_over):
    """(stored DB7 approval fields, the fresh read that produced them). Evidence is
    computed by the gate itself, exactly as C06 would write it at submission."""
    fresh = fresh_ctx(surface=surface, fmt=fmt, vd=vd, ci=ci, offer_ids=offer_ids, offer_status=offer_status,
                      audience=audience, caption=caption, script=script)
    ev = evidence(fresh, assets)
    b = {"id": BRIEF_ID, "version": 2, "g2_decision": "Approved", "g2_approved_revision": 2,
         "g2_reviewer": OWNER, "g2_decided_at": "2026-10-20",
         "g2_packet_manifest": ev["manifest_text"], "g2_submitted_fingerprint": ev["fingerprint"]}
    b.update(brief_over)
    return b, fresh


def design_approval(assets=None, **over):
    return approval(fmt="Carousel", vd="Navy", ci="6 frames", assets=[asset()] if assets is None else assets, **over)


def publication(**over):
    r = {"brief_id": BRIEF_ID, "revision": 2, "surface": FOUNDER,
         "native_post_url": "https://www.linkedin.com/feed/update/urn:li:activity:0000000000000000000/",
         "published_at": "2026-10-21", "publisher": "human:Mary Thuo"}
    r.update(over)
    return r


def publish(appr=None, fresh="default", **record_over):
    brief_fields, approved_fresh = approval() if appr is None else appr
    return g.validate_publication(publication(**record_over), brief_fields, CONTRACT,
                                  approved_fresh if fresh == "default" else fresh)


def with_manifest(appr, mutate):
    """The same approval with its stored manifest edited by `mutate` (re-serialised
    canonically), and the stored fingerprint left as it was."""
    brief_fields, fresh = appr
    m = copy.deepcopy(__import__("json").loads(brief_fields["g2_packet_manifest"]))
    mutate(m)
    return dict(brief_fields, g2_packet_manifest=g.canonical_json(m)), fresh


def _memory_snapshot():
    if not os.path.isdir(MEMORY_DIR):
        return None
    return sorted((n, os.path.getsize(os.path.join(MEMORY_DIR, n))) for n in os.listdir(MEMORY_DIR))


_MEMORY_BEFORE = None


def setUpModule():
    global _MEMORY_BEFORE
    _MEMORY_BEFORE = _memory_snapshot()


def tearDownModule():
    after = _memory_snapshot()
    if after != _MEMORY_BEFORE:
        raise AssertionError("tests changed 04_Content/_memory: %r -> %r" % (_MEMORY_BEFORE, after))


# --------------------------------------------------------------------------- contract

class ContractIntegrity(unittest.TestCase):
    def test_contract_passes_its_own_gate(self):
        self.assertEqual(g.check_contract(CONTRACT), [])

    def test_field_counts_match_live_schemas(self):
        counts = {db["db_id"]: len(db["fields"]) for db in CONTRACT["databases"]}
        self.assertEqual(counts, LIVE_FIELD_COUNTS)

    def test_every_field_has_exactly_one_writer(self):
        for db in CONTRACT["databases"]:
            for f in db["fields"]:
                self.assertIsInstance(f.get("writer"), str, "%s.%s" % (db["db_id"], f["name"]))

    def test_trigger_properties_are_byte_identical(self):
        tc = CONTRACT["trigger_contract"]
        self.assertEqual(sorted(tc["properties"]),
                         sorted(["Title", "Script", "Caption", "Visual Direction",
                                 "Canva Instructions", "Publishing Status"]))
        self.assertEqual(tc["publishing_status_options"],
                         ["Not started", "In progress", "Ready for Design", "Done"])
        self.assertEqual(tc["publishing_status_option_ids"], LIVE_PUBLISHING_STATUS)

    def test_content_never_writes_offers(self):
        db8 = next(d for d in CONTRACT["databases"] if d["db_id"] == "DB8")
        for f in db8["fields"]:
            self.assertFalse(f["writer"].startswith("C"), "Content skill writes DB8.%s" % f["name"])

    def test_gate_catches_a_second_writer(self):
        bad = copy.deepcopy(CONTRACT)
        db7 = next(d for d in bad["databases"] if d["db_id"] == "DB7")
        db7["fields"].append({"name": "Caption", "type": "text", "writer": "C06"})
        self.assertTrue(any(e.startswith("C5") for e in g.check_contract(bad)))

    def test_gate_catches_a_renamed_trigger_property(self):
        bad = copy.deepcopy(CONTRACT)
        db7 = next(d for d in bad["databases"] if d["db_id"] == "DB7")
        for f in db7["fields"]:
            if f["name"] == "Script":
                f["name"] = "Script Text"
        self.assertTrue(any(e.startswith("C4") for e in g.check_contract(bad)))

    def test_gate_catches_audience_dropped_from_translation_key(self):
        bad = copy.deepcopy(CONTRACT)
        db6 = next(d for d in bad["databases"] if d["db_id"] == "DB6")
        db6["natural_key"].remove("Audience Role")
        self.assertTrue(any(e.startswith("C9") for e in g.check_contract(bad)))

    def test_gate_catches_copy_field_losing_publication_flag(self):
        bad = copy.deepcopy(CONTRACT)
        db7 = next(d for d in bad["databases"] if d["db_id"] == "DB7")
        next(f for f in db7["fields"] if f["name"] == "Caption").pop("publication_affecting")
        self.assertTrue(any(e.startswith("C8") for e in g.check_contract(bad)))


# --------------------------------------------------------------------------- the ten owner scenarios

class FounderContentFromVerifiedSource(unittest.TestCase):
    """Scenario 1."""

    def test_founder_brief_with_dated_tiered_source_passes(self):
        v = g.validate_write(brief(), CONTRACT, state=lookup("DB7"))
        self.assertTrue(v.ok, v)


class PageFrameworkContent(unittest.TestCase):
    """Scenario 2: the Page speaks institutionally."""

    def page_brief(self, surface=PAGE):
        return brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                            "translation": translation(surface=surface)})

    def test_page_framework_without_first_person_passes(self):
        p = self.page_brief()
        p["fields"]["Caption"] = "Every tool encodes a data model, a workflow and an owner assumption."
        p["claims"] = [{"text": "Three checks before any purchase", "kind": "framework"}]
        self.assertTrue(g.validate_write(p, CONTRACT, state=lookup("DB7")).ok)

    def test_page_copy_in_first_person_is_refused(self):
        self.assertIn("R15_PAGE_VOICE", g.validate_write(self.page_brief(), CONTRACT, state=lookup("DB7")).codes)


class HospitalityBrief(unittest.TestCase):
    """Scenario 3: a pilot-sector brief is ordinary data, never a default."""

    def test_hospitality_brief_with_family_and_sector_passes(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-misconception-more-leads"],
                         "translation": translation(family="nar-misconception-more-leads", surface=PAGE)})
        p["fields"]["Caption"] = "Your OTA commission is not 15 percent. It is closer to 25 to 30."
        p["fields"]["Sub-Sector"] = ["fx-subsector-accommodation"]
        v = g.validate_write(p, CONTRACT, state=lookup("DB7"))
        self.assertTrue(v.ok, v)

    def test_family_mismatch_is_refused(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-belief-revenue-is-a-system"],
                         "translation": translation(family="nar-misconception-more-leads")})
        self.assertIn("R06_FAMILY_MISMATCH", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)

    def test_translation_family_must_equal_source_truth(self):
        p, _ = translation_create(surface=UNASSIGNED)
        p["links"]["source_truth"] = {"position_id": "nar-b"}
        self.assertIn("R06_FAMILY_MISMATCH", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_no_sector_is_legal_and_never_defaults_to_hospitality(self):
        p = brief()
        self.assertNotIn("Sub-Sector", p["fields"])
        self.assertTrue(g.validate_write(p, CONTRACT, state=lookup("DB7")).ok)


class MissingEvidence(unittest.TestCase):
    """Scenario 4."""

    def codes(self, claims):
        return g.validate_write(brief(claims=claims), CONTRACT, state=lookup("DB7")).codes

    def test_fact_without_source_is_refused(self):
        self.assertIn("R04_UNEVIDENCED", self.codes([{"text": "Hotels lose 30% to OTAs", "kind": "fact", "sources": []}]))

    def test_fact_resting_only_on_t4_is_refused(self):
        self.assertIn("R05_T4_SOURCE", self.codes([verified_fact(tier="T4 Secondary")]))

    def test_client_outcome_without_proof_is_refused(self):
        self.assertIn("R04_UNPROVEN_OUTCOME", self.codes([{
            "text": "We grew a client 40%", "kind": "outcome",
            "sources": [{"id": "x", "tier": "T1 Primary", "verified_at": "2026-10-01"}],
            "proof_status": "Proof required — named"}]))

    def test_pricing_claim_without_quotable_offer_is_refused(self):
        self.assertIn("R16_NO_QUOTABLE_OFFER", self.codes([{"text": "The audit costs $2,500", "kind": "pricing"}]))

    def test_unclassified_claim_is_refused(self):
        self.assertIn("R04_UNCLASSIFIED_CLAIM", self.codes([{"text": "something", "kind": "vibe"}]))


class DragonPasses(unittest.TestCase):
    """Scenario 5."""

    def opp(self, status, notes=""):
        fields = {"Opportunity": "fx", "Opportunity ID": "fx-opp-9", "Source": "fx source",
                  "Strategic DRAGON": status}
        if notes:
            fields["Strategic DRAGON Notes"] = notes
        return {"db": "DB5", "mode": "CREATE", "actor": "C01", "fields": fields,
                "links": {"source_intelligence": ["fx-finding"]}}

    def run_opp(self, p):
        return g.validate_write(p, CONTRACT, state=lookup("DB5"))

    def test_partial_without_reason_is_refused(self):
        self.assertIn("R07_DRAGON_STATUS", self.run_opp(self.opp("Partial")).codes)

    def test_partial_with_reason_passes(self):
        v = self.run_opp(self.opp("Partial", "R: no economic mechanism yet, research named"))
        self.assertTrue(v.ok, v)

    def test_not_applicable_with_reason_passes(self):
        v = self.run_opp(self.opp("Not applicable", "Terminology note, not a market claim"))
        self.assertTrue(v.ok, v)

    def test_blank_pass_on_create_is_refused(self):
        p = self.opp("Complete")
        del p["fields"]["Strategic DRAGON"]
        self.assertIn("R07_DRAGON_STATUS", self.run_opp(p).codes)

    def test_editorial_before_strategic_is_refused(self):
        p = {"db": "DB6", "mode": "UPDATE", "actor": "C03",
             "fields": {"Editorial DRAGON": "Complete"},
             "links": {"opportunity": opportunity(strategic="Not yet run")}}
        self.assertIn("R08_DRAGON_ORDER", g.validate_write(p, CONTRACT, state={}).codes)

    def test_ready_recommendation_needs_both_passes(self):
        p = brief(mode="UPDATE", recommend_ready_for_design=True, fields={"Title": "fx brief"},
                  links={"opportunity": opportunity(strategic="Not yet run"),
                         "narrative_position_ids": ["nar-fx-belief"], "translation": translation()})
        self.assertIn("R08_DRAGON_ORDER", g.validate_write(p, CONTRACT, state={}).codes)


class G2Failure(unittest.TestCase):
    """Scenario 6: a rejected or changes-requested brief cannot be published, and no skill can approve."""

    def test_rejected_brief_cannot_be_published(self):
        v = publish(approval(g2_decision="Rejected"))
        self.assertIn("R11_APPROVAL_MISSING", v.codes)

    def test_skill_cannot_set_approved(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {"G2 Decision": "Approved"}}
        self.assertIn("R01_HUMAN_ONLY", g.validate_write(p, CONTRACT, state={}).codes)

    def test_skill_cannot_write_reviewer_or_date(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C06",
             "fields": {"G2 Reviewer": "Mary Thuo", "G2 Decided At": "2026-10-20"}}
        self.assertEqual(g.validate_write(p, CONTRACT, state={}).codes.count("R01_HUMAN_ONLY"), 2)

    def test_skill_may_submit_a_finished_artifact_for_review(self):
        v = c06_submit()
        self.assertTrue(v.ok, v)


class MissingApprovalRefusal(unittest.TestCase):
    """Scenario 7."""

    def test_submitted_is_not_approved(self):
        v = publish(approval(g2_decision="Submitted for review"))
        self.assertIn("R11_APPROVAL_MISSING", v.codes)

    def test_approval_for_an_older_revision_is_refused(self):
        v = publish(approval(version=3, g2_approved_revision=2), revision=3)
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_approval_without_reviewer_is_refused(self):
        v = publish(approval(g2_reviewer=""))
        self.assertIn("R11_APPROVAL_MISSING", v.codes)

    def test_skill_cannot_flip_ready_for_design(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C04", "fields": {"Publishing Status": "Ready for Design"}}
        self.assertIn("R01_HUMAN_ONLY", g.validate_write(p, CONTRACT, state={}).codes)

    def test_skill_cannot_touch_presence_packet_state(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {"Packet State": "approved"}}
        self.assertIn("R18_FOREIGN_FIELD", g.validate_write(p, CONTRACT, state={}).codes)


class DuplicateHandling(unittest.TestCase):
    """Scenario 8."""

    def test_second_brief_for_same_translation_is_refused(self):
        state = lookup("DB7", [{"Translation": "fx-tr-001"}])
        self.assertIn("R10_DUPLICATE", g.validate_write(brief(), CONTRACT, state=state).codes)

    def test_new_revision_is_a_version_not_a_create(self):
        p = brief(mode="VERSION", fields={"Caption": "Revised caption.", "Version": 3})
        v = g.validate_write(p, CONTRACT, state={"prior": prior_brief()})
        self.assertTrue(v.ok, v)

    def test_duplicate_translation_in_family_is_refused(self):
        p, key = translation_create()
        self.assertIn("R10_DUPLICATE", g.validate_write(p, CONTRACT, state=lookup("DB6", [key])).codes)

    def test_create_without_natural_key_is_refused(self):
        p = brief(key_values={})
        self.assertIn("R10_NO_NATURAL_KEY", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)


class PostizUnavailable(unittest.TestCase):
    """Scenario 9."""

    def test_postiz_route_refused_before_warmup_and_connection(self):
        v = g.validate_publish_route("postiz", {"warmup_cleared": False, "channel_connected": False,
                                                "approval_matrix_row": False})
        self.assertEqual(v.codes.count("R13_ROUTE_UNAVAILABLE"), 3)

    def test_manual_route_with_human_publisher_is_open(self):
        self.assertTrue(g.validate_publish_route("manual", {"publisher": "human:Mary Thuo"}).ok)

    def test_manual_route_cannot_be_run_by_an_agent(self):
        self.assertFalse(g.validate_publish_route("manual", {"publisher": "agent:presence-engagement"}).ok)


class ManualPublicationLinkBack(unittest.TestCase):
    """Scenario 10."""

    def test_complete_record_links_back(self):
        v = publish(approval())
        self.assertTrue(v.ok, v)

    def test_missing_native_url_is_refused(self):
        self.assertIn("R14_LINKBACK", publish(approval(), native_post_url="").codes)

    def test_non_linkedin_url_is_refused(self):
        v = publish(approval(), native_post_url="https://example.com/post/1")
        self.assertIn("R14_LINKBACK", v.codes)

    def test_surface_drift_is_refused(self):
        v = publish(approval(), surface=PAGE)
        self.assertIn("R14_LINKBACK", v.codes)

    def test_agent_publisher_is_refused(self):
        v = publish(approval(), publisher="agent:presence-engagement")
        self.assertIn("R11_APPROVAL_MISSING", v.codes)


class TriggerSchemaGuard(unittest.TestCase):
    def test_renaming_a_trigger_property_is_refused(self):
        v = g.validate_schema_change({"action": "rename", "db": "DB7", "property": "Publishing Status"})
        self.assertIn("R17_TRIGGER_PROPERTY", v.codes)

    def test_adding_a_new_property_is_allowed(self):
        self.assertTrue(g.validate_schema_change({"action": "add", "db": "DB7", "property": "G2 Decision"}).ok)


# --------------------------------------------------------------------------- correction unit, finding 1

def _agent_enum_lists(marker):
    """Every `enum: [...]` list in the content-* agent specs that contains `marker`."""
    found = {}
    for name in sorted(os.listdir(AGENTS_DIR)):
        if not name.startswith("content-"):
            continue
        with open(os.path.join(AGENTS_DIR, name), encoding="utf-8") as fh:
            text = fh.read()
        for m in re.finditer(r"enum:\s*\[([^\]]*)\]", text):
            vals = [x.strip() for x in m.group(1).split(",") if x.strip()]
            if marker in vals:
                found.setdefault(name, []).append(vals)
    return found


class SurfaceVocabulary(unittest.TestCase):
    """Finding 1: one explicit vocabulary, live names and IDs, unknown fails closed."""

    def test_contract_surface_options_equal_live_names_and_ids(self):
        opts = CONTRACT["vocabularies"]["surface"]["options"]
        self.assertEqual({o["notion"]: o["option_id"] for o in opts}, LIVE_SURFACE)

    def test_contract_audience_options_equal_live_names_and_ids(self):
        opts = CONTRACT["vocabularies"]["audience_role"]["options"]
        self.assertEqual({o["notion"]: o["option_id"] for o in opts}, LIVE_AUDIENCE)

    def test_company_page_voice_checked_by_notion_label(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                         "translation": translation(surface="LinkedIn - Company Page")})
        self.assertIn("R15_PAGE_VOICE", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)

    def test_company_page_voice_checked_by_agent_enum(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                         "translation": translation(surface="linkedin_company_page")})
        self.assertIn("R15_PAGE_VOICE", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)

    def test_documented_short_labels_fail_closed(self):
        # The 2026-10-09 decision log wrote "Founder profile" and "Company Page"; neither is a live option.
        for label in ("Company Page", "Founder profile", "LinkedIn — Company Page", "linkedin - company page"):
            p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                             "translation": translation(surface=label)})
            self.assertIn("R09_SURFACE_UNKNOWN", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes, label)

    def test_agent_only_surface_values_never_pass(self):
        for label in ("unknown", "not_applicable"):
            p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                             "translation": translation(surface=label)})
            self.assertIn("R09_SURFACE_UNKNOWN", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes, label)

    def test_notion_write_with_agent_enum_is_refused(self):
        p, _ = translation_create(surface="linkedin_company_page")
        self.assertIn("R09_SURFACE_UNKNOWN", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_linkedin_surface_on_a_newsletter_row_is_refused(self):
        p, _ = translation_create(surface=FOUNDER)
        p["links"]["platform"] = "Newsletter"
        self.assertIn("R09_SURFACE", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_single_identity_surface_on_a_linkedin_row_is_refused(self):
        p, _ = translation_create(surface=CHANNEL)
        self.assertIn("R09_SURFACE", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_linkedin_url_check_applies_to_agent_enum_surface(self):
        v = publish(approval(surface=PAGE), surface="linkedin_company_page", native_post_url="https://example.com/p/1")
        self.assertIn("R14_LINKBACK", v.codes)

    def test_agent_enum_and_notion_label_are_the_same_surface(self):
        v = publish(approval(surface=PAGE), surface="linkedin_company_page")
        self.assertTrue(v.ok, v)

    def test_unknown_publication_surface_fails_closed(self):
        v = publish(approval(surface=PAGE), surface="Company Page")
        self.assertIn("R14_LINKBACK", v.codes)

    def test_unassigned_surface_cannot_be_published(self):
        v = publish(approval(surface=UNASSIGNED), surface=UNASSIGNED)
        self.assertIn("R14_LINKBACK", v.codes)

    def test_every_agent_surface_enum_is_mapped(self):
        voc = CONTRACT["vocabularies"]["surface"]
        known = {o["agent_enum"] for o in voc["options"]} | {a["agent_enum"] for a in voc["agent_only"]}
        found = _agent_enum_lists("linkedin_company_page")
        self.assertTrue(found, "no surface enum found in the content agents")
        for agent, lists in found.items():
            for vals in lists:
                self.assertEqual(set(vals) - known, set(), agent)

    def test_every_agent_audience_enum_is_mapped(self):
        known = {o["agent_enum"] for o in CONTRACT["vocabularies"]["audience_role"]["options"]}
        found = _agent_enum_lists("general_manager_owner")
        self.assertTrue(found, "no audience enum found in the content agents")
        for agent, lists in found.items():
            for vals in lists:
                self.assertEqual(set(vals) - known - {"null"}, set(), agent)

    def test_translation_skill_names_every_live_surface_exactly(self):
        path = os.path.join(g.SKILLS_DIR, "content-surface-translation", "SKILL.md")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for label in LIVE_SURFACE:
            self.assertIn("`%s`" % label, text)


# --------------------------------------------------------------------------- finding 2

class RevisionIntegrity(unittest.TestCase):
    """Finding 2: positive, present revisions; publication-affecting changes bump exactly once."""

    def version(self, fields, mode="VERSION", prior=None):
        p = {"db": "DB7", "mode": mode, "actor": "C04", "fields": fields,
             "links": {"opportunity": opportunity(), "translation": translation(),
                       "narrative_position_ids": ["nar-fx-belief"]}}
        state = {} if prior is False else {"prior": prior or prior_brief()}
        return g.validate_write(p, CONTRACT, state=state)

    def test_copy_edit_without_version_bump_is_refused(self):
        self.assertIn("R21_REVISION_INCREMENT", self.version({"Caption": "Edited caption."}).codes)

    def test_copy_edit_as_update_is_refused(self):
        v = self.version({"Caption": "Edited caption.", "Version": 3}, mode="UPDATE")
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_copy_edit_with_single_bump_passes(self):
        v = self.version({"Caption": "Edited caption.", "Version": 3})
        self.assertTrue(v.ok, v)

    def test_visual_direction_edit_needs_a_bump_too(self):
        self.assertIn("R21_REVISION_INCREMENT", self.version({"Visual Direction": "Green, two charts"}).codes)

    def test_double_bump_is_refused(self):
        self.assertIn("R21_REVISION_INCREMENT", self.version({"Caption": "Edited.", "Version": 4}).codes)

    def test_bump_without_change_is_refused(self):
        v = self.version({"Caption": "Original caption.", "Version": 3})
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_non_publication_field_needs_no_bump_and_no_prior(self):
        v = self.version({"Confidence": "Strong Signal"}, mode="UPDATE", prior=False)
        self.assertTrue(v.ok, v)

    def test_missing_prior_state_is_refused(self):
        v = self.version({"Caption": "Edited.", "Version": 3}, prior=False)
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_brief_on_record_without_version_is_refused(self):
        v = self.version({"Caption": "Edited.", "Version": 1}, prior=prior_brief(Version=None))
        self.assertIn("R20_REVISION_INVALID", v.codes)

    def test_invalid_new_versions_are_refused(self):
        for bad in (None, 0, -1, 2.5, True, "3"):
            v = self.version({"Caption": "Edited.", "Version": bad})
            self.assertIn("R20_REVISION_INVALID", v.codes, repr(bad))

    def test_notion_float_versions_are_accepted(self):
        v = self.version({"Caption": "Edited.", "Version": 3.0}, prior=prior_brief(Version=2.0))
        self.assertTrue(v.ok, v)

    def test_create_with_missing_version_is_refused(self):
        p = brief()
        del p["fields"]["Version"]
        self.assertIn("R20_REVISION_INVALID", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)

    def test_create_must_start_at_one(self):
        p = brief()
        p["fields"]["Version"] = 2
        self.assertIn("R21_REVISION_INCREMENT", g.validate_write(p, CONTRACT, state=lookup("DB7")).codes)

    def test_missing_revisions_at_publication_are_refused(self):
        # Before the correction, None == None let this through.
        v = publish(approval(version=None, g2_approved_revision=None), revision=None)
        self.assertGreaterEqual(v.codes.count("R20_REVISION_INVALID"), 3)

    def test_stale_approval_is_refused(self):
        v = publish(approval(version=3, g2_approved_revision=2), revision=2)
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_submission_of_a_stale_revision_is_refused(self):
        v = g.validate_g2_submission(submission_ctx(revision=1))
        self.assertIn("R12_REVISION_MISMATCH", v.codes)


# --------------------------------------------------------------------------- finding 3

class WorkflowOrder(unittest.TestCase):
    """Finding 3 (correction unit), as hardened: G1 + readiness before Design; human spend
    approval before generation; G2 on the exact finished artifact. Text-only work skips
    Design and spend approval, never G1 (hardening unit)."""

    def test_ready_design_brief_with_g1_passes(self):
        v = g.validate_design_readiness(readiness_ctx())
        self.assertTrue(v.ok, v)

    def test_readiness_without_g1_is_refused(self):
        v = g.validate_design_readiness(readiness_ctx(g1=None))
        self.assertIn("R22_STAGE_ORDER", v.codes)

    def test_g1_by_an_agent_is_refused(self):
        v = g.validate_design_readiness(readiness_ctx(g1=g1(by="agent:content-brief-builder")))
        self.assertIn("R22_STAGE_ORDER", v.codes)

    def test_g1_for_an_older_revision_is_refused(self):
        v = g.validate_design_readiness(readiness_ctx(g1=g1(revision=1)))
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_text_only_brief_does_not_go_to_design(self):
        ctx = readiness_ctx(translation=translation(fmt="Text post"), g1=g1(path="text_only"))
        ctx["brief"].update(visual_direction="", canva_instructions="text-only")
        self.assertIn("R22_STAGE_ORDER", g.validate_design_readiness(ctx).codes)

    def test_readiness_with_unrun_dragon_unassigned_surface_and_bad_revision(self):
        ctx = readiness_ctx(opportunity=opportunity("Not yet run"), translation=translation(surface=UNASSIGNED))
        ctx["brief"]["version"] = None
        codes = g.validate_design_readiness(ctx).codes
        for c in ("R08_DRAGON_ORDER", "R09_SURFACE", "R20_REVISION_INVALID"):
            self.assertIn(c, codes)

    def generation(self, **over):
        return g.validate_generation_start(generation_ctx(**over))

    def test_generation_with_human_spend_approval_passes(self):
        v = self.generation()
        self.assertTrue(v.ok, v)

    def test_generation_without_spend_approval_is_refused(self):
        self.assertIn("R22_STAGE_ORDER", self.generation(spend_approval=None).codes)

    def test_generation_with_agent_spend_approval_is_refused(self):
        sa = dict(generation_ctx()["spend_approval"], by="agent:design-production-engine-coordinator")
        self.assertIn("R22_STAGE_ORDER", self.generation(spend_approval=sa).codes)

    def test_spend_approval_for_an_older_revision_is_refused(self):
        sa = dict(generation_ctx()["spend_approval"], revision=1)
        self.assertIn("R12_REVISION_MISMATCH", self.generation(spend_approval=sa).codes)

    def test_generation_before_design_status_is_refused(self):
        v = self.generation(brief={"id": BRIEF_ID, "version": 2, "publishing_status": "In progress"})
        self.assertIn("R22_STAGE_ORDER", v.codes)

    def test_g2_submission_before_finished_artifact_is_refused(self):
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(submission_ctx(artifacts=[])).codes)

    def test_g2_submission_of_artifact_made_for_older_revision_is_refused(self):
        v = g.validate_g2_submission(submission_ctx(artifacts=[asset(brief_revision=1)]))
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_g2_submission_of_artifact_with_unknown_rights_is_refused(self):
        v = g.validate_g2_submission(submission_ctx(artifacts=[asset(rights="unknown")]))
        self.assertIn("R22_STAGE_ORDER", v.codes)

    def test_text_only_reaches_g2_once_final_copy_exists(self):
        v = g.validate_g2_submission(submission_ctx(fmt="Text post"))
        self.assertTrue(v.ok, v)

    def test_text_only_without_copy_is_refused(self):
        ctx = submission_ctx(fmt="Text post")
        ctx["brief"].update(caption="", script="")
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(ctx).codes)

    def test_readiness_command_reads_a_windows_bom_snapshot_and_fails_closed_on_garbage(self):
        import contextlib
        import io
        import json
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            good, bad = os.path.join(tmp, "snap.json"), os.path.join(tmp, "bad.json")
            sub = os.path.join(tmp, "sub.json")
            with open(good, "w", encoding="utf-8-sig") as fh:  # BOM, as PowerShell 5.1 writes it
                json.dump(readiness_ctx(), fh)
            with open(sub, "w", encoding="utf-8-sig") as fh:
                json.dump(submission_ctx(fmt="Text post"), fh)
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("{not json")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(g.main(["readiness", good]), 0)
                self.assertEqual(g.main(["submission", sub]), 0)
                self.assertEqual(g.main(["readiness", bad]), 2)
                self.assertEqual(g.main(["submission", bad]), 2)
                self.assertEqual(g.main(["readiness", os.path.join(tmp, "missing.json")]), 2)

    def test_c06_cannot_submit_without_context(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {"G2 Decision": "Submitted for review"}}
        self.assertIn("R22_STAGE_ORDER", g.validate_write(p, CONTRACT, state={}).codes)

    def test_design_publication_with_the_approved_artifact_passes(self):
        v = publish(design_approval(), artifacts=[{"asset_id": "fx-asset-1", "version": 1}])
        self.assertTrue(v.ok, v)

    def test_design_publication_with_a_different_artifact_is_refused(self):
        v = publish(design_approval(), artifacts=[{"asset_id": "fx-asset-1", "version": 2}])
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_design_approval_without_artifact_is_refused(self):
        v = publish(approval(fmt="Carousel", vd="Navy", ci="6 frames"))
        self.assertIn("R11_APPROVAL_MISSING", v.codes)


# --------------------------------------------------------------------------- finding 4

class DuplicateLookupState(unittest.TestCase):
    """Finding 4: only a completed lookup counts; audience is part of translation identity."""

    def test_create_with_no_state_is_refused(self):
        self.assertIn("R10_LOOKUP_UNVERIFIED", g.validate_write(brief(), CONTRACT, state=None).codes)

    def test_create_with_empty_state_is_refused(self):
        self.assertIn("R10_LOOKUP_UNVERIFIED", g.validate_write(brief(), CONTRACT, state={}).codes)

    def test_failed_incomplete_or_unknown_lookups_are_refused(self):
        for status in ("failed", "incomplete", "partial", "unknown", "quota_exhausted", None):
            v = g.validate_write(brief(), CONTRACT, state=lookup("DB7", status=status))
            self.assertIn("R10_LOOKUP_UNVERIFIED", v.codes, status)

    def test_complete_lookup_without_a_records_list_is_refused(self):
        state = {"lookups": {"DB7": {"status": "complete", "checked_at": "2026-10-09", "records": None}}}
        self.assertIn("R10_LOOKUP_UNVERIFIED", g.validate_write(brief(), CONTRACT, state=state).codes)

    def test_complete_lookup_without_a_timestamp_is_refused(self):
        state = {"lookups": {"DB7": {"status": "complete", "records": []}}}
        self.assertIn("R10_LOOKUP_UNVERIFIED", g.validate_write(brief(), CONTRACT, state=state).codes)

    def test_lookup_on_another_database_does_not_count(self):
        self.assertIn("R10_LOOKUP_UNVERIFIED", g.validate_write(brief(), CONTRACT, state=lookup("DB6")).codes)

    def test_complete_empty_lookup_allows_create(self):
        v = g.validate_write(brief(), CONTRACT, state=lookup("DB7"))
        self.assertTrue(v.ok, v)

    def test_distinct_audience_variants_are_not_duplicates(self):
        _, gm_key = translation_create(audience="General Manager / Owner")
        p, _ = translation_create(audience="Revenue / Reservations Manager")
        v = g.validate_write(p, CONTRACT, state=lookup("DB6", [gm_key]))
        self.assertTrue(v.ok, v)

    def test_same_audience_variant_is_a_duplicate(self):
        p, key = translation_create(audience="General Manager / Owner")
        self.assertIn("R10_DUPLICATE", g.validate_write(p, CONTRACT, state=lookup("DB6", [key])).codes)

    def test_translation_create_without_audience_is_refused(self):
        p, _ = translation_create()
        del p["fields"]["Audience Role"]
        del p["key_values"]["Audience Role"]
        self.assertIn("R10_NO_NATURAL_KEY", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_audience_agent_enum_in_a_notion_write_is_refused(self):
        p, _ = translation_create(audience="general_manager_owner")
        self.assertIn("R23_UNKNOWN_OPTION", g.validate_write(p, CONTRACT, state=lookup("DB6")).codes)

    def test_no_second_audience_store_is_declared(self):
        db6 = next(d for d in CONTRACT["databases"] if d["db_id"] == "DB6")
        audience_fields = [f["name"] for f in db6["fields"] if "audience" in f["name"].lower()]
        self.assertEqual(audience_fields, ["Audience Role"])


# --------------------------------------------------------------------------- hardening unit (2026-10-09)

def _evidence_cases(valid, rev_key="revision"):
    """(name, evidence, codes that must appear). Every wrong case changes ONE thing."""
    no_brief = {k: v for k, v in valid.items() if k != "brief_id"}
    return [
        ("wrong brief", dict(valid, brief_id=OTHER_BRIEF), {"R24_EVIDENCE_IDENTITY"}),
        ("no brief id", no_brief, {"R24_EVIDENCE_IDENTITY"}),
        ("blank brief id", dict(valid, brief_id="  "), {"R24_EVIDENCE_IDENTITY"}),
        ("stale revision", dict(valid, **{rev_key: 1}), {"R12_REVISION_MISMATCH"}),
        ("zero revision", dict(valid, **{rev_key: 0}), {"R20_REVISION_INVALID"}),
        ("fractional revision", dict(valid, **{rev_key: 2.5}), {"R20_REVISION_INVALID"}),
        ("missing revision", dict(valid, **{rev_key: None}), {"R20_REVISION_INVALID"}),
    ]


class EvidenceBinding(unittest.TestCase):
    """Hardening item 1-2: evidence for a different brief at a matching revision used to pass
    (reproduced against ce310c6). Each stage's evidence now binds to brief ID + current Version."""

    def check(self, run, valid, rev_key="revision", missing_code="R22_STAGE_ORDER"):
        self.assertTrue(run(valid).ok, run(valid))
        for name, ev, expected in _evidence_cases(valid, rev_key):
            with self.subTest(case=name):
                codes = set(run(ev).codes)
                self.assertTrue(expected <= codes, (name, codes))
                self.assertEqual(codes - expected, set(), "only the changed field may fail: %r" % codes)
        if missing_code:
            with self.subTest(case="missing record"):
                self.assertIn(missing_code, run(None).codes)

    def test_g1_at_readiness(self):
        self.check(lambda ev: g.validate_design_readiness(readiness_ctx(g1=ev)), g1())

    def test_g1_at_g2_submission(self):
        self.check(lambda ev: g.validate_g2_submission(submission_ctx(g1=ev)), g1())

    def test_storyboard_before_generation(self):
        self.check(lambda ev: g.validate_generation_start(generation_ctx(storyboard=ev)),
                   generation_ctx()["storyboard"])

    def test_spend_approval_before_generation(self):
        self.check(lambda ev: g.validate_generation_start(generation_ctx(spend_approval=ev)),
                   generation_ctx()["spend_approval"])

    def test_claim_review_at_g2_submission(self):
        self.check(lambda ev: g.validate_g2_submission(submission_ctx(claim_review=ev)),
                   submission_ctx()["claim_review"])

    def test_asset_provenance_at_g2_submission(self):
        def run(prov):
            a = asset()
            a["provenance"] = prov
            return g.validate_g2_submission(submission_ctx(artifacts=[a]))
        self.check(run, asset()["provenance"], rev_key="brief_revision", missing_code="R24_EVIDENCE_IDENTITY")

    def test_approved_asset_provenance_at_publication(self):
        def run(prov):
            appr = with_manifest(design_approval(), lambda m: m["assets"][0].__setitem__("provenance", prov))
            return publish(appr, artifacts=[{"asset_id": "fx-asset-1", "version": 1}])
        self.check(run, asset()["provenance"], rev_key="brief_revision", missing_code="R24_EVIDENCE_IDENTITY")

    def test_brief_without_an_id_cannot_bind_anything(self):
        ctx = readiness_ctx()
        del ctx["brief"]["id"]
        self.assertIn("R24_EVIDENCE_IDENTITY", g.validate_design_readiness(ctx).codes)
        sub = submission_ctx()
        sub["brief"]["id"] = ""
        self.assertIn("R24_EVIDENCE_IDENTITY", g.validate_g2_submission(sub).codes)
        self.assertIn("R24_EVIDENCE_IDENTITY",
                      publish(approval(id=None)).codes)


class AssetValidity(unittest.TestCase):
    """Hardening item 1-2: an asset with no version (or no ID) on BOTH sides used to pass
    publication because the two sets still matched (reproduced against ce310c6)."""

    def publish(self, approved, published):
        if all(g.valid_asset_id(a.get("asset_id")) and g.revision_value(a.get("version")) for a in approved):
            appr = design_approval(assets=approved)
        else:  # an invalid stored set can only exist if the manifest was corrupted; simulate that
            appr = with_manifest(design_approval(), lambda m: m.__setitem__("assets", approved))
        return publish(appr, artifacts=published)

    def test_missing_version_on_both_sides_is_refused(self):
        a = asset()
        del a["version"]
        v = self.publish([a], [{"asset_id": "fx-asset-1"}])
        self.assertGreaterEqual(v.codes.count("R25_ASSET_INVALID"), 2)

    def test_missing_id_on_both_sides_is_refused(self):
        v = self.publish([asset(asset_id=None)], [{"asset_id": None, "version": 1}])
        self.assertGreaterEqual(v.codes.count("R25_ASSET_INVALID"), 2)

    def test_invalid_versions_are_refused(self):
        for bad in (0, -1, 1.5, True, "1"):
            with self.subTest(version=bad):
                v = g.validate_g2_submission(submission_ctx(artifacts=[asset(version=bad)]))
                self.assertIn("R25_ASSET_INVALID", v.codes)

    def test_invalid_ids_are_refused(self):
        for bad in ("", "  ", "a", "https://cdn.vendor.example/tmp/x.png?sig=1", "has space", None, 42):
            with self.subTest(asset_id=bad):
                v = g.validate_g2_submission(submission_ctx(artifacts=[asset(asset_id=bad)]))
                self.assertIn("R25_ASSET_INVALID", v.codes)

    def test_duplicate_asset_is_refused(self):
        v = g.validate_g2_submission(submission_ctx(artifacts=[asset(), asset(version=2)]))
        self.assertIn("R25_ASSET_INVALID", v.codes)

    def test_published_asset_missing_its_version_is_refused(self):
        v = self.publish([asset()], [{"asset_id": "fx-asset-1"}])
        self.assertIn("R25_ASSET_INVALID", v.codes)
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_valid_asset_set_passes(self):
        v = self.publish([asset(), asset(asset_id="fx-asset-2", version=3)],
                         [{"asset_id": "fx-asset-2", "version": 3}, {"asset_id": "fx-asset-1", "version": 1}])
        self.assertTrue(v.ok, v)


class SubmissionTarget(unittest.TestCase):
    """Hardening item 2: the G2 submission context must belong to the page being written."""

    def test_valid_submission_on_its_own_brief_passes(self):
        v = c06_submit()
        self.assertTrue(v.ok, v)

    def test_write_without_a_target_is_refused(self):
        self.assertIn("R24_EVIDENCE_IDENTITY", c06_submit(target=None).codes)

    def test_submission_for_another_brief_is_refused(self):
        # reproduced against ce310c6: a packet for brief A was accepted as a write on brief C
        self.assertIn("R24_EVIDENCE_IDENTITY", c06_submit(target=OTHER_BRIEF,
                                                          prior={"id": OTHER_BRIEF, "Version": 2}).codes)

    def test_target_not_read_back_is_refused(self):
        self.assertIn("R24_EVIDENCE_IDENTITY", c06_submit(prior=None).codes)

    def test_prior_record_of_another_page_is_refused(self):
        self.assertIn("R24_EVIDENCE_IDENTITY", c06_submit(prior={"id": OTHER_BRIEF, "Version": 2}).codes)

    def test_target_moved_on_since_the_packet_is_refused(self):
        self.assertIn("R12_REVISION_MISMATCH", c06_submit(prior={"id": BRIEF_ID, "Version": 3}).codes)

    def test_target_without_a_valid_version_is_refused(self):
        self.assertIn("R20_REVISION_INVALID", c06_submit(prior={"id": BRIEF_ID, "Version": None}).codes)


NOTION_ID = "0123456789abcdef0123456789abcdef"          # synthetic, Notion-shaped
NOTION_ID_DASHED = "01234567-89ab-cdef-0123-456789abcdef"  # the same page, dashed form


def rebound_submission(page_id):
    """submission_ctx() with every identity field moved to `page_id`."""
    sub = copy.deepcopy(submission_ctx())
    sub["brief"]["id"] = page_id
    sub["g1"]["brief_id"] = page_id
    sub["claim_review"]["brief_id"] = page_id
    for a in sub["artifacts"]:
        a["provenance"]["brief_id"] = page_id
    return sub


class SubmissionIdentityTriple(unittest.TestCase):
    """Follow-up unit (2026-10-10): state.prior.id, proposal.target and
    g2_submission.brief.id must each be a valid page ID and exactly equal.
    Reproduced against 9124997: a read-back with a Version but no ID, an empty
    ID or a None ID let Submitted for review through."""

    def ids(self, target, prior_id, packet_id, version=2):
        prior = {"Version": version}
        if prior_id is not ABSENT:
            prior["id"] = prior_id
        return c06_submit(sub=rebound_submission(packet_id), target=target, prior=prior)

    def test_read_back_with_version_but_no_id_is_refused(self):
        self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(BRIEF_ID, ABSENT, BRIEF_ID).codes)

    def test_missing_empty_blank_padded_or_non_string_read_back_id_is_refused(self):
        for bad in ("", None, "   ", " " + BRIEF_ID, BRIEF_ID + " ", BRIEF_ID + "\n", 7, [BRIEF_ID]):
            with self.subTest(prior_id=bad):
                self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(BRIEF_ID, bad, BRIEF_ID).codes)

    def test_missing_blank_or_padded_target_is_refused(self):
        for bad in (None, "", "  ", BRIEF_ID + " "):
            with self.subTest(target=bad):
                self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(bad, BRIEF_ID, BRIEF_ID).codes)

    def test_three_identical_but_invalid_ids_are_refused(self):
        for bad in ("   ", "", 7, "has space"):
            with self.subTest(all_three=bad):
                self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(bad, bad, bad).codes)

    def test_any_one_differing_id_is_refused(self):
        for target, prior_id, packet_id in ((OTHER_BRIEF, BRIEF_ID, BRIEF_ID),
                                            (BRIEF_ID, OTHER_BRIEF, BRIEF_ID),
                                            (BRIEF_ID, BRIEF_ID, OTHER_BRIEF)):
            with self.subTest(target=target, prior=prior_id, packet=packet_id):
                self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(target, prior_id, packet_id).codes)

    def test_dashed_and_undashed_forms_of_one_page_do_not_match(self):
        self.assertIn("R24_EVIDENCE_IDENTITY", self.ids(NOTION_ID, NOTION_ID_DASHED, NOTION_ID).codes)

    def test_three_identical_valid_ids_pass(self):
        for page_id in (BRIEF_ID, NOTION_ID, NOTION_ID_DASHED):
            with self.subTest(page_id=page_id):
                v = self.ids(page_id, page_id, page_id)
                self.assertTrue(v.ok, v)

    def test_revision_checks_still_apply_when_ids_match(self):
        self.assertEqual(set(self.ids(BRIEF_ID, BRIEF_ID, BRIEF_ID, version=3).codes), {"R12_REVISION_MISMATCH"})
        self.assertEqual(set(self.ids(BRIEF_ID, BRIEF_ID, BRIEF_ID, version=None).codes), {"R20_REVISION_INVALID"})


ABSENT = object()


class G1OnBothPaths(unittest.TestCase):
    """Hardening item 3 (owner direction, 2026-10-09): G1 and G2 for every public item.
    Text-only skips Design and spend approval, not G1. Text-capable is not asset-free."""

    def test_text_only_submission_without_g1_is_refused(self):
        # reproduced against ce310c6: accepted with no G1 at all
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(submission_ctx(fmt="Text post", g1=None)).codes)

    def test_design_submission_without_g1_is_refused(self):
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(submission_ctx(g1=None)).codes)

    def test_text_only_with_g1_passes_on_both_text_formats(self):
        for fmt in ("Text post", "Newsletter issue"):
            with self.subTest(fmt=fmt):
                v = g.validate_g2_submission(submission_ctx(fmt=fmt))
                self.assertTrue(v.ok, v)

    def test_g1_must_record_the_path(self):
        rec = g1()
        del rec["path"]
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(submission_ctx(g1=rec)).codes)

    def test_g1_path_must_match_the_brief(self):
        self.assertIn("R22_STAGE_ORDER",
                      g.validate_g2_submission(submission_ctx(fmt="Text post", g1=g1(path="design"))).codes)
        self.assertIn("R22_STAGE_ORDER", g.validate_g2_submission(submission_ctx(g1=g1(path="text_only"))).codes)

    def test_text_capable_format_with_visual_direction_is_design_work(self):
        ctx = submission_ctx(fmt="Newsletter issue", g1=g1(path="text_only"))
        ctx["brief"].update(visual_direction="One header graphic: OTA commission chart")
        codes = g.validate_g2_submission(ctx).codes
        self.assertIn("R22_STAGE_ORDER", codes)  # G1 said text-only; the brief now needs an asset, and has none

    def test_text_only_brief_listing_assets_is_refused(self):
        v = g.validate_g2_submission(submission_ctx(fmt="Text post", artifacts=[asset()]))
        self.assertIn("R22_STAGE_ORDER", v.codes)

    def test_text_only_readiness_refuses_design_and_points_to_g2(self):
        ctx = readiness_ctx(translation=translation(fmt="Text post"), g1=g1(path="text_only"))
        ctx["brief"].update(visual_direction="", canva_instructions="")
        details = " ".join(r["detail"] for r in g.validate_design_readiness(ctx).refusals)
        self.assertIn("G2 submission", details)


# --------------------------------------------------------------------------- storage unit (2026-10-10)

# Option IDs of DB7 G1 Decision as read back from Notion after the storage unit created it.
LIVE_G1_DECISION = {"Passed (design)": "dd5c26e4-77b8-4d1c-a479-ef71995b248b",
                    "Passed (text-only)": "dcb7e2c3-4bce-4db9-9645-eeea3b7545d4",
                    "Returned": "857c39cc-1c86-4116-97dc-32282a8b9b6c"}
LIVE_OFFER_STATUS = {"Active": "0be591e2-dc22-4327-81a6-82dfddece551",
                     "In engineering": "5826dd7e-6528-4c79-b71b-25cf0b117166",
                     "Not quotable": "e0331817-9f17-4103-b27d-6fe57c1aa1f7",
                     "Contested": "bf64d969-f328-4747-a835-adbb8e3a4975"}
# Pinned output of build_evidence(fresh_ctx(), [asset()]). If this changes, every stored
# fingerprint in Notion stops matching: change it only with a recorded migration.
GOLDEN_FINGERPRINT = "sha256:35fb291342927d4b8ee6f52efca37a59a57ca96053a2a75b50582b32ae66b281"
# (Recomputed 2026-10-10 by an independent script built from the published specification,
# not from the gate's code: identical.)


class StorageSchema(unittest.TestCase):
    """The six DB7 properties, their owners, counts and pinned option IDs."""

    def test_six_storage_fields_with_their_writers(self):
        db7 = g.field_index(CONTRACT)["DB7"]
        expected = {"G1 Decision": ("select", "human_only"), "G1 Reviewer": ("text", "human_only"),
                    "G1 Decided At": ("date", "human_only"), "G1 Revision": ("number", "human_only"),
                    "G2 Packet Manifest": ("text", "C06"), "G2 Submitted Fingerprint": ("text", "C06")}
        for name, (typ, writer) in expected.items():
            self.assertEqual((db7[name]["type"], db7[name]["writer"]), (typ, writer), name)

    def test_total_field_count_is_367(self):
        self.assertEqual(sum(len(d["fields"]) for d in CONTRACT["databases"]), 367)

    def test_g1_decision_options_are_pinned_to_live_ids(self):
        opts = CONTRACT["vocabularies"]["g1_decision"]["options"]
        self.assertEqual({o["notion"]: o["option_id"] for o in opts}, LIVE_G1_DECISION)
        self.assertEqual([(o["decision"], o["path"]) for o in opts],
                         [("passed", "design"), ("passed", "text_only"), ("returned", None)])

    def test_offer_status_options_are_pinned_to_live_ids(self):
        opts = CONTRACT["vocabularies"]["offer_status"]["options"]
        self.assertEqual({o["notion"]: o["option_id"] for o in opts}, LIVE_OFFER_STATUS)

    def test_g1_and_g2_are_owner_only(self):
        self.assertEqual((CONTRACT["approvers"]["g1"], CONTRACT["approvers"]["g2"]), ([OWNER], [OWNER]))

    def test_gate_catches_a_storage_field_with_the_wrong_writer(self):
        bad = copy.deepcopy(CONTRACT)
        db7 = next(d for d in bad["databases"] if d["db_id"] == "DB7")
        next(f for f in db7["fields"] if f["name"] == "G1 Revision")["writer"] = "C06"
        self.assertTrue(any(e.startswith("C10") for e in g.check_contract(bad)))

    def test_skills_cannot_write_g1(self):
        for name in ("G1 Decision", "G1 Reviewer", "G1 Decided At", "G1 Revision"):
            p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {name: "x"}}
            self.assertIn("R01_HUMAN_ONLY", g.validate_write(p, CONTRACT, state={}).codes, name)


class Fingerprint(unittest.TestCase):
    """Deterministic: same content, same hash, on any machine; one canonical ID form."""

    def test_golden_fingerprint(self):
        self.assertEqual(evidence(fresh_ctx(), [asset()])["fingerprint"], GOLDEN_FINGERPRINT)

    def test_key_order_and_input_order_do_not_matter(self):
        a = evidence(fresh_ctx(platform=("LinkedIn", "Newsletter")), [asset("fx-asset-1"), asset("fx-asset-2")])
        f = fresh_ctx(platform=("Newsletter", "LinkedIn"))
        f["brief"]["properties"] = dict(reversed(list(f["brief"]["properties"].items())))
        b = evidence(f, [asset("fx-asset-2"), asset("fx-asset-1")])
        self.assertEqual(a["fingerprint"], b["fingerprint"])
        self.assertEqual(a["manifest_text"], b["manifest_text"])

    def test_line_endings_and_unicode_normal_form_do_not_matter(self):
        nfc = evidence(fresh_ctx(caption="Café line one\nline two"))["fingerprint"]
        nfd_crlf = evidence(fresh_ctx(caption="Café line one\r\nline two"))["fingerprint"]
        self.assertEqual(nfc, nfd_crlf)

    def test_whitespace_is_content(self):
        self.assertNotEqual(evidence(fresh_ctx(caption="Final copy"))["fingerprint"],
                            evidence(fresh_ctx(caption="Final copy "))["fingerprint"])

    def test_dashed_and_undashed_ids_give_one_fingerprint(self):
        dashed = lambda h: "%s-%s-%s-%s-%s" % (h[:8], h[8:12], h[12:16], h[16:20], h[20:])
        a = evidence(fresh_ctx(), [asset()])
        b = evidence(fresh_ctx(brief_id=dashed(BRIEF_ID), translation_ids=(dashed(TRANSLATION_ID),),
                               translation_page=dashed(TRANSLATION_ID), platform_ids=(dashed(PLATFORM_ID),)),
                     [asset(brief_id=dashed(BRIEF_ID))])
        self.assertEqual(a["fingerprint"], b["fingerprint"])
        self.assertEqual(a["manifest"]["brief_id"], BRIEF_ID)

    def test_non_canonical_ids_are_refused_not_normalised(self):
        for bad in (BRIEF_ID.upper(), " " + BRIEF_ID, "fx-brief-001"):
            with self.subTest(brief_id=bad):
                v, ev = g.build_evidence(fresh_ctx(brief_id=bad), [], CONTRACT)
                self.assertIsNone(ev)
                self.assertIn("R27_CONTEXT_UNREADABLE", v.codes)

    def test_hand_edited_manifest_is_not_trusted(self):
        text = evidence(fresh_ctx())["manifest_text"]
        for edited in (text.replace(",", ", "), text + " ", "{}", "not json", ""):
            with self.subTest(edited=edited[:20]):
                v = g.Verdict()
                self.assertIsNone(g.parse_manifest(v, edited))
                self.assertIn("R26_FINGERPRINT_MISMATCH", v.codes)

    def test_manifest_records_the_full_resolved_context(self):
        m = evidence(fresh_ctx(offer_ids=(OFFER_ID,)))["manifest"]
        self.assertEqual(m["resolved"], {"translation_id": TRANSLATION_ID, "surface": FOUNDER, "audience_role": "Founder",
                                         "format": "Carousel", "platform_ids": [PLATFORM_ID],
                                         "offers": [{"offer_id": OFFER_ID, "offer_status": "Active"}]})


class FreshContext(unittest.TestCase):
    """Unknown or unreadable context never inherits stored evidence (R27)."""

    def unreadable(self, fresh, code="R27_CONTEXT_UNREADABLE"):
        v, ev = g.build_evidence(fresh, [], CONTRACT)
        self.assertIsNone(ev, v)
        self.assertIn(code, v.codes)

    def test_no_read_back(self):
        self.unreadable(None)

    def test_failed_translation_read(self):
        self.unreadable(fresh_ctx(translation_status="failed"))

    def test_partial_brief_read(self):
        f = fresh_ctx()
        del f["brief"]["properties"]["Caption"]
        self.unreadable(f)

    def test_partial_translation_read(self):
        f = fresh_ctx()
        del f["translation"]["properties"]["Format"]
        self.unreadable(f)

    def test_stale_read(self):
        self.unreadable(fresh_ctx(read_at="2026-10-10T09:00:00Z"))

    def test_read_after_the_check(self):
        self.unreadable(fresh_ctx(read_at="2026-10-10T12:05:00Z"))

    def test_read_without_a_time_zone(self):
        self.unreadable(fresh_ctx(read_at="2026-10-10T11:58:00"))

    def test_part_from_another_session(self):
        f = fresh_ctx()
        f["translation"]["session"] = "fx-session-OLD"
        self.unreadable(f)

    def test_translation_read_is_not_the_linked_page(self):
        self.unreadable(fresh_ctx(translation_page="c1000000000040008000000000000009"), "R24_EVIDENCE_IDENTITY")

    def test_two_linked_translations(self):
        self.unreadable(fresh_ctx(translation_ids=(TRANSLATION_ID, "c1000000000040008000000000000002")))

    def test_linked_offer_not_read(self):
        f = fresh_ctx(offer_ids=(OFFER_ID,))
        f["offers"] = []
        self.unreadable(f)

    def test_offer_read_but_not_linked(self):
        f = fresh_ctx(offer_ids=(OFFER_ID,))
        f["brief"]["properties"]["Offer"] = []
        self.unreadable(f, "R24_EVIDENCE_IDENTITY")

    def test_unknown_surface_and_offer_status(self):
        self.unreadable(fresh_ctx(surface="Company Page"), "R09_SURFACE_UNKNOWN")
        self.unreadable(fresh_ctx(offer_ids=(OFFER_ID,), offer_status="Live"), "R23_UNKNOWN_OPTION")

    def test_read_and_empty_is_null_not_unreadable(self):
        ev = evidence(fresh_ctx(audience=None))
        self.assertIsNone(ev["manifest"]["resolved"]["audience_role"])

    def test_stored_evidence_is_never_inherited_when_the_read_fails(self):
        appr = approval()
        v = publish(appr, fresh=fresh_ctx(translation_status="failed", fmt="Text post", vd="", ci="", script=""))
        self.assertFalse(v.ok)
        self.assertIn("R27_CONTEXT_UNREADABLE", v.codes)
        self.assertFalse(publish(appr, fresh=None).ok)


class ChangeDetection(unittest.TestCase):
    """A publishable copy, asset or resolved-context change without Version +1 is
    caught (R26 at publication, R21 at re-submission). A context-only or asset-only
    change is versioned without inventing a DB7 copy edit."""

    def moved(self, v):
        return " ".join(r["detail"] for r in v.refusals if r["code"] == "R26_FINGERPRINT_MISMATCH")

    def published_with(self, **fresh_over):
        brief_fields, fresh = approval(offer_ids=(OFFER_ID,))
        changed = fresh_ctx(**dict(dict(fmt="Text post", vd="", ci="", script="", offer_ids=(OFFER_ID,)), **fresh_over))
        return publish((brief_fields, fresh), fresh=changed)

    def test_unchanged_passes(self):
        v = self.published_with()
        self.assertTrue(v.ok, v)

    def test_copy_edit_without_a_bump(self):
        v = self.published_with(caption="Final copy, edited in Notion")
        self.assertIn("R26_FINGERPRINT_MISMATCH", v.codes)

    def test_context_changes_beneath_an_unchanged_relation(self):
        cases = {"surface": dict(surface=PAGE), "audience_role": dict(audience="CEO"),
                 "format": dict(fmt="Article / Long-form"), "platform_ids": dict(platform_ids=(OTHER_PLATFORM_ID,)),
                 "offers": dict(offer_status="Not quotable")}
        for key, over in cases.items():
            with self.subTest(component=key):
                v = self.published_with(**over)
                self.assertIn("R26_FINGERPRINT_MISMATCH", v.codes)
                self.assertIn("resolved.%s" % key, self.moved(v))

    def test_asset_swapped_after_approval(self):
        v = publish(design_approval(), artifacts=[{"asset_id": "fx-asset-9", "version": 1}])
        self.assertIn("R26_FINGERPRINT_MISMATCH", v.codes)
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_resubmission_at_the_same_version_after_a_context_change(self):
        stored = evidence(fresh_ctx(), [asset()])
        prior = {"id": BRIEF_ID, "Version": 2.0, "G2 Packet Manifest": stored["manifest_text"],
                 "G2 Submitted Fingerprint": stored["fingerprint"]}
        sub = submission_ctx(translation=translation(surface=PAGE))
        sub["brief"]["caption"] = "Final copy"  # institutional voice, so only the context differs
        v = c06_submit(sub=sub, prior=prior)
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def version(self, reason, prior_manifest=None, fresh=None, extra=None, version=3):
        p = {"db": "DB7", "mode": "VERSION", "actor": "C04", "reason": reason, "fields": {"Version": version},
             "links": {"opportunity": opportunity(), "translation": translation(surface=PAGE),
                       "narrative_position_ids": ["nar-fx-belief"]}}
        p.update(extra or {})
        prior = prior_brief()
        if prior_manifest is not None:
            prior["G2 Packet Manifest"] = prior_manifest
        return p, g.validate_write(p, CONTRACT, state={"prior": prior, "fresh": fresh})

    def test_context_only_version_is_accepted_without_a_copy_edit(self):
        stored = evidence(fresh_ctx(surface=FOUNDER))
        p, v = self.version("context_change", stored["manifest_text"], fresh_ctx(surface=PAGE))
        self.assertTrue(v.ok, v)
        self.assertEqual(set(p["fields"]), {"Version"})

    def test_context_only_version_without_a_change_is_refused(self):
        stored = evidence(fresh_ctx())
        _, v = self.version("context_change", stored["manifest_text"], fresh_ctx())
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_context_only_version_with_an_unreadable_context_is_refused(self):
        stored = evidence(fresh_ctx())
        _, v = self.version("context_change", stored["manifest_text"], fresh_ctx(translation_status="failed"))
        self.assertIn("R27_CONTEXT_UNREADABLE", v.codes)

    def test_context_only_version_needs_a_baseline(self):
        _, v = self.version("context_change", None, fresh_ctx(surface=PAGE))
        self.assertIn("R21_REVISION_INCREMENT", v.codes)
        before = evidence(fresh_ctx(surface=FOUNDER))["manifest"]["resolved"]
        _, v = self.version("context_change", None, fresh_ctx(surface=PAGE), extra={"context_before": before})
        self.assertTrue(v.ok, v)

    def test_context_only_change_must_bump_exactly_once(self):
        stored = evidence(fresh_ctx(surface=FOUNDER))
        _, v = self.version("context_change", stored["manifest_text"], fresh_ctx(surface=PAGE), version=4)
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_asset_only_version(self):
        stored = evidence(fresh_ctx(), [asset()])
        _, v = self.version("asset_change", stored["manifest_text"], None,
                            extra={"assets": [{"asset_id": "fx-asset-1", "version": 2}]})
        self.assertTrue(v.ok, v)
        _, v = self.version("asset_change", stored["manifest_text"], None,
                            extra={"assets": [{"asset_id": "fx-asset-1", "version": 1}]})
        self.assertIn("R21_REVISION_INCREMENT", v.codes)

    def test_after_a_bump_g1_and_g2_must_be_renewed(self):
        self.assertIn("R12_REVISION_MISMATCH", g.validate_design_readiness(readiness_ctx(
            brief=dict(readiness_ctx()["brief"], version=3))).codes)
        self.assertIn("R12_REVISION_MISMATCH", publish(approval(version=3)).codes)


class OwnerOnly(unittest.TestCase):
    """Owner-only G1/G2, initially. A typed-name comparison, not authentication."""

    def test_g1_by_another_human_is_refused(self):
        v = g.validate_design_readiness(readiness_ctx(g1=g1(by="human:Someone Else")))
        self.assertIn("R28_REVIEWER_NOT_AUTHORISED", v.codes)
        v = g.validate_g2_submission(submission_ctx(g1=g1(by="human:Someone Else")))
        self.assertIn("R28_REVIEWER_NOT_AUTHORISED", v.codes)

    def test_g2_by_another_human_or_a_padded_name_is_refused(self):
        for name in ("Someone Else", " Mary Thuo", "mary thuo"):
            with self.subTest(reviewer=name):
                self.assertIn("R28_REVIEWER_NOT_AUTHORISED", publish(approval(g2_reviewer=name)).codes)

    def test_owner_passes(self):
        self.assertTrue(g.validate_design_readiness(readiness_ctx()).ok)
        self.assertTrue(publish().ok)


class G1FromProperties(unittest.TestCase):
    def props(self, **over):
        p = {"G1 Decision": "Passed (design)", "G1 Reviewer": OWNER, "G1 Decided At": "2026-10-20", "G1 Revision": 2.0}
        p.update(over)
        return p

    def test_stored_g1_maps_to_the_gate_record(self):
        r = g.g1_from_properties(self.props(), BRIEF_ID, CONTRACT)
        self.assertEqual(r, {"decision": "passed", "path": "design", "by": "human:" + OWNER, "at": "2026-10-20",
                             "brief_id": BRIEF_ID, "revision": 2.0})
        self.assertTrue(g.validate_design_readiness(readiness_ctx(g1=r)).ok)

    def test_text_only_and_returned(self):
        self.assertEqual(g.g1_from_properties(self.props(**{"G1 Decision": "Passed (text-only)"}), BRIEF_ID, CONTRACT)["path"],
                         "text_only")
        r = g.g1_from_properties(self.props(**{"G1 Decision": "Returned"}), BRIEF_ID, CONTRACT)
        self.assertIn("R22_STAGE_ORDER", g.validate_design_readiness(readiness_ctx(g1=r)).codes)

    def test_empty_unknown_or_stale_g1_is_refused(self):
        self.assertIsNone(g.g1_from_properties(self.props(**{"G1 Decision": None}), BRIEF_ID, CONTRACT))
        for props in (self.props(**{"G1 Decision": "Approved"}), self.props(**{"G1 Revision": 1})):
            with self.subTest(props=props):
                r = g.g1_from_properties(props, BRIEF_ID, CONTRACT)
                self.assertFalse(g.validate_design_readiness(readiness_ctx(g1=r)).ok)


class SubmissionEvidence(unittest.TestCase):
    """C06 writes the manifest and fingerprint the gate computes from a fresh read-back
    of the exact target, together with Submitted for review."""

    def test_valid_submission_passes(self):
        v = c06_submit()
        self.assertTrue(v.ok, v)

    def test_text_only_submission_passes(self):
        v = c06_submit(sub=submission_ctx(fmt="Text post"))
        self.assertTrue(v.ok, v)

    def test_missing_evidence_fields_are_refused(self):
        self.assertIn("R22_STAGE_ORDER", c06_submit(fields=None).codes)

    def test_typed_evidence_is_refused(self):
        v = c06_submit(fields={"G2 Packet Manifest": "{}", "G2 Submitted Fingerprint": "sha256:" + "0" * 64})
        self.assertIn("R26_FINGERPRINT_MISMATCH", v.codes)

    def test_no_fresh_read_is_refused(self):
        self.assertIn("R27_CONTEXT_UNREADABLE", c06_submit(fresh=None, fields={"G2 Packet Manifest": "x",
                                                                               "G2 Submitted Fingerprint": "y"}).codes)

    def test_fresh_read_of_another_page_is_refused(self):
        sub = submission_ctx()
        self.assertIn("R24_EVIDENCE_IDENTITY", c06_submit(sub=sub, fresh=fresh_for_submission(sub, brief_id=OTHER_BRIEF)).codes)

    def test_packet_copy_or_context_differing_from_the_page_is_refused(self):
        sub = submission_ctx()
        self.assertIn("R26_FINGERPRINT_MISMATCH",
                      c06_submit(sub=sub, fresh=fresh_for_submission(sub, caption="Something else")).codes)
        self.assertIn("R26_FINGERPRINT_MISMATCH",
                      c06_submit(sub=sub, fresh=fresh_for_submission(sub, surface=PAGE)).codes)

    def test_asset_made_for_another_brief_is_refused(self):
        v = c06_submit(sub=submission_ctx(artifacts=[asset(brief_id=OTHER_BRIEF)]))
        self.assertIn("R24_EVIDENCE_IDENTITY", v.codes)


# --------------------------------------------------------------------------- tests stay out of production memory

class ProductionMemoryUntouched(unittest.TestCase):
    def test_gate_source_writes_no_files(self):
        with open(g.__file__, encoding="utf-8") as fh:
            src = fh.read()
        self.assertIsNone(re.search(r"open\([^)]*['\"][wax]\+?['\"]", src))
        self.assertNotIn("skill_runs.jsonl", src)


if __name__ == "__main__":
    unittest.main()
