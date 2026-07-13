from logging import Logger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class SeleniumBase:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger