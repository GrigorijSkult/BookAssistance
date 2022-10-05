from typing import Any, List
import requests
from bs4 import BeautifulSoup, ResultSet
import re
import gto


def get_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

  #  test_url = soup.find_all(string=re.compile("Author.Today"))
    if soup.find_all(string=re.compile("Author.Today")) != []:
        quotes = soup.find_all(string=re.compile("Оплата заказа №"))  # or for example window.__data #orderId

        paragraphs: list[str] = []
        for x in quotes:
            paragraphs.append(str(x))

        # order number
        order_number = ""
        first_digit = paragraphs[0].find("№") + 1
        order_text = paragraphs[0][first_digit:first_digit + 30]
        for x in order_text:
            if x == '"':
                break
            else:
                order_number += x

        # order Price
        order_price = ""
        order_currency = ""
        first_digit = paragraphs[0].find("totalPrice" + '"') + 13
        price_text = paragraphs[0][first_digit:first_digit + 30]
        i = 0
        for x in price_text:
            if x == '"':
                order_currency = paragraphs[0][first_digit + i + 18: first_digit + i + 18 + 3]
                i = 0
                break
            else:
                i += 1
                order_price += x

        return gto.BookInfo(order_number, order_price, order_currency)

    else:
        raise gto.ErrorsInfo("Некорректная ссылка")
