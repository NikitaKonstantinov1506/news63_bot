import requests
from bs4 import BeautifulSoup
import datetime
import os


def parse_news():

    url = 'https://63.ru/'
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')


        news_items = soup.find_all('li', class_="itemWrapper_D5XNy")


        today = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"news_{today}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            for item in news_items:
                a_tag = item.find('a', class_="link_J499q")
                if a_tag:
                    title = a_tag.get_text(strip=True)
                    url = a_tag.get('href', '')
                    if title and url:
                        f.write(f"{title}||{url}\n")

        return filename

    except Exception as e:
        print(f"Ошибка парсинга: {e}")
        return None


if __name__ == "__main__":
    parse_news()