from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
simple alert --> only accept
confirmation alert --> accept and dismiss
prompt alert --> type something in the prompt, accept, dismiss
'''

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# actions = ActionChains(driver)

# simple alert
# driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.accept() #--> clicks on ok
# sleep(3)

# confirmation alert
# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.accept() #--> to accept alert; clicks on ok
# sleep(3)

# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.dismiss() #--> clicks on cancel
# sleep(3)

# prompt alert
# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.send_keys('qwerty')
# sleep(3)
# alert.accept()
# sleep(3)

# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.send_keys('qwerty')
# sleep(3)
# alert.dismiss()
# sleep(3)

wait=WebDriverWait(driver,10)
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alert = wait.until(EC.alert_is_present()) #waits for alert to pop up then switches to the alert
sleep(2)
alert.accept()
sleep(3)
