# from selenium import webdriver
# from base.utilities import get_config_data
from .utilities import get_config_data
# from selenium.webdriver.remote.webdriver import WebDriver
from common_imports import *

class Browser:
    @staticmethod
    def navigate_to_url(url:str = "") -> WebDriver:
        driver: WebDriver
        browser = get_config_data("browser")
        if isinstance(browser, dict | int):
            raise Exception("'browser' value in config.json file must be a string")
        match browser.strip().lower():
            case "chrome":
                driver = webdriver.Chrome()
            case "edge":
                driver = webdriver.Edge()
        resolution = get_config_data("screen_resolution")
        if isinstance(resolution, str | int):
            raise Exception("'screen_resolution' value in config.json must be a dictionary")
        driver.set_window_size(resolution["width"], resolution["height"])
        implicit = get_config_data("implicit_wait")
        if isinstance(implicit, str | dict):
            raise Exception("'implicit_wait' value in config.json file must be a number")
        driver.implicitly_wait(implicit)
        if url == "":
            url_config = get_config_data("url")
            if isinstance(url_config, dict | int):
                raise Exception("'url' value in config.json file must be a string")
            url = url_config
        driver.get(url)
        return driver

    @staticmethod
    def clean_up_browser(driver: WebDriver) -> None:
        driver.close()
        driver.quit()