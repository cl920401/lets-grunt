# Validation (private review candidate)

| Scope | Result |
| --- | --- |
| Four entry-point names, frontmatter and shared path | Passed via `python3 scripts/check.py`. Checks resolve references from each skill directory and confirm only the three write-mode policy files are present. |
| Example skeleton | T3 passed: exit 3 with no stdout and explicit not-implemented stderr. T1/T2 require later business implementation and were not run. |
| README installation | Passed under Linux POSIX shell in an isolated HOME: four copied directories match source, duplicate install refuses to overwrite, and moving only those directories removes them. |
| Runtime discovery | Linux Codex CLI 0.172.0-alpha.2 App Server `skills/list` returned exactly four enabled, uniquely named user skills with no discovery errors. |
| Runtime skill use and implicit-selection behavior, editor completion, Mac | Not tested. Discovery confirms registration only; it does not expose the implicit-invocation flag or drive a model turn. |

No changes were made to a real install, project, repository or release.
