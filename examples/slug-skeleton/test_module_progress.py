"""Examples that keep development and independent acceptance separate."""

import unittest


def acceptance_status(module):
    evidence = module["independent_evidence"]
    if evidence is None or evidence["version"] != module["candidate"]:
        return "BLOCKED"
    return evidence["status"]


class ModuleProgressFixture(unittest.TestCase):
    def test_development_done_does_not_imply_independent_qa_pass(self):
        module = {"dev": "done", "candidate": "v1", "independent_evidence": None}
        self.assertEqual(acceptance_status(module), "BLOCKED")

    def test_stale_qa_is_not_carried_forward_to_new_candidate(self):
        module = {
            "dev": "done",
            "candidate": "v2",
            "independent_evidence": {"version": "v1", "status": "PASS"},
        }
        self.assertEqual(acceptance_status(module), "BLOCKED")
        module["independent_evidence"]["version"] = "v2"
        self.assertEqual(acceptance_status(module), "PASS")
