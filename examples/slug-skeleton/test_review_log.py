"""Structural checks for the evidence template and reviewer write boundaries."""
from pathlib import Path
import unittest


class ReviewLogPackage(unittest.TestCase):
    def test_discoverable_record_template_keeps_result_types_separate(self):
        root = Path(__file__).resolve().parents[2]
        ref = root / "skills/lg-spec/references"
        template = (ref / "REVIEW_LOG.md").read_text(encoding="utf-8")
        for value in ("self-check", "independent pre-review", "formal confirmation",
                      "independent QA", "Actor role / ID", "Original trace / time",
                      "Exact revision and scope", "PASS, FAIL and BLOCKED"):
            self.assertIn(value, template)
        rules = (ref / "WORKFLOW.md").read_text(encoding="utf-8")
        self.assertIn("one discoverable project review log", rules)
        self.assertIn("they do not write the project log", rules)
        self.assertIn("Plan and standalone Review return the current note in chat", rules)
        self.assertIn("no fictitious reviewer or trace", rules)
