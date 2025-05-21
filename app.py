import time
from oanda import get_candles
from strategy import place_trade

# ✅ Only include instruments your account supports!
SUPPORTED_INSTRUMENTS = [
    "EUR_USD", "USD_JPY", "GBP_USD",
    "USD_CHF", "AUD_USD", "USD_CAD", "NZD_USD"
]

TIMEFRAME = 2 * 60  # 2 minutes in seconds

def determine_signal(candles):
    if len(candles) < 2:
        return None
    prev = candles[-2]
    current = candles[-1]
    if prev["close"] < prev["open"] and current["close"] > current["open"]:
        return "BUY"
    elif prev["close"] > prev["open"] and current["close"] < current["open"]:
        return "SELL"
    return None

def run_bot():
    print("🔁 Starting trading bot...")
    while True:
        for instrument in SUPPORTED_INSTRUMENTS:
            candles = get_candles(instrument)
            signal = determine_signal(candles)
            if signal:
                print(f"✅ Signal on {instrument}: {signal}")
                place_trade(instrument, signal)
            else:
                print(f"No trade signal on {instrument}")
        time.sleep(TIMEFRAME)

if __name__ == "__main__":
    run_bot()
