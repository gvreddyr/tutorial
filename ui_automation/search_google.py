import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()

d.get("https://www.google.com/")
d.maximize_window()
search_elem = d.find_element(By.NAME, 'q')
search_elem.send_keys("automation tutorial")
search_elem.send_keys(Keys.RETURN)
time.sleep(10)
d.quit()
