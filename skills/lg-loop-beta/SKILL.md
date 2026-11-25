---
name: lg-loop-beta
description: Help a human drive or recover an existing Let's Grunt run when progress, an interrupted handoff, or the next eligible action is unclear. Use to reconcile exact-version evidence and route the current blocker without changing workflow gates.
license: MIT
compatibility: Codex with the Let's Grunt workflow installed alongside this skill. Other hosts require verified equivalent capabilities.
---

# Let's Grunt Loop Beta

Assist the human driving the current run. Read `../lg-spec/references/WORKFLOW.md` and the already selected mode's instructions when available. If the workflow or current mode cannot be established, do read-only triage and surface the missing prerequisite. Keep the existing milestones, mode, re-entry rules, confirmation policy, quorum and permissions. Work already authorized for the current scope may proceed under those rules. A loop request by itself grants no execution authority. Stop at a required re-entry, unresolved gate or mode completion, and return control to the human. Never select a later mode on their behalf.

## Find the next eligible action

- Recover the current goal, mode, milestone, executor and pinned candidate from the available authorized record. Match evidence to the exact project, session, action and revision or digest. With a vague request, ask only for material decisions or missing gate evidence. State a reversible default for small in-scope details and how to change it.
- Classify each actionable item as running, awaiting an answer, awaiting confirmation, blocked by the environment, or verified delivered. Split mixed items by owner and dependency. Continue safe authorized work that is independent of the blocker. For each blocked item, say what is missing, who can resolve it and what would prove resolution.
- Before sending or retrying a handoff, check the authorized record and destination for the exact operation and current ownership. Count a review as submitted only when the destination's native receipt or auditable trace binds the recipient/session, action and candidate. A request to send, a worker summary or an empty response leaves delivery unverified. If delivery is uncertain, query destination state before retrying. Reuse confirmed receipts, avoid overlapping writers, and retry only when non-execution is established and the bounded recovery action is authorized by the workflow. If the host cannot verify state, leave that action blocked and report the capability gap.
- Keep self-check, independent review, formal confirmation and acceptance distinct. Require an independent review of the complete applicable artifact or proposal on the exact candidate version. An older PASS or a PASS on a partial patch does not pass a revised whole candidate. For an ordinary workflow gate, accept a delegated agent's actual exact-step confirmation only if the human's recorded policy makes that verified agent eligible. Record the agent as itself. The executor cannot approve its own work. Human-only gates, including the initiator's outcome confirmation at Spec #9 and platform approvals, stay with the required person.
- When a document keeps returning for revision, first remove or defer detail that belongs to another milestone. Return material product, contract or data-safety issues to the milestone that owns them and preserve its original review and confirmation requirements.

Report the pinned candidate, what has actually happened, the proof and the next eligible action. Record smoke and mock evidence at its tested scope. A refused write is evidence about refusal, while actual write-back requires proof from the real destination. Verify the intended product behavior on the same candidate before reporting final delivery.

For host portability and isolated evaluations, use [the replay guide](references/replay.md). Keep a human driving each stage and supervising confirmations. Use this beta for judgment, evidence and tracking in real projects. Keep automatic exercises in disposable fixtures and keep real file writes, deploys and releases under direct human control.
