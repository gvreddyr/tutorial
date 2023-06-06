import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

d = webdriver.Chrome()
d.get("https://www.dezlearn.com/webtable-example/")
d.maximize_window()


"""
table
    tbody
        td - header
        td - row 1
        td - row 2
        td - row 3
"""
table = d.find_elements(By.XPATH, "//table[@class='tg']/tbody/tr")
n = len(table)
for i in range(2,n+1):
    d.find_element(By.XPATH, "//table[@class='tg']/tbody/tr[%d]/td[3]/input"%i).click()

#
# ac = ActionChains(d)
# row_elem = WebDriverWait(d, 30).until(ec.presence_of_element_located((By.XPATH, "//table[@class='tg']/tbody/tr[4]/td[4]/input")))
# ac.scroll_to_element(row_elem)
# ac.perform()
# row_elem.click()
time.sleep(10)
d.quit()
