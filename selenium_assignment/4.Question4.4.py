# Import required module
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Import Select class
from selenium.webdriver.support.ui import Select

# Using chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# URL of website
url = "https://pythonbasics.org/"
  
# Opening the website
driver.get(url)

#to execute the javaScript to scroll from the start to end of the page
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")

time.sleep(4)
driver.close()