# import allure
# import os
# import pytest

# from base.browser import Browser
# from base.utilities import get_config_data, get_logger
from base import Browser, get_logger, get_config_data
# from datetime import datetime
# from logging import Logger
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webdriver import WebDriver
from common_imports import *
from pb_pages import *

class Pages:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger
        self.home_page = HomePage(driver, wait, logger)
        self.sign_up_page = SignUpPage(driver, wait, logger)

@pytest.fixture
def pages(request):
    testcase_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    request.node.timestamp = timestamp
    logger: Logger = get_logger(testcase_name, timestamp)
    logger.info("Testcase started successfully")
    driver: WebDriver = Browser.navigate_to_url()
    wait: WebDriverWait = WebDriverWait(driver, get_config_data("explicit_wait"))
    yield Pages(driver, wait, logger)
    Browser.clean_up_browser(driver)
    logger.info("Testcase execution completed")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        pages = item.funcargs.get("pages")
        if pages:
            # timestamp = getattr(item, "timestamp", None)
            timestamp = item.timestamp
            folder: str = os.path.join("TestResults", f"{timestamp}_{item.name}")
            pages.logger.error("Testcase Failed.")
            os.makedirs(folder, exist_ok=True)
            # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # screenshot_path = os.path.join(folder, f"{item.name}_{timestamp}.png")
            screenshot_path = os.path.join(folder, f"{item.name}.png")
            pages.driver.save_screenshot(screenshot_path)
            # print(f"Sceenshot captured with timestamp {timestamp}")
            print(f"Sceenshot captured")
            pages.logger.info("Screenshot captured")
            # Add logs as testcase failed
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )