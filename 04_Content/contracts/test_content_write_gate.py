# -*- coding: utf-8 -*-
"""
Tests for the Content (04) write gate.

    python -m unittest discover -s 04_Content/contracts -p "test_*.py"

Every record here is synthetic (ids prefixed `fx-`). Nothing is read from or
written to Notion, the runtime, or any _memory stream.
"""
import copy
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content_write_gate as g  # noqa: E402

CONTRACT = g.load_contract()

# Live field counts read from the Notion schemas on 2026-10-09. If a field is
# added in Notion, the contract must gain an owner for it in the same change.
LIVE_FIELD_COUNTS = {"DB1": 34, "DB2": 44, "DB3": 51, "DB4": 45,
                     "DB5": 54, "DB6": 52, "DB7": 49, "DB8": 32}


def opportunity(strategic="Complete"):
    return {"id": "fx-opp-001", "strategic_dragon": strategic}


def translation(surface="LinkedIn - Founder profile", editorial="Complete", platform="LinkedIn",
                family="nar-fx-belief"):
    return {"id": "fx-tr-001", "family_id": family, "surface": surface,
            "editorial_dragon": editorial, "platform": platform}


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


def approved_brief(**over):
    b = {"id": "fx-brief-001", "version": 2, "surface": "LinkedIn - Founder profile",
         "g2_decision": "Approved", "g2_approved_revision": 2,
         "g2_reviewer": "Mary Thuo", "g2_decided_at": "2026-10-20"}
    b.update(over)
    return b


def publication(**over):
    r = {"brief_id": "fx-brief-001", "revision": 2, "surface": "LinkedIn - Founder profile",
         "native_post_url": "https://www.linkedin.com/feed/update/urn:li:activity:0000000000000000000/",
         "published_at": "2026-10-21", "publisher": "human:Mary Thuo"}
    r.update(over)
    return r


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


class FounderContentFromVerifiedSource(unittest.TestCase):
    """Scenario 1."""

    def test_founder_brief_with_dated_tiered_source_passes(self):
        v = g.validate_write(brief(), CONTRACT, state={"existing": {"DB7": []}})
        self.assertTrue(v.ok, v)


class PageFrameworkContent(unittest.TestCase):
    """Scenario 2: the Page speaks institutionally."""

    def test_page_framework_without_first_person_passes(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                         "translation": translation(surface="LinkedIn - Company Page")})
        p["fields"]["Caption"] = "Every tool encodes a data model, a workflow and an owner assumption."
        p["claims"] = [{"text": "Three checks before any purchase", "kind": "framework"}]
        self.assertTrue(g.validate_write(p, CONTRACT, state={}).ok)

    def test_page_copy_in_first_person_is_refused(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-fx-belief"],
                         "translation": translation(surface="LinkedIn - Company Page")})
        self.assertIn("R15_PAGE_VOICE", g.validate_write(p, CONTRACT, state={}).codes)


class HospitalityBrief(unittest.TestCase):
    """Scenario 3: a pilot-sector brief is ordinary data, never a default."""

    def test_hospitality_brief_with_family_and_sector_passes(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-misconception-more-leads"],
                         "translation": translation(family="nar-misconception-more-leads",
                                                    surface="LinkedIn - Company Page")})
        p["fields"]["Caption"] = "Your OTA commission is not 15 percent. It is closer to 25 to 30."
        p["fields"]["Sub-Sector"] = ["fx-subsector-accommodation"]
        self.assertTrue(g.validate_write(p, CONTRACT, state={}).ok, g.validate_write(p, CONTRACT, state={}))

    def test_family_mismatch_is_refused(self):
        p = brief(links={"opportunity": opportunity(), "narrative_position_ids": ["nar-belief-revenue-is-a-system"],
                         "translation": translation(family="nar-misconception-more-leads")})
        self.assertIn("R06_FAMILY_MISMATCH", g.validate_write(p, CONTRACT, state={}).codes)

    def test_translation_family_must_equal_source_truth(self):
        p = {"db": "DB6", "mode": "CREATE", "actor": "C03",
             "fields": {"Translation": "fx", "Translation Family ID": "nar-a", "Surface": "Not yet assigned",
                        "Editorial DRAGON": "Not yet run"},
             "links": {"opportunity": opportunity(), "platform": "LinkedIn",
                       "source_truth": {"position_id": "nar-b"}},
             "key_values": {"Translation Family ID": "nar-a", "Platform": "LinkedIn",
                            "Surface": "Not yet assigned", "Format": "Carousel"}}
        self.assertIn("R06_FAMILY_MISMATCH", g.validate_write(p, CONTRACT, state={}).codes)

    def test_no_sector_is_legal_and_never_defaults_to_hospitality(self):
        p = brief()
        self.assertNotIn("Sub-Sector", p["fields"])
        self.assertTrue(g.validate_write(p, CONTRACT, state={}).ok)


