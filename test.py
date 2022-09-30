from numpy import place
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
user_name = "sinhabandana993@gmail.com"
password = "Joy.8017"
site="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dabn_yadd_sign_out&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
cart_link="https://www.amazon.in/gp/cart/view.html?ref_=abn_tools_cart_nf"
driver = webdriver.Chrome("/Users/joys/Desktop/Work/Juspay/chromedriver")
driver.get(site)
driver.maximize_window()
element = driver.find_element(By.ID ,'ap_email')
element.send_keys(user_name)
element.send_keys(Keys.RETURN)
element = driver.find_element(By.ID,'ap_password')
element.send_keys(password)
element.send_keys(Keys.RETURN)
print("Please Enter the OTP")
time.sleep(30)
driver.get(cart_link)
time.sleep(10)
buy_button=driver.find_element(By.NAME,'proceedToRetailCheckout')
buy_button.click()
time.sleep(7)
po_continue_bttn=driver.find_element(By.ID,'cof-text-input-value-0')
po_continue_bttn.send_keys(123)
po_continue_bttn.send_keys(Keys.RETURN)
#driver.get("https://www.amazon.in/gp/buy/addressselect/handlers/display.html?hasWorkingJavascript=1")
time.sleep(5)
add_bttn=driver.find_element(By.XPATH,'//*[@id="address-book-entry-0"]/div[2]/span/a')
add_bttn.click()
time.sleep(5)
ship_bttn=driver.find_element(By.CLASS_NAME,'a-button-text')
ship_bttn.click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
card_radio_bttn=driver.find_element(By.XPATH,"//input[starts-with(@value,'SelectableAddCreditCard')]")
card_radio_bttn.click()
time.sleep(2)
holder_name=driver.find_element(By.NAME,'ppw-accountHolderName')
holder_name.clear()
holder_name.send_keys("Joy Sinha")
# holder_name.send_keys(Keys.RETURN)
time.sleep(2)
card_number=driver.find_element(By.NAME,'addCreditCardNumber')
card_number.send_keys("4315812994532000")
card_number.send_keys(Keys.RETURN)
time.sleep(7)

cvv=driver.find_element(By.NAME,'addCreditCardVerificationNumber0')
cvv.send_keys(518)
cvv.send_keys(Keys.RETURN)
time.sleep(2)
try:
    bttn=driver.find_element(By.CLASS_NAME,'a-button-input')
    bttn.click()
    time.sleep(2)
except:
    bttn=driver.find_element(By.CLASS_NAME,'a-button-input a-button-text')
    bttn.click()
    time.sleep(2)

plc_ordr_bttn=driver.find_element(By.NAME,'placeYourOrder1')
plc_ordr_bttn.click()
time.sleep(30)






