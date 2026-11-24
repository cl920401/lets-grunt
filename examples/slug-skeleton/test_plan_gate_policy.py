"""Package assertions for the policy text, not a live agent simulation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
RULES = (ROOT / "skills/lg-spec/references/WORKFLOW.md").read_text()
PLAN = (ROOT / "skills/lg-plan/SKILL.md").read_text()


class PolicyPackage(unittest.TestCase):
    def test_default_and_read_only_capture(self):
        for text in ("default to Authorization mode and the verified project owner",
                     "Choosing a policy does not confirm the first step",
                     "only in authorized durable chat", "authorized Spec step"):
            self.assertIn(text, RULES)
        self.assertIn("without writing files", PLAN)

    def test_and_unsafe_paths_remain_gated(self):
        for text in ("Reverify the policy, scope, actor eligibility", "different initiators",
                     "Independent acceptance is a separate evidence check", "never starts another mode",
                     "Standalone Review retains explicit confirmation", "platform approvals still require",
                     "interruption", "ownership overlaps"):
            self.assertIn(text, RULES)
        for name in ("lg-spec", "lg-build", "lg-refine", "lg-review"):
            self.assertIn("allow_implicit_invocation: false",
                          (ROOT / "skills" / name / "agents/openai.yaml").read_text())
