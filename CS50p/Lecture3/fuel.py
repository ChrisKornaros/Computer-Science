# Build the main function
def main():
    # Prompt the user for a fraction
    p = frac("Fraction: ")
    # Print F, the percentage, or E
    if p <= 0.01 or p >= 0.99:
        match p:
            case _ if p <= 0.01:
                print("E")
            case _ if p >= 0.99:
                print("F")
            case _:
                print("F/E error")
                return
    # Print the percent with the percentage sign
    elif 0.01 < p < 0.99:
        print(f"{int(p*100)}%")

# Build the function for getting the fraction and converting it to a float
def frac(prompt):
    # Initiate a loop to ensure data quality
    while True:
        try:
            # Store the user input and then output it
            f = input(prompt)
            # Store the fraction as a list to separate out the numeric elements
            f = f.split('/')
            # Store the numerator and denominator as x and y
            x = int(f[0])
            y = int(f[1])
            # Verify that Y > X
            if x > y:
                pass
            else:
                return round(x / y, 2)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()

