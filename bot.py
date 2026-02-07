import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from strategy import get_signals
from keyboards import main_menu
from config import BOT_TOKEN

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SYC Forex Bot! Click below to get trading signals.",
        reply_markup=main_menu()
    )

# Callback queries
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_signals":
        signals = get_signals()
        msg = "\n".join([f"{sym}: {sig}" for sym, sig in signals.items()])
        await query.edit_message_text(f"📊 Current Signals:\n{msg}", reply_markup=main_menu())
    elif query.data == "refresh":
        await query.edit_message_text("Refreshing...", reply_markup=main_menu())

# Run the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())