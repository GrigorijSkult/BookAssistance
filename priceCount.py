import requests


margin = 1.20

def get_price_usd(primary_price, currency):
    #check if rub
    response = requests.get('https://api.exchangerate.host/convert?from=RUB&to=USD')
    data = response.json()
    rub_usd = data['result']

    usd_price = primary_price * rub_usd

    return usd_price * margin + 1
