# Install the dependencies
import plates
from plates import is_valid

# Build the test cases
def test_start():
    assert is_valid("E13370") == False
    assert is_valid("10") == False
    assert is_valid("TEST12") == True

def test_length():
    assert is_valid("T") == False
    assert is_valid("TESTME2") == False
    assert is_valid("ITSOK9") == True

def test_end():
    assert is_valid("BAD0N3") == False
    assert is_valid("TE3T12") == False
    assert is_valid("TEST01") == False
    assert is_valid("GOOD13") == True

def test_punctuation():
    assert is_valid("UGLY1!") == False
    assert is_valid("CLEAN1") == True
