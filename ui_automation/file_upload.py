from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import *

d = create_driver()
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/Users/govardhan/Downloads"}
options.add_experimental_option("prefs", prefs)

get_page(d, "https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

# file upload
file_btn = d.find_element(By.NAME, 'upload')
file_btn.send_keys("/Users/govardhan/Downloads/selenium suite.png")

# find download
file_download_btn = d.find_element(By.NAME, 'download')
file_download_btn.click()

d.quit()