from datetime import datetime, timezone
from config import SESSIONS
from oanda import get_candles  # must return list of candles with 'close', 'open' etc

# Track open trades per instrument (simple memory for demo)
open_trades = {}

def is_in_session(session_name):
    start_hour, end_hour = SESSIONS[session_name]
    now_utc = datetime.now(timezone.utc).hour
    if start_hour < end_hour:
        return start_hour <= now_utc < end_hour
    else:
        return now_utc >= start_hour or now_utc < end_hour

def simple_sma(candles, length):
    if len(candles) < length:
        return None
    closes = [c['close'] for c in candles[-length:]]
    return sum(closes) / length

def candle_color(candle):
    return "GREEN" if candle["close"] > candle["open"] else "RED"

def get_signal_for_instrument(instrument):
    # Trade only during London or NY session
    if not (is_in_session("LONDON") or is_in_session("NY")):
        return None
    
    candles = get_candles(instrument)
    if not candles or len(candles) < 200:
        print(f"Not enough candles for {instrument}")
        return None
    
    # Calculate SMA
    sma20 = simple_sma(candles, 20)
    sma200 = simple_sma(candles, 200)
    if sma20 is None or sma200 is None:
        return None

    last_candle = candles[-1]
    prev_candle = candles[-2]

    # Oliver Velez Color Change: Check if candle color changed
    last_color = candle_color(last_candle)
    prev_color = candle_color(prev_candle)

    # Price relation to SMAs
    price = last_candle['close']

    # Check open trade for exit conditions
    trade = open_trades.get(instrument)

    # Exit rule: after buy, if 2 red candles form, exit (return None = no new trade)
    if trade == "BUY":
        # Check last 2 candles color red
        last_two = candles[-2:]
        if all(candle_color(c) == "RED" for c in last_two):
            open_trades.pop(instrument)
            print(f"Exit BUY trade on {instrument} due to 2 red candles")
            return None
        else:
            return "BUY"  # Hold trade

    if trade == "SELL":
        last_two = candles[-2:]
        if all(candle_color(c) == "GREEN" for c in last_two):
            open_trades.pop(instrument)
            print(f"Exit SELL trade on {instrument} due to 2 green candles")
            return None
        else:
            return "SELL"  # Hold trade

    # Entry rules
    if last_color != prev_color:
        if last_color == "GREEN" and price > sma20 and price > sma200:
            open_trades[instrument] = "BUY"
            return "BUY"
        elif last_color == "RED" and price < sma20 and price < sma200:
            open_trades[instrument] = "SELL"
            return "SELL"

    return None
