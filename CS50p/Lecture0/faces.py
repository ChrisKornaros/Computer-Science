# Build main function
def main():
    # Prompt the user for a value
    a = input()

    # Conver the input
    b = convert(a)

    return print(b)

# Build the convert function
def convert(val):
    # Replace the slightly smiling and slightly frowning faces in place and overwrite the input variable
    val = str(val).replace(":)", "\U0001F642").replace(":(", "\U0001f641")

    return val


main()

