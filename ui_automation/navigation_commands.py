import time
from utilities import *
from selenium import webdriver


d = create_driver()

get_page(d, "https://www.browserstack.com/guide/download-file-using-selenium-python")

time.sleep(10)
d.refresh()

time.sleep(10)

d.back()

time.sleep(10)
d.forward()

time.sleep(10)
d.quit()

