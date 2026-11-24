---
name: lg-refine
description: Make a small authorized software improvement within an existing contract and run focused regression checks.
---

# Refine (compatible small changes)

Run only under explicit user direction for a bounded change. Read Refine and Final checks in `../lg-spec/WORKFLOW.md` relative to this skill. If the reference, scope or current contract is missing, stop before writing.

Make one reversible improvement within the authorized paths and current external contract, such as clarifying a test failure or fixing behavior the specification already requires. Preserve unrelated edits and run focused regression checks. If critical function boundaries or wiring change within the contract, repeat the affected skeleton review. For larger execution work suggest `$lg-build`.

If an interface, external behavior, acceptance rule, permission, architecture or data contract would change, stop affected edits and suggest `$lg-spec`. Do not switch modes, silently change the contract or automatically commit, push, deploy or release.
