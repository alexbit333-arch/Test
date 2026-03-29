import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8717329314:AAGo2P9dXE6WT4xygLrrzK-pAytT0Ix-_eM"
GOOGLE_URL = "https://script.google.com/macros/s/AKfycbzecpCxyABxFy6H4A76BjK-fnQe2Tj6HbJRh55juHRqfz2OcdJ4ZdkMms_oP2xfhkvOfw/exec"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    data = {
        "user_id": user.id,
        "username": user.username or "no_username",
        "text": text
    }

    try:
        requests.post(GOOGLE_URL, json=data)
        await update.message.reply_text("☀️ Записано в таблицю")
    except:
        await update.message.reply_text("❌ Помилка")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
