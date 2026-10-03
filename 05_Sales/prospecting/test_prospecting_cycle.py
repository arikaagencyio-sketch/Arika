import copy
import datetime as dt
import tempfile
import unittest
from pathlib import Path
from prospecting_cycle import outside_git, prepare, validate

TODAY = dt.date(2026, 10, 3)


def batch():
    return {"cycle_id": "SYN-TEST", "classification": "PUBLIC_COMPANY_RESEARCH",
            "sources": [{"id": "SRC-1", "url": "https://example.com", "observed_on": "2026-10-03",
                         "review_on": "2026-10-10", "observation": "synthetic company tree"}],
            "companies": [{"company_id": "ORG-TEST", "entity_level": "group", "root_company_id": "ORG-TEST",
                           "parent_company_id": None, "source_ids": ["SRC-1"], "country": "Kenya",
                           "website_url": "https://example.com", "booking_url": "https://example.com/book"},
                          {"company_id": "ORG-TEST-P1", "entity_level": "property", "root_company_id": "ORG-TEST",
                           "parent_company_id": "ORG-TEST", "source_ids": ["SRC-1"], "country": "Kenya"}],
            "accounts": [{"target_company_level_id": "ORG-TEST", "buyer_roles": ["group commercial lead"],
                          "discovery_questions": ["Who owns this decision?"],
                          "contact_route": {"kind": "published_role_inbox", "value": "info@example.com", "source_id": "SRC-1"}}]}


class ProspectingTests(unittest.TestCase):
    def test_group_qualifies_through_sourced_children(self):
        with tempfile.TemporaryDirectory() as folder:
            queue = prepare(batch(), folder, TODAY)
            self.assertEqual(queue["accounts"][0]["offer_route"], "hospitality_group_discovery")
            self.assertFalse(queue["accounts"][0]["mvp_size_fit_only"])
            self.assertEqual(queue["sent_count"], 0)

    def test_missing_children_is_evidence_gap_not_anti_icp(self):
        data = batch()
        data["companies"].pop()
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(prepare(data, folder, TODAY)["accounts"][0]["fit"], "needs_child_structure")

    def test_cycle_refused(self):
        data = batch()
        data["companies"][0]["parent_company_id"] = "ORG-TEST-P1"
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate(data, TODAY)

    def test_missing_source_refused(self):
        data = batch()
        data["companies"][0]["source_ids"] = ["missing"]
        with self.assertRaisesRegex(ValueError, "registered public sources"):
            validate(data, TODAY)

    def test_expired_source_refused(self):
        data = batch()
        data["sources"][0]["review_on"] = "2026-10-02"
        with self.assertRaisesRegex(ValueError, "review window"):
            validate(data, TODAY)

    def test_named_contact_refused(self):
        data = batch()
        data["accounts"][0]["contact_route"]["kind"] = "named_person_email"
        with self.assertRaisesRegex(ValueError, "Named/private"):
            validate(data, TODAY)

    def test_git_destination_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / ".git").mkdir()
            with self.assertRaisesRegex(ValueError, "outside every Git"):
                outside_git(Path(folder) / "queue")

    def test_preparation_preserves_existing_history(self):
        with tempfile.TemporaryDirectory() as folder:
            first = prepare(batch(), folder, TODAY)
            self.assertEqual(prepare(batch(), folder, TODAY), first)
            altered = copy.deepcopy(batch())
            altered["accounts"][0]["buyer_roles"] = ["different role"]
            with self.assertRaisesRegex(ValueError, "Batch changed"):
                prepare(altered, folder, TODAY)


if __name__ == "__main__":
    unittest.main()
