# Let's Grunt: shared workflow

The four mode skills install as adjacent directories. The optional read-only companion, `lg-review`, also depends on Spec and is not a numbered milestone. This authoritative reference and its optional template live inside the Spec skill; do not install or package any entry point in isolation. This file is shared guidance, not another command. If an entry point is narrower than this file, the entry point wins. Selection alone, agreement on a design, a prior mode, successful QA and standing permission for other work do not authorize a new mode, slice, path or external action. Already authorized work may continue within its scope; never advance modes automatically. These instructions are not a sandbox.

## Project filesystem boundary

Before any filesystem operation, bind the task to the verified physical project root and permitted paths for this step. Use an explicitly supplied project root when it can be verified from host or scoped project evidence. Ask only if the root cannot be verified or the sources conflict. A known root does not authorize a numbered step or outside access. Apply the same boundary to the executor, independent reviewers and every delegated tool or process. It covers reads, listings, searches, metadata checks, writes and any files a command or tool would access indirectly. Use the host-supplied skill text or its exact bundled workflow through authorized skill access. Loading those instructions grants no access to external project data.

This Spec reference is the single editing source. Plan packages a read-only copy beneath its own skill directory with the expected digest in its entry point. When its host exposes no bundled file, use an identified in-project copy whose version or digest verifiably matches the packaged workflow. Pause if no matching copy can be obtained through allowed paths. Keep reference access within the host-authorized skill bundle or the verified project.

- Anchor relative paths to a verified in-project base. Normalize traversal, check containment by path components and inspect link metadata only within the allowed boundary. Stop before following a symlink, linked Git metadata or another indirection outside it. For a new file, verify the destination and nearest existing parent. For searches, constrain roots, expansion and link traversal before running the search. A tool's default working directory and read-only mode are insufficient proof of confinement.
- Keep home-directory scans and sibling repositories out of the default scope. Treat external SDKs, Flutter caches, dependency stores and tools that discover external configuration as external accesses. If an operation needs one, give the verified project initiator the exact outside path, operation, purpose and narrowest scope. If the path is unknown, use already supplied evidence or ask for the specific path. Searching the home directory to discover it is outside scope. Wait for explicit approval of the bounded access and preserve the original record. Prior step approval, reviewer status or an OS permission prompt grants no filesystem exception. An approved exception still requires the applicable step and host permissions.
- Use host-enforced filesystem scoping for autonomous execution, child processes and reviewer sessions whenever supported, including read restrictions. Verify the actual scope before dispatch. When enforcement is unavailable, use only operations whose entire access is demonstrably inside the permitted paths or work from already supplied evidence. Stop any affected action or review whose access cannot be constrained, and continue other authorized work. Do not describe an unconfined run as isolated or safe, or retry via another unrestricted tool.

## Step gate chosen in Plan

Use a mode and confirmer rule already stated by the verified human project authority. **Mode 2** means **Trust mode** with confirmation from any one verified eligible project participant, subject to any stricter recorded scope or quorum. Carry a verified choice from Plan into Spec without repeating the question. At the first Plan round, ask only for any necessary choice or confirmer detail that remains unclear. A policy may name specific verified people, eligible project members, an independent verifiable AI explicitly delegated by the human for a bounded workflow gate, or a required combination. “Any” never includes outsiders. With no choice, default to Authorization mode and the verified project owner; if owner authority cannot be verified, block. An invalid or ambiguous rule cannot broaden eligibility. Choosing a policy does not confirm the first step.

Every step in **both modes** requires a fresh actual confirmation of the exact proposal from the eligible actor(s), before execution. Propose one action with target, evidence/deliverable and limits; check predecessor or first-step inputs; obtain confirmation; execute, verify and report. In Authorization mode, stop and wait for re-entry after each step. In Trust mode, after self-review the agent may request the next in-scope confirmation from delegated confirmers without an owner ping or re-entry. It must wait for the actual confirmation and required quorum, counting each verified principal once across channels and aliases. Treat changed proposals and expired or revoked approvals as requiring fresh confirmation. Apply required approver identities and actor-type composition in addition to the count. An applicable denial, unclear or conflicting response from a required confirmer, or an agreed veto, blocks even if enough others assent. Block unresolved conflicting confirmations without a predefined applicable resolution rule; never reinterpret silence, ambiguity or denial as assent. It stops at blockers or mode completion and never starts another mode. Standalone Review retains explicit confirmation. Independent acceptance is a separate evidence check, not supplied by workflow confirmation. Scope changes, external actions and platform approvals still require applicable human authorization; AI cannot grant it.

