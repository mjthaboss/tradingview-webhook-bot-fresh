def place_trade(instrument, signal="BUY"):  # force BUY
    from oanda import get_candles
    from order_execution import place_order_with_sl_tp
    from config import RISK_REWARD_RATIO

    candles = get_candles(instrument)
    if not candles or len(candles) < 2:
        print(f"Not enough candles to place trade for {instrument}")
        return

    entry = candles[-1]["close"]
    high = candles[-1]["high"]
    low = candles[-1]["low"]
    atr = abs(high - low)

    if signal == "BUY":
        sl = entry - atr
        tp = entry + (atr * RISK_REWARD_RATIO)
        units = 1  # <--- VERY small size for test
    else:
        sl = entry + atr
        tp = entry - (atr * RISK_REWARD_RATIO)
        units = -1

    print(f"Placing {signal} trade on {instrument}: entry={entry}, SL={sl}, TP={tp}")
    place_order_with_sl_tp(
        instrument=instrument,
        units=units,
        stop_loss_price=round(sl, 5),
        take_profit_price=round(tp, 5)
    )
