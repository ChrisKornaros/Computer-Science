# Import the required packages
import inflect

# Build the main function
def main():
    p = inflect.engine()
    name = []
    while True:
        try:
            name.append(input("Name: "))
        except EOFError:
            hills = p.join(name, final_sep=",")
            return print("Adieu, adieu, to", hills)

main()

