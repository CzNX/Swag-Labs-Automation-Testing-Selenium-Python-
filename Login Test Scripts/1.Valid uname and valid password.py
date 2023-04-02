# prerequisites for selenium automation
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(
    executable_path=GeckoDriverManager().install()))


# main coding
driver.get('https://www.saucedemo.com/')

# to avoid UI sync issue
driver.implicitly_wait(10)

# test case --> Verify if a user will be able to login with a valid username and valid password.

# test data --> standard_user , secret_sauce


# getting required web elements
uname_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
login_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_url = driver.current_url

# print(login_url)

# passing values
uname_element.send_keys('standard_user')
pass_element.send_keys('secret_sauce')
login_element.click()
applogo_element = driver.find_element(By.XPATH, "//div[@class='app_logo']")
home_url = 'https://www.saucedemo.com/inventory.html'

# print(applogo_element.is_displayed())

# verification

if (driver.current_url == 'https://www.saucedemo.com/inventory.html' and home_url == driver.current_url and applogo_element.is_displayed()):
    print('Test Passed!, Login was successful')
else:
    print('Test Failed!, Login was Failed')
