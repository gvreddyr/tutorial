import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
1. Launch browser
2. Open Google website
3. Enter search string
4. Verify if search results are matching to the entered search string
'''


class TestGoogleSearch:

    @pytest.mark.ui
    @pytest.mark.google
    @pytest.mark.parametrize("search_string", ["automation tutorial", "pytest tutorial"])
    def test_google_search(self, launch_google, search_string):
        driver = launch_google
        search_elem = driver.find_element(By.NAME, 'q')
        search_elem.send_keys(search_string)
        search_elem.send_keys(Keys.RETURN)
        assert search_string in driver.title, "Could not find the search results"

