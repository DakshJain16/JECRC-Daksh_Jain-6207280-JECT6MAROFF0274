from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

'''
<html>
  <iframe>
      <html>
      </html>
  </iframe>
</html>

using driver.switchTo we switch to the inner html
when html is nested with the help of iframes tag, it is an iframe but when there is 
no separate tag it may be part of shadow DOM
'''

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(2)


#single iframe
# iframe = driver.find_element(By.ID,'singleframe')
# driver.switch_to.frame(iframe) #we write windows in place of iframe when switching between windows
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123') #won't work without switching
# sleep(2)

# nested iframe
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
sleep(2)
nested_iframe = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)
sleep(2)

inner_iframe = driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(2)

driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123') #won't work without switching

#driver.switch to default
#driver.switch to parent

driver.switch_to.parent_frame()
driver.switch_to.default_content()