In Plan record the decision only in authorized durable chat or approval history, then carry its reference in the Plan handoff and persist it only in an authorized Spec step. Reverify the policy, scope, actor eligibility and current grant before each step or on resume. Do not combine partial directions from different initiators or reuse an old confirmation. Apply verified revocation or narrowing before any later action.

## Independent review before asking a human

After the executor self-check and before requesting step confirmation, obtain an independent read-only review of the exact step proposal. Check only this step's minimum deliverable, hard phase constraints, actual evidence and risks. Carry the pinned revision or digest, scoped proposal, relevant prior output and source evidence. If this is the first step, record why predecessor evidence is N/A and still review the proposed scope and prerequisites. Ordinary Plan and Spec reviews use this narrow scope.

A finding blocks only the affected scope when it invalidates current acceptance or required evidence, changes a product commitment, or creates material safety, data, permission or recovery risk. Record editorial and reversible implementation choices without blocking; do not reopen a passing step for them. For each blocking finding, give the threatened requirement or invariant, the evidence, and the smallest check or correction that could clear it. Mark suggestions and polish as non-blocking even if worth doing later. Missing prerequisite evidence is a blocker for that check, not a product failure. Do not downgrade an existing hard gate or claim a required check ran.

Save the full outcome review for Spec #9 and use standalone `lg-review` only if explicitly invoked. Asking for a missing product decision or source evidence is a clarification, separate from requesting step confirmation.

Use an independent reviewer in the current host, or equivalent traceable evidence from a genuinely independent person or separate review context. Before dispatch or reuse, verify compliance with the **Project filesystem boundary**, including any approved outside paths. Verify independence from execution, read-only scope, exact proposal and revision, reviewed evidence, result and original reference. Tool names and receipt formats can vary. The executor's own verdict cannot establish independence. Reuse a complete original result while those facts remain valid. Ask for step confirmation only after that review passes. If independence, revision, evidence or a passing result cannot be verified, mark the affected gate **BLOCKED**. This narrow review is neither step confirmation nor the later independent acceptance checks. A reviewer’s report cannot serve as the reviewer's formal step confirmation.

## Review log

Keep one discoverable project review log: reuse an existing authorized evidence record that can hold the required rows. Otherwise propose `docs/REVIEW_LOG.md` at an authorized documentation step; no implicit file creation or new access. The [review log template](REVIEW_LOG.md) defines the rows. Link its entry or authorized chat/trace from the step and module status; do not copy identical findings into multiple records.

Keep executor self-check, independent pre-review, formal confirmation and independent QA as distinct entry types; none substitutes for another. Each row binds role and verifiable non-secret actor ID, actual trace reference, time, exact artifact or proposal and revision/digest, scope, PASS/FAIL/BLOCKED, evidence and findings. If no review ran, record BLOCKED and why, with no fictitious reviewer or trace. A missing or stale result cannot pass; mark a replacement as a new row and link the superseded one.

Reviewers and subagents return findings to the coordinator; they do not write the project log. Plan and standalone Review return the current note in chat and write no project files. The authorized coordinating writer links or records it at the next permitted write step. If no destination is authorized, keep the note in the existing authorized chat, retain its reference, and never treat unavailable required audit evidence as a pass.

## Authority and audit trail

Before execution, record the verified human policy grantor, authority evidence, original policy/grant reference, time, scope and confirmer/quorum rule. For each step record the mode, step or correction ID, pinned revision, scope, deliverable, paths and external-action limits, plus each actual confirmer’s verified identity or auditable AI agent/session ID, actor type, scoped delegation/membership evidence, original confirmation reference and time. Distinguish policy grantor, requester, actual confirmer, executor and independent reviewer. An executor cannot confirm its own step. A standing grant, inferred acceptance, display name, forwarded assent or worker summary is not step confirmation. A revoked, stale or out-of-scope delegation does not count.

Record before execution in an authorized durable record; afterward append outcomes, versions, evidence and blockers. In both solo and multi-person work, missing identity, authority, actual confirmation, quorum, time/reference or authorized audit destination is **BLOCKED**. Do not manufacture agent authority, widen access, or store secrets or whole conversations.

### Interrupted work and exclusive ownership

Use one recorded executor per active step and one writer per overlapping scope. Check the existing authorized audit record before starting; if another executor is active, ownership overlaps, or an interruption ended without a recorded result, block duplicate execution. Reconstruct the actual state from the pinned candidate, working-tree changes and operation receipts as applicable. Record what completed, what is unresolved and who owns the next action. If state cannot be determined, leave it BLOCKED. Do not rerun or take over on the original approval: first resolve ownership and obtain explicit confirmation for one bounded recovery action if new execution is needed. If work is already complete, record reconciled evidence rather than executing it again. Do not invent locks or audit access.

