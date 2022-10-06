import bookInfoRequest, gto, paymentOperation

urlTest = "https://yoomoney.ru/checkout/payments/v2/contract/bankcard?orderId=2ad0f342-000f-5000-9000-1c8b406f1087"

try:
    scan_result = bookInfoRequest.get_book_info(urlTest)
    print(scan_result.order_number, scan_result.order_price, scan_result.order_currency)

    payment_result = paymentOperation.perform_payment(urlTest)
    print(payment_result)

except gto.ErrorsInfo as error:
    print(error)



