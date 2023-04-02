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

# test case --> Verify external link status.

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


all_available_links = driver.find_elements(By.TAG_NAME, "a")


external_links = []
for x in all_available_links:
    if (x.get_attribute('href') and x.get_attribute('href').startswith('https://www.saucedemo.com')):
        continue
    else:
        external_links.append(x.get_attribute('href'))


res = list(filter(lambda item: item is not None, external_links))

# print(res)
broken_link = []
working_link = []

# verification

for x in res:
    try:
        r = requests.get(x, timeout=1)
        if (r.status_code >= 400 and r.status_code != 999):
            broken_link.append(x)
            print(x, '--is broken link')
        else:
            working_link.append(x)
            print(x, '--is working link')

        r.raise_for_status()
    except requests.exceptions.RequestException as errex:
        None

# print(broken_link)
