# Import the required packages
import sys
import random
from pyfiglet import Figlet

# Build the main function
def main():
    # Initialize Figlet
    figlet = Figlet()
    # Get the available fonts
    fonts = figlet.getFonts()
    # Check that there are 0 or 2 arguments
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        # If there are 0 arguments, randomly select a font
        if len(sys.argv) == 1:
            figlet.setFont(font=random.choice(fonts))
        # If there are 2 arguments, select the specified font
        elif len(sys.argv) == 3:
            if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                if sys.argv[2] in fonts:
                    figlet.setFont(font=sys.argv[2])
                else:
                    sys.exit("Invalid usage")
            else:
                sys.exit("Invalid usage")
        # Prompt the user for input and render the text
        base = input("Input: ")
        print(figlet.renderText(base))
    elif len(sys.argv) == 2 or 3 < len(sys.argv):
        sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

main()
