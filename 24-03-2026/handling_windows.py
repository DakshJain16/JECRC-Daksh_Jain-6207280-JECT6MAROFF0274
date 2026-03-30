from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(2)

#current window handle returns the element(address with id)
parent_window = driver.current_window_handle


driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
sleep(2)
all_windows = driver.window_handles  #gives a list of all present windows, indexing of the windows works like python list indexing
#The point is to switch control of the current window to the new opened window
print(len(all_windows))

driver.switch_to.window(all_windows[-1])#switching to most recent window

assert "New" in driver.find_element(By.CLASS_NAME,'example').text
print('done')

#to go back to parent window
driver.switch_to.window(parent_window)

'''
suppose we close the window using driver.close(), in the new window, selenium doesn't 
automatically switch the control back to previous tab, you have to do it manually by storing 
the address of the parent window as done above
'''

#Opening a website in new window
driver.switch_to.new_window('tab')
sleep(2)
driver.get("https://www.cricbuzz.com/")
sleep(2)

driver.switch_to.new_window('window') #opens a new window
sleep(2)
driver.get("https://www.cricbuzz.com/")
sleep(2)


