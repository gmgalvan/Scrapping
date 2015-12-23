from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.fxcm.com/") 
driver.implicitly_wait(10)

while exit != 'x':
 container=driver.find_element_by_css_selector('#GBPUSD_bid > span')
 container2=driver.find_element_by_css_selector('#GBPUSD_ask > span')
 variable=float(container.text)
 variable2=float(container2.text)
 print"GBP/USD"
 print "Bid: ",variable
 print "Ask: ",variable2
 exit=raw_input('Type x for End... :')
 
driver.quit()

