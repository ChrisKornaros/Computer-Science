# Build the main function
def main():
    # Prompt the user for a variable in camelCase
    camel = input("camelCase: ").strip()

    # Convert the variable name to snake_case, first initialize a blank list
    snake = []
    # Iterate through the variable string
    # By adding a print() line in each iteration, I can check to see where code breaks
    start = 1
    for a in camel:
        # Start the snake list with the first letter in the camelCase variable
        # Data quality check: with the binary start variable, if the first letter in the first word is the same as the last, like in test
        # I am able to avoid any bugs/errors
        if a == camel[0] and start == 1:
            snake = snake + list(a)
            # print(snake)
            start -= 1
        # If lowercase, add it to the most recent list item
        elif a.islower():
            snake[-1] = snake[-1] + a
            # print(snake)
        # If uppercase, add a new list item
        elif a.isupper():
            snake = snake + list(a)
            # print(snake)
        else:
            break

    # Create the snake_case output
    for s in snake:
        # Start the string
        if s == snake[0]:
            snake_case = s
            # print(snake_case)
        else:
            snake_case = snake_case + '_' +str(s.lower())
            # print(snake_case)

    print(f"snake_case: {snake_case}")




main()

