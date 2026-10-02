# Guna testing strategy — v1

This standard applies to every Guna project, repository and coding agent.
Products own their critical journeys, canonical commands and acceptance criteria.
Dev Kit owns this shared standard and its adoption tools. Changes travel through
reviewed PRs; an older local copy is not evidence of organization-wide adoption.

## Protect behavior

Protect observable contracts at the strongest appropriate boundary. Before
adding or changing tests, identify the contract, a credible regression, existing
coverage and why this boundary adds distinct proof. Use one primary owner for a
contract; additional layers must protect a different risk, such as integration
wiring, authorization, concurrency or browser interaction.

Use a small set of independent critical-flow E2E journeys. Exercise real UI →
API → persistence, with supported synthetic external providers. Verify meaningful
persisted outcomes, reload or fresh-session continuity and relevant role handoffs.
Do not combine journeys into one giant dependent test. Each product defines its
own journeys; Wake's J1–J6 are not a universal inventory. Add mobile, keyboard and
accessibility coverage where they introduce a distinct risk or acceptance requires
them; preserve explicitly required viewport matrices.

Keep targeted integration tests for database authorization, isolation, replay,
atomicity, reset/hold races and least privilege. Use the actual database engine
when its behavior is the contract. Keep small, database-free unit tests for pure
domain rules. A browser suite cannot reliably isolate every race or transaction;
a mocked unit suite cannot prove deployed integration behavior.

Fixtures establish prerequisites, never fabricate the receipt, admission,
acknowledgement, callback ordering or persisted outcome the owner must produce.
Expected results must be independent of the implementation under test. A negative
case must reach its intended boundary; use a valid positive control where needed.
Bug regressions must fail before the fix for the intended reason and pass after
it. If reproducing the original environment is unavailable, state that gap and
retain the obligation rather than inventing fail-before evidence.

## Authoring and audit checklist

Reject these when they provide no independent observable contract:

- Assertion-free coverage probes, self-comparisons and identity copiers.
- Copied fixture inventories, manifests, exports or implementation text.
- Exact source/import/string greps that merely freeze implementation choices.
- Private predicates or call shapes already proved at a real boundary.
- Duplicate invocations of one contract and provider-local replays of shared helpers.
- Tests that exist only to preserve test-only exports, globals or wrappers, and
  dead production code whose only callers are tests.
- Expected values computed by the helper or renderer being tested.
- Mocks that implement the asserted behavior, or one identical mock substituting
  for APIs with different contracts.
- Persistence assertions against a store the exercised path never writes.
- Capability tests that restate flags without exercising promised delivery or acknowledgement.
- Negative controls that fail at an unrelated guard or an unreachable production path.
- Names or fixtures that claim more than the exercised input and assertions prove.

These are review questions, not a syntax blacklist. Static configuration,
packaging, permissions, migration compatibility, persist-before-ack ordering,
snapshots and provider adapters can have real contracts. Explain the independent
failure they detect. Do not ban mocks, snapshots, static checks or large files
categorically, and do not disguise a weak test to evade a pattern checker.

Improve existing tests and harnesses first. Remove redundant proof only after
identifying the stronger retained test and checking repository requirements.
Do not launch a mass-deletion campaign or set a test-count reduction quota.

## Required PR rationale

For test additions, modifications, deletions or renames, include these five
fields in the PR body. One explanation per distinct contract is sufficient;
group related contracts within each field instead of cataloguing assertions.

```markdown
### Contract protected

### Regression detected

### Existing coverage

### Test boundary

### Verification
```

Fill each field with concrete evidence. Existing coverage names the retained
proof and explains the new test's distinct value, or the proof retained after
deletion. Verification gives canonical commands and actual outcomes, execution
and registration evidence, unexpected skips/retries and limitations. For bug
fixes include fail-before/pass-after evidence. Do not fill fields with placeholders
or treat a rationale passing the parser as a test-quality verdict.

Complete the rationale before requesting review so the reviewer assesses it.
Approval binds to the exact head, not the PR body: editing the body afterwards
(for example to add verification results) needs no new review and no CI rerun.
The merge tool still requires the five filled headings at merge time.

For behavior changes without test-file edits, reviewers still require appropriate
verification and assess missing coverage. Document a justified exception in the
PR with its scope, owner and retained proof; substantive exceptions need repository
maintainer disposition. A concrete rationale explains an exception; there is no
flag to waive the rationale gate.

## Review and enforcement

All agents read their repository's AGENTS.md and the adopted copy before test or
harness changes. Agent-specific entry files reference the same policy. Reviewers
apply the checklist to changed tests, verify meaningful outcomes and intended
negative boundaries, and reject unjustified duplication or unsupported acceptance
claims. Identify the concrete escaped regression and changed location in findings;
preserve the repository's governed severity and disposition rules.

The shared merge tool checks complete changed-file metadata, including deleted
and previous rename paths, and requires filled rationale fields for recognized
test paths. Its local preflight uses the same validator. This is an objective
minimum; unusual test naming, actual execution, assertion quality and indirect
harness changes still require review and the product's canonical CI. Keep required
registration, critical-flow execution and unexpected-skip checks in their owning
product; do not replace them with a second copied test inventory.

There is no new heavy CI job or model call. Old installed merge tools and direct
GitHub merges cannot enforce this new gate; update the supported CLI, adopt the
policy in each repo, and audit bypasses. Adoption does not alter credentials,
reviewer accounts, workflow pins, branch settings, live runners or production
authorization. Automated approval remains necessary but is not proof of product
acceptance. Keep local integration, sandbox and exact-release acceptance distinct.

## Measure value

Report contracts covered and gaps, not counts as acceptance. For a bounded cleanup,
baseline comparable real runs: queue, install/build, suite setup, execution,
retry and critical-path time. Start with duplicated expensive setup and overly
broad selection. Report retained contracts, runner-minutes, developer wait time,
flake/retry changes and uncertainty separately. Do not promise CI savings from
deleted test counts or manufacture PRs to fill a timing window.
