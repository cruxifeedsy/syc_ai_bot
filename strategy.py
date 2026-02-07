import pandas as pd
import ta
import random

def get_signals(symbol="R_100"):
    # Fake market data (temporary until API connected)
    data = pd.DataFrame({
        "close": [random.uniform(100, 200) for _ in range(100)]
    })

    data["rsi"] = ta.momentum.RSIIndicator(data["close"]).rsi()
    data["ema"] = ta.trend.EMAIndicator(data["close"]).ema_indicator()

    last_rsi = data["rsi"].iloc[-1]
    last_price = data["close"].iloc[-1]
    last_ema = data["ema"].iloc[-1]

    if last_rsi < 30 and last_price > last_ema:
        return "BUY 🟢"
    elif last_rsi > 70 and last_price < last_ema:
        return "SELL 🔴"
    else:
        return "NO SIGNAL ⚪"