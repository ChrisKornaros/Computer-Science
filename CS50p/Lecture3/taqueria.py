# Build the main function
def main():
    # Define the food items
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    # Create a loop to continuously prompt the users
    total = 0
    while True:
        try:
            # Prompt the user
            item = food("Item: ").title()
            # Reprompt the user if the food isn't on the menu
            if item in menu.keys():
                # Return the total
                total = round(total + menu.get(item), 2)
                print(f"Total: ${total:.2f}")
            else:
                pass
        except EOFError:
            return print("")

# Build the food input function
def food(prompt):
    f = input(prompt)
    return f

main()
