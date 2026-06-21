# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

This is a small Python project. The test suite (`test_calc.py`) defines the expected behavior of a command-line calculator, but the implementation file `calc.py` **does not exist yet** — the tests will fail until it is created. Implementing `calc.py` to satisfy the tests is the primary outstanding work.

## Commands

```bash
# Run the full test suite
pytest

# Run a single test
pytest test_calc.py::test_divide_by_zero

# Run the calculator (once calc.py exists)
python calc.py <operation> <a> <b>
```

## Architecture

The tests drive the design via a black-box contract: `test_calc.py` invokes `calc.py` as a **subprocess** (`sys.executable calc.py <args>`) rather than importing it, then asserts on exit code and stdout. Any implementation of `calc.py` must therefore be a standalone CLI script, not a library.

The contract the tests expect of `calc.py`:
- CLI form: `calc.py <operation> <a> <b>` where operation is one of `add`, `subtract`, `multiply`, `divide`.
- On success: print only the numeric result to stdout and exit 0. Results are compared as strings (e.g. `divide 20 5` must print `4`, not `4.0`).
- On divide-by-zero: exit with a **non-zero** code and emit a message containing the word "zero" (case-insensitive, on stdout or stderr).
