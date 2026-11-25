from pathlib import Path
import unittest


class BuildFocusPolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[2] / "skills"
        cls.entry = (root / "lg-build/SKILL.md").read_text()
        cls.flow = (root / "lg-spec/references/WORKFLOW.md").read_text()

    def test_work_split_stays_optional_bounded_and_integrated(self):
        self.assertIn("Parallel work, one real outcome", self.entry)
        for rule in ("highest-risk commitment", "disjoint write paths",
                     "one contract owner and one integration owner",
                     "not permission to add a service", "omit an irrelevant lane",
                     "run the primary scenario at #14",
                     "independently retest and accept the same candidate at #15–16"):
            with self.subTest(rule=rule):
                self.assertIn(rule, self.flow)

    def test_review_prioritization_does_not_waive_hard_gates(self):
        for rule in ("A finding blocks only the affected scope",
                     "Record editorial and reversible implementation choices without blocking",
                     "Do not downgrade an existing hard gate",
                     "independent reviewer must verify the same skeleton version"):
            with self.subTest(rule=rule):
                self.assertIn(rule, self.flow + self.entry)

    def test_driver_resumes_from_evidence_without_replay(self):
        self.assertIn("Driver handoff", self.entry)
        for rule in ("last verified evidence", "one eligible action",
                     "Do not resend in-flight work", "unrelated already authorized work",
                     "No new phase, paths or permissions follow from a timer"):
            with self.subTest(rule=rule):
                self.assertIn(rule, self.flow)
