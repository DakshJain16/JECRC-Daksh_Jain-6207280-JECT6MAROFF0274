from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Task 3
1. navigate to amazon
2. search a product through send_keys
BUT dont click on search or keys.enter
3. Wait for the suggestions to appear
4. Click on 4th suggestion
5. Click on Sort By and click on newest
6. Click on free shipping check box
7. wait for first product and return me the name=price
(without using inner text)
'''

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. navigate to amazon
driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 2. search a product through send_keys BUT don't click on search or keys.enter
search = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]')))
search.clear()
search.send_keys('crocs')

# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
suggestion = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.s-suggestion')))
suggestion[3].click()

# 5. Click on Sort By and click on newest
sort = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Sort")]')))
sort.click()

new = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Newest")]')))
new.click()

# 6. Click on free shipping check box
free_ship = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='p_n_free_shipping_eligible/205563695031']/descendant::div[@class='a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left']")))
free_ship.click()

# 7. wait for first product and return me the name=price (without using inner text)
first_prod = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-component-type="s-search-result"][1]')))

name = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/descendant::span')))
print(name.text)

price = wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="sg-col-inner"])[5]/descendant::div[@data-cy="price-recipe"]/div/div/a/span')))
print(price.text)

print(name.text, ' = ', price.text)
driver.quit()