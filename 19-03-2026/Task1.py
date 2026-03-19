from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')

wait = WebDriverWait(driver, 10)

img_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//section[@class="tilegroup tilegroup--homehero tilegroup--landscape"]/descendant::picture/descendant::img')))
for img in img_links:
    print(img.get_attribute('src'))

driver.quit()