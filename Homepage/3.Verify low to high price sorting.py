# prerequisites for selenium automation
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(
    executable_path=GeckoDriverManager().install()))


# main coding
driver.get('https://www.saucedemo.com/')

# to avoid UI sync issue
driver.implicitly_wait(10)

# test case --> Verify low to high price sorting.

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

select_element = driver.find_element(
    By.XPATH, "//select[@class='product_sort_container']")

selector = Select(select_element)

selector.select_by_visible_text('Price (low to high)')


all_available_prices = driver.find_elements(
    By.XPATH, "//div[@class='inventory_item_price']")


default_prices = []
for x in all_available_prices:
    default_prices.append(float(x.text.split('$')[1]))
    # print(x.text)

# highest price after filtering high to low
# default_highest_price = 22
default_lowest_price = default_prices[0]
default_prices.sort()
# highest price in all store
lowest_price_item = default_prices[0]

# print(sorted_prices)
# verification

if (default_lowest_price == lowest_price_item):
    print('Low to High sorting is working fine')
else:
    print('Low to High sorting isnt working properly')


# print(broken_link)
