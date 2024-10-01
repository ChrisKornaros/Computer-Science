# Install the dependencies
import bank
from bank import value

# Define the tests
def test_upper():
    assert value("HELLO") == 0

def test_lower():
    assert value("hello") == 0

def test_variety():
    assert value("Hi, I'm the 3rd test.") == 20



