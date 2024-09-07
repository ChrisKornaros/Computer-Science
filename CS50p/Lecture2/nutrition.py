# Build the main function
def main():
    # Prompt the user for the fruit
    fruit = input("Item: ")
    # Return the calories
    cal_calc(fruit)

# Build the calorie calculator
def cal_calc(f):
    # Dictionary with the fruit and its calories per portion
    cal_dict = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }
    # Check to see if the fruit is listed
    for k, v in cal_dict.items():
        if f.casefold() == k.casefold():
            return print(f"Calories: {v}")

    return None

main()

