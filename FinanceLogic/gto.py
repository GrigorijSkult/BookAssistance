

class BookInfo:
    def __init__(self, order_number, order_price, order_currency):
        self.order_number = order_number
        self.order_price = order_price
        self.order_currency = order_currency

class PriceInfo:
    def __init__(self, exchange_rate_usd_rub, usd_price, usdt_price):
        self.exchange_rate_usd_rub = exchange_rate_usd_rub
        self.usd_price = usd_price
        self.usdt_price = usdt_price

class CryptCoinInfo:
    def __init__(self, coin, network, my_wallet_address, txid=None):
        self.coin = coin
        self.network = network
        self.my_wallet_address = my_wallet_address
        self.txid = txid

class ErrorsInfo(Exception):
    def __int__(self, txt):
        self.txt = txt


