
import asyncio
from telegram import Update, InputFile, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from keyboards import main_menu, pair_menu, expiry_menu, result_buttons, league_menu, match_menu, betting_result_buttons
from strategy import get_signal, get_betting_prediction

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to SYC AI Bot 🤖\nChoose a service:",
        reply_markup=main_menu()
    )

# Handle button clicks
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # --- FOREX ANALYSIS ---
    if data == "analyze":
        await query.edit_message_text("Select Currency Pair:", reply_markup=pair_menu())
    elif data.startswith("pair_"):
        pair = data.split("_")[1]
        await query.edit_message_text(f"{pair} selected.\nChoose expiry:", reply_markup=expiry_menu(pair))
    elif data.startswith("exp_") or data.startswith("repeat_"):
        parts = data.split("_")
        pair, expiry = parts[1], parts[2]
        msg = await query.edit_message_text("🔍 Generating signal")
        for i in range(3):
            await asyncio.sleep(0.1)
            await msg.edit_text("🔍 Generating signal" + "." * (i+1))
        signal, volatility, prob = get_signal(pair)
        image = "images/buy.png" if signal == "BUY" else "images/sell.png"
        caption = (
            f"📊 AI TRADE RESULT\n\n"
            f"Currency Pair: {pair}\n"
            f"Expiry Time: {expiry}\n"
            f"Volatility: {volatility}\n"
            f"Signal Type: {signal}\n"
            f"Probability of Success: {prob}%"
        )
        await query.message.reply_photo(
            photo=InputFile(image),
            caption=caption,
            reply_markup=result_buttons(pair, expiry)
        )
    elif data == "back_main":
        await query.edit_message_text("Main Menu:", reply_markup=main_menu())

    # --- BETTING PREDICTION ---
    elif data == "predict":
        await query.edit_message_text("Select League:", reply_markup=league_menu())
    elif data.startswith("league_"):
        league = data.split("_")[1]
        await query.edit_message_text(f"Matches in {league} today:", reply_markup=match_menu(league))
    elif data.startswith("match_") or data.startswith("repeatbet_"):
        match = "_".join(data.split("_")[1:])
        msg = await query.edit_message_text("Predicting...")
        for i in range(3):
            await asyncio.sleep(0.2)
            await msg.edit_text("Predicting" + "."*(i+1))
        outcome, prob = get_betting_prediction(match)
        await query.message.reply_photo(
            photo=InputFile("images/goodluck.png"),
            caption=f"⚽ Prediction:\n{match}\nResult: {outcome}\nProbability: {prob}%",
            reply_markup=betting_result_buttons(match)
        )

    # --- ABOUT BOT ---
    elif data == "about":
        await query.edit_message_text(
            "SYC AI Bot 🤖\n\n"
            "Forex signals powered by MT5.\n"
            "Betting predictions (dummy) for practice/fun.\n"
            "Use responsibly."
        )

# Run bot
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()