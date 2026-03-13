from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.myntra.com/')
sleep(4)
print('its working fine')

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument('headless') #---> browser runs in the background
driver = webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
sleep(4)
print('its working fine')