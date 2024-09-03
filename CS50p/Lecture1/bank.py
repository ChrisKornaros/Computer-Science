# Build the main function
def main():
    # Prompt the user for a greeting
    greet = input("Greeting? ").lower().strip()

    # Decide how much money the user gets
    match greet:
         case _ if greet.startswith("hello"):
              return print("$0")
         case _ if greet.startswith("h"):
              return print("$20")
         case _:
              return print("$100")


main()