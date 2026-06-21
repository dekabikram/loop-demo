import subprocess
import sys

CALC = "calc.py"


def run_calc(*args):
    """Invoke calc.py as a subprocess and return (returncode, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, CALC, *map(str, args)],
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def test_add():
    code, out, _ = run_calc("add", 3, 4)
    assert code == 0
    assert out == "7"


def test_subtract():
    code, out, _ = run_calc("subtract", 10, 4)
    assert code == 0
    assert out == "6"


def test_multiply():
    code, out, _ = run_calc("multiply", 6, 7)
    assert code == 0
    assert out == "42"


def test_divide():
    code, out, _ = run_calc("divide", 20, 5)
    assert code == 0
    assert out == "4"


def test_divide_by_zero():
    code, out, err = run_calc("divide", 5, 0)
    assert code != 0
    assert "zero" in (out + err).lower()
