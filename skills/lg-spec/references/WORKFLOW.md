# Let's Grunt: shared workflow

The four mode skills install as adjacent directories. The optional read-only companion, `lg-review`, also depends on Spec and is not a numbered milestone. This authoritative reference and its optional template live inside the Spec skill; do not install or package any entry point in isolation. This file is shared guidance, not another command. If an entry point is narrower than this file, the entry point wins. Selection alone, agreement on a design, a prior mode, successful QA and standing permission for other work do not authorize a new mode, slice, path or external action. Already authorized work may continue within its scope; never advance modes automatically. These instructions are not a sandbox.

## One confirmed step at a time

This applies to Plan, Spec, Build and Refine. Before doing project work, propose only the next concrete step: state its action and target, evidence or deliverable, and what it will not modify or do. Then wait for the user’s explicit confirmation of that step. A skill invocation, general direction, old or blanket approval, or assent to a different proposal does not authorize it. If the reply is ambiguous, name the proposed step and ask plainly. If the latest user message clearly confirms that exact pending proposal, do not ask twice.

Execute the confirmed step only, and stop at its boundary even if follow-on work looks obvious. Report actual evidence, outcome and blockers, then stop. You may identify the next eligible milestone for orientation; do not propose it for confirmation until the user re-enters the same mode. Starting a different mode requires a separate invocation. One step can involve several necessary tool calls, not several deliverables or gates. If scope or deliverable must change, stop and propose the revised step instead of treating the old confirmation as permission. Confirmation never expands the mode, tool permissions or external-action authorization; no automatic mode switch, push, deploy or release.

## Authority and audit trail

Before execution, bind the exact confirmation to the mode, numbered step or correction ID, pinned revision, scope, deliverable, allowed paths and external-action limits. Record the requester, executor, reviewer and human approver roles where applicable. In multi-person work, use a verified account and an authoritative role or scoped delegation record to confirm that the human approver can approve that exact action; a display name, forwarded assent and executor or reviewer status alone are not proof. Retain the original confirmation reference and the authority reference, not entire conversations or secrets.

Record that decision in an authorized durable log or existing scoped record before execution. After the step, append the actual outcome, version, check evidence and blockers, including when the step was denied or did not run, where authorized. If multi-person identity, adequate authority, or a durable authorized record cannot be verified, mark the step BLOCKED; do not execute. Plan remains project-read-only: a durable authorized conversation or approval record can be the trail, with no writes to project files. Solo work still records each step via existing safe handoff/evidence, without unnecessary identity checks. Do not create a new tracking destination or widen access without authorization. A single valid confirmation is enough.

### Interrupted work and exclusive ownership

Use one recorded executor per active step and one writer per overlapping scope. Check the existing authorized audit record before starting; if another executor is active, ownership overlaps, or an interruption ended without a recorded result, block duplicate execution. Reconstruct the actual state from the pinned candidate, working-tree changes and operation receipts as applicable. Record what completed, what is unresolved and who owns the next action. If state cannot be determined, leave it BLOCKED. Do not rerun or take over on the original approval: first resolve ownership and obtain explicit confirmation for one bounded recovery action if new execution is needed. If work is already complete, record reconciled evidence rather than executing it again. Do not invent locks or audit access.

## Self-review before asking for the next step

Before proposing a numbered step, check the previous step’s specific scope, expected evidence, exact version, and unresolved gaps against its confirmed proposal. At the first step, check only the supplied prerequisites and say there is no prior output. A justified N/A may be recorded; missing, stale, conflicting or failed material evidence is BLOCKED. Report what is wrong and what is still safe to keep. If new corrective execution is needed, propose one named correction within the affected step and wait for confirmation; do not propose later work as though the issue were resolved. Do not reexecute an already-completed confirmed step or ask to confirm it again. For Build, reconcile the module ledger against exact-version proof before proposing the next milestone. Self-review is neither user approval nor independent review.

## Numbered milestones

Use the next applicable number in order. Each numbered item is one separately confirmed milestone; the finer actions below are its scope, not automatic advancement. Mark N/A with a reason rather than silently skipping. Return to the affected milestone to correct blockers. Keep the dedicated independent gates even when an earlier review succeeded.

