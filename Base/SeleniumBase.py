from logging import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class SeleniumBase:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    def wait_for_element_to_be_visible(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None):
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        wait = wait if isinstance(wait, WebDriverWait) else self.wait
        if isinstance(element, tuple[str, str]):
            wait.until(expected_conditions.visibility_of_element_located(*element))
        else:
            wait.until(expected_conditions.visibility_of(element))

    def wait_for_element_to_be_clickable(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None):
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        wait = wait if isinstance(wait, WebDriverWait) else self.wait
        wait.until(expected_conditions.element_to_be_clickable(element))

    def scroll_to_element(self, element: tuple[str, str] | WebElement):
        if isinstance(element, tuple[str, str]):
            element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)

    def enter_text(self, element: tuple[str, str] | WebElement, text: str, log_message: str, clear: bool = False, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            if isinstance(element, tuple[str, str]):
                element = self.driver.find_element(*element)
            if clear:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"{log_message} | Entered text {text} | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise f"Exception occured: {e}"

    def enter_text_js(self, element: tuple[str, str] | WebElement, text: str, log_message: str, clear: bool = False, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            if isinstance(element, tuple[str, str]):
                element = self.driver.find_element(*element)
            if clear:
                element.clear()
            self.driver.execute_script(f"arguments[0].value='{text}';", element)
            self.logger.info(f"{log_message} | Entered text {text} with js | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise f"Exception occured: {e}"

    def click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple[str, str]):
                element = self.driver.find_element(*element)
            element.click()
            self.logger.info(f"{log_message} | Clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise f"Exception occured: {e}"

    def click_js(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple[str, str]):
                element = self.driver.find_element(*element)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"{log_message} | Clicked on element with js | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise f"Exception occured: {e}"
        
    def double_click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple[str, str]):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).double_click().perform()
            self.logger.info(f"{log_message} | Double clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise f"Exception occured: {e}"