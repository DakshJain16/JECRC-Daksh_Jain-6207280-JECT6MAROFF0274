from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
# 1. navigate to the url: https://codepen.io/gdw96/pen/jOypoYL
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()
sleep(2)
actions = ActionChains(driver)

iframe = driver.find_element(By.XPATH,'//iframe[@id="result"]')
driver.switch_to.frame(iframe)
sleep(2)

# 2. enter username and password
username = driver.find_element(By.XPATH,'//input[@id="username"]')
username.clear()
username.send_keys("Akash")
sleep(2)

passwd = driver.find_element(By.XPATH,'//input[@id="password"]')
passwd.clear()
passwd.send_keys("akash123")
sleep(2)

# 3. click on hold on the eye to view password
show_pw = driver.find_element(By.XPATH,'//button[@id="showPsswd"]')
actions.click_and_hold(show_pw).perform()
sleep(3)
actions.release().perform()
sleep(2)

# 4. click on register
register = driver.find_element(By.XPATH,'//div[@class="form-control center"]/child::input')
register.click()
sleep(5)

# 5. Use sleep for 5sec then refresh the page
driver.switch_to.default_content()
driver.back()
sleep(5)

# 6. Validate the word `Registration` using assert
driver.switch_to.frame(iframe)
form_title = driver.find_element(By.XPATH,'//h1[text()="Registration"]')

assert 'Registration' in form_title.text, "heading of form not found"
print("heading of form has been validated")