# Build main function
def main():
    # Get the height
    blocks = int(3)

    # Print the square
    for h in range(blocks):
        # Print the columns
        for w in range(blocks):
            print("#", end = "")
        # Print the rows
        print()

# Build the row function
def print_row(n):
    print("#" * n)

# Build the column function
def print_col(h):
    for _ in range(h):
        print("#")

main()


