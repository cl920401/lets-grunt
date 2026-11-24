"""Illustrative deterministic evidence checks, not live model enforcement."""

from dataclasses import dataclass, replace
import unittest


@dataclass(frozen=True)
class Run:
    revision: str = "v2"
    scope: str = "approved CLI"
    artifact: str = "diff-ref"
    command: str = "test-cli"
    environment: str = "disposable target"
    exit_code: int = 0
    assertions: tuple = ("explicit not-implemented behavior",)
    executed: int = 1
    skipped: int = 0
    failed: int = 0
    log: str = "independent-run-ref"
    verifier: str = "qa"
    cached: bool = False


def stage_status(run):
    if not run or run.revision != "v2" or run.scope != "approved CLI":
        return "BLOCKED"
    if not all((run.artifact, run.command, run.environment, run.log, run.verifier)):
        return "BLOCKED"
    if (run.exit_code or run.failed or run.skipped or run.cached or run.executed <= 0
            or "explicit not-implemented behavior" not in run.assertions or run.verifier == "dev"):
        return "BLOCKED"
    return "VERIFIED"


class EvidenceGateFixture(unittest.TestCase):
    def test_unsupported_claim_or_missing_evidence_blocks(self):
        self.assertEqual(stage_status(None), "BLOCKED")
        for field in ("artifact", "command", "log"):
            self.assertEqual(stage_status(replace(Run(), **{field: ""})), "BLOCKED")

    def test_noop_skipped_or_cached_is_not_proof(self):
        for run in (replace(Run(), executed=0), replace(Run(), skipped=1),
                    replace(Run(), assertions=()), replace(Run(), cached=True)):
            self.assertEqual(stage_status(run), "BLOCKED")

    def test_stale_mismatched_or_developer_only_proof_blocks(self):
        for run in (replace(Run(), revision="v1"), replace(Run(), scope="different"),
                    replace(Run(), verifier="dev")):
            self.assertEqual(stage_status(run), "BLOCKED")

    def test_matching_independent_run_verifies(self):
        self.assertEqual(stage_status(Run()), "VERIFIED")
