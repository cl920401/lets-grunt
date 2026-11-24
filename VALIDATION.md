# Validation

| Scope | Result |
| --- | --- |
| Four entry points, plain frontmatter, local resources, three explicit-mode policies, bilingual README links | Passed with `python3 scripts/check.py`. In disposable copies, missing workflow, invalid policy and invalid skill name were rejected. This checks the package's chosen format, not every legal Agent Skills form. |
| Example skeleton | T3 passed: exit 3, no stdout, explicit not-implemented stderr. T1/T2 require business implementation and were not run. |
| README installation | The EN and Chinese install scripts are identical. In an isolated Linux home their copied bytes matched, a repeat install refused to overwrite, and uninstall moved only the intended folders. |
| Runtime discovery | Linux Codex CLI 0.172.0-alpha.2 App Server `skills/list` returned exactly four unique enabled entries with no discovery errors. Installed relative workflow references resolved. |
| Cross-session handoff | Four fixture checks passed: independent packet preserves pinned evidence and constraints while omitting developer conclusions, and rejects stale source, missing constraint and leaked verdict. This is deterministic fixture validation. No live model handoff was exercised. |
| Step confirmation | Three deterministic fixture checks passed: generic approvals cannot skip, exact confirmation is consumed before proposing the next step, and changed deliverables or paths require a new confirmation. No live model conversation was exercised. |
| Numbered milestones and prior-step gate | Exact 20-step order and 3/6/8/3 mode counts checked. Three deterministic fixture methods passed: missing, failed or stale evidence blocks; matching evidence or justified N/A permits proposing only; first step checks supplied prerequisites. No live model behavior was exercised. |
| Module progress | Two deterministic fixture checks passed: development done does not imply independent acceptance, and stale independent evidence cannot pass a new candidate. No live model progress updates were evaluated. |
| Step authority and audit | Three deterministic cases passed: unauthorized verified third-party blocked, mismatched or missing evidence/record blocked, and exact authorized match passed. Identity and audit storage were not tested on a live service. |
| Runtime invocation, implicit selection, editor completion and macOS | Not tested. Discovery verifies registration, not model behavior. |

The validation used disposable directories; no real user install, project, repository, or release was touched by these checks.
