# from selenium import webdriver
from base.utilities import get_config_data
# from selenium.webdriver.remote.webdriver import WebDriver
from common_imports import *

class Browser:
    def navigate_to_url(url:str = "") -> WebDriver:
        driver: WebDriver
        match get_config_data("browser").strip().lower():
            case "chrome":
                driver = webdriver.Chrome()
            case "edge":
                driver = webdriver.Edge()
        driver.set_window_size(get_config_data("screen_resolution")["width"], get_config_data("screen_resolution")["height"])
        driver.implicitly_wait(get_config_data("implicit_wait"))
        if url == "":
            driver.get(get_config_data("url"))
        else:
            driver.get(url)
        return driver
    
    def clean_up_browser(driver: WebDriver) -> None:
        driver.close()
        driver.quit()