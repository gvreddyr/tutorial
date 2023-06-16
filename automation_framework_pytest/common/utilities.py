from selenium import webdriver
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
browser = config.get('drivers', 'browser')
timeout = config.get('drivers', 'timeout')


def create_driver():
    if browser == 'chrome':
        return webdriver.Chrome()
    if browser == 'firefox':
        return webdriver.Firefox()
    if browser == 'safari':
        return webdriver.Safari()

    return None


def get_page(driver, url):
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(timeout)


