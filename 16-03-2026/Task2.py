from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Open the radio button page.
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
sleep(2)

# 2. Print the title of the page.
print(f'Title: {driver.title}')

# 3. Locate the "Yes" radio button.
yes_button = driver.find_element(By.XPATH, '//input[@id="yesRadio"]')

# 4. Click the radio button using click().
yes_button.click()
sleep(2)

# 5. Capture and print the result message using .text.
result = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
print(f'Result Message: {result.text}')
sleep(2)

# 6. Use get_attribute() to fetch attributes like class and id
print(f'Radio Button Class: {yes_button.get_attribute("class")}')
print(f'Radio Button ID: {yes_button.get_attribute("id")}')

# 7. Print the current URL.
print(f'Current URL: {driver.current_url}')

driver.quit()