# Build the main function
def main():
    # Prompt the user for a string
    inp = input("Input: ")

    # Convert the string
    out = shorten(inp)

    print(out)

# Build the shorten function
def shorten(prompt):
    # Create a list of vowels
    vow = ['A', 'E', 'I', 'O', 'U']

    for a in prompt:
        for v in vow:
            if a.casefold() in v.casefold():
                prompt = prompt.replace(a, "")
            else:
                prompt = prompt

    return prompt

if __name__ == '__main__':
    main()
