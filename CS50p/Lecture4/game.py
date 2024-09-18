# Import the necessary packages
import random
import sys

# Build the main function
def main():
    # Initialize the random seed
    #random.seed(a=12345)
    # Prompt the user for a positive integer
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n:
                break
        except ValueError:
            pass

    # Generate a random number
    num = random.randint(1, n)
    # Reprompt the user for a guess until they get it correct
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < num:
                print("Too small!")
            elif num < guess:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


main()




