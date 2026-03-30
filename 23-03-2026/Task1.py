# open your favourite ipl team page and scroll to your favourite image 5 times using PAGE_UP

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.mumbaiindians.com/')
driver.maximize_window()
action = ActionChains(driver)
sleep(2)

wait = WebDriverWait(driver, 10)
img = wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="Moments @ The MIX: A Mumbai Indians Experience"]')))

action.scroll_to_element(img).perform()
sleep(3)

for i in range(4):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)

sleep(3)