import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

d = webdriver.Chrome()

d.get("https://www.amazon.in/")
d.maximize_window()

signin_panel = d.find_element(By.ID, "nav-link-accountList")

ac = ActionChains(d)
ac.move_to_element(signin_panel)
ac.perform()

signin_elem = d.find_element(By.ID, "nav-al-signin")
ac.click(signin_elem)
ac.perform()

time.sleep(10)

d.quit()