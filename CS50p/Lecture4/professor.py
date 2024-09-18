# Import the necessary packages
import random

# Build the main function
def main():
    # Prompt the user for a level, n of value 1, 2, or 3
    level = get_level()

    # Initialize the score
    score = 0

    # Generate the equations
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        # Allow the user up to three attempts per equation
        attempt = 0
        while attempt < 3:
            try:
                # Prompt the user for the answer
                a = int(input(f"{x} + {y} = "))

                # Check the answer
                if a == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
            # If the input isn't an integer
            except ValueError:
                print("EEE")
                attempt += 1

        # If the user fails after 3 attempts, show the correct answer
        if attempt == 3:
            print(f"{x} + {y} = {x + y}")

    # Output the user's score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


# Build the generate integer function
def generate_integer(level):
    # See which level and generate an X and Y value
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == '__main__':
    main() # Unclear why this worked, but just using main() did not when submitting.