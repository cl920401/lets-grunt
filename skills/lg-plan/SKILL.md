---
name: lg-plan
description: Explore a software project's goals, boundaries and tradeoffs without writing files or starting implementation.
license: MIT
compatibility: Requires skill loading and authorized access to the bundled workflow.
---

# Plan (read-only)

**OpenCode only.** Before any project read, search or independent review, verify from current host state that the primary agent is native Plan (`plan`). Use host-reported state without filesystem probes. A loaded skill attachment, a requested agent or a prior turn does not verify the current agent. If the current agent is Build, another agent, or unknown, stop at a chat reply and tell the developer to open `/agents`, select **Plan**, then resubmit. API callers should explicitly select `plan` through their supported native entry and verify the agent that actually ran. Leave agent selection to the developer or API caller. Preserve the existing filesystem and step permissions. Native Plan selection alone cannot establish filesystem isolation. Hosts without OpenCode's primary-agent selection follow the normal read-only path below.

Follow **Step gate chosen in Plan**, **Self-review before asking for the next step**, **Authority and audit trail**, **Independent review before asking a human**, and the single **Numbered milestones** list in the shared workflow. Authorization mode is the default; Trust mode can request the next in-scope confirmation without an owner ping or re-entry, but still waits for fresh exact-step confirmation and quorum. The invocation itself never grants authority.

Read **Project filesystem boundary** and Planning in `references/WORKFLOW.md`. Prefer the matching workflow supplied by the host or the mirror bundled with this Plan skill, using authorized skill access. If neither is available, use an identified in-project copy only if its content matches the pinned digest below. Verify the same version before use. Do not probe sibling skills or external directories to find it. If no verified copy is available, report the missing reference and stop. Bind reads, searches and independent reviews to the verified project root. Wait for the project initiator's explicit approval before any outside project-data access. Inspect existing materials read-only. Do not modify files, run commands that may write, alter project state or dispatch execution.

Workflow SHA-256: 8872e46362088ac52dbdfdf9130ab81a265d894b284a967baa005a217b87bd43

Use shared steps **1–3** separately. Inspect the project and constraints, define commitments and the minimum observable acceptance for the first useful outcome, then return the Plan #3 handoff in chat. Leave UI details, algorithms and failure-test design to the relevant Spec or Build steps. When Plan is complete, stop. The user invokes `lg-spec` separately.

Start with the user's request in plain language. Show the in-scope Plan and confirmed decisions first, with reversible assumptions inline. Follow **Plan and Spec reply order**. Put material product questions under **Needs your decision** in the user's language at the end. Prefer a native question card when supported. Use text instead when the card is unavailable or confirmed unsent. Keep step authorization, initiator confirmation and missing evidence separate. While a required reply is pending, keep the handoff open. After Plan is complete, give a single manual Spec hint on the last line using **Manual next step by host**. Keep milestone numbers, approval mechanics, reviewer names and receipt references in the existing handoff or audit record.

On entry or resume, follow the shared **Plan, Spec and Build transitions**. Reuse verifiable discussion and completed steps. Check source evidence for missing facts. Apply and disclose reversible defaults without asking, within the authorized step. At #3, ask the initiator only about material unresolved choices in the goal, boundaries and first useful outcome. For a missing decision or required evidence, identify what is missing, who can resolve it and which action pauses. Carry prior decisions and original references into the handoff, with assumptions recorded separately. Use the ordinary step review to check the current deliverable, constraints, evidence and risk.

Use the supplied project root and step policy when independently verifiable. Mode 2 means Trust with confirmation from any one verified eligible project participant, subject to any stricter recorded policy. Ask only if the root or policy remains unclear after verification. Record the current policy and original reference in chat and the Plan brief, without writing files. A known root or mode does not authorize a numbered step or outside access.
