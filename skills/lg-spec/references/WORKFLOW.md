# Let's Grunt: shared workflow

The four entry points install as adjacent directories. This authoritative reference and its optional template live inside the Spec skill; do not install or package any entry point in isolation. This file is shared guidance, not another command. If an entry point is narrower than this file, the entry point wins. Selection alone, agreement on a design, a prior mode, successful QA and standing permission for other work do not authorize a new mode, slice, path or external action. Already authorized work may continue within its scope; never advance modes automatically. These instructions are not a sandbox.

## Planning

Start with a concrete user and desired outcome, the smallest usable path, non-goals and one recommended tradeoff. Check source facts without writing. Ask questions only when the answer could change architecture, product behavior, authority, distribution rights or material cost; state reversible assumptions instead of asking by default. Identify verified facts, decisions, assumptions and blockers separately. A fixture illustrates acceptance; it is not the product.

## Specification

Freeze a coherent version before implementation. Keep existing document organization; a small project may combine sections. Only write within the authorized documentation scope. If an input is missing, document the question, recommended default, consequence, and affected work; independent parts can continue.

| Contract | Evidence or decision needed |
| --- | --- |
| Goals and scope | Actors, usable path, non-goals, behavioral invariants, failure expectations and measurable acceptance with stable IDs such as R1. Quantitative claims need a workload and measurement method. |
| Architecture | Module ownership, request flow, data authority, trust/deployment boundaries, errors and recovery. Explain decisions, rejected options and reconsideration conditions. |
| Data | If applicable: schema, constraints, indexes, concurrency, transactions, retention, cache/queue semantics and recovery. A Markdown DDL draft is review-only; do not create migrations or execute SQL in Spec. State why data design is inapplicable if none. |
| Interfaces and UX | Examples, input/output, roles, errors, state transition, compatibility, retry/timeout/idempotency as needed. Map UI or CLI flows to contracts, including loading, denial, retry and recovery where applicable. |
| Reuse and authority | Separate actual dependencies from candidates. Record primary source, pinned version, applicable license, reuse boundary and exit plan. For access or AI features, document identities, isolation, revocation, egress, usage source and unknown outcomes. |
| Acceptance | Map requirements to implementation seams and assertions, environment and evidence. In-scope failure calls for repair; explicitly unsupported behavior tests expected rejection or degradation, not expansion. |

## Handoff

Use a common specification version or commit and one owner per writable path. Each role card names the role, task ID, pinned inputs, requirement/test IDs, allowed files, non-goals, prerequisites, verification method, expected evidence, stop condition and status. Report blocked dependencies explicitly. Separate product clarification, development, independent review/testing and coordination. A card is not authorization or proof that an agent ran. If a file is not yet written, include its exact text or a verified readable input rather than a future path.

### Context handoff

Share the facts a recipient needs, not a transcript of the conversation. Plan ends with a pasteable decision/unknowns brief; Spec verifies source anchors and keeps confirmed constraints separate from pending decisions. For substantive or multi-stage Build work use separate clean development and independent review contexts when the host supports them. Keep truly local, small work in the current context if that is sufficient and briefly record why; this does not waive any independent gate. If clean contexts are unavailable, provide a safe handoff instead of claiming one was opened or resuming on a recipient’s behalf.

A developer handoff carries pinned SPEC/CHANGE references, the allowed slice and material design decisions. An independent reviewer receives the exact candidate and pinned SPEC/CHANGE references, allowed paths, exact check commands, expected outcomes, untested items and factual evidence; exclude the full chat and developer verdict by default. If a shared CHANGE record contains a developer verdict, point the reviewer only to its factual sections or supply a clean projection. The reviewer checks the authority and actual results independently.

Compress narrative, not constraints. Carry write and external-action limits, non-goals, invariants, failure behavior, acceptance expectations and provenance even if that makes the handoff longer. Use selective anchors to things the recipient can read, and verify their authoritative versions before acting. Missing, stale or conflicting inputs block the affected work; do not inherit chat approvals or infer new authority from the handoff.

### Evidence that survives a new session

- **Spec handoff:** record the exact specification path and revision (commit or content digest), affected requirement IDs, agreed write paths and the validations expected. Unwritten or mutable inputs are not pinned.
- **Skeleton gate:** record the exact skeleton revision or digest, the independent reviewer and their review result, the actual commands and their outcomes, and any remaining blocker. A developer's self-check is not independent approval.
- **Acceptance handoff:** record the exact implementation revision, checked requirements, commands, result and untested cases. Keep scope and artifacts available to the next worker rather than relying on chat memory. For a nontrivial cross-session handoff, use the adjacent [CHANGE.md template](CHANGE.md) in a user-authorized documentation path or an existing issue or handoff record. Do not create duplicate records, force the template for tiny same-session changes, or write from Plan. If no destination is authorized, return the evidence in the response instead.

## Build

### A. Skeleton before logic

For the smallest useful vertical slice, wire typed signatures and replaceable boundaries; use explicit not-implemented states, never fake a valid result. Do not call real dependencies, mutate data or run migrations in this skeleton phase. Use inline or same-version pseudocode to map requirements to validation, authorization, side effects, transaction and error boundaries, and applicable timeout/retry/compensation rules. Omit irrelevant mechanics but make boundary decisions explicit.

An independent person or agent who did not write the skeleton reviews that exact commit or fingerprint against the pinned specification. Run the relevant build, type or equivalent checks and verify wiring, replaceable test boundaries and safe placeholder behavior. Record commands, artifact version and pass/block result. No independent approval means no business logic for the affected slice. Recheck affected skeletons when boundary or contract changes invalidate prior evidence.

### B. Implementation and acceptance

Implement the approved slice with its pinned inputs and constraints. Developers check their work; an independent reviewer verifies the exact implementation candidate. Close material findings and rerun affected checks. If independent final acceptance is unavailable on the exact implementation candidate, report acceptance as BLOCKED, name the missing review, and leave the implementation status separate. For individual checks report pass/fail/not-run/not-applicable with real evidence. Do not treat a screenshot, simulation or test count as a substitute for required acceptance. Compare outcomes and residual risks to the original goals; acceptance does not prove production readiness or usefulness.

## Refine

Use the existing contract for one scoped, compatible improvement. Preserve work outside the allowed paths and do not weaken expectations to get a green test. For changed in-scope behavior, record focused regression evidence and note untested effects; add tests only in allowed paths and mark the required check blocked if you cannot run or supply it. If the externally observable contract or architectural boundary would change, stop the affected part and return to Spec only through a separately directed invocation.

## Final checks

Trace core requirements to the responsible module or seam, contract, observation and task. Verify document and artifact versions agree. Report only real changes, evidence, blockers and the next eligible step. No automatic Git commits, remotes, merges, pushes, deploys or releases, and no circumvention of filesystem or runtime controls.
