# Ingest the required packages
import emoji

# Build the main function
def main():
    # Prompt the user for text
    prompt = input("Input: ")
    # Transform the str into an emoji
    output = emoji.emojize(prompt, language="alias")
    # Print the output
    print(output)

main()
