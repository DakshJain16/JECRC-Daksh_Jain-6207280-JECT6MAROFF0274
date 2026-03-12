# To open Chrome browser
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
'''
driver is an object --> opens the browser and closes it as soon as the commands 
have been executed
'''
sleep(5)
driver.get('https://supertails.com/') #browser opens this website
driver.maximize_window() #browser window is maximized
sleep(2)
driver.back() #will show blank page again
sleep(2)
driver.forward() #will show supertails again
sleep(2)

# print(f'Title: {driver.title}') #---> prints title of website
# print(f'Current URL: {driver.current_url}') #---> prints the current url
# print(f'Browser Name: {driver.name}') #---> prints the browser name

# driver.refresh() #will refresh the page
# sleep(2)
# driver.minimize_window() #browser window gets minimized and shows up in the task bar
# sleep(2)

# Edge
# driver = webdriver.Edge()
# sleep(5)
# driver.get('https://youtube.com/')
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(5)

# FireFox
# driver = webdriver.Firefox()
# sleep(5)

