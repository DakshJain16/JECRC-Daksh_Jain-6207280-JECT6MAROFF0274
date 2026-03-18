from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/upload")
# driver.maximize_window()
# sleep(2)
#
# choose_file = driver.find_element(By.ID, 'file-upload')
# choose_file.send_keys(r"/Users/dakshjain/Desktop/Screenshot 2026-03-18 at 13.27.51.png")
#
# submit = driver.find_element(By.ID, 'file-submit')
# submit.click()
# sleep(5)
#
# driver.quit()

######################################################

driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//a[text()="Screenshot 2025-12-24 164603.png"]').click()
sleep(10)
print('downloaded')

driver.quit()