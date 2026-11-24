"""Deterministic authorization examples, not model behavior tests."""

from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class Step:
    key: str
    action: str
    deliverable: str
    allowed_paths: tuple


ARCH = Step("spec-architecture", "draft architecture", "architecture sketch", ("docs/ARCH.md",))
API = Step("spec-api", "draft API", "API contract", ("docs/API.md",))
PROPOSAL_CHANGED = Step(
    "spec-architecture", "draft architecture", "architecture and implementation", ("docs/ARCH.md", "src/")
)


def authorized_step(*, pending, confirmed, counted):
    """Only an explicit match to the exact pending proposal authorizes work."""
    return pending if pending == confirmed and pending.key not in counted else None


class StepConfirmationFixture(unittest.TestCase):
    def test_invocation_or_blanket_approval_cannot_skip(self):
        for confirmation in (None, "run all Spec steps"):
            with self.subTest(confirmation=confirmation):
                self.assertIsNone(authorized_step(pending=ARCH, confirmed=confirmation, counted=set()))

    def test_exact_confirmation_once_then_stop_for_next_step(self):
        self.assertEqual(authorized_step(pending=ARCH, confirmed=ARCH, counted=set()), ARCH)
        self.assertIsNone(authorized_step(pending=ARCH, confirmed=ARCH, counted={ARCH.key}))
        self.assertIsNone(authorized_step(pending=API, confirmed=ARCH, counted={ARCH.key}))
        self.assertEqual(authorized_step(pending=API, confirmed=API, counted={ARCH.key}), API)

    def test_same_id_changed_deliverable_or_paths_requires_new_confirmation(self):
        self.assertIsNone(authorized_step(pending=PROPOSAL_CHANGED, confirmed=ARCH, counted=set()))
