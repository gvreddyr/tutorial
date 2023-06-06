import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()
d.get("https://www.techlistic.com/p/selenium-practice-form.html")
d.maximize_window()
drop_down_elem = d.find_element(By.ID, "continents")
select_obj = Select(drop_down_elem)
select_obj.select_by_index(3)
time.sleep(10)
d.quit()
