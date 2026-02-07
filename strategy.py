import MetaTrader5 as mt5
import pandas as pd
import ta
import random
from config import MT5_LOGIN, MT5_PASSWORD, MT5_SERVER

# Connect to MT5
def mt5_connect():
    if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
        print("MT5 Initialize failed")
        return False
    return True

# Get live Forex signal
def get_signal(pair):
    if not mt5_connect():
        return "BUY", "Moderate", 80  # fallback

    rates = mt5.copy_rates_from_pos(pair, mt5.TIMEFRAME_M1, 0, 100)
    if rates is None or len(rates) == 0:
        return "BUY", "Moderate", 80

    df = pd.DataFrame(rates)

    # EMA, RSI, MACD
    df['ema'] = ta.trend.ema_indicator(df['close'], window=20)
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    last = df.iloc[-1]
    buy_score = 0
    sell_score = 0

    if last['close'] > last['ema']:
        buy_score += 1
    else:
        sell_score += 1

    if last['rsi'] < 30:
        buy_score += 1
    elif last['rsi'] > 70:
        sell_score += 1

    if last['macd'] > last['macd_signal']:
        buy_score += 1
    else:
        sell_score += 1

    if buy_score > sell_score:
        return "BUY", "Moderate", 85
    else:
        return "SELL", "Moderate", 85

# Dummy betting prediction (replace with API later)
def get_betting_prediction(match):
    outcomes = ["Team A Wins", "Team B Wins", "Draw"]
    probability = random.randint(60, 75)
    return random.choice(outcomes), probability