from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# sleep(2)

# # 1. locating xpath using ancestor
# element1 = driver.find_elements(By.XPATH, '//span[text()="All"]/ancestor::div[@id="nav-main"]')
# print('working fine')
#
# element2 = driver.find_elements(By.XPATH, '//span[text()="Returns"]/ancestor::div[@id="nav-tools"]')
# print('working fine')
#
# # 2. locating xpath using descendant
# element3 = driver.find_elements(By.XPATH, '//div[@id="nav-main"]/descendant::span[text()="All"]')
# print('working fine')
#
# element4 = driver.find_elements(By.XPATH, '//div[@class="nav-left"]/descendant::span[contains(text(), "Update location")]')
# print('working fine')
#
# element5 = driver.find_elements(By.XPATH,'//div[@id="gw-layout"]/descendant::h2[contains(text(), "Revamp your home in style")]')
# print('working fine')
#
# # 3. locating xpath using parent --> it locates the immediate parent only.
# element6 = driver.find_elements(By.XPATH, '//label[contains(text(), "Search Amazon.in")]/parent::div[@class="nav-search-field "]')
# print('working fine')
#
# # 4. locating xpath using child --> it locates the immediate child only.
# element7 = driver.find_elements(By.XPATH, '//div[@id="nav-cart-text-container"]/child::span[contains(text(), "Cart")]')
# print('working fine')
#
# # 5. locating xpath using preceding-sibling
# element8 = driver.find_elements(By.XPATH, '//a[text()="Mobiles"]/ancestor::li/preceding-sibling::li[3]')
# print('working fine')
#
# #6. locating xpath using following-sibling
# element9 = driver.find_elements(By.XPATH, '//span[text()="Fresh"]/ancestor::li/following-sibling::li[2]')
# print('working fine')

# Practice
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)

element10 = driver.find_elements(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
print('working fine')

element11 = driver.find_element(By.XPATH,'//td[text()="Amod"]/ancestor::tr/preceding-sibling::tr[4]/td[3]')
print('working fine')

element12 = driver.find_elements(By.XPATH,'//td[text()="300"]/preceding-sibling::td[3]')
print('working fine')

element13 = driver.find_elements(By.XPATH,'//tbody[@id="rows"]/descendant::tr/td[1]')
print('working fine')

driver.quit()