| # | Mode | Step and expected outcome |
| --- | --- | --- |
| 1 | Plan | Inspect the current project read-only: users, existing code or workflow, known constraints. |
| 2 | Plan | Define goals and boundaries: what the first version includes and excludes, and how to judge success. |
| 3 | Plan | Return a pasteable discussion brief separating decisions, assumptions, open issues and blockers; do not write a file. |
| 4 | Spec | Draft product specification: user flow, business rules, states, failures and acceptance measures. |
| 5 | Spec | Design architecture: modules, key call flow, data ownership, dependencies and open-source reuse, recovery. Mark security, privacy, performance and reliability as required or N/A with reasons. |
| 6 | Spec | Design API and UI/CLI interactions: inputs, outputs, errors, permissions, states, compatibility. |
| 7 | Spec | Design the data model and DDL: tables, indexes, constraints, transactions, migration and rollback. Markdown review only; no SQL execution. |
| 8 | Spec | Design test methods: in-scope behavior versus denial/degradation at boundaries; case, environment, fixture, trigger, expectation and evidence. For each required nonfunctional item specify scenario, pass criterion and observable evidence. |
| 9 | Spec | Cross-check and freeze the exact SPEC: align architecture/API/DDL/UI/tests; check required nonfunctional items map to acceptance; record version, task division, writable files and blockers. |
| 10 | Build | Design the smallest skeleton: call flow, signatures, wiring and pseudocode in a sketch, without writing functions or business logic. |
| 11 | Build | Create buildable skeleton with wired interfaces and explicit not-implemented outcomes, without real side effects. |
| 12 | Build | Independently review the exact skeleton’s signatures, wiring and build evidence. A failure blocks business logic. |
| 13 | Build | Implement the approved slice and relevant tests. Separate development and test roles; contract conflicts go to Spec, not altered acceptance. |
| 14 | Build | Developer self-tests: applicable build, static checks, unit/integration tests; capture commands, version and omissions. |
| 15 | Build | Independent code review and retest: the reviewer reports findings only. Any correction requires a separately confirmed developer action with bounded scope and a refreshed candidate digest; the independent reviewer retests that exact corrected candidate. No developer self-signoff. |
| 16 | Build | Independent acceptance of realistic operation paths; as needed, test end-to-end, recovery, performance and deployment rehearsal. Missing evidence is BLOCKED. |
| 17 | Build | Deliver and evaluate: verify documentation, configuration and startup, compare measured outcomes to goals, report gaps/risks and a recommendation. |
| 18 | Refine | Agree on one compatible refinement and regression points, including behavior that must stay unchanged. |
| 19 | Refine | Make one approved change only; fill relevant test gaps only within the approved paths. |
| 20 | Refine | Run targeted regression and report. Repeat the affected independent review if a core boundary changes; stop and return to Spec if a contract must change. |

### Optional production release (outside the 20 steps)

Step 17 is delivery and evaluation, not deployment. If production release is requested, verify readiness and propose each needed external action separately: commit, push, actual migration, deployment or publication. Before deployment agree on the exact candidate, migration/rollback plan, rollback triggers, monitoring window and responsible operator. After an authorized deploy run the approved smoke checks and observe the agreed signals; record results and escalate or invoke the separately authorized rollback procedure on a trigger. Without a verified candidate, operation approval, or recovery plan for material risk, block that production action. Do not add a numbered milestone or release by default.

## Planning

For the confirmed read-only planning step, start with a concrete user and desired outcome, the smallest usable path, non-goals and one recommended tradeoff. Check source facts without writing. Ask questions only when the answer could change architecture, product behavior, authority, distribution rights or material cost; state reversible assumptions instead of asking by default. Identify verified facts, decisions, assumptions and blockers separately. A fixture illustrates acceptance; it is not the product.

## Specification

Freeze a coherent version before implementation. Keep existing document organization; a small project may combine sections. Only write within the authorized documentation scope. If an input is missing, document the question, recommended default, consequence, and affected work; independent parts can continue. After recording goals, propose and confirm each applicable design step separately: product specification → architecture → API/UI → data/DDL → test methods → cross-check and freeze. This is a drafting order, not permission to run anything; reconcile dependencies before freezing the specification. Scale depth to risk, use a single page when enough, and mark inapplicable items N/A with a brief reason.

| Contract | Evidence or decision needed |
| --- | --- |
| Goals and scope | Actors, usable path, non-goals, behavioral invariants, failure expectations and measurable acceptance with stable IDs such as R1. Quantitative claims need a workload and measurement method. |
| 1. Architecture | Module ownership, request flow, data authority, trust/deployment boundaries, errors and recovery. Explain decisions, rejected options and reconsideration conditions. |
| 2. API and UI/CLI | Examples, input/output, roles, errors, state transition, compatibility, retry/timeout/idempotency as needed. Map UI or CLI flows to contracts, including loading, denial, retry and recovery where applicable. |
| 3. Data and DDL | If applicable: schema, constraints, indexes, concurrency, transactions, retention, cache/queue semantics and recovery. A Markdown DDL draft is review-only; do not create migrations or execute SQL in Spec. State why data design is inapplicable if none. |
| 4. Test methods | For each material requirement, record a case ID, fixture/environment, trigger (normal input or, where relevant, a benign simulated dependency failure), assertion and what observation decides pass/fail. Describe what a separate reviewer should check and retain, and distinguish skeleton checks from final behavior checks. Plan tests only; do not execute them in Spec. |
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

Confirm these steps separately: design the skeleton, prepare the runnable skeleton, run independent skeleton review, implement the authorized slice, run developer self-tests, run independent review/retest, run independent acceptance, and deliver with outcome evaluation. A passed review does not itself authorize the next step. In complex projects, pin shared contracts and repeat Build per independently verifiable vertical slice; work in parallel only where scopes and write ownership do not overlap, and check cross-module integration in the existing acceptance step.

