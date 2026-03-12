# Write a for loop to open a list of browsers one by one

from selenium import webdriver
from time import sleep

browsers = [
    webdriver.Chrome(),
    webdriver.Edge(),
    webdriver.Firefox(),
]

for browser in browsers:
    driver = browser
    driver.get('https://www.google.com')
    sleep(5)
    driver.quit()
