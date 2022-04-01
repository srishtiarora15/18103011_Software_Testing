# Here Chrome  will be used
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
  
  # URL of website
url = "https://www.samsung.com/in/"
  
# Opening the website
driver.get(url)
  
# Getting current URL source code
get_title = driver.title
  
# Printing the title of this URL
print(get_title)