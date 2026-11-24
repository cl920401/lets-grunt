---
name: lg-refine
description: Make a small authorized software improvement within an existing contract and run focused regression checks.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Refine (compatible small changes)

Follow **One confirmed step at a time**, **Self-review before asking for the next step**, **Authority and audit trail**, and the single **Numbered milestones** list in the shared workflow: first propose only the next concrete action, deliverable/evidence and allowed boundary, then wait for explicit confirmation of that exact step. After executing only that step, report evidence and stop; propose only after re-entry. The invocation itself never confirms execution.

Run only under explicit user direction for a bounded change. Read Refine and Final checks in `../lg-spec/references/WORKFLOW.md` relative to this skill. If the reference, scope or current contract is missing, stop before writing.

A small, unambiguous change can stay in the current context. For substantial work or uncertain scope, stop the affected change and provide a scoped handoff; route contract ambiguity to Spec. Keep all authority and acceptance boundaries intact. Use steps **18–20** in three separate rounds: agree on scope and risk, make one approved compatible change, then run focused regression and report. Preserve unrelated edits. Apply the shared Evidence gate to regression; do not equate a reported result with verified evidence. If an in-contract change affects authorization, data or a critical path, independently re-verify the affected behavior. If critical function boundaries or wiring change within the contract, repeat the affected skeleton review. For larger execution work suggest `$lg-build`.

If an interface, external behavior, acceptance rule, permission, architecture or data contract would change, stop affected edits and suggest `$lg-spec`. Do not switch modes, silently change the contract or automatically commit, push, deploy or release.
