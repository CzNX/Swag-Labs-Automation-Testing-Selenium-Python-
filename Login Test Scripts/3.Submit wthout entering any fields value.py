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

# test case --> Verify if a user will be able to login with empty fields.

# test data -->

# getting required web elements
uname_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
login_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_url = driver.current_url

# print(login_url)

# passing values
# uname_element.send_keys('standard_user')
# pass_element.send_keys('secret_sauce22')
login_element.click()

home_url = 'https://www.saucedemo.com/inventory.html'


# verification

if (driver.current_url == home_url):
    print('Login Passed')
else:
    print('Login Failed')
