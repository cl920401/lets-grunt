"""Package assertions for the policy text, not a live agent simulation."""
from hashlib import sha256
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
RULES = (ROOT / "skills/lg-spec/references/WORKFLOW.md").read_text()
PLAN = (ROOT / "skills/lg-plan/SKILL.md").read_text()


def native_plan_gate(host, actual_primary_agent):
    return host != "OpenCode" or actual_primary_agent == "plan"


class PolicyPackage(unittest.TestCase):
    def test_default_and_read_only_capture(self):
        for text in ("default to Authorization mode and the verified project owner",
                     "Choosing a policy does not confirm the first step",
                     "only in authorized durable chat", "authorized Spec step"):
            self.assertIn(text, RULES)
        self.assertIn("without writing files", PLAN)

    def test_known_project_root_and_mode_do_not_replace_step_approval(self):
        spec = (ROOT / "skills/lg-spec/SKILL.md").read_text()
        for entry in (PLAN, spec):
            self.assertIn("Mode 2 means Trust with confirmation from any one verified eligible", entry)
            self.assertIn("A known root or mode does not authorize a numbered step or outside access", entry)
        self.assertIn("Carry a verified choice from Plan into Spec without repeating the question", RULES)
        self.assertIn("Ask only if the root cannot be verified or the sources conflict", RULES)

    def test_plan_reference_loads_from_its_own_packaged_directory(self):
        plan_dir = ROOT / "skills/lg-plan"
        entry = (plan_dir / "SKILL.md").read_text()
        reference, = re.findall(r"`([^`]*WORKFLOW\.md)`", entry)
        expected, = re.findall(r"^Workflow SHA-256: ([0-9a-f]{64})$", entry, re.MULTILINE)
        bundled = plan_dir / reference
        self.assertEqual(reference, "references/WORKFLOW.md")
        self.assertTrue(bundled.resolve().is_relative_to(plan_dir.resolve()))
        self.assertFalse(bundled.is_symlink())
        self.assertEqual(sha256(bundled.read_bytes()).hexdigest(), expected)
        self.assertIn("If no verified copy is available, report the missing reference and stop", entry)

    def test_opencode_native_gate_uses_actual_agent_not_skill_attachment(self):
        for agent in ("build", "other", None):
            with self.subTest(agent=agent):
                self.assertFalse(native_plan_gate("OpenCode", agent))
        self.assertTrue(native_plan_gate("OpenCode", "plan"))
        self.assertTrue(native_plan_gate("Codex", None))
        self.assertTrue(native_plan_gate("DSH", None))

    def test_opencode_entry_checks_agent_before_project_work(self):
        check = PLAN.split("**OpenCode only.**", 1)[1].split("Follow **Step gate", 1)[0]
        for phrase in ("Before any project read, search or independent review",
                       "without filesystem probes", "loaded skill attachment", "stop at a chat reply",
                       "open `/agents`, select **Plan**, then resubmit",
                       "Preserve the existing filesystem and step permissions",
                       "Native Plan selection alone cannot establish filesystem isolation"):
            self.assertIn(phrase, check)
        self.assertIn("select it manually before invoking the next skill", RULES)

    def test_and_unsafe_paths_remain_gated(self):
        for text in ("Reverify the policy, scope, actor eligibility", "different initiators",
                     "Independent acceptance is a separate evidence check", "never starts another mode",
                     "Standalone Review retains explicit confirmation", "platform approvals still require",
                     "interruption", "ownership overlaps"):
            self.assertIn(text, RULES)
        for name in ("lg-spec", "lg-build", "lg-refine", "lg-review"):
            self.assertIn("allow_implicit_invocation: false",
                          (ROOT / "skills" / name / "agents/openai.yaml").read_text())
