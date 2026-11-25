---
name: lg-drive
description: Convert natural-language intent into one scoped next-action prompt before a driver dispatches to an existing project agent.
license: MIT
compatibility: Driver-side preprocessing only; no required host tool or product architecture.
---

# Driver prompt conversion

Run immediately before each outbound task or steering prompt to a project agent. Consume casual language as-is; the requester does not fill a template. This does not start a new phase, grant permission, or change modes. Do not wrap status queries, tool calls, ordinary replies, or messages the owner typed directly.

1. Read the latest verified session state, current gate, exact artifact/version, and actual authority. If the same action is in flight or already accepted, **do not send**. Pin only facts and constraints established in this lane; never import another lane's work. Use the sender's real role.
2. Preserve actual intent, exclusions, permissions, and required evidence. Label an inferred low-risk reversible default as an assumption, not an owner decision. Let the executor choose routine details. An unproven fact stays unknown; ask for the smallest eligible proof instead of guessing.
3. Choose one eligible action that produces the next independently checkable result or removes its real blocker. Include only the necessary context: desired result; exact scope/gate; one action; observable exit evidence; and a stop rule. No unnecessary plan, tool or platform syntax. Keep existing approvals, hard limits and independent review intact.
4. If the answer could change a product promise, acceptance, significant risk or permissions, do not guess or dispatch that dependent action. Put only the necessary question last: concrete scenario, invariant that must hold, recommended option and trade-off, one credible alternative, and what acceptance changes. Keep unrelated authorized work moving.

## Choose emphasis by stage and risk

Use the current stage to decide what to extract: Plan scopes the next useful outcome; Spec turns it into observable behavior and trade-offs; Build chooses the smallest authorized implementation or verification action; Review looks for matching proof and gaps; Refine preserves the existing contract and selects targeted regression. A preference is not a product decision or execution approval.

For the specific change, identify the outcome to prove, the constraints that must hold, and plausible failure consequences. Let the most consequential unresolved risk and the cheapest conclusive check determine what to verify next. If two risks interact, prefer a small scenario that can distinguish both; otherwise sequence the evidence by consequence and dependency. Project labels and examples are hints, not categories or rules.

This is a reversible decision about order and depth of evidence, not a change to acceptance, permissions or risk gates. If the risk is uncertain, gather the least-cost in-scope evidence; ask only if the missing answer changes a commitment or required check.

Output either a short dispatch in the project's language, one consolidated material question, or no send with the reason. The driver uses the verified destination only, then checks actual acceptance or output and deduplicates before any retry. Conversion alone does not permit sending or prove delivery.
