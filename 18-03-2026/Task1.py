from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# 1. Go to https://the-internet.herokuapp.com/
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

# 2. Find the "Checkboxes" link using LINK_TEXT
checkboxes = driver.find_element(By.LINK_TEXT, 'Checkboxes')
print("Element Found using LINK_TEXT!")
sleep(1)

# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
drag = driver.find_element(By.PARTIAL_LINK_TEXT, 'Drop')
print('Element Found using PARTIAL_LINK_TEXT!')
sleep(1)

# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME.
# Print the count.
li_tag = driver.find_elements(By.TAG_NAME, 'li')
print(f'Total no. of <li> elements: {len(li_tag)}')
sleep(1)

# 5. Navigate to https://the-internet.herokuapp.com/tables
driver.get('https://the-internet.herokuapp.com/tables')
driver.maximize_window()
sleep(2)

# 6.Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com"
# in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
website = driver.find_element(By.XPATH, '//table[@id="table1"]/descendant::td[text()="jdoe@hotmail.com"]/following-sibling::td[2]')
print(f'Website: {website.text}')
sleep(1)

# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
del_link = driver.find_element(By.XPATH, '//table[@id="table1"]/descendant::td[text()="Bach"]/following-sibling::td[5]/a[@href="#delete"]')
print('Delete Link Found!')
sleep(1)

# 8. Write an XPath to find the second table (<table>) on the page using indexing.
table = driver.find_element(By.XPATH, '//table[2]')
print('Second Table Found!')
sleep(1)

# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent element.
cell = driver.find_element(By.XPATH, '//table[@id="table2"]/descendant::tr[4]/td[4]')
print('Element $100.00 Found!')
parent = driver.find_element(By.XPATH, '//table[@id="table2"]/descendant::td[text()="$100.00"]/parent::tr')
print('Parent of $100.00 Found!')
sleep(1)

driver.quit()