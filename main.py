import requests
from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = "8717329314:AAGo2P9dXE6WT4xygLrrzK-pAytT0Ix-_eM"
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzecpCxyABxFy6H4A76BjK-fnQe2Tj6HbJRh55juHRqfz2OcdJ4ZdkMms_oP2xfhkvOfw/exec"

def handle_message(update, context):
    user = update.message.from_user
    text = update.message.text

    data = {
        "user_id": user.id,
        "username": user.username,
        "text": text
    }

    try:
        requests.post(GOOGLE_SCRIPT_URL, json=data)
        update.message.reply_text("✅ Записано в таблицю")
    except Exception as e:
        update.message.reply_text("❌ Помилка")
        print(e)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Бот запущений...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
