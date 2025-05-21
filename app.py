import time
from oanda import get_candles
from strategy import place_trade

INSTRUMENT = "XAU_USD"
TIMEFRAME = 2 * 60  # 2 minutes

def determine_signal(candles):
    if len(candles) < 2:
        return None
    prev = candles[-2]
    curr = candles[-1]
    if prev["close"] < prev["open"] and curr["close"] > curr["open"]:
        return "BUY"
    elif prev["close"] > prev["open"] and curr["close"] < curr["open"]:
        return "SELL"
    return None

def run_bot():
    print("🚀 Bot running...")
    while True:
        candles = get_candles(INSTRUMENT)
        signal = determine_signal(candles)
        if signal:
            print(f"📢 Signal detected: {signal}")
            place_trade(INSTRUMENT, signal)
        else:
            print("⏳ No signal.")
        time.sleep(TIMEFRAME)

if __name__ == "__main__":
    run_bot()
