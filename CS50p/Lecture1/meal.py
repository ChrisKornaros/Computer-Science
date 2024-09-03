# Build the main function
def main():
    # Prompt the user for the time
    ut = input("What time is it? ")

    # Convert the time to a float
    tm = convert(ut)

    # Return what meal corresponds to the time, if any
    match tm:
        case _ if 7.00 <= tm <= 8.00:
            return print("breakfast time")
        case _ if 12.00 <= tm <= 13.00:
            return print("lunch time")
        case _ if 18.00 <= tm <= 19.00:
            return print("dinner time")
        case _:
            return exit

def convert(time):
    # Convert the string via code that performs several operations at once
    # The string time is split at the ':', the first item is converted to float
    # The Second item is converted to float and then divided by 60 to convert it to a decimal
    time = float(time.split(":")[0]) + float(time.split(":")[1])/60


    return time

if __name__ == '__main__':
    main()

