# Swag-Labs-Automation-Testing-Selenium-Python-

https://www.saucedemo.com/  

A demo ecommerce testing website used for automation practice using selenium webdriver with python.
Test cases includes scenarios like:

Login---Logout----Homepage----filtering----Add to cart----cart_page etc.

used:
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(
    executable_path=GeckoDriverManager().install()))
    
most used selector : XPATH

import requests---> for broken links / working links
python sort and sorted for filtering lists
