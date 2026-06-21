# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A minimal Python command-line calculator (`calc.py`) with a pytest suite and a GitHub Actions CI pipeline. The test suite, not a spec doc, is the source of truth for `calc.py`'s behavior.

## Commands

```bash
# Run the full test suite
pytest

# Run a single test
pytest test_calc.py::test_divide_by_zero

# Lint and format-check (same as CI)
ruff check .
ruff format --check .
ruff format .          # auto-fix formatting

# Run the calculator
python calc.py <add|subtract|multiply|divide> <a> <b>
```

Note: a developer machine may not have Python installed locally; in that case CI (GitHub Actions) is what actually runs the tests and lint.

## Architecture

**Black-box subprocess testing.** `test_calc.py` does not import `calc.py` — it invokes it as a subprocess (`sys.executable calc.py <args>`) and asserts on exit code and stdout. This contract constrains the implementation:

- `calc.py` must remain a standalone CLI script (a `__main__` entry point), never a pure library.
- On success: print **only** the numeric result to stdout and exit 0. Output is compared as exact strings, so whole-number results must print without a trailing `.0` (e.g. `divide 20 5` → `4`, not `4.0`). `calc.py` handles this in `_format()`.
- Divide-by-zero must exit **non-zero** and emit a message containing the word "zero" (case-insensitive, stdout or stderr).

If you change `calc.py`'s output format or error behavior, update both the implementation and the corresponding assertions in `test_calc.py` together.

## CI/CD

`.github/workflows/ci.yml` runs on every push, PR to `main`, and `v*` tag, with two parallel jobs:
- **lint** — `ruff check` + `ruff format --check` (config in `pyproject.toml`: py310 target, 100-char lines, rules `E F I UP B`).
- **test** — `pytest` across Python 3.10 / 3.11 / 3.12.

Release a version by tagging: `git tag vX.Y.Z && git push origin vX.Y.Z` (triggers the pipeline against the tag).

`todo.txt` is local scratch and is gitignored — not part of the project.
