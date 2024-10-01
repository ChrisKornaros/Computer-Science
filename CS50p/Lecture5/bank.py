# Build the main function
def main():
    # Prompt the user for a greeting
    g = input("Greeting: ")
    v = value(g)

    # Return the value of the greeting
    return print(f"${v}")


# Build the value function
def value(greeting):
    # Convert the string to an int
    if greeting.isalpha():
        # Check to see if the string starts with hello
        if str(greeting[0:5]).casefold() == "hello".casefold():
            return 0
        elif str(greeting[0]).casefold() == "h".casefold() and str(greeting[0:5]).casefold() != "hello".casefold():
            return 20
        else:
            return 100
    else:
        return TypeError


if __name__ == '__main__':
   main()
