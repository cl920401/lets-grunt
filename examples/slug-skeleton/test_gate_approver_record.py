"""Package contract: these checks inspect the documentation, not live identity."""
from pathlib import Path
import unittest


class ApproverRecordPackage(unittest.TestCase):
    def test_both_modes_require_a_verifiable_human_record(self):
        root = Path(__file__).resolve().parents[2]
        reference = root / "skills/lg-spec/references"
        workflow = (reference / "WORKFLOW.md").read_text()
        audit = (reference / "CHANGE.md").read_text()
        for phrase in ("Every step in **both modes** requires a fresh actual confirmation",
                       "counting each verified principal once", "An executor cannot confirm its own step",
                       "A standing grant", "revoked, stale or out-of-scope", "**BLOCKED**",
                       "only in an authorized Spec step", "AI cannot grant it"):
            self.assertIn(phrase, workflow)
        self.assertIn("Distinguish confirmer, grantor, executor", audit)


def has_quorum(votes, *, step, executor, eligible, required, hard_external=False, required_types=(), required_actors=(),
               veto_actors=(), objections=(), unresolved_conflict=False):
    """Synthetic checklist example, not a production identity verifier."""
    accepted = {actor for actor, evidence, confirmed_step, role in votes
                if actor != executor and eligible.get(actor) == role and evidence
                and confirmed_step == step and not hard_external}
    return (not unresolved_conflict and not set(objections).intersection((*required_actors, *veto_actors))
            and set(required_actors).issubset(accepted) and len(accepted) >= required
            and set(required_types).issubset({eligible[actor] for actor in accepted}))


class ConfirmationExamples(unittest.TestCase):
    def test_step_receipts_not_grants_or_self_approval(self):
        facts = dict(step="spec@v2", executor="worker", required=2,
                     eligible={"worker": "ai", "owner": "human", "reviewer": "ai"})
        owner = ("owner", "msg-1", "spec@v2", "human")
        reviewer = ("reviewer", "session-2", "spec@v2", "ai")
        for invalid in ([], [owner, owner], [owner, ("worker", "msg-2", "spec@v2", "ai")],
                        [owner, ("reviewer", "", "spec@v2", "ai")],
                        [owner, ("reviewer", "session-2", "spec@v1", "ai")],
                        [owner, ("outsider", "msg-3", "spec@v2", "human")]):
            self.assertFalse(has_quorum(invalid, **facts))
        self.assertTrue(has_quorum([owner, reviewer], **facts))
        self.assertFalse(has_quorum([owner, reviewer], **facts, hard_external=True))


    def test_enough_assents_cannot_override_required_denial_or_role_composition(self):
        actors = {"owner": "human", "peer": "human", "qa": "ai"}
        votes = [(actor, "receipt-" + actor, "v2", role) for actor, role in actors.items()]
        facts = dict(step="v2", executor="worker", eligible=actors, required=2,
                     required_types=("human", "ai"), required_actors=("owner",))
        self.assertTrue(has_quorum(votes, **facts))
        self.assertFalse(has_quorum(votes[:2], **facts))
        self.assertFalse(has_quorum(votes, **facts, objections=("owner",)))
        self.assertFalse(has_quorum(votes, **facts, objections=("qa",), veto_actors=("qa",)))
        self.assertFalse(has_quorum(votes, **facts, unresolved_conflict=True))
