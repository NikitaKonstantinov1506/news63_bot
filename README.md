# news63_bot
Автоматический парсер новостей с сайта [63.ru](https://63.ru) + отправка в личку Telegram.
### Что умеет:
- Парсит свежие новости каждый день
- Сохраняет в файл
- Отправляет тебе в Telegram ровно в 9:30 утра
- Работает на сервере по расписанию (cron)
- Защищённые токены через `.env`

### Стек:
Python • BeautifulSoup • Telegram Bot API • cron • dotenv

### Как запустить локально:

git clone https://github.com/NikitaKonstantinov1506/news-telegram-bot.git
cd news-telegram-bot
cp .env.example .env        # вставить свои токены
pip install -r requirements.txt
python main.py              # тестовая отправка
