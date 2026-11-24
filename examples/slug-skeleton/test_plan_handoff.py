"""Structural assertions and a lightweight illustrative handoff check."""
from pathlib import Path
import unittest


def ready_packages(packages, verified):
    return [p["id"] for p in packages if p["role"] and p["deliverable"] and p["evidence"]
            and not p["blocker"] and set(p["depends"]).issubset(verified)
            and not (p.get("qa") and p["qa"] == p["role"])]


class PlanHandoffFixture(unittest.TestCase):
    def test_plan_reference_contains_deliverable_and_dependency_fields(self):
        root = Path(__file__).resolve().parents[2]
        rules = (root / "skills/lg-spec/references/WORKFLOW.md").read_text()
        section = rules.split("### Plan #3 handoff", 1)[1].split("### Context handoff", 1)[0]
        for phrase in ("one-page", "exclusions", "acceptance conditions", "predecessor IDs",
                       "concrete deliverable", "completion evidence", "independent QA",
                       "smallest next eligible step", "not architecture"):
            self.assertIn(phrase, section)

    def test_dependency_missing_evidence_and_self_qa_do_not_look_ready(self):
        spec = dict(id="spec", role="product", deliverable="contract", evidence="pinned doc",
                    depends=[], blocker=None)
        build = dict(id="build", role="dev", qa="reviewer", deliverable="CLI",
                     evidence="acceptance record", depends=["spec"], blocker=None)
        self.assertEqual(ready_packages([spec, build], set()), ["spec"])
        for change in (dict(evidence=""), dict(qa="dev"), dict(blocker="scope unknown")):
            self.assertEqual(ready_packages([build | change], {"spec"}), [])
        self.assertEqual(ready_packages([build], {"spec"}), ["build"])
