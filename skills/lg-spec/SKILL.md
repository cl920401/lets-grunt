---
name: lg-spec
description: Turn an agreed software plan into documented contracts, acceptance criteria and agent handoff without implementing it.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Spec (documentation only)

Follow **One confirmed step at a time**, **Self-review before asking for the next step**, **Authority and audit trail**, and the single **Numbered milestones** list in the shared workflow: first propose only the next concrete action, deliverable/evidence and allowed boundary, then wait for explicit confirmation of that exact step. After executing only that step, report evidence and stop; propose only after re-entry. The invocation itself never confirms execution.

Run this mode only under explicit user direction. Read `references/WORKFLOW.md` relative to this skill, especially Specification and Handoff. If it is missing, stop without changing files.

Use the agreed plan and verify relevant source anchors against authoritative versions. Separate confirmed constraints and acceptance expectations from open questions and assumptions. If evidence is missing, stale, or conflicts, block the affected slice rather than guessing. Use the ordered design checklist: architecture → API/UI → data/DDL → test methods → cross-check and freeze. Capture decisions and reviewer expectations before handing off the pinned design. Scale the detail to risk and explain any N/A item. Label affected work blocked when required input is missing. Write only the documentation paths the user authorizes; otherwise return a draft. DDL belongs in a Markdown review draft, not a migration file. Skeleton design belongs to Build. Do not create source stubs, run tests or SQL, write source/tests/configuration, change the environment or start execution. Report the exact version and readiness; do not advance to Build.
