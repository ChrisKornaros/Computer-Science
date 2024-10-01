# Build the main function
def main():
    # Prompt the user for a plate
    plate = input("Plate: ")
    # Check the plate's validity
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
        #elif i.isdigit() and s[0:n].find('0')
    # 0 can't be the first number
    for n, i in enumerate(s):
        if i == '0' and s[0:n].isalpha():
            return False
    if not s.isalnum():
        return False
    else:
        return True


if __name__ == '__main__':
    main()
