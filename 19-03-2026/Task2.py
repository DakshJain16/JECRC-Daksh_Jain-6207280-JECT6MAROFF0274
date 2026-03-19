from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

full_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]')))
full_name.clear()
full_name.send_keys('Harsh Rao')

email = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="email"]')))
email.clear()
email.send_keys('harsh123rao@gmail.com')

tel = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="tel"]')))
tel.clear()
tel.send_keys('9876556789')

upload = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="datafile"]')))
upload.send_keys('/Users/dakshjain/Desktop/Screenshot 2026-03-18 at 22.01.07.png')

gender = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name="sgender"]')))
select = Select(gender)
select.select_by_value('male')

yoe = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="three"]')))
yoe.click()

man_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="manualtesting"]')))
man_test.click()
auto_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="automationtesting"]')))
auto_test.click()
java = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="java"]')))
java.click()

tools = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@id="tools"]')))
select2 = Select(tools)
select2.select_by_value('cypress')

submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="submit"]')))
submit.click()

# driver.quit()