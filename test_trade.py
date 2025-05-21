from config import OANDA_API_KEY, OANDA_ACCOUNT_ID, OANDA_URL
import requests

def place_test_order(instrument, units=1):
    url = f"{OANDA_URL}/accounts/{OANDA_ACCOUNT_ID}/orders"
    headers = {
        "Authorization": f"Bearer {OANDA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "order": {
            "units": str(units),          # positive for buy, negative for sell
            "instrument": instrument,
            "timeInForce": "FOK",         # Fill or kill
            "type": "MARKET",
            "positionFill": "DEFAULT"
        }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Test order placed successfully: {response.json()}")
    else:
        print(f"Failed to place test order: {response.status_code} {response.text}")

if __name__ == "__main__":
    instrument = "EUR_USD"  # or any from your allowed list
    place_test_order(instrument)
