# order_execution.py
import requests
from config import OANDA_API_KEY, OANDA_ACCOUNT_ID, OANDA_URL

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OANDA_API_KEY}"
}

def place_order_with_sl_tp(instrument, units, stop_loss_price, take_profit_price):
    endpoint = f"{OANDA_URL}/accounts/{OANDA_ACCOUNT_ID}/orders"
    
    data = {
        "order": {
            "instrument": instrument,
            "units": str(units),
            "type": "MARKET",
            "positionFill": "DEFAULT",
            "stopLossOnFill": {
                "price": f"{stop_loss_price}"
            },
            "takeProfitOnFill": {
                "price": f"{take_profit_price}"
            }
        }
    }
    
    response = requests.post(endpoint, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"✅ Order placed: {response.json()}")
    else:
        print(f"❌ Order failed: {response.status_code} - {response.text}")
