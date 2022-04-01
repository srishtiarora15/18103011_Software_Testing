# Import required module
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

# Find object using the element id
select_element  = driver.find_element_by_id('searchDropdownBox')
select_object  = Select(select_element)

# Select by value
#store all the elements in the list
all_available_options = select_object.options
# for index in range(1, len(all_available_options) + 1):
#     print()

#printing all the elements in the list using for loop
for element in all_available_options:
    print(element.text)
    
print()

time.sleep(4)
driver.close()