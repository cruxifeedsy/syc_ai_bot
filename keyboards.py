from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Analyze Trade 📉", callback_data="analyze_trade")]
    ]
    return InlineKeyboardMarkup(keyboard)

def pair_keyboard():
    pairs = ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF"]
    keyboard = [[InlineKeyboardButton(p, callback_data=f"pair_{p}")] for p in pairs]
    return InlineKeyboardMarkup(keyboard)

def expiry_keyboard():
    expiries = ["5s", "15s", "30s", "1m", "2m", "3m", "5m"]
    keyboard = [[InlineKeyboardButton(e, callback_data=f"expiry_{e}")] for e in expiries]
    return InlineKeyboardMarkup(keyboard)