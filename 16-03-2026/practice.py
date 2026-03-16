from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

'''
1. Navigate to flipkart
2. find search field and search for a product
3. get attribute of the product searched
4. click on search button
5. click on a checkbox or boxes in filter
6. get the text of that filter
'''
driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(2)

search = driver.find_element(By.XPATH, '//form[@class="lilxh_ header-form-search"]/descendant::input[@class="nw1UBF v1zwn25"]')
search.clear()
search.send_keys('watch')
sleep(2)

print(search.get_attribute('placeholder'))
print(search.get_attribute('value'))


search_button = driver.find_element(By.XPATH, '//div[@class="VCplLH mIK8ju"]/descendant::button[@type="submit"]')
search_button.click()
sleep(2)

fil = driver.find_element(By.XPATH, '//a[@class="yQhGfT"][1]')
print(f'Filter: {fil.text}')
fil.click()
sleep(2)

image = driver.find_element(By.XPATH, '//div[@data-id="WATHF5KGFXQQXDKX"]/descendant::img[@class="MZeksS"]')
print(image.get_attribute('src'))
sleep(2)
driver.quit()