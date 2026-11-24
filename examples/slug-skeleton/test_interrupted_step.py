"""Deterministic cases for preventing replay after interruption."""

import unittest


def next_action(*, active_owner, proposed_owner, overlapping_owner, state, fresh_recovery=False):
    if active_owner != proposed_owner or overlapping_owner:
        return "BLOCKED_OWNER"
    if state == "complete":
        return "RECORD_ONLY"
    if state in {"unknown", "interrupted"}:
        if state == "interrupted" and fresh_recovery:
            return "RECOVERY_ONLY"
        return "BLOCKED_RECONCILE"
    return "START"


class InterruptedStepFixture(unittest.TestCase):
    def setUp(self):
        self.scope = dict(active_owner="dev-a", proposed_owner="dev-a", overlapping_owner=False)

    def test_duplicate_owner_or_overlapping_writer_cannot_start(self):
        self.assertEqual(next_action(**dict(self.scope, proposed_owner="dev-b"), state="new"), "BLOCKED_OWNER")
        self.assertEqual(next_action(**dict(self.scope, overlapping_owner=True), state="new"), "BLOCKED_OWNER")

    def test_interruption_blocks_replay_and_unknown_state_blocks_recovery(self):
        self.assertEqual(next_action(**self.scope, state="interrupted"), "BLOCKED_RECONCILE")
        self.assertEqual(next_action(**self.scope, state="unknown", fresh_recovery=True), "BLOCKED_RECONCILE")
        self.assertEqual(next_action(**self.scope, state="interrupted", fresh_recovery=True), "RECOVERY_ONLY")

    def test_completed_step_records_evidence_without_rerunning(self):
        self.assertEqual(next_action(**self.scope, state="complete"), "RECORD_ONLY")
