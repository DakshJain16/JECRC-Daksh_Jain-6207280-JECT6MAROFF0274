from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Navigate to https://www.amazon.in/
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(1)

# 2. Locate the main search bar using its ID with a CSS Selector.
search = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
print('working fine')

# 3. Locate the Amazon logo (usually an <a> tag with an ID like nav-logo sprites) using a CSS Selector.
logo = driver.find_elements(By.CSS_SELECTOR, 'a[id="nav-logo-sprites"]')
print('working fine')

# 4. Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
cart = driver.find_elements(By.CSS_SELECTOR, 'a[id="nav-cart"]')
print('working fine')

# 5. Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
signin = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-tools"] div[id="nav-link-accountList"] a[href*="https://www.amazon.in/ap/signin?"]')
print('working fine')

# 6. Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
categories = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-xshop"] ul[class="nav-ul"] li[class="nav-li"] div[class="nav-div"] a[href*="nav_"]')
# categories = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-xshop"] a')
print(f'Total Categories: {len(categories)}')
print('working fine')
# Inspect their common parent and use descendant way and to find all the <a> tags within it.Use find_elements and print the count.
print('script completed!')
driver.quit()