from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
# # driver.find_element(locator, locator_expression)
# name = driver.find_element(By.ID, 'name')
# name.clear() #---> clears the text field
# # send_keys('') ---> it enters the particular text into the text field
# name.send_keys('Daksh')
# sleep(2)
#
# email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
# email.send_keys('abc@gmail.com')
# sleep(5)
#
# # get_attribute will get whatever is present at the attribute
# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))

# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# sleep(2)
# search = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
# search.clear()
#
# # 1. After importing keys class, this will click on the search button with value 'watch'
# search.send_keys('watch', Keys.ENTER)
# sleep(5)

# 2. we can also click the button without importing keys class
# search.send_keys('Shoes')
# sleep(2)
# search_button = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
# search_button.click()

# print(search.get_attribute('placeholder'))
# print(search.get_attribute('value'))

# driver.get('https://www.myntra.com/')
# driver.maximize_window()
# sleep(2)
# search = driver.find_element(By.XPATH, '//input[@class="desktop-searchBar"]')
# search.clear()
#

# search.send_keys('shirt', Keys.ENTER)
# sleep(2)

# driver.find_element(By.ID,'male').click() #---> for clicking radio button & checkbox
# sleep(2)
#
# driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
# sleep(2)

# monday_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text) #---> will only return  the inner text

# write script to toggle between both the genders
# ids = driver.find_elements(By.XPATH,'//input[@name="gender"]')
#
# for r in range(5):
#     for i in ids:
#         i.click()
#         sleep(1)

# write script to check all checkboxes return their inner text and uncheck all checkboxes backwards
# days = driver.find_elements(By.XPATH, '//div[@class="form-check form-check-inline"]/child::input[@type="checkbox"]')
# for day in days:
#     label = day.find_element(By.XPATH, './following-sibling::label')
#     day.click()
#     sleep(1)
#     print(label.text)
#
# for day in days[::-1]:
#     day.click()
#     sleep(1)

'''
is_displayed() ---> returns true if element is displayed on the screen
is_enabled() ---> returns true if elements(like buttons) is enabled on the screen
is_selected() ---> returns true if elements(like checkboxes, radio buttons) is selected on the screen.
'''

male = driver.find_element(By.ID, 'male')
male.click()
print(male.is_displayed())
print(male.is_enabled()) #---> only for buttons

check = driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected())
driver.quit()