# Print Title name, Current URL and browser name for all the browsers

from selenium import webdriver
from time import sleep
browsers = [
    webdriver.Chrome(),
    webdriver.Edge(),
    webdriver.Firefox(),
]

for browser in browsers:
    driver = browser
    driver.get('https://www.amazon.in/')
    driver.maximize_window()
    sleep(3)
    print(f'Title: {driver.title}')
    print(f'Current URL: {driver.current_url}')
    print(f'Browser: {driver.name}')
    print('\n')
