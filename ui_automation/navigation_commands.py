import time

from selenium import webdriver


d = webdriver.Chrome()

d.get("https://www.browserstack.com/guide/download-file-using-selenium-python")
d.maximize_window()

time.sleep(10)
d.refresh()

time.sleep(10)

d.back()

time.sleep(10)
d.forward()

time.sleep(10)
d.quit()