## Self-review before asking for the next step

Before proposing or starting after fresh confirmation in Trust mode a numbered step, check the previous step’s specific scope, expected evidence, exact version, and unresolved gaps against its recorded proposal and authority. At the first step, check only the supplied prerequisites and say there is no prior output. A justified N/A may be recorded; missing, stale, conflicting or failed material evidence is BLOCKED. Report what is wrong and what is still safe to keep. If new corrective execution is needed, propose one named correction within the affected step and wait for confirmation; do not propose later work as though the issue were resolved. Do not reexecute an already-completed confirmed step or ask to confirm it again. For Build, reconcile the module ledger against exact-version proof before proposing the next milestone. Self-review is neither user approval nor independent review.

## Numbered milestones

Use the next applicable number in order. Each numbered item is one separately scoped milestone governed by the chosen step policy; the finer actions below are its scope, not automatic advancement. Mark N/A with a reason rather than silently skipping. Return to the affected milestone to correct blockers. Keep the dedicated independent gates even when an earlier review succeeded.

| # | Mode | Step and expected outcome |
| --- | --- | --- |
| 1 | Plan | Inspect the current project read-only: users, existing code or workflow, known constraints. |
| 2 | Plan | Define goals and boundaries: what the first version includes and excludes, and how to judge success. |
| 3 | Plan | Ask the task initiator about the goal, boundaries and first useful outcome. Return a pasteable, actionable Plan handoff with the answers, acceptance, work packages, owners, evidence, dependencies, blockers and next step. Keep it in chat. |
| 4 | Spec | Draft product specification: user flow, business rules, states, failures and acceptance measures. |
| 5 | Spec | Design architecture: modules, key call flow, data ownership, dependencies and open-source reuse, recovery. Mark security, privacy, performance and reliability as required or N/A with reasons. |
| 6 | Spec | Design API and UI/CLI interactions: inputs, outputs, errors, permissions, states, compatibility. |
| 7 | Spec | Design the data model and DDL: tables, indexes, constraints, transactions, migration and rollback. Markdown review only; no SQL execution. |
| 8 | Spec | Design test methods: in-scope behavior versus denial/degradation at boundaries; case, environment, fixture, trigger, expectation and evidence. For each required nonfunctional item specify scenario, pass criterion and observable evidence. |
| 9 | Spec | Have an independent reviewer assess whether the candidate solves the initiator's problem and whether its direction and tradeoffs make sense. Cross-check the design and acceptance, walk through the candidate on paper, and obtain the verified task initiator's confirmation before freezing that exact SPEC version. Record task division, writable files and blockers. |
| 10 | Build | Verify the freeze, walkthrough and task-initiator confirmation for the exact pinned SPEC. With the regular step authorization, sketch the smallest skeleton: call flow, signatures, wiring and pseudocode. Function and logic work belongs to later steps. |
| 11 | Build | Create buildable skeleton with wired interfaces and explicit not-implemented outcomes, without real side effects. |
| 12 | Build | Independently review the exact skeleton’s signatures, wiring and build evidence. A failure blocks business logic. |
| 13 | Build | Implement the approved slice and relevant tests. Separate development and test roles; contract conflicts go to Spec, not altered acceptance. |
| 14 | Build | Developer self-tests: applicable build, static checks, unit/integration tests; capture commands, version and omissions. |
| 15 | Build | Independent code review and retest: the reviewer reports findings only. Any correction after failed evidence requires a separately and explicitly confirmed scoped developer action and a refreshed candidate digest; the independent reviewer retests that exact corrected candidate. No developer self-signoff. |
| 16 | Build | Independent acceptance of realistic operation paths; as needed, test end-to-end, recovery, performance and deployment rehearsal. Missing evidence is BLOCKED. |
| 17 | Build | Deliver and evaluate: verify documentation, configuration and startup, compare measured outcomes to goals, report gaps/risks and a recommendation. |
| 18 | Refine | Agree on one compatible refinement and regression points, including behavior that must stay unchanged. |
| 19 | Refine | Make one approved change only; fill relevant test gaps only within the approved paths. |
| 20 | Refine | Run targeted regression and report. Repeat the affected independent review if a core boundary changes; stop and return to Spec if a contract must change. |

### Optional production release (outside the 20 steps)

Step 17 is delivery and evaluation, not deployment. If production release is requested, verify readiness and propose each needed external action separately: commit, push, actual migration, deployment or publication. Before deployment agree on the exact candidate, migration/rollback plan, rollback triggers, monitoring window and responsible operator. After an authorized deploy run the approved smoke checks and observe the agreed signals; record results and escalate or invoke the separately authorized rollback procedure on a trigger. Without a verified candidate, operation approval, or recovery plan for material risk, block that production action. Do not add a numbered milestone or release by default.

