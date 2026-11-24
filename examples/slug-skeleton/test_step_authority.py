"""Deterministic examples for multi-person step authorization, not a live audit system."""

from dataclasses import dataclass, replace
import unittest


@dataclass(frozen=True)
class Proposal:
    mode: str = "spec"
    step: int = 5
    revision: str = "spec-v1"
    scope: str = "one CLI architecture sketch"
    deliverable: str = "architecture note"
    allowed_paths: tuple = ("docs/ARCH.md",)
    external_actions: tuple = ()


@dataclass(frozen=True)
class Approval:
    proposal: Proposal
    account: str
    confirmation_ref: str
    authority_ref: str


def decide(proposal, approval, *, verified_accounts, scoped_grants, audit_ref):
    if not approval or approval.proposal != proposal or not audit_ref:
        return "BLOCKED"
    if approval.account not in verified_accounts or not approval.confirmation_ref:
        return "BLOCKED"
    grant = (approval.account, approval.authority_ref, proposal)
    return "PASS" if approval.authority_ref and grant in scoped_grants else "BLOCKED"


class StepAuthorityFixture(unittest.TestCase):
    def setUp(self):
        self.proposal = Proposal()
        self.owner = Approval(self.proposal, "owner-id", "msg-123", "grant-456")
        self.facts = dict(
            verified_accounts={"owner-id", "reviewer-id"},
            scoped_grants={("owner-id", "grant-456", self.proposal)},
            audit_ref="audit-789",
        )

    def test_verified_third_party_without_scoped_grant_is_blocked(self):
        reviewer = replace(self.owner, account="reviewer-id")
        self.assertEqual(decide(self.proposal, reviewer, **self.facts), "BLOCKED")

    def test_mismatched_or_absent_evidence_is_blocked(self):
        for approval in (
            None,
            replace(self.owner, confirmation_ref=""),
            replace(self.owner, authority_ref=""),
            replace(self.owner, proposal=replace(self.proposal, revision="spec-v0")),
            replace(self.owner, proposal=replace(self.proposal, allowed_paths=("src/",))),
        ):
            with self.subTest(approval=approval):
                self.assertEqual(decide(self.proposal, approval, **self.facts), "BLOCKED")
        self.assertEqual(decide(self.proposal, self.owner, **dict(self.facts, audit_ref="")), "BLOCKED")

    def test_aligned_identity_scope_evidence_and_record_can_pass(self):
        self.assertEqual(decide(self.proposal, self.owner, **self.facts), "PASS")
