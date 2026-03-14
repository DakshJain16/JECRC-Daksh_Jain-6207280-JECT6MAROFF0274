from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver .get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)

'''
-- If inner text is present in anchor tag or tags with links then only we will use 
Link_Text and Partial_Link_Text.
-- The inner text and link should be present to use both of these locators.
'''

link = driver.find_element(By.LINK_TEXT, 'Udemy Courses')
print('I found the element')

partial = driver.find_element(By.PARTIAL_LINK_TEXT, 'Udemy')
print('I found the element')

driver.quit()

