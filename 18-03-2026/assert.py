from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get('https://www.lenskart.com/')
# driver.maximize_window()
# sleep(2)
#
# eye = driver.find_element(By.ID, 'lrd1')
# print(eye.text)
# #Assert is a keyword in python which checks if a statement is true or false.
# # If it is true then it continues and if false then it throws an assertion error
# assert 'EYEGLASSES' in eye.text, 'did not find EYEGLASSES text' #---> True
# print('success')
#
# assert 'GLASSES' == eye.text, 'did not find EYEGLASSES text' #---> False
# print('success')

driver.get('https://www.lenskart.com/john-jacobs-jj-e11540-c6-eyeglasses.html')
driver.maximize_window()
sleep(5)
check = driver.find_element(By.XPATH, '//button[@class="sc-39b66eee-0 boDzrJ"]')
print(check.text)
assert 'Check' in check.text, 'did not find check text'
print(check.is_enabled())
check.click()
sleep(5)
pincode = driver.find_element(By.TAG_NAME, 'input')
check1 = driver.find_element(By.XPATH, '//div[@data-cy="check-enterd-pincode"]')
print(check1.is_enabled())
pincode.send_keys('302005')
if check1.is_enabled():
    check1.click()
    print('success')
# driver.get('https://world.benetton.com/')
# driver.maximize_window()
# sleep(2)
#
# ben = driver.find_element(By.XPATH, '//h1[contains(text(), "WELCOME TO")]/child::span[contains(text(), "BENETTON")]')
# print(ben.text)
#
# assert "BEN" in ben.text, "didn't find"
# print('success')
driver.quit()

