from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
# opts.add_argument('headless') #---> browser runs in the background
driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(1)
'''find element by Id
if no element is present, it will generate an error
id > name > tag name > css selector > xpath '''
# name = driver.find_element(By.ID, 'name')
# # print(name)
# phone_no = driver.find_element(By.ID, 'phone')

'''find element by Name
if no element is present, it will generate an error'''
# nav_bar = driver.find_element(By.NAME, 'Navbar')

'''find elements by class name
if no elements are found, find_elements will return an empty list.'''
# radio_button = driver.find_elements(By.CLASS_NAME, 'form-check-input')
# print(radio_button)
# print(len(radio_button))
# print('radio button found')

'''Disadvantages of id, name, class
-- difficulty in finding unique elements.
-- sometimes in real-time applications, id and name attributes are not present'''

'''find elements by tag name'''
# inp = driver.find_elements(By.TAG_NAME, 'input')
# print(len(inp))

'''find elements by css selector
drawback:
1. can only traverse downwards. difficulty in finding unique elements. you have to travel the DOM tree to
get unique element
2. can't find inner text.
-- inner text--> <a _link_>HOME</a> here HOME is inner text'''
# 1. using tag name css selector--> tag_name[attribute="value"]
# animals = driver.find_element(By.CSS_SELECTOR, 'select[id="animals"]')
# print('working fine')

# link1 = driver.find_elements(By.CSS_SELECTOR, 'a[href*="testautomationpractice"]')
# print('working fine')
## * for substring present in between

# link2 = driver.find_elements(By.CSS_SELECTOR, 'a[href^="http://"]')
# print('working fine')
## ^ for substring present in starting

# link3 = driver.find_element(By.CSS_SELECTOR, 'a[href$=".com"]')
# print('working fine')
## $ for substring present in last

# 2. using id ---> #attribute_value
# animals = driver.find_element(By.CSS_SELECTOR, '#animals')
# print('working fine')

# 3. using class ---> .attribute_value
# content = driver.find_element(By.CSS_SELECTOR, '.content')
# print('working fine')

# 4. to find unique element tag1 tag2 tag3 ... tagn[attribute="value"]
#example ---> div input img[link*="abc"]

# 5. using two css selectors at a time
#example ---> input[type="text"][class="register"]

'''find elements by xpath
-- x in xpath ---> xml language
-- very powerful and efficient
-- can traverse anywhere(parent, child, sibling)
-- can find elements using inner text
-- slower than css selector
-- complex xpath; very difficult to understand and read
-- two types:- relative xpath, absolute xpath
absolute xpath example- /html/body/div/input[@id="name"]
relative xpath example- //input[@id="name"] 
    -- if multiple same tags are present(like multiple input tags the
    relative path will be (//input[@id="name"])[1] ---> using indexing'''

# path1 = driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
# print('working fine')
#
# path2 = driver.find_element(By.XPATH, '//button[@name="start"]')
# print('working fine')
#
# path3 = driver.find_element(By.XPATH, '//input[@id="txtDate"]')
# print('working fine')
#
# path4 = driver.find_element(By.XPATH, '//input[@placeholder="End Date"]')
# print('working fine')
#
# path5 = driver.find_element(By.XPATH, '//label[@for="monday"]')
# print('working fine')

# xpath for inner text
path6 = driver.find_element(By.XPATH, '//a[text()="GUI Elements"]')
print('working fine')

path7 = driver.find_element(By.XPATH, '//h2[text()="Tabs"]')
print('working fine')

path8 = driver.find_element(By.XPATH, '//label[text()="Wednesday"]')
print('working fine')

path9 = driver.find_element(By.XPATH, '(//button[text()="Submit"])[3]')
print('working fine')

path10 = driver.find_element(By.XPATH, '//option[contains(text(),"Blue")]')
print('working fine')
'''sometimes the text contains some extra spaces along eith text, but the text() method
is unable to identify it and displays error. so to handle that we use "contains" '''
driver.quit()