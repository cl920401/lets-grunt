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
