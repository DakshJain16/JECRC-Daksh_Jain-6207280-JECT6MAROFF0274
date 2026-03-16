from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(2)

# 2. Get and print the title of the page.
print(f'Title: {driver.title}')

# 3. Locate the username input field and use clear() if needed.
username = driver.find_element(By.XPATH, '//input[@name = "username"]')
username.clear()

# 4. Enter the username using send_keys().
username.send_keys('Admin')
sleep(2)

# 5. Locate the password input field and enter the password using send_keys().
password = driver.find_element(By.XPATH, '//input[@name = "password"]')
password.send_keys('admin123')
sleep(2)

# 6. Submit the login form using either: click() on the Login button, or Keys.ENTER
submit = driver.find_element(By.XPATH, '//button[@type = "submit"]')
submit.click()
sleep(2)

# 7. After login, print the current URL.
print(f'Current URL: {driver.current_url}')
sleep(2)

# 8. Check if dashboard is present in that url using 'in'.
if "dashboard" in driver.current_url:
    # 9. Print 'successful login'
    print("Successful login!")

driver.quit()