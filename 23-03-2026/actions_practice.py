from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
driver = webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()

wait = WebDriverWait(driver, 10)
drag_ele = wait.until(EC.visibility_of_element_located((By.ID, 'draggable')))
drop_ele = wait.until(EC.visibility_of_element_located((By.ID, 'droppable')))

actions = ActionChains(driver)
sleep(2)
actions.drag_and_drop(drag_ele, drop_ele).perform()
sleep(5)

text = driver.find_element(By.XPATH, '//p[text()="Dropped!"]')
assert 'Dropped!' == text.text, 'Drop not working!'
print('Working Fine!')



