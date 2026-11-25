# Validation

| Scope | Result |
| --- | --- |
| Four mode entries and one companion, plain frontmatter, local resources, four explicit-only policies, bilingual README links | Passed with `python3 scripts/check.py`. In disposable copies, missing workflow, invalid policy and invalid skill name were rejected. This checks the package's chosen format, not every legal Agent Skills form. |
| Example skeleton | T3 passed: exit 3, no stdout, explicit not-implemented stderr. T1/T2 require business implementation and were not run. |
| README installation | The EN and Chinese install scripts are identical. In a pre-companion isolated Linux home their copied bytes matched for the four modes, a repeat install refused to overwrite, and uninstall moved only the intended folders. |
| Runtime discovery | The pre-companion snapshot on Linux Codex CLI 0.172.0-alpha.2 App Server `skills/list` returned four unique enabled mode entries with no discovery errors, and their workflow references resolved. Live discovery and behavior of the companion were not tested. |
| Cross-session handoff | Four fixture checks passed: independent packet preserves pinned evidence and constraints while omitting developer conclusions, and rejects stale source, missing constraint and leaked verdict. This is deterministic fixture validation. No live model handoff was exercised. |
| Step confirmation | Three deterministic fixture checks passed: generic approvals cannot skip, exact confirmation is consumed before proposing the next step, and changed deliverables or paths require a new confirmation. No live model conversation was exercised. |
| Numbered milestones and prior-step gate | Exact 20-step order and 3/6/8/3 mode counts checked. Three deterministic fixture methods passed: missing, failed or stale evidence blocks; matching evidence or justified N/A permits proposing only; first step checks supplied prerequisites. No live model behavior was exercised. |
| Module progress | Two deterministic fixture checks passed: development done does not imply independent acceptance, and stale independent evidence cannot pass a new candidate. No live model progress updates were evaluated. |
| Step authority and audit | Three deterministic cases passed: unauthorized verified third-party blocked, mismatched or missing evidence/record blocked, and exact authorized match passed. Identity and audit storage were not tested on a live service. |
| Interrupted-step audit | Three illustrative deterministic fixtures passed: overlapping ownership blocks, unknown or interrupted state is not replayed, and already completed work records evidence without rerunning. No live concurrency or crash-resume behavior was tested. |
| Evidence gate | Four deterministic cases passed: unsupported claims, no-op/skips/cache, stale or mismatched proof and matching independent proof. The manual matrix and live model behavior have not been exercised. |
| Plan step policy | Structural package checks cover Authorization mode fallback, read-only capture, scoped opt-in, current authority and unchanged explicit skill selection. Existing fixtures cover interrupted/overlapping work and previous evidence. No live agent policy behavior tested. |
| Approver records | Structural check and illustrative quorum fixture cover both modes, human policy grant, exact-step confirmation, duplicate or excluded actors, stale or missing evidence, external authority boundary and read-only Plan handoff. No live account verification. |
| Plan #3 handoff | Structural checks and illustrative dependency/evidence fixture verify that a handoff can distinguish ready work from missing prerequisites, evidence or independent review. No live handoff executed. |
| Pre-human independent review | Structural and illustrative checks cover exact reviewed proposal/evidence, failed/missing/stale or self-review, unavailable subagent, and first-step scope. No live subagent invocation. |
| Review log | Structural checks verify the bundled template, links, required result types and read-only reviewer boundaries. No live reviewer or audit-store invocation. |
| Risk-based delivery and delta scope | Candidate package checks plus fixtures cover missing environment versus test failure, scope-specific blocking versus suggestions, dependency-local continuation, and four contrasting project shapes. These are structural and deterministic examples, not live agent behavior. |
| Runtime invocation, implicit selection, editor completion and macOS | Not tested. Discovery verifies registration, not model behavior. |

The validation used disposable directories; no real user install, project, repository, or release was touched by these checks.
