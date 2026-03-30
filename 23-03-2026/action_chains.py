from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

'''
action chains = related to performing mouse and keyboard actions
hovering action
drag and drop action
we have to import it from common
'''

'''drag and drop'''
# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(3)
#
# action = ActionChains(driver)
# origin_ele = driver.find_element(By.ID, 'column-a')
# target_ele = driver.find_element(By.ID, 'column-b')
#
# action.drag_and_drop(origin_ele, target_ele).perform()
# # without .perform() actions won't take place so it is mandatory to use it
# sleep(5)

'''Mouse Hover'''
# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# action = ActionChains(driver)
#
# doggo = driver.find_element(By.XPATH, '(//span[contains(text(),"Dogs")])[1]')
# sleep(3)
# action.move_to_element(doggo).perform()
# sleep(5)

'''Scrolling to element'''
# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# action = ActionChains(driver)
#
# catto = driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
# action.scroll_to_element(catto).perform()
# sleep(5)
#
# action.scroll_by_amount(0,-1500).perform()
# sleep(5)
#
# action.scroll_by_amount(0, 1000).perform()
# sleep(5)

''' Mouse click '''
# click --> left click of mouse context_click --> right click of mouse
# double_click --> double click using mouse

'''Keyboard actions'''
# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# action = ActionChains(driver)
#
# # action.send_keys(Keys.PAGE_DOWN).perform()
# # sleep(5)
# # action.send_keys(Keys.PAGE_UP).perform()
# sleep(5)
#
# action.key_down(Keys.COMMAND).send_keys('a').perform()
# sleep(2)
# # key_down means pressing the key and key up means releasing the key
# action.key_up(Keys.COMMAND).perform()
# sleep(2)

'''copying and pasting for address fields'''
# driver = webdriver.Chrome()
# driver.get(r'file:///Users/dakshjain/PycharmProjects/23-03-2026/address_fields.html')
# driver.maximize_window()
# action = ActionChains(driver)
#
# present = driver.find_element(By.ID, 'presentAddress')
# permanent = driver.find_element(By.ID, 'permanentAddress')
#
# present.send_keys('JECRC, Jaipur, Raj.')
# sleep(2)
# present.click()
# action.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).perform()
# sleep(1)
# action.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND).perform()
# permanent.click()
# sleep(2)
# action.key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
# sleep(5)

'''Password Visibility'''
driver = webdriver.Chrome()
driver.get(r'file:///Users/dakshjain/PycharmProjects/23-03-2026/index1.html')
driver.maximize_window()
action = ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys('abcd')
sleep(3)
show_pwd = driver.find_element(By.ID, 'eyeBtn')
action.click_and_hold(show_pwd).perform()
sleep(3)
action.release()