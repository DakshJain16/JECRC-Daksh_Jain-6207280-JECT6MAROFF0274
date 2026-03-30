from unicodedata import category

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Go to myntra, hover over men or women, choose a category and click on it
scroll to a 4th or 5th row product (use proper waits)'''

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.myntra.com/')
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)

men = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@data-group="men"]')))
sleep(3)
action.move_to_element(men).perform()
sleep(3)

cat = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@data-reactid="99"]/a')))
cat.click()
sleep(2)

prod = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@id="39234766"]')))
action.scroll_to_element(prod).perform()
sleep(3)