---
name: lg-build
description: Implement an authorized software slice from pinned contracts, gated by buildable skeleton and independent review.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Build (scoped execution)

Run only when explicitly directed to use Build, with an authorized slice and pinned contracts. Read Handoff and Build in `../lg-spec/references/WORKFLOW.md`, relative to this skill. If the reference, scope, fixed version or necessary approval is missing, stop that slice and state why.

First create typed interfaces, empty functions with explicit not-implemented behavior, minimal wiring and pseudocode. Prove they build or pass equivalent checks without reporting business success or performing real side effects. An independent reviewer must verify the same skeleton version before any business implementation in that slice. If independent review is unavailable, stop at the skeleton and report the blocker.

Then implement only the authorized slice and run developer checks followed by independent acceptance. Record evidence, gaps and results separately from a passed skeleton. Without independent final acceptance on the exact implementation candidate, mark acceptance **BLOCKED**, not passed. If a contract must change, stop affected work and suggest `$lg-spec`; do not invoke it. Do not automatically commit, push, deploy or release.
