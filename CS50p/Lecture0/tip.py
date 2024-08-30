def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Should accept a str as input in excepted format of $##.## and remove the leading $
    d = d.replace("$", "")
    # Convert d to a float
    d = float(d)

    return d


def percent_to_float(p):
    # Should accept a str as input in expected format of ##% and remove the trailing %
    p = p.replace("%", "")
    # Return p as a percentage, stored as a decimal float
    p = float(p) * 0.01

    return p


main()