## Planning

For each authorized read-only planning step, identify the user, product commitments, constraints and minimum observable acceptance for the first useful result. Use primary project evidence to resolve facts. Leave UI details, algorithms and the failure-test matrix to their applicable Spec or Build steps. Keep facts, decisions, assumptions and blockers distinct.

### Plan, Spec and Build transitions

On entry, resume or a user-directed switch between Plan and Spec or from Spec to Build, first read the available verifiable discussion, handoff and current step state. Check each relevant decision, outcome and authorization against its original source and scope. Carry forward valid evidence and completed work without repeating questions, steps or confirmations. A past confirmation may prove its own step was completed; any new action still needs its own applicable authorization. Never switch modes automatically or report an incomplete Plan as complete.

Classify each missing input before deciding whether to wait:

- **A. Reversible detail.** If the answer can be inferred or corrected without materially affecting the goal, boundaries, first useful outcome, authority or risk, use the available evidence. If it does not resolve the detail and no answer has arrived, tell the user what default or assumption you adopted, what it affects and how it can be corrected. Continue the currently authorized step. Record the assumption as provisional, separate from anything the initiator confirmed.
- **B. Material decision or required evidence.** First check accessible sources for missing facts. If a material fact remains unverifiable, request the missing evidence or access from its holder. Ask the task initiator about unresolved product tradeoffs that would change the goal, boundaries or first useful result. Ask the appropriate authority for a missing authorization. Identify exactly what is missing, why it matters, who must respond and where the affected action pauses. Continue unrelated authorized work. Resume the affected action after receiving and recording a valid response or evidence. Independent review, same-version SPEC outcome confirmation by the initiator, and numbered-step authorization always require actual verifiable evidence.

If the user invokes Spec directly and a material Plan input is missing, surface and resolve only that input using the same diagnosis. Reuse the completed parts of Plan and wait at the affected prerequisite before starting Spec work that depends on it. Clarifying the missing input does not execute a Plan milestone. If resolving it needs authorized Plan work, ask the user to invoke Plan explicitly. Apply the same diagnosis to missing prerequisites on a return to Plan.

In Build, A applies only to a clearly explainable, low-risk, reversible implementation detail outside the contract and within the current authorized step. Record the assumption, its effect and correction path. If the answer could change a user commitment or an architecture, API, DDL or permission boundary, treat it as B. Pause the affected Build step and point to the exact Spec step that owns the decision. Identify the authorized decision-maker and required reply. Have the user explicitly invoke Spec for contract changes. Keep Build edits within the pinned contract. A missing or unverifiable same-version freeze, substantive independent Spec Review, paper walkthrough, initiator outcome confirmation or numbered-step authorization is always B. Diagnose the missing item and pause even when implementation could otherwise proceed.

Start from the user's request in plain language. Keep the numbered milestones and technical audit in the working record. Handle reversible defaults and accessible evidence yourself. If blocked before there is a deliverable to show, state what is missing, who can resolve it and where work resumes. Keep next-phase procedures in the working record.

When the current host supports native-agent selection and the next task needs a different agent, explain how the developer can select it manually before invoking the next skill. Keep native agent selection, skill invocation and authorization separate. Apply the project filesystem boundary regardless of the agent.

### Plan and Spec reply order

Show the complete in-scope Plan or Spec deliverable and confirmed decisions first. State reversible assumptions inline. Keep Plan at the level of the goal, key exclusions and minimum acceptance.

At the end, use a prominent **Needs your decision** heading in the user's language, such as **需要你决定**, for material product tradeoffs only. For each item, ask the question directly, give the viable options and their main impact, and recommend one when there is a basis. Put the question and the information needed to answer it in this section. Links or line numbers may support it. Omit this section if there are no product decisions to make.

Use one native question card after the design when supported. Put the answerable question and its options, impact and recommendation in the card under the heading or directly below it. Use text when cards are unavailable or confirmed unsent. Check uncertain delivery before falling back. Avoid repeating a card question in text and report only cards actually sent.

Use separate end labels for step authorization, initiator confirmation and evidence only when a response of that type is required. Keep those requests separate from product tradeoffs. Do not repeat the design in those sections. While a required reply is pending, state which dependent work is paused and leave the handoff open. Other authorized work can continue. After the phase is complete, put the manual next-step hint on the last line.

A product answer records that choice. Formal step authorization and the initiator's own outcome confirmation require separate valid records. Apply any delegation only within its recorded scope and preserve human-only decisions.

