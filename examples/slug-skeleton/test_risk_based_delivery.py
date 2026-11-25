"""Illustrative policy fixtures; these do not exercise a live agent."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


def proof_status(*, required, candidate_matches, prerequisites_ready, ran, passed):
    if not required:
        return "NOT APPLICABLE"
    if not candidate_matches or not prerequisites_ready or not ran:
        return "BLOCKED"
    return "VERIFIED" if passed else "FAILED"


def disposition(*, required_evidence, changes_contract, material_risk):
    return "BLOCKING" if required_evidence or changes_contract or material_risk else "ADVICE"


def eligible_packages(packages, proven):
    return [name for name, dependencies in packages.items() if dependencies <= proven]


class RiskBasedDeliveryFixture(unittest.TestCase):
    def test_product_failure_is_not_a_missing_environment(self):
        for label, p in (("offline client", False), ("loaded service", True),
                         ("migration rehearsal", False)):
            with self.subTest(project=label):
                self.assertEqual(proof_status(required=True, candidate_matches=True,
                                 prerequisites_ready=p, ran=False, passed=False), "BLOCKED")
        self.assertEqual(proof_status(required=True, candidate_matches=True,
                         prerequisites_ready=True, ran=True, passed=False), "FAILED")
        self.assertEqual(proof_status(required=True, candidate_matches=False,
                         prerequisites_ready=True, ran=True, passed=True), "BLOCKED")
        self.assertEqual(proof_status(required=False, candidate_matches=True,
                         prerequisites_ready=True, ran=False, passed=False), "NOT APPLICABLE")

    def test_skips_optional_polish_but_stops_real_risk(self):
        for label, flags, wanted in (
                ("wording", (False, False, False), "ADVICE"),
                ("changed client promise", (False, True, False), "BLOCKING"),
                ("oversell/retry", (False, False, True), "BLOCKING"),
                ("migration rollback not exercised", (True, False, False), "BLOCKING")):
            with self.subTest(case=label):
                d = disposition(required_evidence=flags[0], changes_contract=flags[1],
                                material_risk=flags[2])
                self.assertEqual(d, wanted)

    def test_only_dependencies_really_missing_should_wait(self):
        for packages, ready in (
                ({"edit": set(), "device acceptance": {"device"}}, ["edit"]),
                ({"service invariant": set(), "load validation": {"dataset"}}, ["service invariant"]),
                ({"reconciliation fixture": set(), "rollout": {"recovery"}}, ["reconciliation fixture"])):
            self.assertEqual(eligible_packages(packages, set()), ready)

    def test_entrypoints_use_risk_and_delta_rules_without_hardcoding_project_shape(self):
        workflow = (ROOT / "skills/lg-spec/references/WORKFLOW.md").read_text()
        for rule in ("Scope the change, not the whole system", "observable pass/fail",
                     "Do not force rollout machinery onto a small reversible change",
                     "Reuse unaffected evidence only when the candidate and dependency match",
                     "missing prerequisite evidence is a blocker for that check, not a product failure"):
            with self.subTest(rule=rule):
                self.assertIn(rule.lower(), workflow.lower())
        sample = (ROOT / "examples/risk-based-delivery.md").read_text()
        for shape in ("单机客户端", "高并发服务", "数据迁移", "小而可逆"):
            self.assertIn(shape, sample)
