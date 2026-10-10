# -*- coding: utf-8 -*-
"""
Tests for the Content (04) write gate.

    python -m unittest discover -s 04_Content/contracts -p "test_*.py"

Every record here is synthetic (ids prefixed `fx-`). Nothing is read from or
written to Notion, the runtime, or any _memory stream; ProductionMemoryUntouched
checks that last point on every run.
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

# Live field counts read from the Notion schemas on 2026-10-09. If a field is
# added in Notion, the contract must gain an owner for it in the same change.
LIVE_FIELD_COUNTS = {"DB1": 34, "DB2": 44, "DB3": 51, "DB4": 45,
                     "DB5": 54, "DB6": 52, "DB7": 49, "DB8": 32}

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
    ctx = {"brief": {"id": "fx-brief-001", "version": 2, "caption": "Copy", "script": "S1 ...",
                     "visual_direction": "Navy, one chart per frame", "canva_instructions": "1080x1350, 6 frames"},
           "links": {"opportunity": "fx-opp-001", "translation": "fx-tr-001", "narrative_position_ids": ["nar-fx-belief"]},
           "opportunity": opportunity(),
           "translation": translation(),
           "g1": g1()}
    ctx.update(over)
    return ctx


BRIEF_ID, OTHER_BRIEF = "fx-brief-001", "fx-brief-OTHER"


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


def design_approval(**over):
    b = approved_brief(format="Carousel", visual_direction="Navy", canva_instructions="6 frames",
                       g2_approved_artifacts=[asset()])
    b.update(over)
    return b


def c06_submit(sub=None, target=BRIEF_ID, prior="default"):
    p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {"G2 Decision": "Submitted for review"},
         "g2_submission": submission_ctx() if sub is None else sub}
    if target is not None:
        p["target"] = target
    state = {"prior": {"id": BRIEF_ID, "Version": 2.0}} if prior == "default" else ({"prior": prior} if prior else {})
    return g.validate_write(p, CONTRACT, state=state)


def approved_brief(**over):
    b = {"id": "fx-brief-001", "version": 2, "surface": FOUNDER, "format": "Text post",
         "visual_direction": "", "canva_instructions": "",
         "g2_decision": "Approved", "g2_approved_revision": 2,
         "g2_reviewer": "Mary Thuo", "g2_decided_at": "2026-10-20"}
    b.update(over)
    return b


def publication(**over):
    r = {"brief_id": "fx-brief-001", "revision": 2, "surface": FOUNDER,
         "native_post_url": "https://www.linkedin.com/feed/update/urn:li:activity:0000000000000000000/",
         "published_at": "2026-10-21", "publisher": "human:Mary Thuo"}
    r.update(over)
    return r


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
        v = g.validate_publication(publication(), approved_brief(g2_decision="Rejected"))
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
        v = g.validate_publication(publication(), approved_brief(g2_decision="Submitted for review"))
        self.assertIn("R11_APPROVAL_MISSING", v.codes)

    def test_approval_for_an_older_revision_is_refused(self):
        v = g.validate_publication(publication(revision=3), approved_brief(version=3, g2_approved_revision=2))
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_approval_without_reviewer_is_refused(self):
        v = g.validate_publication(publication(), approved_brief(g2_reviewer=""))
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
        v = g.validate_publication(publication(), approved_brief())
        self.assertTrue(v.ok, v)

    def test_missing_native_url_is_refused(self):
        self.assertIn("R14_LINKBACK", g.validate_publication(publication(native_post_url=""), approved_brief()).codes)

    def test_non_linkedin_url_is_refused(self):
        v = g.validate_publication(publication(native_post_url="https://example.com/post/1"), approved_brief())
        self.assertIn("R14_LINKBACK", v.codes)

    def test_surface_drift_is_refused(self):
        v = g.validate_publication(publication(surface=PAGE), approved_brief())
        self.assertIn("R14_LINKBACK", v.codes)

    def test_agent_publisher_is_refused(self):
        v = g.validate_publication(publication(publisher="agent:presence-engagement"), approved_brief())
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
        v = g.validate_publication(publication(surface="linkedin_company_page", native_post_url="https://example.com/p/1"),
                                   approved_brief(surface=PAGE))
        self.assertIn("R14_LINKBACK", v.codes)

    def test_agent_enum_and_notion_label_are_the_same_surface(self):
        v = g.validate_publication(publication(surface="linkedin_company_page"), approved_brief(surface=PAGE))
        self.assertTrue(v.ok, v)

    def test_unknown_publication_surface_fails_closed(self):
        v = g.validate_publication(publication(surface="Company Page"), approved_brief(surface=PAGE))
        self.assertIn("R14_LINKBACK", v.codes)

    def test_unassigned_surface_cannot_be_published(self):
        v = g.validate_publication(publication(surface=UNASSIGNED), approved_brief(surface=UNASSIGNED))
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
        v = g.validate_publication(publication(revision=None), approved_brief(version=None, g2_approved_revision=None))
        self.assertGreaterEqual(v.codes.count("R20_REVISION_INVALID"), 3)

    def test_stale_approval_is_refused(self):
        v = g.validate_publication(publication(revision=2), approved_brief(version=3, g2_approved_revision=2))
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
        v = g.validate_publication(publication(artifacts=[{"asset_id": "fx-asset-1", "version": 1}]),
                                   design_approval())
        self.assertTrue(v.ok, v)

    def test_design_publication_with_a_different_artifact_is_refused(self):
        v = g.validate_publication(publication(artifacts=[{"asset_id": "fx-asset-1", "version": 2}]),
                                   design_approval())
        self.assertIn("R12_REVISION_MISMATCH", v.codes)

    def test_design_approval_without_artifact_is_refused(self):
        v = g.validate_publication(publication(), approved_brief(format="Carousel", visual_direction="Navy",
                                                                 canva_instructions="6 frames"))
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
            a = asset()
            a["provenance"] = prov
            return g.validate_publication(publication(artifacts=[{"asset_id": "fx-asset-1", "version": 1}]),
                                          design_approval(g2_approved_artifacts=[a]))
        self.check(run, asset()["provenance"], rev_key="brief_revision", missing_code="R24_EVIDENCE_IDENTITY")

    def test_brief_without_an_id_cannot_bind_anything(self):
        ctx = readiness_ctx()
        del ctx["brief"]["id"]
        self.assertIn("R24_EVIDENCE_IDENTITY", g.validate_design_readiness(ctx).codes)
        sub = submission_ctx()
        sub["brief"]["id"] = ""
        self.assertIn("R24_EVIDENCE_IDENTITY", g.validate_g2_submission(sub).codes)
        self.assertIn("R24_EVIDENCE_IDENTITY",
                      g.validate_publication(publication(), approved_brief(id=None)).codes)


class AssetValidity(unittest.TestCase):
    """Hardening item 1-2: an asset with no version (or no ID) on BOTH sides used to pass
    publication because the two sets still matched (reproduced against ce310c6)."""

    def publish(self, approved, published):
        return g.validate_publication(publication(artifacts=published), design_approval(g2_approved_artifacts=approved))

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


# --------------------------------------------------------------------------- tests stay out of production memory

class ProductionMemoryUntouched(unittest.TestCase):
    def test_gate_source_writes_no_files(self):
        with open(g.__file__, encoding="utf-8") as fh:
            src = fh.read()
        self.assertIsNone(re.search(r"open\([^)]*['\"][wax]\+?['\"]", src))
        self.assertNotIn("skill_runs.jsonl", src)


if __name__ == "__main__":
    unittest.main()
