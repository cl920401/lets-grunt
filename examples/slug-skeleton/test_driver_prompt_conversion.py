"""Illustrative driver routing; no model call, host invocation or approval."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


def route(text, *, in_flight=False, probe=False, isolated=True, material_unknown=False):
    if in_flight:
        return "NO DISPATCH", None
    if probe:
        return ("VERBATIM TEST", text) if isolated else ("NO DISPATCH", None)
    if material_unknown:
        return "ASK", None
    return "SCOPED DISPATCH", text


class DriverPromptConversion(unittest.TestCase):
    def test_casual_intent_goes_to_conversion_without_a_form(self):
        self.assertEqual(route("先把并发那块做扎实")[0], "SCOPED DISPATCH")
        self.assertEqual(route("给我跑一下看看", material_unknown=True), ("ASK", None))

    def test_deliberate_ambiguity_is_verbatim_or_not_sent(self):
        text = "差不多能用了就交我。"
        self.assertEqual(route(text, probe=True), ("VERBATIM TEST", text))
        self.assertEqual(route(text, probe=True, isolated=False), ("NO DISPATCH", None))

    def test_accepted_action_must_not_dispatch_again(self):
        self.assertEqual(route("继续", in_flight=True), ("NO DISPATCH", None))

    def test_stage_and_project_risk_change_emphasis_not_authority(self):
        skill = (ROOT / "driver/lg-drive/SKILL.md").read_text()
        for case in ("Plan scopes", "Spec turns", "Build chooses", "Review looks",
                     "Refine preserves", "outcome to prove", "constraints that must hold",
                     "plausible failure consequences", "cheapest conclusive check",
                     "Project labels and examples are hints, not categories or rules",
                     "not a change to acceptance",
                     "Do not inject these inferences into a deliberate ambiguity test"):
            with self.subTest(case=case):
                self.assertIn(case, skill)

    def test_driver_shipped_separately_and_keeps_boundaries(self):
        path = ROOT / "driver/lg-drive/SKILL.md"
        adapter = path.read_text()
        for rule in ("before each outbound task", "does not fill a template",
                     "sender's real role", "unproven fact stays unknown",
                     "recommended option and trade-off", "preserve their tested wording verbatim",
                     "Conversion alone does not permit sending or prove delivery"):
            self.assertIn(rule, adapter)
        self.assertFalse((ROOT / "skills/lg-drive").exists())
