import bookInfoRequest
import gto

urlTest = "https://yoomoney.ru/checkout/payments/v2/contract/bankcard?orderId=2acff545-000f-5000-9000-1be81c750fe7"

# try:
#     scan_result = bookInfoRequest.get_book_info(urlTest)
#     print(scan_result.order_number, scan_result.order_price, scan_result.order_currency)
# except gto.ErrorsInfo as error:
#    print(error)



# https://selenium-python.readthedocs.io/
# https://www.youtube.com/watch?v=RDzy_oFj6lY

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'C:\Users\User02\Documents\geckodriver.exe') # https://github.com/mozilla/geckodriver/releases
driver.get(urlTest)

card = driver.find_element(By.CSS_SELECTOR, "#root > div > div.PaymentContractLayout__StyledPaymentContractLayout-sc-1wkeaf1-0.jYRLxu > div:nth-child(3) > div > div > div > div.AnyCardForm__StyledFormWrapper-sc-1e1lq8d-0.kNMxAV > div > form > div.AnyCardPaymentFormView__StyledAnyCardFormletWrapper-sc-1152jhr-1.gsZhM > fieldset > div.PtForm__StyledPtFormItem-sc-19hay49-1.kvoHYn > div.MuiInputBase-root.MuiOutlinedInput-root.text-input__StyledOutlinedInput-sc-1233pm3-0.oBcCG.MuiInputBase-fullWidth.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd > input")
card.send_keys("5550")
# driver.close()
