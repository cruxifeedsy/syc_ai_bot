from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Main menu
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📉 Analyze Trade", callback_data="analyze")],
        [InlineKeyboardButton("⚽ Predict Game", callback_data="predict")],
        [InlineKeyboardButton("ℹ️ About Bot", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Currency pairs menu
def pair_menu():
    pairs = ["EURUSD","GBPUSD","USDJPY","AUDUSD","USDCAD","USDCHF",
             "EURGBP","EURJPY","GBPJPY","XAUUSD"]
    keyboard = [[InlineKeyboardButton(p, callback_data=f"pair_{p}")] for p in pairs]
    keyboard.append([InlineKeyboardButton("↩️ Back", callback_data="back_main")])
    return InlineKeyboardMarkup(keyboard)

# Expiry menu for selected pair
def expiry_menu(pair):
    times = ["5s","15s","30s","1m","2m","3m","5m"]
    keyboard = [[InlineKeyboardButton(t, callback_data=f"exp_{pair}_{t}")] for t in times]
    keyboard.append([InlineKeyboardButton("↩️ Back", callback_data="analyze")])
    return InlineKeyboardMarkup(keyboard)

# Result buttons after Forex signal
def result_buttons(pair, expiry):
    keyboard = [
        [InlineKeyboardButton("🍀 Repeat", callback_data=f"repeat_{pair}_{expiry}")],
        [InlineKeyboardButton("↩️ Back", callback_data="analyze")]
    ]
    return InlineKeyboardMarkup(keyboard)

# League menu for betting
def league_menu():
    leagues = ["Premier League","La Liga","Serie A","Bundesliga","Ligue 1"]
    keyboard = [[InlineKeyboardButton(l, callback_data=f"league_{l}")] for l in leagues]
    keyboard.append([InlineKeyboardButton("↩️ Back", callback_data="back_main")])
    return InlineKeyboardMarkup(keyboard)

# Match menu (dummy for now)
def match_menu(league):
    matches = ["TeamA vs TeamB", "TeamC vs TeamD", "TeamE vs TeamF"]  # Replace with API later
    keyboard = [[InlineKeyboardButton(m, callback_data=f"match_{m}")] for m in matches]
    keyboard.append([InlineKeyboardButton("↩️ Back", callback_data="predict")])
    return InlineKeyboardMarkup(keyboard)

# Betting result buttons
def betting_result_buttons(match):
    keyboard = [
        [InlineKeyboardButton("🍀 Repeat", callback_data=f"repeatbet_{match}")],
        [InlineKeyboardButton("↩️ Back", callback_data="predict")]
    ]
    return InlineKeyboardMarkup(keyboard)