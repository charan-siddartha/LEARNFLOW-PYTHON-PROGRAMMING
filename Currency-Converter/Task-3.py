

import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    params = {"apikey": api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        rates = response.json()["rates"]
        if target_currency in rates:
            return rates[target_currency]
        else:
            print(f"Invalid target currency: {target_currency}")
    else:
        print(f"Failed to fetch exchange rates. Status code: {response.status_code}")

def convert_currency(api_key, amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount, target_currency
    else:
        return None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your Open Exchange Rates API key
    currencies = {
        "USD": "Dollar",
        "EUR": "Euro",
        "INR": "Rupee",
        
    }

    print("Supported currencies:")
    for code, name in currencies.items():
        print(f"{code}: {name}")

    amount = float(input("Enter the amount: "))
    base_currency = input("Enter the base currency code: ").upper()
    target_currency = input("Enter the target currency code: ").upper()

    if base_currency not in currencies or target_currency not in currencies:
        print("Invalid currency code.")
        return

    result = convert_currency(api_key, amount, base_currency, target_currency)

    if result is not None:
        converted_amount, target_currency = result
        print(f"{amount:.2f} {currencies[base_currency]} is equal to {converted_amount:.2f} {currencies[target_currency]}")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main()




