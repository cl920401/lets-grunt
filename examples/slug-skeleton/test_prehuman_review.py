"""Structural policy and synthetic pre-review checks, not agent execution."""
from dataclasses import dataclass, replace
from pathlib import Path
import unittest


@dataclass(frozen=True)
class Review:
    reviewer: str = "independent"
    candidate: str = "rev-1"
    proposal: str = "scope-1"
    prior_evidence: str = "prior-1"
    verdict: str = "PASS"


def can_ask_human(review, *, executor, expected, subagent_available):
    if not subagent_available or not review or not review.reviewer or review.reviewer == executor:
        return False
    actual = (review.candidate, review.proposal, review.prior_evidence)
    return actual == expected and review.verdict == "PASS"


class PreHumanReviewFixture(unittest.TestCase):
    def test_exact_independent_review_or_no_request(self):
        review = Review()
        facts = dict(executor="executor", expected=("rev-1", "scope-1", "prior-1"),
                     subagent_available=True)
        self.assertTrue(can_ask_human(review, **facts))
        for invalid in (None, replace(review, verdict="FAIL"), replace(review, proposal="old"),
                        replace(review, candidate="old"), replace(review, prior_evidence="old"),
                        replace(review, reviewer="executor"), replace(review, reviewer="")):
            self.assertFalse(can_ask_human(invalid, **facts))
        self.assertFalse(can_ask_human(review, **(facts | {"subagent_available": False})))

    def test_first_step_requires_scope_review_and_review_is_not_confirmation(self):
        root = Path(__file__).resolve().parents[2]
        workflow = (root / "skills/lg-spec/references/WORKFLOW.md").read_text()
        section = workflow.split("## Independent review before asking a human", 1)[1].split(
            "## Authority", 1)[0]
        for phrase in ("first step", "still review the proposed scope", "only after",
                       "neither step confirmation nor the later independent acceptance"):
            self.assertIn(phrase, section)
