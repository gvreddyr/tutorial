from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get("https://www.google.com")
d.maximize_window()

d.save_screenshot("../screenshots/google.png")
d.quit()