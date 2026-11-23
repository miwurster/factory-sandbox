# Coding standards

## Tests

A test earns its place by proving a **contract**: caller-visible behavior of the `sandbox` package, an invariant, or an independent external promise.
Each contract has one **owner** test, written at the strongest boundary that reaches it: the package's public functions, imported the way a caller imports them.

### Every new or changed test

- It names the contract it protects, and its name promises only behavior its inputs and assertions exercise.
- It names a credible regression that turns it red, and that regression is one the existing tests in `tests/` miss.
- It calls the real production function and asserts on its return value or observable effect.
- Its expected values come from outside the subject: literals written in the test, never output the subject generates.
- It stays green through a behavior-preserving refactor, such as renaming or inlining a private helper.
- A new case for an existing contract becomes a row in that contract's test, through `subTest` or a shared table, rather than a new near-duplicate test.
- A bug fix carries one regression test at the owner, red before the fix and green after it, for the intended reason.
- A negative case goes red only on the guard it names.

### Junk to flag

A reviewer flags a test that matches any of these patterns:

- **Call-shape assertions**: a test that patches an internal function with `unittest.mock` and asserts how it was called (`assert_called_with`, `call_args`, `call_count`) instead of asserting what the public function returns.
- **Lying mocks**: a mock that supplies the very behavior under assertion, so the test passes whatever the production code does.
- **Empty proof**: no assertion, a self-comparison, or an expected value computed by the subject itself.
- **Duplicate proof**: a second test of a contract another test already owns, with no distinct risk of its own.
- **Copied inventories**: a test that restates a list of exports or greps source text.
- **Test-only seams**: a production export, flag, parameter, or wrapper whose only caller is a test; the proof belongs at the real boundary, with production left untouched.
- **Lying names**: a name promising behavior the test never exercises.

### Tests to keep

A static or narrow test stays when it guards an independent contract: the public API of `sandbox`, exact output bytes a caller depends on, defaults, or observable ordering.
