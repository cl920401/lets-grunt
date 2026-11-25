---
name: lg-build
description: Implement an authorized software slice from pinned contracts, gated by buildable skeleton and independent review.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Build (scoped execution)

Follow **Step gate chosen in Plan**, **Self-review before asking for the next step**, **Authority and audit trail**, **Independent review before asking a human**, and the single **Numbered milestones** list in the shared workflow. Authorization mode is the default; Trust mode can request the next in-scope confirmation without an owner ping or re-entry, but still waits for fresh exact-step confirmation and quorum. The invocation itself never grants authority.

Run only when explicitly directed to use Build, with an authorized slice and pinned contracts. Read Handoff and Build in `../lg-spec/references/WORKFLOW.md`, relative to this skill. If the reference, scope, fixed version or necessary approval is missing, stop that slice and state why.

Before proposing #10 or resuming any Build step, verify that the pinned SPEC matches the #9 freeze, independent Spec Review and paper walkthrough, and that the verified task initiator explicitly confirmed the expected outcome of that exact version. Missing, ambiguous, conflicting or wrong-version evidence blocks Build. Keep #10 authorization and subsequent independent checks on actual Build artifacts separate from the product confirmation and paper walkthrough.

Follow the shared **Plan, Spec and Build transitions** on entry and resume. Disclose and record a provisional assumption only for a low-risk, reversible detail outside the contract and within the current authorized step. For a missing prerequisite, identify the exact evidence, who must supply it and where work is paused. For a material decision that changes a commitment or contract boundary, pause the affected Build step and point to the Spec step that requires a decision by the authorized person. Wait for a separately directed Spec invocation and a matching authorized handoff before continuing the affected work.

For substantive or multi-stage work, start a clean development context and a separate independent review context when supported. Follow the shared Context handoff rules. If the host cannot open one, return a scoped handoff and state that it was not opened; never simulate independence. A truly local small step can stay in context with a brief rationale, but this never waives independent acceptance.

Use shared steps **10–17**, as distinct steps under the chosen policy. At step 10, design the minimal skeleton as a sketch: entry point, signatures, wiring and pseudocode, without creating functions. In the next authorized step, create typed interfaces, empty functions with explicit not-implemented behavior, minimal wiring and pseudocode. Prove they build or pass equivalent checks without reporting business success or performing real side effects. An independent reviewer must verify the same skeleton version before any business implementation in that slice. If independent review is unavailable, stop at the skeleton and report the blocker.

Use shared **Module progress** after each authorized Build step: record separate development and test/independent results per module, bound to its exact candidate. Reconcile before proposing the next step; if no writable record is authorized, report the rows without writing.

After the separate runnable skeleton (11) and independent skeleton review (12), keep separate implementation (13), developer self-tests (14), independent code review and exact-candidate retest (15), independent acceptance (16), and delivery/outcome evaluation (17). A reviewer reports findings; corrections after failed evidence require a separately and explicitly confirmed developer action and a fresh digest for retest. Delivery is not deployment. Record evidence, gaps and results separately from a passed skeleton. Apply the shared Evidence gate before accepting reported completion or any test claim. Without independent final acceptance on the exact implementation candidate, mark acceptance **BLOCKED**, not passed. If a contract must change, stop affected work and suggest `$lg-spec`; do not invoke it. Do not automatically commit, push, deploy or release.
