# Validation

| Scope | Result |
| --- | --- |
| Four entry points, plain frontmatter, local resources, three explicit-mode policies, bilingual README links | Passed with `python3 scripts/check.py`. In disposable copies, missing workflow, invalid policy and invalid skill name were rejected. This checks the package's chosen format, not every legal Agent Skills form. |
| Example skeleton | T3 passed: exit 3, no stdout, explicit not-implemented stderr. T1/T2 require business implementation and were not run. |
| README installation | The EN and Chinese install scripts are identical. In an isolated Linux home their copied bytes matched, a repeat install refused to overwrite, and uninstall moved only the intended folders. |
| Runtime discovery | Linux Codex CLI 0.172.0-alpha.2 App Server `skills/list` returned exactly four unique enabled entries with no discovery errors. Installed relative workflow references resolved. |
| Cross-session handoff | Shared template is packaged and referenced. Manual behaviors are described in the example; no live model handoff was exercised. |
| Runtime invocation, implicit selection, editor completion and macOS | Not tested. Discovery verifies registration, not model behavior. |

The validation used disposable directories; no real user install, project, repository, or release was touched by these checks.
