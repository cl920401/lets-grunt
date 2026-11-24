---
name: lg-build
description: Implement an authorized software slice from pinned contracts, gated by buildable skeleton and independent review.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Build (scoped execution)

Follow **One confirmed step at a time**, **Self-review before asking for the next step**, **Authority and audit trail**, and the single **Numbered milestones** list in the shared workflow: first propose only the next concrete action, deliverable/evidence and allowed boundary, then wait for explicit confirmation of that exact step. After executing only that step, report evidence and stop; propose only after re-entry. The invocation itself never confirms execution.

Run only when explicitly directed to use Build, with an authorized slice and pinned contracts. Read Handoff and Build in `../lg-spec/references/WORKFLOW.md`, relative to this skill. If the reference, scope, fixed version or necessary approval is missing, stop that slice and state why.

For substantive or multi-stage work, start a clean development context and a separate independent review context when supported. Follow the shared Context handoff rules. If the host cannot open one, return a scoped handoff and state that it was not opened; never simulate independence. A truly local small step can stay in context with a brief rationale, but this never waives independent acceptance.

Use shared steps **10–17**, not as a single invocation. At step 10, design the minimal skeleton as a sketch: entry point, signatures, wiring and pseudocode, without creating functions. After separate confirmation, create typed interfaces, empty functions with explicit not-implemented behavior, minimal wiring and pseudocode. Prove they build or pass equivalent checks without reporting business success or performing real side effects. An independent reviewer must verify the same skeleton version before any business implementation in that slice. If independent review is unavailable, stop at the skeleton and report the blocker.

Use shared **Module progress** after each confirmed Build step: record separate development and test/independent results per module, bound to its exact candidate. Reconcile before proposing the next step; if no writable record is authorized, report the rows without writing.

After the separately confirmed runnable skeleton (11) and independent skeleton review (12), separately confirm implementation (13), developer self-tests (14), independent code review and exact-candidate retest (15), independent acceptance (16), and delivery/outcome evaluation (17). A reviewer reports findings; corrections require a separately confirmed developer action and a fresh digest for retest. Delivery is not deployment. Record evidence, gaps and results separately from a passed skeleton. Apply the shared Evidence gate before accepting reported completion or any test claim. Without independent final acceptance on the exact implementation candidate, mark acceptance **BLOCKED**, not passed. If a contract must change, stop affected work and suggest `$lg-spec`; do not invoke it. Do not automatically commit, push, deploy or release.
