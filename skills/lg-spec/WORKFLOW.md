# Let's Grunt: shared workflow

The four entry points install as adjacent directories. This file is shared guidance, not another command. If an entry point is narrower than this file, the entry point wins. Selection alone, agreement on a design, a prior mode, successful QA and standing permission for other work do not authorize a new mode, slice, path or external action. Already authorized work may continue within its scope; never advance modes automatically. These instructions are not a sandbox.

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

### Evidence that survives a new session

- **Spec handoff:** record the exact specification path and revision (commit or content digest), affected requirement IDs, agreed write paths and the validations expected. Unwritten or mutable inputs are not pinned.
- **Skeleton gate:** record the exact skeleton revision or digest, the independent reviewer and their review result, the actual commands and their outcomes, and any remaining blocker. A developer's self-check is not independent approval.
- **Acceptance handoff:** record the exact implementation revision, checked requirements, commands, result and untested cases. Keep scope and artifacts available to the next worker rather than relying on chat memory. Store evidence only where writing has been authorized.

## Build

### A. Skeleton before logic

For the smallest useful vertical slice, wire typed signatures and replaceable boundaries; use explicit not-implemented states, never fake a valid result. Do not call real dependencies, mutate data or run migrations in this skeleton phase. Use inline or same-version pseudocode to map requirements to validation, authorization, side effects, transaction and error boundaries, and applicable timeout/retry/compensation rules. Omit irrelevant mechanics but make boundary decisions explicit.

An independent person or agent who did not write the skeleton reviews that exact commit or fingerprint against the pinned specification. Run the relevant build, type or equivalent checks and verify wiring, replaceable test boundaries and safe placeholder behavior. Record commands, artifact version and pass/block result. No independent approval means no business logic for the affected slice. Recheck affected skeletons when boundary or contract changes invalidate prior evidence.

### B. Implementation and acceptance

Implement the approved slice with its pinned inputs and constraints. Developers check their work; an independent reviewer verifies the exact implementation candidate. Close material findings and rerun affected checks. Report pass/fail/not-run/not-applicable with real evidence. Do not treat a screenshot, simulation or test count as a substitute for required acceptance. Compare outcomes and residual risks to the original goals; acceptance does not prove production readiness or usefulness.

## Refine

Use the existing contract for one scoped, compatible improvement. Preserve work outside the allowed paths and do not weaken expectations to get a green test. Verify the smallest relevant regression and note untested effects. If the externally observable contract or architectural boundary would change, stop the affected part and return to Spec only through a separately directed invocation.

## Final checks

Trace core requirements to the responsible module or seam, contract, observation and task. Verify document and artifact versions agree. Report only real changes, evidence, blockers and the next eligible step. No automatic Git commits, remotes, merges, pushes, deploys or releases, and no circumvention of filesystem or runtime controls.
