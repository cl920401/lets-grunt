"""Structural assertions and a lightweight illustrative handoff check."""
from pathlib import Path
import unittest


def ready_packages(packages, verified):
    return [p["id"] for p in packages if p["role"] and p["deliverable"] and p["evidence"]
            and not p["blocker"] and set(p["depends"]).issubset(verified)
            and not (p.get("qa") and p["qa"] == p["role"])]


def missing_input_action(*, reversible_detail=False, material=False, missing_gate=False,
                         authorized_step=True):
    if material or missing_gate or not authorized_step or not reversible_detail:
        return "pause"
    return "provisional-assumption"


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

    def test_plan_to_spec_missing_outcome_vs_reversible_detail(self):
        self.assertEqual(missing_input_action(material=True), "pause")
        self.assertEqual(missing_input_action(reversible_detail=True), "provisional-assumption")

    def test_spec_to_build_assumptions_require_in_contract_authorized_work(self):
        self.assertEqual(missing_input_action(reversible_detail=True), "provisional-assumption")
        for extra in (dict(material=True), dict(missing_gate=True), dict(authorized_step=False)):
            with self.subTest(extra=extra):
                self.assertEqual(missing_input_action(reversible_detail=True, **extra), "pause")

    def test_transition_rules_reuse_evidence_and_route_material_gaps(self):
        skills = Path(__file__).resolve().parents[2] / "skills"
        title = "Plan, Spec and Build transitions"
        for name in ("lg-plan", "lg-spec", "lg-build"):
            with self.subTest(skill=name):
                self.assertIn(title, (skills / name / "SKILL.md").read_text())
        workflow = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        section = workflow.split(f"### {title}", 1)[1].split("## Specification", 1)[0]
        for phrase in ("verifiable discussion", "separate from anything the initiator confirmed",
                       "only that input", "explicitly", "exact Spec step", "is always B"):
            self.assertIn(phrase, section)
