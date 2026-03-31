from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Complete Flow On Amazon
Steps:
Open website
Verify homepage title & URL
Search for product → "Headphones"
Apply filters (Brand,price(upto 500 or above 1000 anything))
Open a product → switch to new tab
Verify product details (title, price) using assert
Add to cart
Go to cart verify item (using assert with the name used earlier)
'''

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()

assert 'amazon' in driver.current_url, 'Error'
print('Valid!')

wait = WebDriverWait(driver, 10)

searchbox = wait.until(EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox')))
searchbox.send_keys('Headphones')

driver.find_element(By.ID, 'nav-search-submit-button').click()

wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@id="filter-p_123"]/descendant::li[3]'))).click()
sleep(10)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="priceRefinements"]/descendant::a[6]'))).click()
sleep(10)
new_product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="listitem"]/descendant::h2/span')))
product_title = new_product.text
new_product.click()

driver.switch_to.window(driver.window_handles[-1])

product_price = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//span[@class="a-price"]/span[@class="a-offscreen"]'))).text

assert product_title in wait.until(EC.presence_of_element_located(
    (By.ID, 'productTitle'))).text, 'Product not found'
print('Product found!')

assert product_price in wait.until(EC.presence_of_element_located(
    (By.XPATH, "//span[@class='a-price-whole']"))).text, 'Product not found'
print('Product found!')

cart_button = wait.until(EC.presence_of_element_located((By.ID, 'add-to-cart-button')))
cart_button.click()

cart = wait.until(EC.presence_of_element_located((By.ID, 'nav-cart')))
cart.click()

assert product_title in wait.until(EC.presence_of_element_located(
    (By.XPATH, '//span[@class="a-truncate-full a-offscreen"]'))).get_attribute('textContent'), 'Wrong Product'
print('Product present in cart!')

assert product_price in wait.until(EC.presence_of_element_located(
    (By.XPATH, '//span[@class="a-offscreen"]'))).text, 'Wrong product'
print('Correct Price!')

driver.quit()