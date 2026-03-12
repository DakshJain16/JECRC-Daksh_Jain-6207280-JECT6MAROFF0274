from selenium import webdriver
'''
class that has configurations that you want to set the browser with before the browser opens.
'''

# Chrome
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
# driver.get('https://supertails.com/')
# driver.maximize_window()
# print(f'Title: {driver.title}') #---> prints title of website
# print(f'Current URL: {driver.current_url}') #---> prints the current url
# print(f'Browser Name: {driver.name}') #---> prints the browser name

# Edge
opts = webdriver.EdgeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Edge(options=opts)
driver.get('https://supertails.com/')
driver.maximize_window()
print(f'Title: {driver.title}') #---> prints title of website
print(f'Current URL: {driver.current_url}') #---> prints the current url
print(f'Browser Name: {driver.name}') #---> prints the browser name

# FireFox
# opts = webdriver.FirefoxOptions()
# opts.set_preference('detach', True)
# driver = webdriver.Firefox(options=opts)
# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# driver.close()