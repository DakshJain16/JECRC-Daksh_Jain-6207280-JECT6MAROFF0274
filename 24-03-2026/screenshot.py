import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

'''
We import os when trying to take screenshot to keep the screenshots in the same 
location/destination/path/folder.
os is a module that is used to create directories and set a path
'''
folder = os.path.join(os.getcwd(),'screenshots')
#foldername(joins screenshots to current working directory)+directory you want (here, current working directory)

os.makedirs(folder,exist_ok=True)
'''
checks if that directory is already present and if not then it will create a new one
if directory is already present then it will continue with the script
if we don't use exist_ok=True then an exception error is thrown if the directory already exists
'''

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
action=ActionChains(driver)

driver.save_screenshot(f'{folder}/pinterest_full_page.png')
sleep(3)
'''
save_screenshot --> takes screenshot of the whole page
element_screenshot --> find the screenshot and save in object element then take a screenshot 
of the element. 
For both, if the name is same then the image will get replaced

save_screenshot({folder}/{file name}) --> saves page in .png extension
'''

ele = driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
#path could also have been '//img[contains(@alt,"Photo of a woman in a cherry-patterned")]
action.scroll_to_element(ele).perform()
sleep(3)
ele.screenshot(f'{folder}/pinterest_element.png')

#windows+v takes you to a list of all items copied to clipboard