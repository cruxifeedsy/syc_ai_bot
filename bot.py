import os
import asyncio
from telegram import Update, InputFile, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from strategy import get_signal
from keyboards import main_menu_keyboard, pair_keyboard, expiry_keyboard

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Bot start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SYC AI Forex Bot!\nSelect an option:",
        reply_markup=main_menu_keyboard()
    )

# Handle menu selections
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "analyze_trade":
        await query.edit_message_text("Select currency pair:", reply_markup=pair_keyboard())
    elif data.startswith("pair_"):
        pair = data.split("_")[1]
        context.user_data['pair'] = pair
        await query.edit_message_text(
            f"Selected {pair}. Choose expiry time:",
            reply_markup=expiry_keyboard()
        )
    elif data.startswith("expiry_"):
        expiry = data.split("_")[1]
        pair = context.user_data.get('pair')
        await query.edit_message_text(f"Generating signal for {pair} ({expiry})... ⏳")
        signal = await get_signal(pair, expiry)
        img_path = f"images/{signal['signal'].lower()}.png"  # buy.png or sell.png
        caption = (
            f"Currency Pair: {pair}\n"
            f"Expiry: {expiry}\n"
            f"Volatility: {signal['volatility']}\n"
            f"Probability: {signal['probability']}%"
        )
        await query.edit_message_media(
            media=InputFile(img_path),
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🍀 Repeat", callback_data=f"expiry_{expiry}"),
                InlineKeyboardButton("↩️ Back", callback_data="analyze_trade")
            ]])
        )
        await query.edit_message_caption(caption)

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))
    print("Bot is running...")
    app.run_polling()