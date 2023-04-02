# prerequisites for selenium automation
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import requests
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(
    executable_path=GeckoDriverManager().install()))


# main coding
driver.get('https://www.saucedemo.com/')

# to avoid UI sync issue
driver.implicitly_wait(10)

# test case -->removing all items from cart.

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


# add an item to cart
add_to_cart_tag = 'add-to-cart'
remove_tag = 'remove'
# //button[@id = 'add-to-cart-sauce-labs-backpack']


item1_addtocart = driver.find_element(
    By.XPATH, "//button[@id='"+add_to_cart_tag+"-sauce-labs-backpack']").click()


item2 = driver.find_element(
    By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
item3 = driver.find_element(
    By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
cart_element = driver.find_element(
    By.XPATH, "//a[@class='shopping_cart_link']")

# no .of items added to cart using xpath
items_added_to_cart = driver.find_elements(
    By.XPATH, "//button[starts-with(@name, 'remove')]")

# removing an item from cart
item1_remove = driver.find_element(
    By.XPATH, "//button[@id='"+remove_tag+"-sauce-labs-backpack']").click()
item2_remove = driver.find_element(
    By.XPATH, "//button[@id='"+remove_tag+"-test.allthethings()-t-shirt-(red)']").click()
item3_remove = driver.find_element(
    By.XPATH, "//button[@id='"+remove_tag+"-sauce-labs-fleece-jacket']").click()

items_added_to_cart = driver.find_elements(
    By.XPATH, "//button[starts-with(@name, 'remove')]")

if cart_element.text == '':
    if (len(items_added_to_cart) == 0):
        print('Test passed! , No items are  added to cart')
    else:
        print(
            'Test Failed! ,No.of items shown doesnt match with no.of items being selected')
else:
    if (int(cart_element.text) == len(items_added_to_cart)):
        print('Test passed! , No. of items selected matches with no. shown in cart badge')
    else:
        print(
            'Test Failed! ,No.of items shown doesnt match with no.of items being selected')

print(len(items_added_to_cart))
