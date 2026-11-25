---
name: lg-plan
description: Explore a software project's goals, boundaries and tradeoffs without writing files or starting implementation.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Plan (read-only)

Follow **Step gate chosen in Plan**, **Self-review before asking for the next step**, **Authority and audit trail**, **Independent review before asking a human**, and the single **Numbered milestones** list in the shared workflow. Authorization mode is the default; Trust mode can request the next in-scope confirmation without an owner ping or re-entry, but still waits for fresh exact-step confirmation and quorum. The invocation itself never grants authority.

Read the planning section in `../lg-spec/references/WORKFLOW.md` relative to this skill. If unavailable, report the missing reference and stop. Inspect existing materials read-only. Do not modify files, run commands that may write, alter project state or dispatch execution.

Use shared steps **1–3** separately: inspect the current project and known constraints; define the first usable outcome and boundaries; then return the pasteable actionable Plan #3 handoff at step 3 only (see the shared Plan #3 handoff section). Do not write the brief to disk. Ask only about gaps that materially affect the current step. When Plan is complete, stop; the user can invoke `$lg-spec` separately.

On entry or resume, follow the shared **Plan, Spec and Build transitions**. Reuse verifiable discussion and completed steps. Disclose reversible assumptions and continue the authorized step. For a missing material decision or required evidence, identify what is missing, who must answer and where Plan is paused. At #3, clarify any gaps in the goal, boundaries and first useful outcome with the task initiator. Carry their answers and source references into the read-only handoff for Spec, with assumptions recorded separately.

In the first Plan round, ask once which mode to use and who confirms each step, including any required quorum (see shared workflow). Record the choice and its scope/reference in the conversation and the pasteable Plan brief, without writing files.
