"""Deterministic examples for the prior-step self-review gate."""

from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class Evidence:
    scope_ok: bool
    expected_artifact: bool
    version: str
    material_gaps: tuple = ()
    justified_na: bool = False


def ready(*, prior_required, expected_version, evidence, prerequisites_ok=True):
    if not prior_required:
        return prerequisites_ok
    if not evidence or not evidence.scope_ok or evidence.material_gaps:
        return False
    if evidence.version != expected_version:
        return False
    return evidence.expected_artifact or evidence.justified_na


class PriorStepFixture(unittest.TestCase):
    def test_missing_failed_or_stale_previous_evidence_blocks_next(self):
        invalid = (
            None,
            Evidence(False, True, "pinned"),
            Evidence(True, False, "pinned"),
            Evidence(True, True, "older"),
            Evidence(True, True, "pinned", ("unresolved material issue",)),
        )
        for evidence in invalid:
            with self.subTest(evidence=evidence):
                self.assertFalse(ready(prior_required=True, expected_version="pinned", evidence=evidence))

    def test_exact_evidence_or_justified_na_can_propose_but_not_approve(self):
        for evidence in (Evidence(True, True, "pinned"), Evidence(True, False, "pinned", justified_na=True)):
            self.assertTrue(ready(prior_required=True, expected_version="pinned", evidence=evidence))

    def test_first_step_requires_only_available_prerequisites(self):
        self.assertTrue(ready(prior_required=False, expected_version=None, evidence=None))
        self.assertFalse(ready(prior_required=False, expected_version=None, evidence=None, prerequisites_ok=False))
