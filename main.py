from typing import Any, List

import requests
from bs4 import BeautifulSoup, ResultSet
import re

url = 'https://yoomoney.ru/checkout/payments/v2/contract/bankcard?orderId=2ac2a21c-000f-5000-8000-15697ec7c852'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes1 = soup.find_all("span", class_="Text__StyledTextSpan-sc-9bqqn7-0")
quotes2: ResultSet[Any] = soup.find_all(string=re.compile("Оплата заказа №"))# window.__data #orderId

#print(quotes2)

paragraphs: list[str] = []
for x in quotes2:
    paragraphs.append(str(x))

first = paragraphs[0].find("№") + 1
orderNumber = paragraphs[0][first:first+8]
orderPrice = 0

print(orderNumber)






#print(quotes1)
#print(soup.prettify())

#https://istories.media/workshops/2021/09/10/parsing-s-pomoshchyu-python-urok-1/
#https://tproger.ru/articles/tips-and-libraries-for-web-scraping/

# /html/body/div[3]/div/div[1]/div[1]/div/div[2]/div/div/span
#'<span class="Text__StyledTextSpan-sc-9bqqn7-0 jOxTDb">Оплата заказа №19012351</span>


#<span class="Text__StyledTextSpan-sc-9bqqn7-0 dZyMnu">150</span>
#/html/body/div[3]/div/div[1]/div[1]/div/div[1]/span/span/span[1]





