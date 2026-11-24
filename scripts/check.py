"""Check the Let's Grunt package using Python's standard library."""
from pathlib import Path
import re
import subprocess
import sys


def verify(test, message):
    if not test:
        raise SystemExit(message)


root = Path(__file__).resolve().parents[1]
expected = {"lg-plan", "lg-spec", "lg-build", "lg-refine"}
skills = root / "skills"
entries = sorted(skills.glob("*/SKILL.md"))
verify(len(entries) == 4 and {p.parent.name for p in entries} == expected,
       "expected exactly four skill entries")
common = skills / "lg-spec" / "WORKFLOW.md"
verify(common.is_file(), "missing shared workflow")
for entry in entries:
    verify(entry.is_file() and not entry.is_symlink() and not entry.parent.is_symlink(),
           f"nonregular skill entry: {entry}")
    text = entry.read_text(encoding="utf-8")
    front = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
    verify(front is not None and front[1] == entry.parent.name and front[2].strip(),
           f"bad frontmatter in {entry}")
    target = next((s for s in re.findall(r"`([^`]*WORKFLOW\.md)`", text)), None)
    verify(target is not None and (entry.parent / target).resolve() == common.resolve(),
           f"bad shared workflow reference in {entry}")
    policy = entry.parent / "agents" / "openai.yaml"
    if entry.parent.name == "lg-plan":
        verify(not policy.exists(), "Plan should use the host's default policy")
    else:
        verify(policy.is_file() and not policy.is_symlink()
               and policy.read_text(encoding="utf-8") == "policy:\n  allow_implicit_invocation: false\n",
               f"missing explicit invocation policy in {entry.parent.name}")
print("Let's Grunt package: 4 skills + shared reference OK", flush=True)
subprocess.run(
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", "examples/slug-skeleton", "-v"],
    check=True, cwd=root,
)
