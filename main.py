import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# 👉 ВСТАВ СЮДИ СВОЇ ДАНІ
TELEGRAM_TOKEN = "8717329314:AAGo2P9dXE6WT4xygLrrzK-pAytT0Ix-_eM"
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzecpCxyABxFy6H4A76BjK-fnQe2Tj6HbJRh55juHRqfz2OcdJ4ZdkMms_oP2xfhkvOfw/exec"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    data = {
        "user_id": user.id,
        "username": user.username,
        "text": text
    }

    try:
        requests.post(GOOGLE_SCRIPT_URL, json=data)
        await update.message.reply_text("✅ Записано в таблицю")
    except Exception as e:
        await update.message.reply_text("❌ Помилка запису")
        print(e)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
