import requests

BOT_TOKEN = "8717329314:AAGo2P9dXE6WT4xygLrrzK-pAytT0Ix-_eM"
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzecpCxyABxFy6H4A76BjK-fnQe2Tj6HbJRh55juHRqfz2OcdJ4ZdkMms_oP2xfhkvOfw/exec"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": text
    })

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

    params = {"timeout": 30}
    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)
    return response.json()

def main():
    print("Бот запущений...")

    offset = None

    while True:
        data = get_updates(offset)

        for update in data.get("result", []):
            offset = update["update_id"] + 1

            if "message" not in update:
                continue

            message = update["message"]
            text = message.get("text")

            chat_id = message["chat"]["id"]
            user = message["from"]

            if not text:
                continue

            payload = {
                "user_id": user.get("id"),
                "username": user.get("username"),
                "text": text
            }

            try:
                requests.post(GOOGLE_SCRIPT_URL, json=payload)
                send_message(chat_id, "✅ Записано в таблицю")
            except Exception as e:
                print("Error:", e)
                send_message(chat_id, "❌ Помилка")

if __name__ == "__main__":
    main()
