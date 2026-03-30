from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
using the backend to target elements
interacting with DOM
'''

driver = webdriver.Chrome()
driver.get("https://www.pinterest.com/")
driver.maximize_window()
sleep(3)

#scroll to bottom of page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(3)
#document.body.scroll --> detects page height and scrolls till the bottom of the document

#scrolling to origin
driver.execute_script("window.scrollTo(0,0);")
sleep(3)
#scrollTo always has positive numbers, always considered from(0,0), considers negative numbers as zero by default

#using scrollBy
driver.execute_script("window.scrollBy(0,500);")#scroll down
sleep(3)
driver.execute_script("window.scrollBy(0,-200);")#scrolls up 200 pixels from 500 pixels
sleep(3)

#scrolling to element
ele = driver.find_element(By.XPATH,'//img[contains(@alt,"Photo of a woman in a cherry-patterned")]')
driver.execute_script("arguments[0].scrollIntoView();",ele)
sleep(3)

#clicking
ele_click = driver.find_element(By.XPATH,'//div[text()="Join Pinterest"]')
driver.execute_script('arguments[0].click();',ele_click)
sleep(3)

#scroll to and scroll by is done by windows
#scrollIntoView and click is done using arguments[0]