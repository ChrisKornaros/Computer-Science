# Build the main function
def main():
    # Prompt the user for a fraction, convert it
    frac = input("Fraction: ")
    try:
        percentage = convert(frac)
        return print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        return e

def convert(fraction):
    # Initiate a loop to ensure data quality
    # Store the user input and then output it
    # Store the fraction as a list to separate out the numeric elements
    f = fraction.split('/')
    # Store the numerator and denominator as x and y
    try:
        x = int(f[0])
        y = int(f[1])
    except ValueError:
        raise ValueError
    # Verify that both values are integers, Y > X, and Y != 0
    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    return round((x / y) * 100)

def gauge(percentage):
    # Print F, the percentage, or E
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == '__main__':
    main()


