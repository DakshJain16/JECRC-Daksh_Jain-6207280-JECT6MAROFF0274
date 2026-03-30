from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# 1. navigate to the url: `https://demoqa.com/alerts`
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
sleep(2)

# 2. work on all the 4 alerts one after the other
# first alert
driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.accept()
sleep(3)

# second alert
driver.find_element(By.XPATH,'//button[@id="timerAlertButton"]').click()
sleep(10)
alert = driver.switch_to.alert
alert.accept()
sleep(3)

# third alert
driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.accept()
sleep(3)

# 3. validate the result appearing, eg: for `ok` you should assert with it the result shown
result = driver.find_element(By.ID, 'confirmResult').text
assert 'Ok' in result, 'clicked cancel'
print('Ok!')

driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.dismiss()
sleep(3)

# fourth alert
driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(3)
alert = driver.switch_to.alert
alert.send_keys('happy')
sleep(3)
alert.accept()
sleep(3)

# 3. validate the result appearing, eg: for `ok` you should assert with it the result shown
result = driver.find_element(By.ID, 'promptResult').text
assert 'happy' in result, 'not matched'
print('matched!')

driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys('happy')
sleep(3)
alert.dismiss()
sleep(3)