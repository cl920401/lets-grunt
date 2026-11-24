"""Deterministic paired handoff fixture check; not a model evaluation."""

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
COMMON = {
    "role", "sources", "allowed_paths", "hard_constraints", "expected_checks", "facts",
}
REQUIRED = {
    "external_actions", "non_goals", "invariants", "failure_behavior", "acceptance", "provenance",
}
EXPECTED_SOURCES = {
    "spec": "README.md", "change": "HANDOFF-CHANGE.md", "candidate": "slug.py",
}


def validate_review(packet):
    if packet.keys() != COMMON or packet["role"] != "independent_review":
        raise ValueError("review context contains unexpected fields")
    if packet["hard_constraints"].keys() != REQUIRED or not all(packet["hard_constraints"].values()):
        raise ValueError("missing hard constraints")
    if packet["allowed_paths"] != ["slug.py", "test_skeleton.py"]:
        raise ValueError("unexpected write scope")
    if not packet["expected_checks"] or not packet["facts"]:
        raise ValueError("missing checks or evidence")
    if packet["sources"].keys() != EXPECTED_SOURCES.keys():
        raise ValueError("missing pinned source")
    for key, path in EXPECTED_SOURCES.items():
        source = packet["sources"][key]
        if source["path"] != path or sha256((ROOT / path).read_bytes()).hexdigest() != source["sha256"]:
            raise ValueError("stale or conflicting pinned source")


class HandoffFixture(unittest.TestCase):
    def setUp(self):
        self.dev = json.loads((ROOT / "handoff-development.json").read_text(encoding="utf-8"))
        self.review = json.loads((ROOT / "handoff-review.json").read_text(encoding="utf-8"))

    def test_review_keeps_required_facts_but_not_developer_verdict(self):
        validate_review(self.review)
        self.assertIn("developer_verdict", self.dev)
        self.assertNotIn("developer_verdict", self.review)
        self.assertNotIn("design_notes", self.review)
        self.assertEqual(
            {key: self.dev[key] for key in COMMON - {"role"}},
            {key: self.review[key] for key in COMMON - {"role"}},
        )

    def test_stale_source_is_rejected(self):
        packet = deepcopy(self.review)
        packet["sources"]["spec"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "stale"):
            validate_review(packet)

    def test_missing_constraint_is_rejected(self):
        packet = deepcopy(self.review)
        del packet["hard_constraints"]["failure_behavior"]
        with self.assertRaisesRegex(ValueError, "missing hard constraints"):
            validate_review(packet)

    def test_developer_verdict_is_rejected_in_reviewer_packet(self):
        packet = deepcopy(self.review)
        packet["developer_verdict"] = self.dev["developer_verdict"]
        with self.assertRaisesRegex(ValueError, "unexpected fields"):
            validate_review(packet)