class MissingEvidence(unittest.TestCase):
    """Scenario 4."""

    def test_fact_without_source_is_refused(self):
        p = brief(claims=[{"text": "Hotels lose 30% to OTAs", "kind": "fact", "sources": []}])
        self.assertIn("R04_UNEVIDENCED", g.validate_write(p, CONTRACT, state={}).codes)

    def test_fact_resting_only_on_t4_is_refused(self):
        p = brief(claims=[verified_fact(tier="T4 Secondary")])
        self.assertIn("R05_T4_SOURCE", g.validate_write(p, CONTRACT, state={}).codes)

    def test_client_outcome_without_proof_is_refused(self):
        p = brief(claims=[{"text": "We grew a client 40%", "kind": "outcome",
                           "sources": [{"id": "x", "tier": "T1 Primary", "verified_at": "2026-10-01"}],
                           "proof_status": "Proof required — named"}])
        self.assertIn("R04_UNPROVEN_OUTCOME", g.validate_write(p, CONTRACT, state={}).codes)

    def test_pricing_claim_without_quotable_offer_is_refused(self):
        p = brief(claims=[{"text": "The audit costs $2,500", "kind": "pricing"}])
        self.assertIn("R16_NO_QUOTABLE_OFFER", g.validate_write(p, CONTRACT, state={}).codes)

    def test_unclassified_claim_is_refused(self):
        p = brief(claims=[{"text": "something", "kind": "vibe"}])
        self.assertIn("R04_UNCLASSIFIED_CLAIM", g.validate_write(p, CONTRACT, state={}).codes)


class DragonPasses(unittest.TestCase):
    """Scenario 5."""

    def opp(self, status, notes=""):
        fields = {"Opportunity": "fx", "Opportunity ID": "fx-opp-9", "Source": "fx source",
                  "Strategic DRAGON": status}
        if notes:
            fields["Strategic DRAGON Notes"] = notes
        return {"db": "DB5", "mode": "CREATE", "actor": "C01", "fields": fields,
                "links": {"source_intelligence": ["fx-finding"]}}

    def test_partial_without_reason_is_refused(self):
        self.assertIn("R07_DRAGON_STATUS", g.validate_write(self.opp("Partial"), CONTRACT, state={}).codes)

    def test_partial_with_reason_passes(self):
        v = g.validate_write(self.opp("Partial", "R: no economic mechanism yet, research named"), CONTRACT, state={})
        self.assertTrue(v.ok, v)

    def test_not_applicable_with_reason_passes(self):
        v = g.validate_write(self.opp("Not applicable", "Terminology note, not a market claim"), CONTRACT, state={})
        self.assertTrue(v.ok, v)

    def test_blank_pass_on_create_is_refused(self):
        p = self.opp("Complete")
        del p["fields"]["Strategic DRAGON"]
        self.assertIn("R07_DRAGON_STATUS", g.validate_write(p, CONTRACT, state={}).codes)

    def test_editorial_before_strategic_is_refused(self):
        p = {"db": "DB6", "mode": "UPDATE", "actor": "C03",
             "fields": {"Editorial DRAGON": "Complete"},
             "links": {"opportunity": opportunity(strategic="Not yet run")}}
        self.assertIn("R08_DRAGON_ORDER", g.validate_write(p, CONTRACT, state={}).codes)

    def test_ready_recommendation_needs_both_passes(self):
        p = brief(mode="UPDATE", recommend_ready_for_design=True,
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

    def test_skill_may_submit_for_review(self):
        p = {"db": "DB7", "mode": "UPDATE", "actor": "C06", "fields": {"G2 Decision": "Submitted for review"}}
        self.assertTrue(g.validate_write(p, CONTRACT, state={}).ok)


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
        state = {"existing": {"DB7": [{"Translation": "fx-tr-001"}]}}
        self.assertIn("R10_DUPLICATE", g.validate_write(brief(), CONTRACT, state=state).codes)

    def test_new_revision_is_an_update_not_a_create(self):
        state = {"existing": {"DB7": [{"Translation": "fx-tr-001"}]}}
        p = brief(mode="UPDATE")
        self.assertTrue(g.validate_write(p, CONTRACT, state=state).ok)

    def test_duplicate_translation_in_family_is_refused(self):
        key = {"Translation Family ID": "nar-a", "Platform": "LinkedIn",
               "Surface": "LinkedIn - Company Page", "Format": "Carousel"}
        p = {"db": "DB6", "mode": "CREATE", "actor": "C03",
             "fields": {"Translation": "fx", "Translation Family ID": "nar-a",
                        "Surface": "LinkedIn - Company Page", "Editorial DRAGON": "Not yet run"},
             "links": {"opportunity": opportunity(), "platform": "LinkedIn",
                       "source_truth": {"position_id": "nar-a"}},
             "key_values": key}
        self.assertIn("R10_DUPLICATE", g.validate_write(p, CONTRACT, state={"existing": {"DB6": [key]}}).codes)

    def test_create_without_natural_key_is_refused(self):
        p = brief(key_values={})
        self.assertIn("R10_NO_NATURAL_KEY", g.validate_write(p, CONTRACT, state={}).codes)


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
        self.assertTrue(g.validate_publication(publication(), approved_brief()).ok)

    def test_missing_native_url_is_refused(self):
        self.assertIn("R14_LINKBACK", g.validate_publication(publication(native_post_url=""), approved_brief()).codes)

    def test_non_linkedin_url_is_refused(self):
        v = g.validate_publication(publication(native_post_url="https://example.com/post/1"), approved_brief())
        self.assertIn("R14_LINKBACK", v.codes)

    def test_surface_drift_is_refused(self):
        v = g.validate_publication(publication(surface="LinkedIn - Company Page"), approved_brief())
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


if __name__ == "__main__":
    unittest.main()
