"""Structural and synthetic checks for project scoping, with no host sandbox claims."""
from hashlib import sha256
from pathlib import Path, PurePosixPath
import posixpath
import unittest


PROJECT = PurePosixPath("/work/project")


def allowed(accesses, *, bounded, approvals=()):
    """Model a fully enumerated tool call, including any resolved targets."""
    if not bounded:
        return False
    for operation, path in accesses:
        target = PurePosixPath(posixpath.normpath(PROJECT / path))
        if not target.is_relative_to(PROJECT) and (operation, target) not in approvals:
            return False
    return True


class ProjectFilesystemBoundaryFixture(unittest.TestCase):
    def test_project_paths_and_traversal(self):
        self.assertTrue(allowed([("read", "docs/SPEC.md"), ("write", "docs/new.md")],
                                bounded=True))
        for path in ("../sibling/SPEC.md", "/work/project-copy/SPEC.md", "/home/user"):
            with self.subTest(path=path):
                self.assertFalse(allowed([("search", path)], bounded=True))

    def test_external_link_targets_and_toolchain_paths_need_exact_scope(self):
        sdk = PurePosixPath("/home/user/flutter/cache")
        accesses = [("read", "docs/sdk-link"), ("read", sdk)]
        self.assertFalse(allowed(accesses, bounded=True))
        self.assertTrue(allowed(accesses, bounded=True, approvals={("read", sdk)}))
        self.assertFalse(allowed([("write", sdk)], bounded=True, approvals={("read", sdk)}))
        self.assertFalse(allowed([("read", sdk.parent)], bounded=True, approvals={("read", sdk)}))

    def test_unknown_reviewer_scope_blocks_only_that_operation(self):
        self.assertFalse(allowed([("search", ".")], bounded=False))
        self.assertTrue(allowed([("read", "docs/SPEC.md")], bounded=True))

    def test_project_workflow_fallback_needs_scope_and_matching_content(self):
        content = b"matching workflow"
        expected = sha256(content).digest()

        def matching_project_copy(path, data):
            return (allowed([("read", path)], bounded=True)
                    and sha256(data).digest() == expected)

        self.assertTrue(matching_project_copy("docs/WORKFLOW.md", content))
        self.assertFalse(matching_project_copy("docs/WORKFLOW.md", b"older workflow"))
        self.assertFalse(matching_project_copy("../sibling/WORKFLOW.md", content))
        self.assertFalse(matching_project_copy("/home/user/WORKFLOW.md", content))

    def test_plan_spec_and_review_reference_the_same_boundary(self):
        skills = Path(__file__).resolve().parents[2] / "skills"
        for name in ("lg-plan", "lg-spec"):
            with self.subTest(skill=name):
                entry = (skills / name / "SKILL.md").read_text()
                self.assertIn("Project filesystem boundary", entry)
                self.assertIn("project initiator's explicit approval", entry)
        workflow = (skills / "lg-spec/references/WORKFLOW.md").read_text()
        for phrase in ("verified physical project root", "executor, independent reviewers",
                       "Stop before following a symlink", "home-directory scans",
                       "Flutter caches", "read-only mode are insufficient",
                       "Verify the actual scope before dispatch", "continue other authorized work",
                       "Before dispatch or reuse, verify compliance"):
            self.assertIn(phrase, workflow)
