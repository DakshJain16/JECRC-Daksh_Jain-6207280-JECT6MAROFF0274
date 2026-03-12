# Use all the methods in one script for Chrome
# 1. using sleep
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(2)
# get method
driver.get('https://www.amazon.in/')

# maximize method
driver.maximize_window()
sleep(2)

# back method
driver.back()
sleep(2)

# forward method
driver.forward()
sleep(2)

# refresh method
driver.refresh()
sleep(2)

# minimize method
driver.minimize_window()
sleep(2)

# close method
driver.close()

# 2. using ChromeOptions
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

driver.quit()