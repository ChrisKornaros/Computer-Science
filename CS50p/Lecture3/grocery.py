# Build the main function
# Try using enumerate or some other similar function to number the iterations of the food
def main():
    # Create an empty list for groceries
    item = []
    # Function to populate the list
    while True:
        try:
            item.append(input().strip().upper())
        except EOFError:
            # Function to transform the list
            grocery_list = final(item)
            # Return the final list
            for k, v in grocery_list.items():
                print(f"{v} {k}")
            break

def final(item_list):
    # Initialize a blank dictionary to store counts
    output = {}
    # Sort the list alphabetically
    item_list = sorted(item_list)
    # Iterate through the list, store values and counts in the dictionary
    for i in item_list:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1

    return output

main()
