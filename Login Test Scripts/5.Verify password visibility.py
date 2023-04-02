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

# test case --> 	Verify if the data in password field is either visible as asterisk or bullet signs.all(iterable)

# test data --> standard_user234 , secret_sauce124


# getting required web elements
uname_element = driver.find_element(By.XPATH, "//input[@id='user-name']")
pass_element = driver.find_element(By.XPATH, "//input[@id='password']")
login_element = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_url = driver.current_url

# print(login_url)

# passing values
uname_element.send_keys('standard_user234')
pass_element.send_keys('secret_sauce124')
# login_element.click()

pass_element_type = pass_element.get_attribute('type')


# verification

if (pass_element_type == 'password'):
    print('Password is hidden and secured')

else:
    print('Password is visible to everyone')
