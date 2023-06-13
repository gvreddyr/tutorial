import time
from utilities import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = create_driver()
get_page(d,"https://www.techlistic.com/p/selenium-practice-form.html")

f_name_elem = d.find_element(By.NAME, "firstname")
f_name_elem.send_keys("Rama")
s_name_elem = d.find_element(By.NAME, "lastname")
s_name_elem.send_keys("Laxmi")
s_elem = d.find_element(By.ID, "sex-1")
s_elem.click()
time.sleep(10)
d.quit()
