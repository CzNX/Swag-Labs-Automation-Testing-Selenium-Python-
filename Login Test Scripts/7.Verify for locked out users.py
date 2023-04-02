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

# test case --> Verify the messages for entering only username.

# test data --> locked_out_user ,secret_sauce


# getting required web elements
uname_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
login_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_url = driver.current_url

# print(login_url)

# passing values
uname_element.send_keys('locked_out_user')
pass_element.send_keys('secret_sauce')
login_element.click()


#
erromsg_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
lockedusermsg = 'Epic sadface: Sorry, this user has been locked out.'

home_url = 'https://www.saucedemo.com/inventory.html'

# print(applogo_element.is_displayed())

# verification

if driver.current_url != home_url:
    if erromsg_element.is_displayed() and erromsg_element.text == lockedusermsg:
        print(erromsg_element.text)
else:
    print('Login successful')
