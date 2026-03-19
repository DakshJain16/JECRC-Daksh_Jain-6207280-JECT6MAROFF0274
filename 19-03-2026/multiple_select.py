from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demo.mobiscroll.com/select/multiple-select')
driver.maximize_window()

multi_drop = driver.find_element(By.XPATH, '//select[@id="multiple-select-select"]')
select = Select(multi_drop)

if select.is_multiple():  #---> is_multiple() returns true if element is multi-select, else false
    select.select_by_value('8')
    select.select_by_index(6)
    select.select_by_visible_text('Movies, Music & Games')

sleep(5)
select.deselect_by_index(6)  #---> deselect the option
select.deselect_all() #--->deselect all the options
print(select.first_selected_option)  #---> prints the first selected option
print(select.all_selected_options)  #---> prints all selected options
driver.quit()