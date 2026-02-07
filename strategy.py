import os
import asyncio
from deriv_api import DerivAPI
import random  # For demo/random signal generation
import pandas as pd
import ta

DERIV_TOKEN = os.getenv("DERIV_TOKEN")
api = DerivAPI(token=DERIV_TOKEN, environment="demo")  # demo mode

async def get_signal(pair: str, expiry: str):
    """
    Fetch live signal from Deriv or generate dummy demo signal.
    Returns a dict with signal, volatility, probability.
    """
    # Map expiry to seconds
    expiry_seconds = {
        "5s": 5, "15s": 15, "30s": 30,
        "1m": 60, "2m": 120, "3m": 180,
        "5m": 300
    }.get(expiry, 60)

    # Normally here you would fetch live candles:
    # candles = api.get_candles(symbol=pair, interval=expiry_seconds)

    # For demo, generate random signal
    signal = random.choice(["BUY", "SELL"])
    probability = random.randint(70, 95)
    volatility = random.choice(["Low", "Moderate", "High"])

    # If using real data, you can calculate EMA/RSI/MACD here:
    # df = pd.DataFrame(candles)
    # df['ema'] = ta.trend.EMAIndicator(df['close']).ema_indicator()
    # ...

    return {
        "signal": signal,
        "probability": probability,
        "volatility": volatility
    }