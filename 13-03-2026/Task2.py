from wsgiref.validate import header_re

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Go to https://the-internet.herokuapp.com/login.
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
sleep(1)

# 2.Locate the username field using XPath with Tag and name attribute.
username = driver.find_element(By.XPATH, '//input[@name="username"]')
print('working fine')

# 3.Locate the password field using XPath with Tag and id attribute.
password = driver.find_element(By.XPATH, '//input[@id="password"]')
print('working fine')

# 4.Locate the "Login" button using XPath with Tag and type attribute.
login = driver.find_element(By.XPATH, '//button[@type="submit"]')
print('working fine')

# 5.Locate the "Elemental Selenium" link using its exact text with text().
link = driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
print('working fine')

# 5.Locate the main heading "Login Page" using contains() with text.
heading = driver.find_element(By.XPATH, '//h2[contains(text(), "Login Page")]')
print('working fine')

print('script completed!')
driver.quit()