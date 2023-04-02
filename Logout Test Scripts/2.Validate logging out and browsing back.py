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

# test case --> Verify logout and browsing back.

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

home_url = 'https://www.saucedemo.com/inventory.html/'
login_url = 'https://www.saucedemo.com/'

# logout process
menubtn.click()
logoutbtn.click()

# navigating back
driver.back()
loginlogo_element = driver.find_element(By.XPATH, "//div[@class='login_logo']")

# print(applogo_element.is_displayed())

# verification

if (driver.current_url != home_url and loginlogo_element.is_displayed()):
    print('Test Passed!, We are still in login page')
else:
    print('Test Failed!, login page was accessed even after logging out by browsing back')

# print(driver.current_url, login_url)
