import FinanceLogic.bookInfoRequest
from FinanceLogic import gto, priceCount, criptoCoinLogic, criptoCheck

import time

# only Yoomoney
urlTest = "https://yoomoney.ru/checkout/payments/v2/contract/bankcard?orderId=2ad393bb-000f-5000-9000-18e1c77be76f"

# Variables
operation_max_time = 2400 # 40 min in sek
payment_lead_time = 60 # sek
stock_in_case = 170 # RUB - just to have in case of any errors during multiple connection


try:
    start_time = time.time()
    scan_result = FinanceLogic.bookInfoRequest.get_book_info(urlTest)
    print(scan_result.order_number, scan_result.order_price, scan_result.order_currency)

    reader = open('AdditionaFiles/remainingAmount.txt', 'r')
    remaining_amount = float(reader.read())
    reader.close()

    if  scan_result.order_price < remaining_amount + 50.00:
        price_result = priceCount.get_price_usd(scan_result.order_price, scan_result.order_currency)
        # print(price_result.exchange_rate_usd_rub, price_result.usd_price, price_result.usdt_price)

        # Выбор сетей в usdt
        # print(criptoCoinLogic.coin_list[0])

        # check if thansaction was sent - to my card + the amount + the status green
        criptoCheck

        # ...  TO DO ...






        if time.time() - start_time < operation_max_time - payment_lead_time:

            # payment_result = paymentOperation.perform_payment(urlTest)
            # print(payment_result)

            print("Total time", round(time.time() - start_time, 4), "sek")

        else:
            raise gto.ErrorsInfo("Время транзакции превышенно, ссылка не активна")
    else:
        raise gto.ErrorsInfo("Тех инфо - не достаточно финансов на счету")

except gto.ErrorsInfo as error:
    print(error)



