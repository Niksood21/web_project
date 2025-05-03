from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

data = []

for page in range(1, 4):
    url = f'https://www.chitai-gorod.ru/collections/o-druzhbe-lyudey-i-zhivotnyh-265?page={page}'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    book_cards = soup.find_all('article', class_='product-card product-card product')

    for card in book_cards:
        for card in book_cards:
            name = (card.find("div", class_="product-title__head").text.replace('\n', "").
                    replace('\n', ""))
            author = card.find("div", class_="product-title__author").text.replace('\n', "")
            try:
                avg_rating = card.find("span", itemprop="ratingValue").text.replace('\n', "")
            except AttributeError:
                avg_rating = "None"

            try:
                old_price = card.find("div", class_="product-price__old").text.replace('\n', "")
            except AttributeError:
                old_price = "None"

            try:
                new_price = (card.find("div", class_="product-price__value product-price__value--discount").
                             text.replace('\n', ""))
            except AttributeError:
                new_price = "None"

            try:
                publishing = card.find("a", class_="product-detail-characteristics__"
                                                   "item-value product-detail-characteristics__item-value--link").text
            except AttributeError:
                publishing = "None"

            try:
                img_tag = card.find("img")
                if img_tag:
                    cover_url = img_tag.get('data-src')
                    if cover_url and cover_url.startswith('/'):
                        cover_url = 'https://www.chitai-gorod.ru' + cover_url
                else:
                    cover_url = "None"
            except AttributeError:
                cover_url = "None"

            item_card = {
                'name': name,
                'author': author,
                'avg_rating': avg_rating,
                'old_price': old_price,
                'new_price': new_price,
                'publishing': publishing,
                'cover_url': cover_url
            }
            data.append(item_card)

with open('books.json', 'w', encoding='utf8') as jsonData:
    json.dump(data, jsonData, ensure_ascii=False, indent=4)
driver.quit()