### Manual next step by host

After Plan completes, the next skill is `lg-spec`. After Spec #9 completes, it is `lg-build`. Use the current host's verified skill picker, registration or other native invocation for that exact skill. Confirm the entry from host-provided evidence within the permitted scope. Apply this based on available capabilities, including on unlisted hosts.

Use the same host check for a manual Build or Refine referral. If work is blocked, explain the blocker and name the skill for resolving it without presenting the phase as complete.

Examples of native entries, when verified in the current host:

- **Codex:** a dollar sign (`$`) followed by the skill ID.
- **OpenCode V2:** use `@lg-spec` or `@lg-build` only when the host verifies it is a native skill-picker entry. The user selects the native agent manually where needed, then selects the skill. Do not suggest OpenCode slash commands to load these skills.
- **DSH:** show its short command only when that exact command is registered in the current host. Use the spelling returned by the host.

If support cannot be verified, give a plain-language instruction naming the skill and its purpose, such as **下一步：手动加载 lg-spec，继续当前项目的规格设计。** Give only one next-step line. Leave invocation and native-agent selection to the user.

## Specification

Freeze a coherent version before implementation. Keep existing document organization; a small project may combine sections. Only write within the authorized documentation scope. If an input is missing, document the question, recommended default, consequence, and affected work; independent parts can continue. After recording goals, scope each applicable design step separately under the selected gate policy: product specification → architecture → API/UI → data/DDL → test methods → cross-check and freeze. This is a drafting order, not permission to run anything; reconcile dependencies before freezing the specification. Scale depth to risk, use a single page when enough, and mark inapplicable items N/A with a brief reason.

| Contract | Evidence or decision needed |
| --- | --- |
| Goals and scope | Actors, usable path, non-goals, behavioral invariants, failure expectations and measurable acceptance with stable IDs such as R1. Quantitative claims need a workload and measurement method. |
| 1. Architecture | Module ownership, request flow, data authority, trust/deployment boundaries, errors and recovery. Explain decisions, rejected options and reconsideration conditions. |
| 2. API and UI/CLI | Examples, input/output, roles, errors, state transition, compatibility, retry/timeout/idempotency as needed. Map UI or CLI flows to contracts, including loading, denial, retry and recovery where applicable. |
| 3. Data and DDL | If applicable: schema, constraints, indexes, concurrency, transactions, retention, cache/queue semantics and recovery. A Markdown DDL draft is review-only; do not create migrations or execute SQL in Spec. State why data design is inapplicable if none. |
| 4. Test methods | For each material requirement, record a case ID, fixture/environment, trigger (normal input or, where relevant, a benign simulated dependency failure), assertion and what observation decides pass/fail. Describe what a separate reviewer should check and retain, and distinguish skeleton checks from final behavior checks. Plan tests only; do not execute them in Spec. |
| Reuse and authority | Separate actual dependencies from candidates. Record primary source, pinned version, applicable license, reuse boundary and exit plan. For access or AI features, document identities, isolation, revocation, egress, usage source and unknown outcomes. |
| Acceptance | Map requirements to implementation seams and assertions, environment and evidence. In-scope failure calls for repair; explicitly unsupported behavior tests expected rejection or degradation, not expansion. |

### Scope the change, not the whole system

For an existing system, record what this slice changes and which nearby behavior must stay unchanged. Link to the exact existing contract or verified evidence instead of restating it. Keep requirement IDs stable and link changed IDs to affected scenarios and dependencies. When implementation reveals a contract conflict, identify the changed behavior and impacted checks, then pause only dependent work and return to the authorized Spec step. Reuse unaffected evidence only when the candidate and dependency match are established; an affected digest, confirmation or required approval still needs its own gate.

At #8, choose the smallest discriminating test for the actual risk. Describe precondition, trigger, observable pass/fail and the environment or data required, including what cannot be tested there. For a consequential or irreversible change, add the relevant failure or recovery check: compatibility/mixed versions, partial failure, rollback or forward recovery, and signals or thresholds needed to decide whether to proceed. Do not force rollout machinery onto a small reversible change; if an irreversible change has no credible recovery, name that constraint and block the affected action rather than invent a rollback.

### Spec #9 outcome walkthrough and confirmation

Apply the **Project filesystem boundary** to the reviewer and any reused evidence. The pinned SPEC and supplied evidence should suffice for the paper walkthrough.

