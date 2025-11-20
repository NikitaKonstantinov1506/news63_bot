import requests
from bs4 import BeautifulSoup
import datetime
import os
import time


BOT_TOKEN = "your_token"
CHAT_ID = "your_tg_chat_id"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print("Ошибка отправки:", e)


def send_today_news():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"news_{today}.txt"

    if not os.path.exists(filename):
        send_message(f"Новостей за {today} пока нет или файл ещё не создан.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        send_message(f"Файл за {today} пустой.")
        return

    # Если сообщение слишком длинное — разобьём на части (лимит 4096 символов)
    max_len = 4000
    parts = [content[i:i + max_len] for i in range(0, len(content), max_len)]

    send_message(f"<b>Новости 63.ru за {today}</b>\n\n")

    for part in parts:
        send_message(part)
        time.sleep(1)  # чтоб телеграм не ругался на флуд

    print(f"Отправлено новостей за {today}")


if __name__ == "__main__":
    send_today_news()