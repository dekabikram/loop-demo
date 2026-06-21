"""A tiny command-line calculator: calc.py <operation> <a> <b>."""

import sys

OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}


def _format(value):
    # Print whole numbers without a trailing ".0" so output matches expectations.
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main(argv):
    if len(argv) != 3:
        print(f"usage: calc.py <{'|'.join(OPERATIONS)}> <a> <b>", file=sys.stderr)
        return 2

    op, a_raw, b_raw = argv
    if op not in OPERATIONS:
        print(f"unknown operation: {op}", file=sys.stderr)
        return 2

    a, b = float(a_raw), float(b_raw)
    if op == "divide" and b == 0:
        print("error: cannot divide by zero", file=sys.stderr)
        return 1

    print(_format(OPERATIONS[op](a, b)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
