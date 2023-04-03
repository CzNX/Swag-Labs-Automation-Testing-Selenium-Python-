# prerequisites for selenium automation
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import requests
import time
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(
    executable_path=GeckoDriverManager().install()))


# main coding
driver.get('https://www.saucedemo.com/')

# to avoid UI sync issue
driver.implicitly_wait(10)

# test case -->verify cart badge no to cart list no.

# test data --> standard_user , secret_sauce


# getting required web elements
uname_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
login_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
# login_url = driver.current_url

# print(login_url)

# passing values
uname_element.send_keys('standard_user')
pass_element.send_keys('secret_sauce')

# logging in
login_element.click()
menubtn = driver.find_element(
    By.XPATH, "//button[@id='react-burger-menu-btn']")
logoutbtn = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
applogo_element = driver.find_element(By.XPATH, "//div[@class='app_logo']")


item1_addtocart = driver.find_element(
    By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
item2 = driver.find_element(
    By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
item3 = driver.find_element(
    By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
cart_element = driver.find_element(
    By.XPATH, "//a[@class='shopping_cart_link']").click()

time.sleep(5)
# removing an item from cart list
driver.find_element(
    By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()


cart_element = driver.find_element(
    By.XPATH, "//a[@class='shopping_cart_link']")
noshownincart = int(cart_element.text)
noofitemsincartlist = driver.find_elements(
    By.XPATH, "//div[@class='cart_item']")


# print(noshownincart, len(noofitemsincartlist))

# Verification

if (noshownincart == len(noofitemsincartlist)):
    print('No.of items shown in cart badge matches no. of items in cart list')
else:
    print('No.of items shown in cart badge doesnt match no. of items in cart list')
