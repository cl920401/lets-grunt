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

    def test_spec_events_have_separate_types_and_handoff_links(self):
        ref = Path(__file__).resolve().parents[2] / "skills/lg-spec/references"
        log = (ref / "REVIEW_LOG.md").read_text(encoding="utf-8")
        change = (ref / "CHANGE.md").read_text(encoding="utf-8")
        for event in ("Independent Spec Review", "Spec paper walkthrough",
                      "Initiator outcome confirmation"):
            self.assertIn(f"**{event}**", log)
            self.assertIn(f"| {event} (#9) |", change)
        self.assertIn("formal confirmation type only for numbered-step authorization", log)
