from oanda import get_candles
from order_execution import place_order_with_sl_tp
from config import RISK_REWARD_RATIO

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
