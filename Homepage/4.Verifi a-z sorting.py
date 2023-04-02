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

# test case --> Verify a-z sorting.

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

selector.select_by_visible_text('Name (A to Z)')


all_available_titles = driver.find_elements(
    By.XPATH, "//div[@class='inventory_item_name']")


default_titles = []
for x in all_available_titles:
    default_titles.append(x.text)
    # print(x.text)


# a-z default before sorting
# default_titles.append('hello')
# using sorted to sort alphabets regardless of capitalization
sorted_list = sorted(default_titles, key=str.lower)

# # verification

if (sorted_list == default_titles):
    print('A-Z  sorting is working fine')
else:
    print('A-Z sorting isnt working properly')