Before the paper walkthrough, a read-only reviewer independent of the SPEC authors must inspect the actual pinned candidate against the initiator's goal. Ask whether it solves the right problem, whether the proposed outcome is useful, and whether the direction and tradeoffs are justified. Require a recorded pass on substance for that exact version. Accept traceable evidence from any supported independent review context. Keep the technical cross-check of architecture, API/UI, data/DDL, test design and nonfunctional criteria against acceptance, and keep the initiator's own outcome confirmation separate.

Using representative inputs and the exact SPEC version intended for freezing, walk through one typical path and one critical failure or recovery path on paper. Show the user a short result card in their language: what they get when it works, what happens to their data or process on failure, what remains out of scope or unverified, and any uncertainty that could change the recommendation. After the card, ask whether that same-version outcome meets their needs under a separate initiator confirmation label. Save the scenarios, evidence and technical detail in the existing audit record.

Require explicit confirmation from the verified human task initiator that the expected outcome of this exact SPEC version meets their needs. Keep this product confirmation separate from technical review, the Plan-defined confirmer policy, and numbered-step authorization. Preserve the existing pre-human independent review and step approvals. Freeze after receiving the actual explicit confirmation. If the initiator raises an objection, revise the SPEC within the authorized scope and resolve it. A missing or unverifiable initiator identity, missing or unclear confirmation, a version mismatch, or unresolved conflicting feedback blocks the Build handoff. After #9 is complete, give one manual next-step line for Build using **Manual next step by host**. Build authorization remains a separate step.

Reuse complete, verifiable #9 evidence for the exact unchanged version, including a record that is ready while another is still pending. Reuse any matching initiator confirmation. Every revision or digest change requires fresh confirmation on the new version from the initiator. If the outcome or commitments change, repeat independent Spec Review and the paper walkthrough first. For an editorial change, obtain a traceable independent check explicitly binding the prior findings and scenarios to the new version. Record confirmation outside the pinned SPEC so the receipt cannot change its digest.

Use an existing authorized handoff, project evidence record or durable chat. Record the exact SPEC path and revision or content digest, the independent review reference, scenarios and inputs, expected results and gaps, material assumptions, recommendation, and the verified confirmer's identity, confirmation time and original message or receipt reference. Use distinct references for independent Spec Review, the paper walkthrough and the outcome confirmation. Build reviews actual artifacts and run evidence separately.

## Handoff

Use a common specification version or commit and one owner per writable path. Each role card names the role, task ID, pinned inputs, requirement/test IDs, allowed files, non-goals, prerequisites, verification method, expected evidence, stop condition and status. Report blocked dependencies explicitly. Separate product clarification, development, independent review/testing and coordination. A card is not authorization or proof that an agent ran. If a file is not yet written, include its exact text or a verified readable input rather than a future path.

### Plan #3 handoff

Before handing off to Spec, check the initiator's existing answers about the goal, boundaries and first useful result. Ask only about material gaps or conflicts. Return a one-page brief by default in chat, not another project artifact. Separate the verified goal, exclusions and acceptance conditions (with available source anchors) from assumptions, pending choices and blocking unknowns. Preserve the initiator's answers and their source references alongside the verified mode/confirmation policy and scope reference.

In the default user message, give the first useful result and key exclusions before any questions that need a person. Follow **Plan and Spec reply order**. When Plan is complete, end with one manual next-step line for Spec using **Manual next step by host**. Keep the technical handoff and its sources available separately in the existing chat or authorized record.

Break the outcome into the fewest useful work packages. For each give an ID, owner or role (separate development and independent QA where relevant), predecessor IDs or sequence, concrete deliverable, observable completion evidence and any open gate. Identify parallel lanes only where dependencies and write ownership allow it. Mark unnamed owners or unverified inputs as pending; do not invent a decision, assignment, permission or result. Record the smallest next eligible step and its prerequisite/confirmation. Leave `lg-spec` selection and invocation to the user. Scale detail with risk. Make the first useful package independently verifiable: name the observable result, the prerequisite that actually gates it, and what finding would make it fail. When Plan is already clear, reuse existing records instead of creating another checklist. This is a handoff to Spec, not architecture, API/DDL design, implementation, dispatch or permission to write.

### Context handoff

Share the facts a recipient needs, not a transcript of the conversation. Plan ends with a pasteable actionable brief; Spec verifies source anchors and keeps confirmed constraints separate from pending decisions. For substantive or multi-stage Build work use separate clean development and independent review contexts when the host supports them. Keep truly local, small work in the current context if that is sufficient and briefly record why; this does not waive any independent gate. If clean contexts are unavailable, provide a safe handoff instead of claiming one was opened or resuming on a recipient’s behalf.

