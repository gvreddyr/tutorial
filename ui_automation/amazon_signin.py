import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utilities import *

d = create_driver()
get_page(d,"https://www.amazon.in/")

signin_panel = d.find_element(By.ID, "nav-link-accountList")

ac = ActionChains(d)
ac.move_to_element(signin_panel)
ac.perform()

signin_elem = d.find_element(By.ID, "nav-al-signin")
ac.click(signin_elem)
ac.perform()

time.sleep(10)

d.quit()