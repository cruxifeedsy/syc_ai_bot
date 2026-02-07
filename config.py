import os

# FXCM API token (add to Railway env variables)
FXCM_TOKEN = os.getenv("FXCM_TOKEN")

# Forex pairs
PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD",
    "USD/CAD", "USD/CHF", "NZD/USD", "EUR/GBP",
    "EUR/JPY", "GBP/JPY", "AUD/JPY"
]

# Expiry times
EXPIRIES = ["5s","15s","30s","1m","2m","3m","4m","5m"]