import time
from datetime import datetime
import pytz
from oanda import get_candles
from order_execution import place_order_with_sl_tp
from config import RISK_REWARD_RATIO

# Use a top 7 pair (replace or loop through more instruments if needed)
INSTRUMENT = "EUR_USD"
TIMEFRAME = 2 * 60  # 2 minutes

def is_asian_session():
    tz = pytz.timezone("America/Chicago")
    now = datetime.now(tz)
    return 20 <= now.hour <= 23  # 8 PM–11 PM Mississippi (CST/CDT)

def determine_out_of_session_signal(candles):
    if len(candles) < 2:
        return None
    prev = candles[-2]
    current = candles[-1]
    if prev["close"] < prev["open"] and current["close"] > current["open"]:
        return "BUY"
    elif prev["close"] > prev["open"] and current["close"] < current["open"]:
        return "SELL"
    return None

def place_trade(instrument, signal):
    candles = get_candles(instrument)
    if not candles or len(candles) < 2:
        print("Not enough candles to place trade.")
        return

    entry = candles[-1]["close"]
    high = candles[-1]["high"]
    low = candles[-1]["low"]
    atr = abs(high - low)

    if signal == "BUY":
        sl = entry - atr
        tp = entry + atr * RISK_REWARD_RATIO
        units = 10000
    elif signal == "SELL":
        sl = entry + atr
        tp = entry - atr * RISK_REWARD_RATIO
        units = -10000
    else:
        return

    print(f"📈 Placing {signal}: entry={entry}, SL={sl}, TP={tp}")
    place_order_with_sl_tp(instrument, units, round(sl, 5), round(tp, 5))

def run_bot():
    print("🚀 Bot started.")
    while True:
        if is_asian_session():
            print("🌙 Asian session active.")
            candles = get_candles(INSTRUMENT)
            signal = determine_out_of_session_signal(candles)
            if signal:
                print(f"✅ Signal (Asian session): {signal}")
                place_trade(INSTRUMENT, signal)
            else:
                print("No trade signal (Asian session).")
        else:
            print("⏳ Outside Asian session. Bot is idle.")
        time.sleep(TIMEFRAME)

if __name__ == "__main__":
    run_bot()
