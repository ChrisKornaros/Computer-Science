# Install the dependencies
from fuel import convert, gauge
import pytest

# Build test cases
def test_convert():
    # Test valid fractions
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99

    # Test raising exceptions
    with pytest.raises(ValueError):
        convert("2/1")  # X is greater than Y

    with pytest.raises(ValueError):
        convert("invalid/100")  # Non-integer input

    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Division by zero

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
