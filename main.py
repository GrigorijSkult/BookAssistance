import bookInfoRequest


urlTest = "https://yoomoney.ru/checkout/payments/v2/contract?orderId=2ac7b4eb-000f-5000-9000-1033d7aa51e0"

scan_result = bookInfoRequest.get_book_info(urlTest)
print(scan_result.order_number, scan_result.order_price, scan_result.order_currency)


