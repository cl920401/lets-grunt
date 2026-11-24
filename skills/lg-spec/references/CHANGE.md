# Change handoff

Use for a substantive change handed to another session, agent, or reviewer. Reuse an existing record instead of adding a duplicate. Copy only applicable rows to an authorized destination; keep secrets and private data out.

| Item | Record |
| --- | --- |
| Scope | Task ID, owner, allowed paths, non-goals, requirement IDs |
| Spec | Exact path plus commit or content digest |
| Skeleton review | Exact artifact version, independent reviewer, checks and result or BLOCKED |
| Implementation | Exact candidate version, changed paths, developer checks |
| Independent acceptance | Reviewer, exact implementation version, checks and outcomes or BLOCKED |
| Review context | Pinned inputs, allowed paths, exact check commands, expected outcomes, untested items and factual evidence only; keep any developer verdict outside the reviewer handoff |
| Next eligible step | What can proceed now, untested areas and what would unblock remaining work |

A green skeleton check is not implementation acceptance. Do not carry a review forward to changed evidence without rechecking affected areas.

## Build module progress

Use one row per module; reuse the authorized task sheet if it already has equivalent columns. Do not mark independent progress passed without a reviewer’s evidence for the bound candidate; developer tests are evidence, not acceptance.

| Module | Dev / test owners | Development status | Test / independent status | Candidate version | Evidence | Blockers |
| --- | --- | --- | --- | --- | --- | --- |
| Example CLI | Developer A / reviewer B | Implemented; developer checks passed | Independent review pending; acceptance BLOCKED | Example commit v1 | Developer checks, v1; no independent record | Independent acceptance missing |


## Step audit

Record the Plan mode, eligible confirmers and quorum, verified human grantor, authority, original policy reference, time and approved scope. For each step in either mode record the exact step/revision, scope, deliverable, paths and limits, plus each actual confirmer's verified actor ID and type, authority, original confirmation reference and time. Distinguish confirmer, grantor, executor, requester and independent reviewer. Do not treat a standing grant as confirmation. Missing evidence or quorum blocks execution. Append result and evidence to the same authorized record. Plan records only in authorized durable chat; persist from handoff only in authorized Spec. Never paste secrets or whole conversations.

For interrupted or overlapping work, record the active step owner, exact candidate, observed effects or receipts, and whether work is complete, BLOCKED, or awaiting a separately approved bounded recovery action. Never treat a missing result as permission to rerun.

## Verification record

Link the relevant [review log](REVIEW_LOG.md) entry or authorized chat/trace here and in step or module status. Keep the review result in one place; use the existing authorized evidence record or proposed `docs/REVIEW_LOG.md`, not both.

Record planned, in progress, reported and verified distinctly. For a candidate, link actual artifact or diff and exact revision; for checks, record command, environment, exit outcome, named assertions, executed/skipped/failed counts and a retained run log or independent rerun. Identify who verified; do not mark required skipped, no-op, zero-execution, stale or unsupported claims as passed. For external actions link an original receipt or independently observed target state. Record gaps and blockers.
