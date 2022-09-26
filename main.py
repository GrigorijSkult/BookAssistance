from typing import Any, List

import requests
from bs4 import BeautifulSoup, ResultSet
import re

url = 'https://yoomoney.ru/checkout/payments/v2/contract/bankcard?orderId=2ac40155-000f-5000-9000-150055c1d0cf'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes: ResultSet[Any] = soup.find_all(string=re.compile("Оплата заказа №"))# window.__data #orderId

paragraphs: list[str] = []
for x in quotes:
    paragraphs.append(str(x))

#order number
orderNumber = ""
firstDigit = paragraphs[0].find("№") + 1
orderText = paragraphs[0][firstDigit:firstDigit + 30]
for x in orderText:
    if x == '"':
        break
    else:
        orderNumber += x

#order Price
orderPrice = ""
orderCurrency = ""
firstDigit = paragraphs[0].find("totalPrice" + '"' ) + 13
priceText = paragraphs[0][firstDigit:firstDigit + 30]
i=0
for x in priceText:
    if x == '"':
        orderCurrency = paragraphs[0][firstDigit + i + 18 : firstDigit + i + 18 + 3]
        i = 0
        break
    else:
        i+=1
        orderPrice += x


print(orderNumber)
print(orderPrice)
print(orderCurrency)
