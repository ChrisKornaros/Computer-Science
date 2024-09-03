# Build the main function
def main():
    # Prompt the user for the answer to the Great Question of Life, the Universe and Everything
    ans = input("What's the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

    match ans:
        case "42" | "forty-two" | "forty two":
            return print("Yes")
        case _:
            return print("No")


main()