A developer handoff carries pinned SPEC/CHANGE references, the allowed slice and material design decisions. An independent reviewer receives the exact candidate and pinned SPEC/CHANGE references, allowed paths, exact check commands, expected outcomes, untested items and factual evidence; exclude the full chat and developer verdict by default. If a shared CHANGE record contains a developer verdict, point the reviewer only to its factual sections or supply a clean projection. The reviewer checks the authority and actual results independently.

Compress narrative, not constraints. Carry write and external-action limits, non-goals, invariants, failure behavior, acceptance expectations and provenance even if that makes the handoff longer. Use selective anchors to things the recipient can read, and verify their authoritative versions before acting. Missing, stale or conflicting inputs block the affected work; do not inherit chat approvals or infer new authority from the handoff.

### Evidence that survives a new session

- **Spec handoff:** record the exact specification path and revision (commit or content digest), affected requirement IDs, agreed write paths and the validations expected. Include the independent Spec Review, #9 walkthrough and original initiator confirmation references bound to that version. Unwritten or mutable inputs are not pinned.
- **Skeleton gate:** record the exact skeleton revision or digest, the independent reviewer and their review result, the actual commands and their outcomes, and any remaining blocker. A developer's self-check is not independent approval.
- **Acceptance handoff:** record the exact implementation revision, checked requirements, commands, result and untested cases. Keep scope and artifacts available to the next worker rather than relying on chat memory. For a nontrivial cross-session handoff, use the adjacent [CHANGE.md template](CHANGE.md) in a user-authorized documentation path or an existing issue or handoff record. Do not create duplicate records, force the template for tiny same-session changes, or write from Plan. If no destination is authorized, return the evidence in the response instead.

## Build

Keep these as separate steps: design the skeleton, prepare the runnable skeleton, run independent skeleton review, implement the authorized slice, run developer self-tests, run independent review/retest, run independent acceptance, and deliver with outcome evaluation. A passed review does not itself authorize the next step. In complex projects, pin shared contracts and repeat Build per independently verifiable vertical slice; work in parallel only where scopes and write ownership do not overlap, and check cross-module integration in the existing acceptance step.

### Parallel work, one real outcome

At #10 pick the smallest observable outcome that exercises this slice's highest-risk commitment. Record one primary scenario, its critical failure or recovery check and the evidence that would prove it. Use the existing milestone, not another ceremony. A UI-heavy slice may need a real user path; a concurrency-heavy slice may need a headless load and recovery scenario. A skeleton or mock is not that outcome.

When it helps, split responsibility at the #10 contract into frontend/interaction and backend/domain or infrastructure, with disjoint write paths, one contract owner and one integration owner. Pin the shared seam: inputs, outputs, errors, side-effect owner, and a synthetic fixture. This is a work split, not permission to add a service, change deployment, or dispatch workers. Keep a single worker or omit an irrelevant lane if the split adds more coordination than it removes.

Within separately authorized #13, let the frontend validate against the pinned fake and the backend validate the real risky behavior without waiting for the UI. Integrate a real adapter on the earliest authorized candidate, run the primary scenario at #14, then independently retest and accept the same candidate at #15–16. Label fakes and missing checks explicitly. Do not call either lane's isolated success, a mock-only run or a buildable skeleton product delivery.

### Driver handoff

On each resumed check, read the last verified evidence and current running or waiting state. Choose one eligible action most likely to produce evidence or remove the current blocker; verify its receipt or outcome. Do not resend in-flight work, reopen accepted decisions, or let a blocked dependency stop unrelated already authorized work. At the agreed checkpoint, report the real artifact and its verification, or the exact failed or missing check, who can unblock it and the next eligible action. No new phase, paths or permissions follow from a timer. Distinguish a test that ran and failed from one that never ran because of the environment, dependency, authorization or unavailable evidence. Prove the next eligible dependency or test, not the same status again.

### Evidence gate

Apply at milestones 12, 14–17 and 20, and to each module row. Keep states separate: **planned** (no work yet), **in progress**, **reported** (a worker claims a result), and **verified** (matching observable evidence was inspected or independently rerun). Use the previous-step self-review to reconcile reported against verified. Never turn a worker summary, pasted output, or test count alone into verified completion. The required independent verifier is not the developer.

For a change, inspect the actual artifact or diff, its allowed scope and provenance, and pin the exact candidate revision. For a test claim, require the actual command, environment and exit outcome, names of assertions or cases, executed/skipped/failed counts, and a retained run artifact or independent rerun. Verify the assertions required by the current milestone actually ran and passed on that revision. A no-op, zero discovered or executed, required skips, unverified cached results, or a stale revision is not proof. For external operations require the original service receipt or an independently observed state tied to the confirmed target, not a report alone. Flag the missing evidence and mark affected acceptance BLOCKED; do not promote progress or propose the next numbered step until material evidence is verified. A justified N/A is recorded as N/A, not a passing run.

