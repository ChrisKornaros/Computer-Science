# Install the dependencies
import twttr
from twttr import shorten

# Need to modify the code so it catches errors with capitalized vowel replacement
# Unsure on exact steps/what this means
# Trying a few different things, genuinely unclear on what "without capitalized vowel replacement" means
# Maybe it means replacing vowels without forcing all to caps and/or lowers?
def test_alpha():
    assert shorten("Twitter") == "Twttr"

def test_special():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_alnum():
    assert shorten("CS50") == "CS50"
