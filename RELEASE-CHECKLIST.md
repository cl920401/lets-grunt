# Release checklist

- [ ] Confirm the public name and repository destination. Inspect the release tree for secrets, personal information, private paths, and unrelated work.
- [x] The rights holder approved MIT for this project; the approved text and copyright notice are in [LICENSE](LICENSE).
- [ ] Record provenance and required notices for any third-party material actually reused. This project contains original workflow text and a sample, not Grill skill text or code. Documentation links are usage references.
- [ ] Reproduce package checks and run the [behavior matrix](examples/slug-skeleton/README.md) in an isolated target client. Record actual results, client version, and untested cases. Verify explicit invocation of all three write modes and that uninvoked write modes are not automatically selected; also verify Plan leaves the tree unchanged. Discovery is not an invocation test.
- [ ] Review the exact artifact and obtain specific publication authorization. Neither approval of the design nor QA is approval to release.
