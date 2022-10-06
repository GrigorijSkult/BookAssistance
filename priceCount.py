import re
import requests
from bs4 import BeautifulSoup
from lxml import etree

import gto

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests

margin = 1.20

def get_price_usd(primary_price, currency):
    # response = requests.get("https://www.investing.com/currencies/rub-usd")
    # soup = BeautifulSoup(response.content, 'html.parser')
    # dom = etree.HTML(str(soup))
    # rub_usd = dom.xpath('//*[@id="__next"]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span')[0].text
    # working but slow

    # url = 'https://api.exchangerate.host/convert?from=RUB&to=USD'
    # response = requests.get(url)
    # data = response.json()
    # print(data)
    # find value


    response = requests.get("https://api.exchangerate.host/convert?from=RUB&to=USD")
    soup = BeautifulSoup(response.content, 'html.parser')
    dom = etree.HTML(str(soup))
    rub_usd = dom.xpath('/html/body/div/div/div/div[1]/div/div/div[2]/table/tbody/tr[13]/td[2]/span/span')[0].text
    print(rub_usd)

    #
    # usd_price = primary_price * rub_usd
    # print(usd_price)

    # return usd_price * margin + 1
    return 0