from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# navigate to the url: https://demoqa.com/browser-windows
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
sleep(2)
parent_window = driver.current_window_handle

# work on all the 3 windows one after the other
# first window
driver.find_element(By.ID, 'tabButton').click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])

# validate the text result appearing, you should use assert with it the result shown
txt = driver.find_element(By.ID, 'sampleHeading').text
sleep(2)
assert 'This is a sample page' in txt, 'Invalid!'
print('Valid!')
driver.close()

driver.switch_to.window(parent_window)
sleep(3)

# second window
driver.find_element(By.ID, 'windowButton').click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# validate the text result appearing, you should use assert with it the result shown
txt = driver.find_element(By.ID, 'sampleHeading').text
sleep(2)
assert 'This is a sample page' in txt, 'Invalid!'
print('Valid!')
driver.close()

driver.switch_to.window(parent_window)
sleep(3)

# third window
driver.find_element(By.ID, 'messageWindowButton').click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])

# # validate the text result appearing, you should use assert with it the result shown
# body_text = driver.find_element(By.TAG_NAME, 'body').text
# sleep(2)
# assert 'Knowledge increases' in body_text, 'Invalid!'
# print('Valid!')
driver.close()

driver.switch_to.window(parent_window)
sleep(3)

driver.quit()