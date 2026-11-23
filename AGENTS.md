# factory-sandbox

This repo is a sandbox the software factory practices on in its end-to-end tests.
It holds a tiny Python 3.12 package, `sandbox`, that uses only the standard library.
Tests live in `tests/` and use `unittest`; there are no third-party dependencies.

## Verification checks

A change must pass this command from the repo root before it is pushed:

```sh
python3 -m unittest discover -s tests -v
```

CI runs the same command in the `test` job on every pull request and every push to `main`.
