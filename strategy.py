import time
from deriv import Client as Deriv
from config import DERIV_TOKEN, TRADING_SYMBOLS

# Connect to Deriv
deriv_client = Deriv(DERIV_TOKEN)

def get_signal(symbol: str):
    """
    Fetch a simple forex signal from Deriv API
    Returns: 'BUY', 'SELL', or 'HOLD'
    """
    try:
        # Get market info (simple example using ticks)
        ticks = deriv_client.ticks(symbol=symbol, count=1)
        price = ticks[-1]["quote"]

        # Simple dummy logic: compare last two prices
        prev_price = ticks[-2]["quote"] if len(ticks) > 1 else price
        if price > prev_price:
            return "BUY"
        elif price < prev_price:
            return "SELL"
        else:
            return "HOLD"
    except Exception as e:
        print("Error getting signal:", e)
        return "HOLD"

def get_signals():
    """Return signals for all symbols"""
    signals = {}
    for sym in TRADING_SYMBOLS:
        signals[sym] = get_signal(sym)
        time.sleep(0.5)  # avoid API spam
    return signals