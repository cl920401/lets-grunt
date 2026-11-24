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

For each step, link its exact proposal and original confirmation. Record mode/step ID, pinned revision, scope, deliverable, allowed paths and external-action limits, with the requester, executor, independent reviewer and human approver roles as applicable. For multi-person work, link the approver’s verified account and scoped authority evidence. Record before execution; afterward append actual outcome, evidence/version and blockers to the same authorized record. Never paste secrets or whole conversations.
