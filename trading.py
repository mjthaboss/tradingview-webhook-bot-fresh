import oandapyV20
import oandapyV20.endpoints.orders as orders
from config import OANDA_API_KEY, OANDA_ACCOUNT_ID, RISK_REWARD_RATIO

client = oandapyV20.API(access_token=OANDA_API_KEY)

def place_market_order(instrument, units, stop_loss_price, take_profit_price):
    order = {
        "order": {
            "instrument": instrument,
            "units": str(units),
            "type": "MARKET",
            "positionFill": "DEFAULT",
            "stopLossOnFill": {
                "price": str(stop_loss_price)
            },
            "takeProfitOnFill": {
                "price": str(take_profit_price)
            }
        }
    }

    r = orders.OrderCreate(accountID=OANDA_ACCOUNT_ID, data=order)
    try:
        response = client.request(r)
        print(f"Trade executed: {response}")
    except Exception as e:
        print(f"Error placing trade: {e}")
