# Import the required packages
import sys
import requests

# Build the main function
def main():
    n = float(sys.argv[1])
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif type(n / 2) != type(2.5):
        sys.exit("Command-line argument is not a number")

    btc = btc_price()
    total = btc * n
    print(f"${total:,.4f}")


# Build the Bitcoin API Function
def btc_price():
    try:
        api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        btc_json = api.json()
    except requests.RequestException:
        return("Error connecting to CoinDesk.")

    btc = btc_json["bpi"]["USD"]["rate"]
    btc = btc.split(",")
    btc_usd = float(btc[0]+btc[1])
    return btc_usd

main()
