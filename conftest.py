import os
import pytest

from Base.Browser import Browser
from Base.Utilities import get_config_data
from datetime import datetime
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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        pages = item.funcargs.get("pages")
        if pages:
            folder: str = "screenshots"
            os.makedirs(folder, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pages.driver.save_screenshot(os.path.join(folder, f"{item.name}_{timestamp}.png"))
            print(f"Sceenshot captured with timestamp {timestamp}")