#Use all the locators in one script for the cricbuzz website
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.cricbuzz.com/')
driver.maximize_window()
sleep(1)

# 1. using id locator
id = driver.find_element(By.ID, 'main-header')
print('working fine')

# 2. using className locator
class_name = driver.find_elements(By.CLASS_NAME, 'page-wrapper')
print('working fine')

# 3. using name locator
name = driver.find_elements(By.NAME, 'google_ads_iframe_/1024780/Desktop_new/MPU2/Home_0')
print('working fine')

# 4. using tagName locator
tag = driver.find_elements(By.TAG_NAME, 'h2')
print('working fine')

# 5. using CSS selector
class_name2 = driver.find_elements(By.CSS_SELECTOR, '.col-span-9')
print('working fine')

id2 = driver.find_element(By.CSS_SELECTOR, '#goog_plcm_frame')
print('working fine')

title = driver.find_element(By.CSS_SELECTOR, 'a[title="Live Cricket Score"]')
print('working fine')

# 6. using Xpath
element1 = driver.find_element(By.XPATH, '/html/body/div/div[2]')
print('working fine')

element2 = driver.find_element(By.XPATH, '//h2[text()="LATEST NEWS"]')
print('working fine')

print('Script completed!')

driver.quit()
