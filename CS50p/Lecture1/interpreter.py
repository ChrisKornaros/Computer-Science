# Build the main function
def main():
    # Prompt the user for an expression
    exp = input("Expression: ")

    # Split the expression into x, y, and z
    x, y, z = exp.split(' ')

    # Ensure Data Quality
    x = float(x)
    z = float(z)

    # Evaluate the expression
    match y:
        case _ if y == '+':
            return print(x + z)
        case _ if y == '-':
            return print(x - z)
        case _ if y == '*':
            return print(x * z)
        case _ if y == '/':
            return print(x / z)
        case _:
            return 0




main()


