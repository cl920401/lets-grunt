"""Check the Let's Grunt package using Python's standard library."""
from pathlib import Path
import re
import subprocess
import sys


def verify(test, message):
    if not test:
        raise SystemExit(message)


root = Path(__file__).resolve().parents[1]
expected = {"lg-plan", "lg-spec", "lg-build", "lg-refine", "lg-review", "lg-loop-beta"}
skills = root / "skills"
entries = sorted(skills.glob("*/SKILL.md"))
verify(len(entries) == len(expected) and {p.parent.name for p in entries} == expected,
       "expected four mode skills, Review and Loop Beta")
common = skills / "lg-spec" / "references" / "WORKFLOW.md"
verify(common.is_file() and not common.is_symlink() and not common.parent.is_symlink(),
       "missing or nonregular shared workflow")
handoff = common.with_name("CHANGE.md")
verify(handoff.is_file() and not handoff.is_symlink(), "missing or nonregular handoff template")
review_log = common.with_name("REVIEW_LOG.md")
verify(review_log.is_file() and not review_log.is_symlink(), "missing or nonregular review log template")
for source in (common, handoff):
    verify("](REVIEW_LOG.md)" in source.read_text(encoding="utf-8"),
           f"missing review log link in {source}")
for entry in entries:
    verify(entry.is_file() and not entry.is_symlink() and not entry.parent.is_symlink(),
           f"nonregular skill entry: {entry}")
    text = entry.read_text(encoding="utf-8")
    # This package deliberately uses plain, single-line YAML scalars.
    # This is a package convention check, not a general YAML parser.
    parts = text.split("---\n", 2)
    verify(len(parts) == 3 and not parts[0] and parts[2].strip(),
           f"missing frontmatter or body in {entry}")
    fields = {}
    for line in parts[1].splitlines():
        key, sep, value = line.partition(": ")
        verify(bool(sep) and key not in fields and bool(value.strip())
               and not re.search(r"[:#]\s|^[\[\]{}&*!>|@`]", value),
               f"invalid, duplicate or non-plain frontmatter in {entry}")
        fields[key] = value
    verify(fields.keys() == {"name", "description", "license", "compatibility"},
           f"unexpected frontmatter keys in {entry}")
    name = fields["name"]
    verify(len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
           and name == entry.parent.name, f"invalid skill name in {entry}")
    verify(1 <= len(fields["description"]) <= 1024, f"invalid description in {entry}")
    verify(fields["license"] == "MIT" and 1 <= len(fields["compatibility"]) <= 500
           and "Codex" in fields["compatibility"], f"invalid package metadata in {entry}")
    refs = re.findall(r"`([^`]*WORKFLOW\.md)`", parts[2])
    expected_ref = "references/WORKFLOW.md" if entry.parent.name == "lg-spec" else "../lg-spec/references/WORKFLOW.md"
    verify(refs == [expected_ref] and (entry.parent / expected_ref).resolve() == common.resolve(),
           f"bad shared workflow reference in {entry}")
    policy = entry.parent / "agents" / "openai.yaml"
    if entry.parent.name == "lg-plan":
        verify(not policy.exists() and not policy.is_symlink(), "Plan should use the host's default policy")
    else:
        verify(policy.is_file() and not policy.is_symlink() and not policy.parent.is_symlink()
               and policy.read_text(encoding="utf-8") == "policy:\n  allow_implicit_invocation: false\n",
               f"missing explicit invocation policy in {entry.parent.name}")
for name, counterpart in (("README.md", "README.zh-CN.md"), ("README.zh-CN.md", "README.md")):
    readme = root / name
    doc = readme.read_text(encoding="utf-8")
    verify(f"]({counterpart})" in doc, f"missing language link in {name}")
    verify(set(re.findall(r"\$(lg-[a-z]+(?:-[a-z]+)*)", doc)) == expected,
           f"mismatched command set in {name}")
    for link in re.findall(r"\]\(([^ )]+)\)", doc):
        if "://" not in link:
            verify((readme.parent / link.split("#", 1)[0]).exists(),
                   f"broken local link {link} in {name}")
print("Let's Grunt package: 4 mode skills + 2 companions + shared reference OK", flush=True)
subprocess.run(
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", "examples/slug-skeleton", "-v"],
    check=True, cwd=root,
)
