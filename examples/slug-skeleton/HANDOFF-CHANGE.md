# Example change evidence

- Scope: one local CLI skeleton, with writes limited to `slug.py` and `test_skeleton.py`.
- Spec: `README.md` requirements R1–R3. Pin its exact revision in a real handoff.
- Candidate: `slug.py`. No user-file writes, network, persistence, or external actions.
- Expected check: T3 returns 3, no stdout, and explicit not-implemented stderr. T1/T2 remain blocked pending implementation.
- This fixture asserts what to check, not a review verdict.
