import oandapyV20
import oandapyV20.endpoints.instruments as instruments
from config import OANDA_API_KEY

client = oandapyV20.API(access_token=OANDA_API_KEY)

def get_candles(instrument, count=50, granularity="M2"):
    params = {
        "count": count,
        "granularity": granularity,
        "price": "M"
    }
    r = instruments.InstrumentsCandles(instrument=instrument, params=params)
    try:
        response = client.request(r)
        candles = response["candles"]
        return [{
            "time": c["time"],
            "open": float(c["mid"]["o"]),
            "high": float(c["mid"]["h"]),
            "low": float(c["mid"]["l"]),
            "close": float(c["mid"]["c"])
        } for c in candles if c["complete"]]
    except Exception as e:
        print(f"Error fetching candles: {e}")
        return []
