import pytest
from example_app import example_app
import subprocess
import sys
from pathlib import Path

# --- Logic tests for is_prime ---

@pytest.mark.parametrize("value,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (97, True),
    (100, False),
])
def test_is_prime(value, expected):
    assert example_app.is_prime(value) == expected

# --- Output capture for list_primes_below ---

def test_list_primes_below(capsys):
    example_app.list_primes_below(10)
    output = capsys.readouterr().out.strip().splitlines()
    assert output == ['2', '3', '5', '7']

# --- CLI behavior with subprocess ---

def run_cli(args):
    script_path = Path(__file__).parents[1] / "src" / "example_app" / "example_app.py"
    result = subprocess.run(
        [sys.executable, str(script_path), *args],
        capture_output=True,
        text=True
    )
    return result

def test_cli_output_20():
    result = run_cli(["20"])
    assert result.returncode == 0
    lines = result.stdout.strip().splitlines()
    assert lines == ['2', '3', '5', '7', '11', '13', '17', '19']

def test_cli_output_1():
    result = run_cli(["1"])
    assert result.stdout.strip() == ""

def test_cli_invalid_args():
    result = run_cli([])  # no arguments
    assert result.returncode != 0
    assert "usage:" in result.stderr.lower()

def test_cli_non_integer():
    result = run_cli(["notanumber"])
    assert result.returncode != 0
    assert "invalid int value" in result.stderr.lower()
