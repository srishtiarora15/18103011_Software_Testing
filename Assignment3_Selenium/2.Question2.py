#import the required modules
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from getpass import getpass

#to be displayed on the console for user input
user_name=input('Enter Email Id:')
password = getpass('Enter Password:') 

#chrome driver is used
driver = webdriver.Chrome(ChromeDriverManager().install())

#opening the website
driver.get('https://www.facebook.com/')
print ("Opened facebook")
sleep(1)

#automation of filling email_id
username_box = driver.find_element_by_id('email')
username_box.send_keys(user_name)
print ("Email Id entered")
sleep(1)

#automation of filling password
password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)
print ("Password entered")

#automation of login button
login_box = driver.find_element_by_name("login")
login_box.click()

#to be printed after the completion
print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")