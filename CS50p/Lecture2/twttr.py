# Build the main function
def main():
    # Prompt the user for a string
    inp = input("Input: ")
    # Create a list of vowels
    vow = ['A', 'E', 'I', 'O', 'U']

    for i in inp:
        if i.upper() in vow:
            inp = inp.replace(i, "")
        else:
            inp = inp


    print(inp)




main()