### Evidence gate

Apply at milestones 12, 14–17 and 20, and to each module row. Keep states separate: **planned** (no work yet), **in progress**, **reported** (a worker claims a result), and **verified** (matching observable evidence was inspected or independently rerun). Use the previous-step self-review to reconcile reported against verified. Never turn a worker summary, pasted output, or test count alone into verified completion. The required independent verifier is not the developer.

For a change, inspect the actual artifact or diff, its allowed scope and provenance, and pin the exact candidate revision. For a test claim, require the actual command, environment and exit outcome, names of assertions or cases, executed/skipped/failed counts, and a retained run artifact or independent rerun. Verify the assertions required by the current milestone actually ran and passed on that revision. A no-op, zero discovered or executed, required skips, unverified cached results, or a stale revision is not proof. For external operations require the original service receipt or an independently observed state tied to the confirmed target, not a report alone. Flag the missing evidence and mark affected acceptance BLOCKED; do not promote progress or propose the next numbered step until material evidence is verified. A justified N/A is recorded as N/A, not a passing run.

### How the user can verify acceptance

At independent acceptance (#16), give the user a short verification recipe and carry it into delivery (#17). Include the exact tested revision or digest, the directory and prerequisites, and one copy-paste command if possible (otherwise the shortest numbered manual steps). State what proves a pass, what indicates failure or skipped checks, and which behavior was not tested. Use the same format for focused regression (#20) when the user needs to reproduce the result. A recipe is not proof that a check ran.

### Module progress

Maintain one row per active submodule in the authorized [CHANGE.md](CHANGE.md) or an existing task sheet. Record module, development and test owners as applicable, development status, test/independent status, bound candidate revision or digest, evidence and blockers. Update after each authorized Build milestone within the same step’s approved scope; if no writable destination was authorized, return the updated rows in the result instead. This adds no confirmation milestone, file write or external tool by default.

Keep development and testing independent: implemented or developer-tested does not mean independently accepted. Apply the Evidence gate to development and test claims separately. Associate each result with its exact version, preserve prior results as history, and mark affected tests pending or blocked when a changed candidate needs recheck. At self-review, verify both tracks against exact-version proof; never advance one track by inference from the other.

### A. Skeleton before logic

At milestone 10, design one useful vertical slice with a compact diagram or table showing its entry point, dependencies, typed signatures or contracts, and explicit not-implemented outcome. Use pseudocode for validation, authorization, sequencing, side-effect, transaction and failure boundaries as applicable. Deliver a sketch only; do not create runnable stubs until milestone 11 is separately confirmed.

For the smallest useful vertical slice, wire typed signatures and replaceable boundaries; use explicit not-implemented states, never fake a valid result. Do not call real dependencies, mutate data or run migrations in this skeleton phase. Use inline or same-version pseudocode to map requirements to validation, authorization, side effects, transaction and error boundaries, and applicable timeout/retry/compensation rules. Omit irrelevant mechanics but make boundary decisions explicit.

An independent person or agent who did not write the skeleton reviews that exact commit or fingerprint against the pinned specification. Run the relevant build, type or equivalent checks and verify wiring, replaceable test boundaries and safe placeholder behavior. Record commands, artifact version and pass/block result. No independent approval means no business logic for the affected slice. Recheck affected skeletons when boundary or contract changes invalidate prior evidence.

### B. Implementation and acceptance

Implement the approved slice with its pinned inputs and constraints. Developers check their work; an independent reviewer verifies the exact implementation candidate. Close material findings and rerun affected checks. If independent final acceptance is unavailable on the exact implementation candidate, report acceptance as BLOCKED, name the missing review, and leave the implementation status separate. For individual checks report pass/fail/not-run/not-applicable with real evidence. Do not treat a screenshot, simulation or test count as a substitute for required acceptance. Compare outcomes and residual risks to the original goals; acceptance does not prove production readiness or usefulness.

## Refine

For each refinement, confirm scope, implementation and regression as separate steps. At scope review, classify risk: low-risk wording or presentation changes need targeted regression; contract-compatible changes touching authorization, data, or a critical path require affected independent re-verification; a change to the contract returns to Spec. Do not use Refine to bypass a gate. Use the existing contract for one scoped, compatible improvement. Preserve work outside the allowed paths and do not weaken expectations to get a green test. For changed in-scope behavior, record focused regression evidence and note untested effects; add tests only in allowed paths and mark the required check blocked if you cannot run or supply it. If the externally observable contract or architectural boundary would change, stop the affected part and return to Spec only through a separately directed invocation.

## Final checks

Trace core requirements to the responsible module or seam, contract, observation and task. Verify document and artifact versions agree. Report only real changes, evidence, blockers and the next eligible step. No automatic Git commits, remotes, merges, pushes, deploys or releases, and no circumvention of filesystem or runtime controls.
