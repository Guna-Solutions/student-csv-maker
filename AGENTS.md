<!-- guna-testing:v1 -->

## Testing strategy

Before changing tests or harnesses, read [.github/testing-strategy.md](.github/testing-strategy.md).
Protect observable contracts with focused critical-flow E2E, targeted real
database/integration tests and pure domain tests. Identify the credible regression,
existing proof and distinct risk before adding another test. Fixtures establish
prerequisites; the production path must produce the asserted outcome. Negative
controls must reach the intended boundary. Preserve product-specific journeys,
canonical validation and security/acceptance requirements.

Test-changing PRs require five filled Markdown headings: `Contract protected`,
`Regression detected`, `Existing coverage`, `Test boundary`, `Verification`.
For deletions identify retained proof; for bug fixes give fail-before/pass-after
evidence or state the reproduction gap. Reject self-fulfilling or unjustifiably
duplicated tests; do not blanket-ban mocks, snapshots or static contract checks.
Reviewers apply the same strategy and name concrete escaped regressions, not
style preferences. Passing counts and rationale fields are not acceptance evidence.
Use this repository's configured review/merge controls. Where `guna-review-merge`
is configured, its updated version enforces rationale presence alongside
exact-head review and CI. Otherwise enforce the rationale in review and report
the automation gap; do not invoke an unconfigured merge tool as a new blocker.

<!-- /guna-testing:v1 -->
