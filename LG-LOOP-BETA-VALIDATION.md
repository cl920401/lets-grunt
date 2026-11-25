# Loop Beta validation

Candidate `lg-loop-beta-v0.1.0-beta.1`, based on public commit `39f1cf56472c7c6457985d54c02458b879bc9525`. The replayed skill entry had SHA-256 `1765815ebd056da2da6dc5d51c3acf78387f867f5a92357d2e162f867478432d`. Fixtures and receipts were synthetic. No real project or installed skill was modified.

| Check | Observed result |
| --- | --- |
| Package and schema | `python3 -B scripts/check.py` passed all 40 existing tests, including the package's frontmatter, policy and links checks. Ruby YAML separately parsed the beta frontmatter and explicit-invocation policy. |
| Codex discovery | macOS Codex CLI 0.171.0-alpha.13.2, App Server `skills/list`, returned one enabled repo-scoped `lg-loop-beta` and zero discovery errors. User-scope copies of stable skills also appeared in the listing. |
| Codex invocation, Spec replay | A fresh read-only ephemeral `codex exec` turn used just the explicit skill name and “帮我接着推一下。” It asked for the material import decision, gave a reversible sample filename, kept the rollback issue, and deferred out-of-stage code. It separated the delegated ordinary confirmation from Spec #9, required the same-version whole review, and paused the unverified handoff without retrying. |
| Codex invocation, Build replay | The same opening in a second disposable project kept smoke and mock results separate from denied real write-back and pending product acceptance. It stopped for Authorization-mode re-entry and required the existing Build evidence. |
| Separate agent fixture replays | Two agents directly loaded the same skill and applied it independently to the two synthetic ledgers. Both stopped at the relevant gates. These agents shared task context, and direct file loading was separate from native client discovery. |
| OpenCode 1.1.36 | `opencode debug skill` discovered the beta once from a disposable project. Explicit invocation, model behavior, Codex policy enforcement and dispatch were untested on this host. |
| DSH | Untested for this candidate. There is no verified beta loader or dispatch receipt evidence. |

The Codex turns received no follow-up checklist. The replays exercised the decision paths in the [replay guide](skills/lg-loop-beta/references/replay.md) using static records. Live dispatch, positive retry on confirmed non-delivery, native approval and audit, unattended operation, implicit-selection behavior, editor completion, and real product write-back were untested. The repository's full per-mode live invocation matrix was also untested for this beta. Keep a human in charge of stage progression and confirmation.
