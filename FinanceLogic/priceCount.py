import requests
from FinanceLogic import gto


margin = 1.20
network_fee = 1.00

def get_price_usd(primary_price, currency):
    #check if rub
    if currency == "RUB":

        response = requests.get('https://api.exchangerate.host/convert?from=RUB&to=USD')
        data = response.json()
        rub_usd = data['result']

        usd_price = round(float(primary_price) * rub_usd, 4)

        return gto.PriceInfo(round(rub_usd, 5), usd_price, usd_price * margin + network_fee)
    else:
        raise gto.ErrorsInfo("Некорректная валюта")