
class BookInfo:
    def __init__(self, order_number, order_price, order_currency):
        self.order_number = order_number
        self.order_price = order_price
        self.order_currency = order_currency

    def info(self):
        print(self.order_number,  self.order_price,  self.order_currency)