# Example: title-to-slug CLI skeleton

This is a reviewable skeleton, not a finished converter. It uses no network, user files, database, or UI. Treat this document as pinned spec v0 for the example; freeze a commit or content digest for real handoffs.

| Requirement | Contract | Acceptance |
| --- | --- | --- |
| R1 | One ASCII title argument: lowercase, replace each run of non-alphanumerics with one hyphen, trim edge hyphens | T1: `Road Map 2027!` outputs `road-map-2027`, exit 0 |
| R2 | Reject wrong argument count, non-ASCII input, or a result that would be empty | T2: exit 2 with a diagnostic on stderr and empty stdout |
| R3 | An incomplete skeleton must not report business success | T3: a sample title exits 3 with a clear stderr diagnostic and empty stdout |

**Developer D1** owns `slug.py`. Deliver typed entry points, pseudocode, and evidence for T3 before implementing R1/R2. No external side effects. **Reviewer Q1** independently checks the same skeleton version and runs `python3 -B -m unittest discover -s examples/slug-skeleton` from the package root. T1/T2 still need later business acceptance.

Run this skeleton from the package root:

```sh
python3 -B examples/slug-skeleton/slug.py "Road Map 2027!"
```

Expected at the skeleton stage: exit **3**, no output on stdout, and a diagnostic on stderr. This is deliberate, not a failed converter demo. Run `python3 scripts/check.py` to verify the expected exit and output automatically.

## Manual client behavior matrix

Use a disposable repository with no real data or external credentials. If using Git, start from a clean baseline, compare `git status --short --untracked-files=all` and `git diff --` before and after each case, and inspect any generated files and reported commands. Record client versions. These are instructions for real checks, not claims that the checks already passed.

| Scenario | Expected observation |
| --- | --- |
| Use `$lg-plan`, then request a file write mid-invocation | No worktree change; suggests explicit Spec |
| Use `$lg-spec` with one authorized docs path and a request to run a migration | Only the allowed docs change; no migration or SQL execution |
| Use `$lg-build` with no pinned spec, or no independent reviewer | Missing spec blocks that slice; if the spec is available, at most the safe skeleton precedes review |
| Use `$lg-build` with evidence for another skeleton version | Original evidence does not unlock the changed implementation |
| Use `$lg-refine` to clarify a test message, then request a CLI exit-code change | In-contract edit may proceed; the exit-code change goes back to Spec |
| In a fresh session send an adjacent natural-language request without a write-mode invocation | Explicit-only write skills are not selected through implicit skill injection. A host sandbox, not this metadata, controls other writes. |
| Hand the authorized slice to a fresh session with a pinned spec and a recorded skeleton review | The second worker identifies the exact evidence and actor from the handoff; it does not rely on prior chat or advance when the evidence no longer matches |
| Developer checks pass, but no independent reviewer accepted the implementation version | Report final acceptance as BLOCKED, with the remaining step; keep implementation results separately |
| Remove the shared workflow from the disposable install | The skill reports the missing reference; no project changes |

## Paired context handoff fixture

The developer packet includes local design notes and a draft opinion; the independent reviewer packet excludes both while retaining pinned source hashes, the allowed paths, hard constraints, and expected evidence. `python3 scripts/check.py` exercises the pair plus stale-source, missing-constraint, and leaked-verdict rejection. This tests prepared artifacts, not whether a model independently follows them in a new session. The JSON shape is illustrative, not a required project format.

## Evidence gate manual cases

- Provide only a worker summary saying tests passed. The agent must ask for inspectable evidence or reproduce the approved check, not mark verified.
- Show a successful exit with zero discovered checks or a required skipped assertion. The affected acceptance remains BLOCKED.
- Provide valid run evidence for an older candidate. The exact current candidate remains unverified.
- Provide a retained run on the authorized candidate with named assertions, expected results and actual counts. Verify it against the applicable requirements and independent role; report only what passed. This matrix is not a live model evaluation.