### How the user can verify acceptance

At independent acceptance (#16), give the user a short verification recipe and carry it into delivery (#17). Include the exact tested revision or digest, the directory and prerequisites, and one copy-paste command if possible (otherwise the shortest numbered manual steps). State what proves a pass, what indicates failure or skipped checks, and which behavior was not tested. Use the same format for focused regression (#20) when the user needs to reproduce the result. A recipe is not proof that a check ran.

### Module progress

Maintain one row per active submodule in the authorized [CHANGE.md](CHANGE.md) or an existing task sheet. Record module, development and test owners as applicable, development status, test/independent status, bound candidate revision or digest, evidence and blockers. Update after each authorized Build milestone within the same step’s approved scope; if no writable destination was authorized, return the updated rows in the result instead. This adds no confirmation milestone, file write or external tool by default.

Keep development and testing independent: implemented or developer-tested does not mean independently accepted. Apply the Evidence gate to development and test claims separately. Associate each result with its exact version, preserve prior results as history, and mark affected tests pending or blocked when a changed candidate needs recheck. At self-review, verify both tracks against exact-version proof; never advance one track by inference from the other.

### A. Skeleton before logic

Before proposing or starting #10, and whenever entering or resuming Build at any step, verify the pinned SPEC against the #9 freeze, independent Spec Review, walkthrough and original product confirmation from the verified task initiator. Require a matching exact version, a clear affirmative confirmation, and no unresolved conflicting feedback. If any check fails, mark #10 **BLOCKED** and pause the affected slice at its current step. Tell the user what Spec evidence is missing, who can supply it and to return to Spec manually. Leave the result card, request for confirmation and future Build procedure out of this blocked response. General assent, a technical review result or a numbered-step approval cannot satisfy this check. Once it passes, #10 still requires its own review and authorization under the selected step policy.

At milestone 10, design one useful vertical slice with a compact diagram or table showing its entry point, dependencies, typed signatures or contracts, and explicit not-implemented outcome. Use pseudocode for validation, authorization, sequencing, side-effect, transaction and failure boundaries as applicable. Deliver a sketch only; do not create runnable stubs until milestone 11 is separately scoped and authorized under the chosen gate policy.

For the smallest useful vertical slice, wire typed signatures and replaceable boundaries; use explicit not-implemented states, never fake a valid result. Do not call real dependencies, mutate data or run migrations in this skeleton phase. Use inline or same-version pseudocode to map requirements to validation, authorization, side effects, transaction and error boundaries, and applicable timeout/retry/compensation rules. Omit irrelevant mechanics but make boundary decisions explicit.

An independent person or agent who did not write the skeleton reviews that exact commit or fingerprint against the pinned specification. Run the relevant build, type or equivalent checks and verify wiring, replaceable test boundaries and safe placeholder behavior. Record commands, artifact version and pass/block result. No independent approval means no business logic for the affected slice. Recheck affected skeletons when boundary or contract changes invalidate prior evidence.

### B. Implementation and acceptance

Implement the approved slice with its pinned inputs and constraints. Developers check their work; an independent reviewer verifies the exact implementation candidate. Close material findings and rerun affected checks. If independent final acceptance is unavailable on the exact implementation candidate, report acceptance as BLOCKED, name the missing review, and leave the implementation status separate. For individual checks report pass/fail/not-run/not-applicable with real evidence. Do not treat a screenshot, simulation or test count as a substitute for required acceptance. Compare outcomes and residual risks to the original goals; acceptance does not prove production readiness or usefulness.

## Refine

For each refinement, treat scope, implementation and regression as separate steps under the selected gate policy. At scope review, classify risk: low-risk wording or presentation changes need targeted regression; contract-compatible changes touching authorization, data, or a critical path require affected independent re-verification; a change to the contract returns to Spec. Do not use Refine to bypass a gate. Use the existing contract for one scoped, compatible improvement. Preserve work outside the allowed paths and do not weaken expectations to get a green test. For changed in-scope behavior, record focused regression evidence and note untested effects; add tests only in allowed paths and mark the required check blocked if you cannot run or supply it. If the externally observable contract or architectural boundary would change, stop the affected part and return to Spec only through a separately directed invocation.

## Final checks

Trace core requirements to the responsible module or seam, contract, observation and task. Verify document and artifact versions agree. Report only real changes, evidence, blockers and the next eligible step. No automatic Git commits, remotes, merges, pushes, deploys or releases, and no circumvention of filesystem or runtime controls.
