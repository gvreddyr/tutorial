import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

from utilities import *

# URL
URL = "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver"
#create driver
d = create_driver()
# get the page
get_page(d, URL)

# get alert
d.find_element(By.NAME, "prompt").click()

# handle alert
a = Alert(d)
a.send_keys(Keys.ESCAPE)
time.sleep(10)

if a.text == 'I am prompt':
    print("I'm accepting")
    a.accept()
else:
    print("I'm dismissing")
    a.dismiss()

# quit browser
time.sleep(10)
d.quit()