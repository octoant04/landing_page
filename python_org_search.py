from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application"
#chrome_driver_binary = "C:/Program Files (x86)/Google/chromedriver"

s = Service('C:/Program Files (x86)/Google/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()