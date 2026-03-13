from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)

# find element by id
id1 = driver.find_element(By.ID, 'name')
print('id="name" found')
id2 = driver.find_element(By.ID, 'email')
print('id="email" found')
id3 = driver.find_element(By.ID, 'phone')
print('id="phone" found')
id4 = driver.find_element(By.ID, 'country')
print('id="country" found')
id5 = driver.find_element(By.ID, 'animals')
print('id="animals" found')

# find elements by name
name1 = driver.find_element(By.NAME, 'Navbar')
print('name="navbar" found')
name2 = driver.find_element(By.NAME, 'Cross-Column')
print('name="cross-column" found')
name3 = driver.find_element(By.NAME, 'Main')
print('name="main" found')
name4 = driver.find_elements(By.NAME, 'gender')
print('name="gender" found')
name5 = driver.find_elements(By.NAME, 'animals')
print('name="animals" found')


# find elements by class name
class1 = driver.find_elements(By.CLASS_NAME, 'title')
print('title class found')
print(len(class1))

class2 = driver.find_elements(By.CLASS_NAME, 'content')
print('content class found')
print(len(class2))

class3 = driver.find_elements(By.CLASS_NAME, 'form-control')
print('form-control class found')
print(len(class3))

class4 = driver.find_elements(By.CLASS_NAME, 'widget-content')
print('widget content class found')
print(len(class4))

class5 = driver.find_elements(By.CLASS_NAME, 'form-group')
print('form-group class found')
print(len(class5))

# find elements by tag name
inp = driver.find_elements(By.TAG_NAME, 'input')
print('input found')
print(f'no. of input tags: {len(inp)}')

h1 = driver.find_elements(By.TAG_NAME, 'h1')
print('h1 found')
print(f'no. of h1 tags: {len(h1)}')

script = driver.find_elements(By.TAG_NAME, 'script')
print('script found')
print(f'no. of script tags: {len(script)}')

option = driver.find_elements(By.TAG_NAME, 'option')
print('option found')
print(f'no. of option tags: {len(option)}')

title = driver.find_elements(By.TAG_NAME, 'title')
print('title found')
print(f'no. of title tags: {len(title)}')

driver.quit()