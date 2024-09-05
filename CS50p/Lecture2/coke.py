# Build the main function
def main():

    # Initial money needed to buy the Coke
    due = 50
    # Initialize a start flag
    start = 1
    # Repeat while > 0
    while due > 0:
        if start == 1:
            # Provide the amount of money owed
            print(f"Amount Due: {due}")
            # Prompt the user for the coin
            coin = int(input("Insert Coin: "))
            # Stop this conditional from repeating
            start -= 1
        # Ensure the coin is a nickle, dime, or quarter
        if coin not in [25, 10, 5]:
            due = due
            print(f"Amount Due: {due}")
            coin = int(input("Insert Coin: "))
        elif coin in [25, 10, 5]:
            due = due - coin
            if due > 0:
                print(f"Amount Due: {due}")
                coin = int(input("Insert Coin: "))
            elif due <= 0:
                print(f"Change Owed: {abs(due)}")
                break


main()



