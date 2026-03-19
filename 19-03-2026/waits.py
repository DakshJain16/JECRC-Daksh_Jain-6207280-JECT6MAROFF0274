from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

'''
Drawbacks of Xpath- we can't find svg element. It will work with CSS selector

common always imports By, Keys and Actions. Rest we need to import with support
Sleep pauses the python execution, it is an unconditional wait.
using a lot of sleeps is bad for execution. that is why we use waits. 
Waits are used for resolving synchronization issues. Waits are of two types:-
1. implicit waits: 
-- waits until the element is found; find element in that certain period of time, if not found throws
element not found exception; it is a global wait i.e., it applies for all components of program.
Components of a program -> Python, Python Selenium, DOM, UI; Python is the fastest component
-- if the element is present in DOM but not appearing on screen then also implicit wait will work.
-- it takes only one condition, it should be found in the DOM structure, but if DOM has loaded, 
UI has not, it won't check UI part. So it won't care if a button is clickable/enabled or not.

syntax: driver.implicitly_wait(5) --> time in seconds, for minutes- convert to seconds

2. explicit waits:
-- waits for certain element until condition is satisfied
-- import 2 things webdriver wait and expected condition(has all expected conditions if clickable, visible etc)
-- check multiple conditions
-- check if visible ,is enabled we check these conditions
-- find element, wait for condition to be satisfied and give output
-- always confined to a particular element. It is not global like implicit wait

We should use only one type of wait, either implicit wait or explicit wait.
if we combine, the seconds with overlap and both time will combine.
'''

driver.get('https://abc.com/')
driver.maximize_window()

# driver.implicitly_wait(10)
#
# ele = driver.find_element(By.XPATH, '//a[@class="AnchorLink"]/parent::li/descendant::img[1]')
# print(ele.get_attribute('src'))

## example of explicit wait
wait_obj = WebDriverWait(driver, 10, poll_frequency=200)
submit_button = wait_obj.until(EC.element_to_be_clickable((By.ID, 'button')))
submit_button.click()
driver.quit()

