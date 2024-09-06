# Build the main function
def main():
    # Get the plate, assuming it will be all uppercase
    plate = input("Plate: ")

    # Check if the plate is valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check the first two values in s
    if not s[:2].isalpha():
        return False
    # Check the length of s
    if not 2 <= len(s) <= 6:
        return False
    # Numbers cannot be used in the middle of a plate
    for n, i in enumerate(s):
        if i.isdigit() and not s[n:].isdigit():
            return False
    # 0 can't be the first number
    for n, i in enumerate(s):
        if i == '0' and s[0:n].isalpha():
            return False
    # No punctuation, spaces, special characters, etc.
    if not s.isalnum():
        return False

    return True



main()
