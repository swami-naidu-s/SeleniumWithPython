import pytest

from Base.Browser import Browser
from Base.Utilities import get_config_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

class Pages:
    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

@pytest.fixture
def pages():
    driver: WebDriver = Browser.navigate_to_url()
    wait: WebDriverWait = WebDriverWait(driver, get_config_data("explicit_wait"))
    yield Pages(driver, wait)
    Browser.clean_up_browser(driver)