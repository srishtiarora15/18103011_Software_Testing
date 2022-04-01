from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm"

#opening the url
driver.get(url)

# identify dropdown with Select class
select_element = Select(driver.find_element_by_xpath("//select[@name='continents']"))

#select by select_by_visible_text() method
time.sleep(5)
select_element.select_by_visible_text("Africa")
time.sleep(5)

#select by select_by_index() method
select_element.select_by_index(0)
time.sleep(5)
driver.close()