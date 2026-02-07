from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    buttons = [
        [InlineKeyboardButton("Get Signals Now", callback_data="get_signals")],
        [InlineKeyboardButton("Refresh", callback_data="refresh")],
    ]
    return InlineKeyboardMarkup(buttons)