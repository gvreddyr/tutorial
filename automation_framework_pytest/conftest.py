import time
import pytest

from common.utilities import *


@pytest.fixture
def launch_google():
    driver = create_driver()
    get_page(driver, "https://www.google.com")

    yield driver

    # time.sleep(3)
    driver.quit()


@pytest.fixture
def input_value():
    in_put = 39
    return in_put
