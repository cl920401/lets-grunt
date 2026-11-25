"""Check the packaged instructions and illustrate the #9 to #10 gate."""
from pathlib import Path
import unittest


def spec_ready_for_build(spec, freeze, walkthrough, confirmation, initiator, *, review=None, conflict=False):
    if not spec or not freeze or not walkthrough or not confirmation or not initiator or conflict:
        return False
    return (
        freeze == walkthrough == review == confirmation["spec"] == spec
        and confirmation["actor"] == initiator
        and confirmation["decision"] == "outcome-meets-needs"
        and bool(confirmation["time"] and confirmation["source"])
    )


class SpecOutcomeGateFixture(unittest.TestCase):
    def setUp(self):
        self.spec = "spec-digest-2"
        self.confirmation = dict(spec=self.spec, actor="verified-initiator",
                                 decision="outcome-meets-needs", time="2026-01-01T00:00:00Z",
                                 source="chat:outcome-reply")
        self.context = dict(spec=self.spec, freeze=self.spec, walkthrough=self.spec,
                            confirmation=self.confirmation, initiator="verified-initiator",
                            review=self.spec)

    def ready(self, **changes):
        return spec_ready_for_build(**(self.context | changes))

    def test_missing_ambiguous_or_conflicting_confirmation_blocks_build(self):
        for record in (None, self.confirmation | {"decision": "looks-good"},
                       self.confirmation | {"decision": "step-approved"},
                       self.confirmation | {"source": ""}, self.confirmation | {"actor": "reviewer"}):
            with self.subTest(record=record):
                self.assertFalse(self.ready(confirmation=record))
        self.assertFalse(self.ready(initiator=None))
        self.assertFalse(self.ready(conflict=True))

    def test_wrong_version_blocks_build_until_matching_evidence_exists(self):
        old = "spec-digest-1"
        for changes in (dict(freeze=old), dict(walkthrough=old), dict(review=old),
                        dict(review=None), dict(confirmation=self.confirmation | {"spec": old})):
            with self.subTest(changes=changes):
                self.assertFalse(self.ready(**changes))
        self.assertTrue(self.ready())

    def test_packaged_entry_points_require_the_handoff(self):
        skills = Path(__file__).resolve().parents[2] / "skills"
        for name, phrase in (
            ("lg-plan", "goal, boundaries and first useful outcome"),
            ("lg-spec", "Spec #9 outcome walkthrough and confirmation"),
            ("lg-build", "Missing, ambiguous, conflicting or wrong-version evidence blocks Build"),
        ):
            with self.subTest(skill=name):
                self.assertIn(phrase, (skills / name / "SKILL.md").read_text())

        workflow = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        spec = workflow.split("### Spec #9 outcome walkthrough and confirmation", 1)[1].split(
            "## Handoff", 1)[0]
        self.assertIn("one typical path and one critical failure or recovery path", spec)
        self.assertIn("fresh confirmation on the new version", spec)
        self.assertIn("read-only reviewer independent of the SPEC authors", spec)
        self.assertIn("recorded pass on substance for that exact version", spec)
        self.assertIn("Reuse complete, verifiable #9 evidence", spec)
        self.assertIn("short result card", spec)
        self.assertRegex(spec, r"After #9 is complete[^\n]+\*\*Manual next step by host\*\*")
        self.assertIn("Record confirmation outside the pinned SPEC", spec)
        build = workflow.split("### A. Skeleton before logic", 1)[1].split(
            "### B. Implementation and acceptance", 1)[0]
        self.assertIn("mark #10 **BLOCKED**", build)
        self.assertIn("whenever entering or resuming Build at any step", build)
        self.assertIn("#10 still requires its own review and authorization", build)
