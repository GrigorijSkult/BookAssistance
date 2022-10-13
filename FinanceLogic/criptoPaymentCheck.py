# Проверка перевода  по TXID
#
#     кошелек получателя - наш ли?
#     Валюта корректна?
#     сумма перевода  == расчетной?
#     статус заказа - Result == success
#     Время отправки - не позднее часа с начала транзакции
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import criptoCoinInfo

def check_transaction(txid, payment_amount, currency):

    driver = webdriver.Firefox(executable_path=r'../../Library/geckodriver.exe')  # https://github.com/mozilla/geckodriver/releases
    driver.get("https://tronscan.org/#/")



    return 0