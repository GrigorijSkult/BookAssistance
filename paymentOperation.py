# https://selenium-python.readthedocs.io/
# https://www.youtube.com/watch?v=RDzy_oFj6lY
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def perform_payment(url):

    driver = webdriver.Firefox(executable_path=r'Library/geckodriver.exe')  # https://github.com/mozilla/geckodriver/releases
    driver.get(url)

    # Enter the card values
    card_number = driver.find_element(By.CSS_SELECTOR, "#root > div > div.PaymentContractLayout__StyledPaymentContractLayout-sc-1wkeaf1-0.jYRLxu > div:nth-child(3) > div > div > div > div.AnyCardForm__StyledFormWrapper-sc-1e1lq8d-0.kNMxAV > div > form > div.AnyCardPaymentFormView__StyledAnyCardFormletWrapper-sc-1152jhr-1.gsZhM > fieldset > div.PtForm__StyledPtFormItem-sc-19hay49-1.kvoHYn > div.MuiInputBase-root.MuiOutlinedInput-root.text-input__StyledOutlinedInput-sc-1233pm3-0.oBcCG.MuiInputBase-fullWidth.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd > input")
    card_number.send_keys("5168 1557 4474 9655")

    month_expiration = driver.find_element(By.CSS_SELECTOR, "#root > div > div.PaymentContractLayout__StyledPaymentContractLayout-sc-1wkeaf1-0.jYRLxu > div:nth-child(3) > div > div > div > div.AnyCardForm__StyledFormWrapper-sc-1e1lq8d-0.kNMxAV > div > form > div.AnyCardPaymentFormView__StyledAnyCardFormletWrapper-sc-1152jhr-1.gsZhM > fieldset > div.AnyCardFormlet__StyledFieldsBlock-eu7kh-1.bhvlyx > div:nth-child(1) > div.ExpiryDateFieldset__StyledFieldsetWrapper-sc-1c3yvry-0.gQYuUV > div > div:nth-child(1) > div > input")
    month_expiration.send_keys("11")

    year_expiration = driver.find_element(By.CSS_SELECTOR, "#root > div > div.PaymentContractLayout__StyledPaymentContractLayout-sc-1wkeaf1-0.jYRLxu > div:nth-child(3) > div > div > div > div.AnyCardForm__StyledFormWrapper-sc-1e1lq8d-0.kNMxAV > div > form > div.AnyCardPaymentFormView__StyledAnyCardFormletWrapper-sc-1152jhr-1.gsZhM > fieldset > div.AnyCardFormlet__StyledFieldsBlock-eu7kh-1.bhvlyx > div:nth-child(1) > div.ExpiryDateFieldset__StyledFieldsetWrapper-sc-1c3yvry-0.gQYuUV > div > div:nth-child(3) > div > input")
    year_expiration.send_keys("25")

    cvc = driver.find_element(By.CSS_SELECTOR, "#root > div > div.PaymentContractLayout__StyledPaymentContractLayout-sc-1wkeaf1-0.jYRLxu > div:nth-child(3) > div > div > div > div.AnyCardForm__StyledFormWrapper-sc-1e1lq8d-0.kNMxAV > div > form > div.AnyCardPaymentFormView__StyledAnyCardFormletWrapper-sc-1152jhr-1.gsZhM > fieldset > div.AnyCardFormlet__StyledFieldsBlock-eu7kh-1.bhvlyx > div:nth-child(2) > div > div > div.MuiInputBase-root.MuiOutlinedInput-root.text-input__StyledOutlinedInput-sc-1233pm3-0.oBcCG > input")
    cvc.send_keys("777")

    button_get_invoice = driver.find_element(By.XPATH, "//*[@id='send-email-invoice']")
    button_get_invoice.click()

    invoice_email = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[3]/div/div/div/div[2]/div/form/fieldset/label/div[2]/div/div/input")
    invoice_email.send_keys("book.assis@gmail.com")

    button_pay = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[3]/div/div/div/div[2]/div/form/div[3]/div/button")
    button_pay.click()


    # Get results from the
    payment_result = ""
    time.sleep(3)  # could be 4sek, but 10sek just in case
    try:
        error_message = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div[2]/div/div/div[2]").text  # looking for error message
        payment_result += error_message
    except NoSuchElementException:
        payment_result = "Нет технической ошибки платежа"

        #
        # TO BE CONTINUE
        #


    finally:
        # driver.close()  # TO DO - open for production
        return payment_result



