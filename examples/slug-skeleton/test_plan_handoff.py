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


def decision_surface(material_choice, delivery):
    if not material_choice:
        return None
    if delivery in ("unavailable", "confirmed-unsent"):
        return "text"
    if delivery == "sent":
        return "card"
    return "check-delivery"


def manual_handoff(complete, skill_id, verified_entry=None):
    if not complete:
        return None
    return verified_entry or f"Manually load {skill_id}."


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

    def test_plan_keeps_user_handoff_short_and_the_switch_manual(self):
        skills = Path(__file__).resolve().parents[2] / "skills"
        plan = (skills / "lg-plan/SKILL.md").read_text()
        for phrase in ("minimum observable acceptance", "Leave UI details, algorithms",
                       "**Manual next step by host**", "reversible defaults without asking",
                       "only about material unresolved choices"):
            self.assertIn(phrase, plan)
        workflow = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        self.assertIn("Keep the numbered milestones and technical audit in the working record", workflow)

    def test_plan_and_spec_show_design_before_user_decisions(self):
        skills = Path(__file__).resolve().parents[2] / "skills"
        for name in ("lg-plan", "lg-spec"):
            with self.subTest(skill=name):
                entry = (skills / name / "SKILL.md").read_text()
                self.assertIn("**Plan and Spec reply order**", entry)
                self.assertIn("**Needs your decision**", entry)
                self.assertIn("keep the handoff open", entry.lower())

        rules = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        order = rules.split("### Plan and Spec reply order", 1)[1].split("## Specification", 1)[0]
        self.assertLess(order.index("confirmed decisions first"), order.index("Needs your decision"))
        for phrase in ("reversible assumptions inline", "viable options and their main impact",
                       "information needed to answer it in this section",
                       "Omit this section if there are no product decisions"):
            self.assertIn(phrase, order)

    def test_required_replies_keep_the_handoff_open_and_separate(self):
        rules = (Path(__file__).resolve().parents[2] /
                 "skills/lg-spec/references/WORKFLOW.md").read_text()
        order = rules.split("### Plan and Spec reply order", 1)[1].split("## Specification", 1)[0]
        for phrase in ("separate end labels for step authorization, initiator confirmation and evidence",
                       "which dependent work is paused", "leave the handoff open",
                       "After the phase is complete", "manual next-step hint on the last line"):
            self.assertIn(phrase, order)
        self.assertIn("under a separate initiator confirmation label", rules)

    def test_product_choice_uses_one_surface_and_checks_uncertain_delivery(self):
        self.assertIsNone(decision_surface(False, "unavailable"))
        self.assertEqual(decision_surface(True, "sent"), "card")
        self.assertEqual(decision_surface(True, "unavailable"), "text")
        self.assertEqual(decision_surface(True, "confirmed-unsent"), "text")
        self.assertEqual(decision_surface(True, "unknown"), "check-delivery")

    def test_handoff_uses_verified_capability_or_plain_text_only_when_complete(self):
        entry = "Choose Spec in the workspace skill picker."
        self.assertEqual(manual_handoff(True, "lg-spec", entry), entry)
        self.assertEqual(manual_handoff(True, "lg-build"), "Manually load lg-build.")
        self.assertIsNone(manual_handoff(False, "lg-spec", entry))

        skills = Path(__file__).resolve().parents[2] / "skills"
        for name in ("lg-plan", "lg-spec", "lg-build", "lg-refine"):
            with self.subTest(skill=name):
                text = (skills / name / "SKILL.md").read_text()
                self.assertIn("**Manual next step by host**", text)
                self.assertNotRegex(text, r"\$lg-")

        workflow = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        section = workflow.split("### Manual next step by host", 1)[1].split("## Specification", 1)[0]
        self.assertIn("plain-language instruction", section)
        self.assertIn("Leave invocation and native-agent selection to the user", section)
        self.assertNotRegex(workflow, r"\$lg-")
