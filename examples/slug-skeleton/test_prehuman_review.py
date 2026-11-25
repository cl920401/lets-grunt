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
    source: str = "review-session:original-result"
    independent: bool = True
    read_only: bool = True


def can_ask_human(review, *, executor, expected):
    if not review or not review.reviewer or review.reviewer == executor:
        return False
    actual = (review.candidate, review.proposal, review.prior_evidence)
    return (actual == expected and review.verdict == "PASS"
            and bool(review.source) and review.independent and review.read_only)


class PreHumanReviewFixture(unittest.TestCase):
    def test_exact_independent_review_or_no_request(self):
        review = Review()
        facts = dict(executor="executor", expected=("rev-1", "scope-1", "prior-1"))
        self.assertTrue(can_ask_human(review, **facts))
        for invalid in (None, replace(review, verdict="FAIL"), replace(review, proposal="old"),
                        replace(review, candidate="old"), replace(review, prior_evidence="old"),
                        replace(review, reviewer="executor"), replace(review, reviewer=""),
                        replace(review, source=""), replace(review, independent=False),
                        replace(review, read_only=False)):
            self.assertFalse(can_ask_human(invalid, **facts))

    def test_original_results_can_be_reused_across_review_contexts(self):
        for source in ("review-session:result", "peer-review:original-comment"):
            with self.subTest(source=source):
                self.assertTrue(can_ask_human(Review(source=source), executor="executor",
                                             expected=("rev-1", "scope-1", "prior-1")))

    def test_first_step_requires_scope_review_and_review_is_not_confirmation(self):
        root = Path(__file__).resolve().parents[2]
        workflow = (root / "skills/lg-spec/references/WORKFLOW.md").read_text()
        section = workflow.split("## Independent review before asking a human", 1)[1].split(
            "## Authority", 1)[0]
        for phrase in ("first step", "still review the proposed scope", "only after",
                       "minimum deliverable", "full outcome review for Spec #9",
                       "Tool names and receipt formats can vary",
                       "neither step confirmation nor the later independent acceptance"):
            self.assertIn(phrase, section)
