---
name: lg-refine
description: Make a small authorized software improvement within an existing contract and run focused regression checks.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Refine (compatible small changes)

Follow **Step gate chosen in Plan**, **Self-review before asking for the next step**, **Authority and audit trail**, **Independent review before asking a human**, and the single **Numbered milestones** list in the shared workflow. Authorization mode is the default; Trust mode can request the next in-scope confirmation without an owner ping or re-entry, but still waits for fresh exact-step confirmation and quorum. The invocation itself never grants authority.

Run only under explicit user direction for a bounded change. Read Refine and Final checks in `../lg-spec/references/WORKFLOW.md` relative to this skill. If the reference, scope or current contract is missing, stop before writing.

A small, unambiguous change can stay in the current context. For substantial work or uncertain scope, stop the affected change and provide a scoped handoff; route contract ambiguity to Spec. Keep all authority and acceptance boundaries intact. Use steps **18–20** in three separate rounds: agree on scope and risk, make one approved compatible change, then run focused regression and report. Preserve unrelated edits. Apply the shared Evidence gate to regression; do not equate a reported result with verified evidence. If an in-contract change affects authorization, data or a critical path, independently re-verify the affected behavior. If critical function boundaries or wiring change within the contract, repeat the affected skeleton review. For larger execution work suggest `$lg-build`.

If an interface, external behavior, acceptance rule, permission, architecture or data contract would change, stop affected edits and suggest `$lg-spec`. Do not switch modes, silently change the contract or automatically commit, push, deploy or release.
