from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Go to: https://demoqa.com/automation-practice-form
driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(2)

# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`

first_name = driver.find_element(By.ID, 'firstName')
first_name.clear()
first_name.send_keys('Ankit')
sleep(1)

last_name = driver.find_element(By.ID, 'lastName')
last_name.clear()
last_name.send_keys('Sharma')
sleep(1)

email = driver.find_element(By.ID, 'userEmail')
email.clear()
email.send_keys('ankitsharma123@gmail.com')
sleep(1)

gender = driver.find_element(By.XPATH, '//input[@value="Male"]')
gender.click()
sleep(1)

mobile = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
mobile.clear()
mobile.send_keys('9876547890')
sleep(1)

subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
subjects.clear()
subjects.send_keys('Maths')
subjects.send_keys(Keys.ENTER)
sleep(1)
subjects.send_keys('English')
subjects.send_keys(Keys.ENTER)
sleep(1)
subjects.send_keys('Physics')
subjects.send_keys(Keys.ENTER)
sleep(2)

hobby1 = driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-1"]/following-sibling::label')
hobby1.click()
sleep(1)
hobby2 = driver.find_element(By.XPATH, '//input[@id="hobbies-checkbox-2"]/following-sibling::label')
hobby2.click()
sleep(1)

choose_file = driver.find_element(By.ID, 'uploadPicture')
choose_file.send_keys('/Users/dakshjain/Desktop/Screenshot 2026-03-18 at 22.01.07.png')
sleep(2)

address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
address.clear()
address.send_keys('Baskin Robins, High Street, Jagatpura')
sleep(1)

state = driver.find_element(By.ID, 'react-select-3-input')
state.send_keys("Rajasthan", Keys.ENTER)
sleep(1)

state = driver.find_element(By.ID, 'react-select-4-input')
state.send_keys("Jaipur", Keys.ENTER)
sleep(1)

# 3. Click on submit button
submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
submit.click()
sleep(2)

driver.quit()