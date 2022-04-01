# Import the required modules
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Import Select class
from selenium.webdriver.support.ui import Select

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of website
url = "https://www.amazon.in/"
  
# Opening the website
driver.get(url)

# Find the object using the element id
select_element = driver.find_element_by_id('searchDropdownBox')
select_object = Select(select_element)

# Select the object usint the value 
select_object.select_by_value("search-alias=amazon-devices")
time.sleep(4)
driver.close()