"""Check the Let's Grunt package using Python's standard library."""
from hashlib import sha256
from pathlib import Path
import re
import subprocess
import sys


def verify(test, message):
    if not test:
        raise SystemExit(message)


root = Path(__file__).resolve().parents[1]
expected = {"lg-plan", "lg-spec", "lg-build", "lg-refine", "lg-review"}
skills = root / "skills"
entries = sorted(skills.glob("*/SKILL.md"))
verify(len(entries) == 5 and {p.parent.name for p in entries} == expected,
       "expected four mode skills and one companion")
common = skills / "lg-spec" / "references" / "WORKFLOW.md"
verify(not common.parent.parent.is_symlink() and not common.parent.is_symlink()
       and not common.is_symlink() and common.is_file(),
       "missing or nonregular shared workflow")
plan = skills / "lg-plan"
plan_entry = plan / "SKILL.md"
plan_references = plan / "references"
plan_workflow = plan_references / "WORKFLOW.md"
verify(not plan.is_symlink() and not plan_entry.is_symlink() and plan_entry.is_file()
       and not plan_references.is_symlink() and not plan_workflow.is_symlink(),
       "nonregular or linked Plan workflow path")
source = common.read_bytes()
digest = sha256(source).hexdigest().encode("ascii")
marker = rb"^Workflow SHA-256: [0-9a-f]{64}$"
entry_bytes = plan_entry.read_bytes()
verify(len(re.findall(marker, entry_bytes, re.MULTILINE)) == 1, "missing or duplicate Plan workflow digest")
expected_entry = re.sub(marker, b"Workflow SHA-256: " + digest, entry_bytes, flags=re.MULTILINE)
verify(sys.argv[1:] in ([], ["--sync-plan-workflow"]), "usage: check.py [--sync-plan-workflow]")
if sys.argv[1:] == ["--sync-plan-workflow"]:
    plan_references.mkdir(exist_ok=True)
    if not plan_workflow.exists() or plan_workflow.read_bytes() != source:
        plan_workflow.write_bytes(source)
    if expected_entry != entry_bytes:
        plan_entry.write_bytes(expected_entry)
verify(plan_workflow.is_file() and plan_workflow.read_bytes() == source
       and plan_entry.read_bytes() == expected_entry,
       "stale or missing Plan workflow mirror or digest; run check.py --sync-plan-workflow")
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
    verify(fields["license"] == "MIT" and 1 <= len(fields["compatibility"]) <= 500,
           f"invalid package metadata in {entry}")
    refs = re.findall(r"`([^`]*WORKFLOW\.md)`", parts[2])
    local_workflow = entry.parent.name in {"lg-plan", "lg-spec"}
    expected_ref = "references/WORKFLOW.md" if local_workflow else "../lg-spec/references/WORKFLOW.md"
    expected_file = plan_workflow if entry == plan_entry else common
    verify(refs == [expected_ref] and (entry.parent / expected_ref).resolve() == expected_file.resolve(),
           f"bad shared workflow reference in {entry}")
    # Validate the shipped Codex metadata independently of other hosts' discovery rules.
    policy = entry.parent / "agents" / "openai.yaml"
    if entry.parent.name == "lg-plan":
        verify(not policy.exists() and not policy.is_symlink(), "Plan should use the host's default policy")
    else:
        verify(policy.is_file() and not policy.is_symlink() and not policy.parent.is_symlink()
               and policy.read_text(encoding="utf-8") == "policy:\n  allow_implicit_invocation: false\n",
               f"missing explicit invocation policy in {entry.parent.name}")
driver = root / "driver" / "lg-drive" / "SKILL.md"
verify(driver.is_file() and not driver.is_symlink() and not driver.parent.is_symlink()
       and not driver.parent.parent.is_symlink()
       and driver.read_text(encoding="utf-8").startswith("---\nname: lg-drive\n"),
       "missing or invalid optional driver adapter")
for name, counterpart in (("README.md", "README.zh-CN.md"), ("README.zh-CN.md", "README.md")):
    readme = root / name
    doc = readme.read_text(encoding="utf-8")
    verify(f"]({counterpart})" in doc, f"missing language link in {name}")
    verify(set(re.findall(r"\blg-[a-z]+\b", doc)) == expected | {"lg-drive"},
           f"mismatched skill IDs in {name}")
    for link in re.findall(r"\]\(([^ )]+)\)", doc):
        if "://" not in link:
            verify((readme.parent / link.split("#", 1)[0]).exists(),
                   f"broken local link {link} in {name}")
print("Let's Grunt package: 4 mode skills + 1 companion + shared reference OK", flush=True)
subprocess.run(
    [sys.executable, "-B", "-m", "unittest", "discover", "-s", "examples/slug-skeleton", "-v"],
    check=True, cwd=root,
)
