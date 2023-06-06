import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

# URL
URL = "https://www.amazon.in/"

# XPATH
PRODUCT_XPATH = "(//span[@data-component-type='s-search-results']"\
                "//div[@data-component-type='s-search-result'])[%d]//h2/a"
GET_IT_TODAY = "//li[@aria-label='Get It by Tomorrow']//i"
TEN_PERCENT = "//span[text()='10% Off or more']"
SEARCH_BOX = "twotabsearchtextbox"
DROP_DOWN = "searchDropdownBox"
ADD_TO_CART = "add-to-cart-button"
CART_ELEM = "nav-cart-count-container"

# SEARCH STRINGS
DROP_DOWN_VALUE = "Electronics"
SEARCH_STRING = "Samsung TV"
PRODUCT_INDEX = 4

# Create a driver and get the page
d = webdriver.Chrome()
d.get(URL)
d.maximize_window()
d.implicitly_wait(3)

# select dropdown
drop_down_elem = d.find_element(By.ID, DROP_DOWN)
select_obj = Select(drop_down_elem)
select_obj.select_by_visible_text(DROP_DOWN_VALUE)

# search for a product
search_elem = d.find_element(By.ID, SEARCH_BOX)
search_elem.send_keys(SEARCH_STRING)
search_elem.send_keys(Keys.ENTER)

# filter the products
ac = ActionChains(d)
ten_percent_elem = WebDriverWait(d, 30).until(ec.presence_of_element_located((By.XPATH, TEN_PERCENT)))
ac.scroll_to_element(ten_percent_elem)
ac.click(ten_percent_elem)
ac.perform()

get_it_today_filter_elem = WebDriverWait(d, 10).until(ec.presence_of_element_located((By.XPATH, GET_IT_TODAY)))
get_it_today_filter_elem.click()


# click on the product
product_elem = WebDriverWait(d, 10).until(ec.presence_of_element_located((By.XPATH, PRODUCT_XPATH % PRODUCT_INDEX)))
product_elem.click()

# switch to window
main_window = d.current_window_handle
if WebDriverWait(d, 10).until(ec.number_of_windows_to_be(2)):
    window_handles = d.window_handles
    d.switch_to.window(window_handles[1])

# add to cart
add_to_cart_elem = d.find_element(By.ID, ADD_TO_CART)
add_to_cart_elem.click()

# go to cart
cart_elem = d.find_element(By.ID, CART_ELEM)
ac.double_click(cart_elem)
ac.perform()

# switch to main window
#d.switch_to.window(main_window)

# quit browser
time.sleep(10)
d.quit()
