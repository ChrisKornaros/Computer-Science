def main():
    # Prompt the user for an integer
    m = int(input("m: "))

    # Store the speed of light
    c = 300000000

    # Calculate the energy
    e = m * (c ** 2)

    return print(f"E: {e}")

main()
