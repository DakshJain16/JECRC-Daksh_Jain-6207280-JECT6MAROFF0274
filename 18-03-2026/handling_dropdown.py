from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window() #--> we use it so that elements do not overlap.
# sleep(2)
#
# country_dropdown = driver.find_element(By.ID, 'country')
# dropdown = Select(country_dropdown)
#
# # 1. select by value
# dropdown.select_by_value('australia')
# sleep(2)
#
# # 2. select by index --> here index starts from 0 unlike xpath where index starts with 1.
# dropdown.select_by_index(4)
# sleep(2)
#
# # 3. select by visible text
# dropdown.select_by_visible_text('Japan')
# sleep(5)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(3)

search = driver.find_element(By.ID, 'autocomplete-0-input')
search.clear()
search.send_keys('cat eye', Keys.ENTER)
sleep(2)

sort_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(sort_dropdown)

dropdown.select_by_value('high_price')
sleep(2)

print(driver.find_element(By.XPATH, '//div[@id="listing-wrapper"]/descendant::div[@data-cy="plpCardContainer"]/descendant::div[@class="sc-23b7d3eb-6 hYdmOJ"]/descendant::p[@data-cy="plpProductTitle"]').text)
driver.quit()