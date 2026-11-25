---
name: lg-spec
description: Turn an agreed software plan into documented contracts, acceptance criteria and agent handoff without implementing it.
license: MIT
compatibility: Designed for Codex. Install the four skill folders together.
---

# Spec (documentation only)

Follow **Step gate chosen in Plan**, **Self-review before asking for the next step**, **Authority and audit trail**, **Independent review before asking a human**, and the single **Numbered milestones** list in the shared workflow. Authorization mode is the default; Trust mode can request the next in-scope confirmation without an owner ping or re-entry, but still waits for fresh exact-step confirmation and quorum. The invocation itself never grants authority.

Run this mode only under explicit user direction. Read `references/WORKFLOW.md` relative to this skill, especially Specification and Handoff. If it is missing, stop without changing files.

On entry or resume, follow the shared **Plan, Spec and Build transitions**. Read the available verifiable discussion and current step state, including on a direct Spec invocation. If a material Plan decision is missing, diagnose and clarify only that item before dependent work. Keep completed work and valid evidence. Disclose reversible assumptions and continue the currently authorized step. Keep confirmed decisions separate from assumptions and wait for actual, recorded evidence at every required gate. Apply the same diagnosis when preparing the Build handoff.

Use steps **4–9** separately: product specification → architecture → API/UI → data/DDL → test methods → cross-check and freeze. Align security, privacy, performance and reliability criteria or record why each is N/A. Capture decisions and reviewer expectations before handing off the pinned design. Scale the detail to risk and explain any N/A item. Write only the documentation paths the user authorizes; otherwise return a draft. DDL belongs in a Markdown review draft, not a migration file. Skeleton design belongs to Build. Do not create source stubs, run tests or SQL, write source/tests/configuration, change the environment or start execution. Report the exact version and readiness; do not advance to Build.

At #9, follow the shared **Spec #9 outcome walkthrough and confirmation**. First obtain an independent review of whether the candidate solves the right problem and justifies its direction and tradeoffs. After it passes, walk through a typical path and a critical failure or recovery path on paper. Present likely results, remaining limits, material uncertainties and a recommendation in the initiator's language. Freeze only after the verified initiator explicitly confirms the outcome of that exact SPEC version. Keep confirmation outside the pinned SPEC. Keep technical review and numbered-step authorization separate.
