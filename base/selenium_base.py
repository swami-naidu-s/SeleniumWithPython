# from logging import Logger
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from common_imports import *

class SeleniumBase:
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    def wait_for_element_to_be_visible(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None):
        wait = None
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        wait = wait if isinstance(wait, WebDriverWait) else self.wait
        if isinstance(element, tuple):
            wait.until(expected_conditions.visibility_of_element_located(element))
        else:
            wait.until(expected_conditions.visibility_of(element))

    def wait_for_element_to_be_invisible(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None):
        wait = None
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        wait = wait if isinstance(wait, WebDriverWait) else self.wait
        if isinstance(element, tuple):
            wait.until(expected_conditions.invisibility_of_element_located(element))
        else:
            wait.until(expected_conditions.invisibility_of_element(element))

    def wait_for_element_to_be_clickable(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None):
        wait = None
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        wait = wait if isinstance(wait, WebDriverWait) else self.wait
        wait.until(expected_conditions.element_to_be_clickable(element))

    def scroll_to_element(self, element: tuple[str, str] | WebElement):
        if isinstance(element, tuple):
            element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \"center\"});", element)

    def enter_text(self, element: tuple[str, str] | WebElement, text: str, log_message: str, clear: bool = False, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            if clear:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"{log_message} | Entered text {text} | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")

    def enter_text_js(self, element: tuple[str, str] | WebElement, text: str, log_message: str, clear: bool = False, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            if clear:
                element.clear()
            self.driver.execute_script(f"arguments[0].value='{text}';", element)
            self.logger.info(f"{log_message} | Entered text {text} with js | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")

    def click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            element.click()
            self.logger.info(f"{log_message} | Clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")

    def click_js(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"{log_message} | Clicked on element with js | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def right_click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).context_click().perform()
            self.logger.info(f"{log_message} | Right clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def is_element_enabled(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None = None) -> bool:
        result: bool = False
        if isinstance(element, tuple):
            element = self.driver.find_element(*element)
        if isinstance(timeout_seconds, type(None)):
            result = element.is_enabled()
        else:
            while timeout_seconds > 0:
                result = element.is_enabled()
                if result:
                    break
                else:
                    sleep(1)
                    timeout_seconds -= 1
        return result
        
    def is_element_checked(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None = None) -> bool:
        result: bool = False
        if isinstance(element, tuple):
            element = self.driver.find_element(*element)
        if isinstance(timeout_seconds, type(None)):
            result = element.is_selected()
        else:
            while timeout_seconds > 0:
                result = element.is_selected()
                if result:
                    break
                else:
                    sleep(1)
                    timeout_seconds -= 1
        return result
        
    def is_element_displayed(self, element: tuple[str, str] | WebElement, timeout_seconds: int | None = None) -> bool:
        result: bool = False
        if isinstance(element, tuple):
            element = self.driver.find_element(*element)
        if isinstance(timeout_seconds, type(None)):
            result = element.is_displayed()
        else:
            while timeout_seconds > 0:
                result = element.is_displayed()
                if result:
                    break
                else:
                    sleep(1)
                    timeout_seconds -= 1
        return result
    
    def select_dropdown_by_text(self, element: tuple[str, str] | WebElement, text: str, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            Select(element).select_by_visible_text(text)
            self.logger.info(f"{log_message} | Selected {text} from dropdown | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def select_dropdown_by_value(self, element: tuple[str, str] | WebElement, value: str, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            Select(element).select_by_value(value)
            self.logger.info(f"{log_message} | Selected value {value} from dropdown | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def select_dropdown_by_index(self, element: tuple[str, str] | WebElement, index: int, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            Select(element).select_by_index(index)
            self.logger.info(f"{log_message} | Selected index {index} from dropdown | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def is_alert_present(self, timeout_seconds: int) -> bool:
        t: int = 0
        while True:
            try:
                self.driver.switch_to.alert
                return True
            except Exception as e:
                t += 1
                if t >= timeout_seconds:
                    return False
                sleep(1)
    
    def accept_alert(self, log_message: str, timeout_seconds: int | None = None):
        try:
            wait = None
            if isinstance(timeout_seconds, int):
                wait = WebDriverWait(self.driver, timeout_seconds)
            elif isinstance(timeout_seconds, type(None)):
                wait = self.wait
            alert = wait.until(expected_conditions.alert_is_present())
            self.logger.info(f"Alert Text: {alert.text}")
            alert.accept()
            self.logger.info(f"{log_message} | Accepted the alert")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
    
    def dismiss_alert(self, log_message: str, timeout_seconds: int | None = None):
        try:
            wait = None
            if isinstance(timeout_seconds, int):
                wait = WebDriverWait(self.driver, timeout_seconds)
            elif isinstance(timeout_seconds, type(None)):
                wait = self.wait
            alert = wait.until(expected_conditions.alert_is_present())
            self.logger.info(f"Alert Text: {alert.text}")
            alert.dismiss()
            self.logger.info(f"{log_message} | Dismissed the alert")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def get_alert_text(self, log_message: str, timeout_seconds: int | None = None) -> str:
        wait = None
        if isinstance(timeout_seconds, int):
            wait = WebDriverWait(self.driver, timeout_seconds)
        elif isinstance(timeout_seconds, type(None)):
            wait = self.wait
        alert = wait.until(expected_conditions.alert_is_present())
        text: str = alert.text
        self.logger.info(f"Alert Text: {text}")
        return text

    def get_attribute(self, element: tuple[str, str] | WebElement, attribute: str, log_message: str, timeout_seconds: int | None = None) -> str:
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            value = element.get_attribute(attribute)
            if isinstance(value, type(None)):
                value = ""
            self.logger.info(f"{log_message} | Retrieved attribute {attribute} value - {value} | {element}")
            return value
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")

    def get_text(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None) -> str:
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            value = element.text
            self.logger.info(f"{log_message} | Retrieved text value - {value} | {element}")
            return value
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def wait_for_page_load(self, timeout_seconds: int | None = None):
        try: 
            wait = None
            if isinstance(timeout_seconds, int):
                wait = WebDriverWait(self.driver, timeout_seconds)
            wait = wait if isinstance(wait, WebDriverWait) else self.wait
            wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")

    def double_click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).double_click().perform()
            self.logger.info(f"{log_message} | Double clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def click_and_hold(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).click_and_hold().perform()
            self.logger.info(f"{log_message} | Click and holded on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def drag_and_drop(self, source_element: tuple[str, str] | WebElement, destination_element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(source_element, timeout_seconds)
            self.wait_for_element_to_be_visible(destination_element, timeout_seconds)
            self.scroll_to_element(source_element)
            if isinstance(source_element, tuple):
                source_element = self.driver.find_element(*source_element)
            if isinstance(destination_element, tuple):
                destination_element = self.driver.find_element(*destination_element)
            ActionChains(self.driver).drag_and_drop(source_element, destination_element).perform()
            self.logger.info(f"{log_message} | Dragged and dropped | {source_element}, {destination_element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def press_tab(self, element: tuple[str, str] | WebElement | None = None, timeout_seconds: int | None = None):
        try:
            if isinstance(element, type(None)):
                ActionChains(self.driver).send_keys(Keys.TAB).perform()
            else:
                self.wait_for_element_to_be_visible(element, timeout_seconds)
                self.scroll_to_element(element)
                if isinstance(element, tuple):
                    element = self.driver.find_element(*element)
                element.send_keys(Keys.TAB)
            self.logger.info(f"Pressed Tab | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def hover(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info(f"{log_message} | Hovered on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")
        
    def hover_and_click(self, element: tuple[str, str] | WebElement, log_message: str, timeout_seconds: int | None = None):
        try:
            self.wait_for_element_to_be_visible(element, timeout_seconds)
            self.scroll_to_element(element)
            self.wait_for_element_to_be_clickable(element, timeout_seconds)
            if isinstance(element, tuple):
                element = self.driver.find_element(*element)
            ActionChains(self.driver).move_to_element(element).click().perform()
            self.logger.info(f"{log_message} | Hovered and Clicked on element | {element}")
        except Exception as e:
            self.logger.exception(e)
            raise Exception(f"Exception occurred: {e}")