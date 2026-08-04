from base import SeleniumBase
from common_imports import *

class SignUpPage(SeleniumBase):
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    __label_textbox = lambda self, label: (By.XPATH, f"//td[contains(.,'{label}')]/following-sibling::td/input")
    __register_button: tuple[str, str] = (By.XPATH, "//input[@value='Register']")
    __title: tuple[str, str] = (By.XPATH, "//h1[@class='title']")
    __success_note: tuple[str, str] = (By.XPATH, "//div[@id='rightPanel']/p")

    def enter_label_textbox(self, label_name: str | list[str], text: str | list[str]):
        if isinstance(label_name, str) and isinstance(text, str):
            self.enter_text(self.__label_textbox(label_name), text, label_name)
        elif isinstance(label_name, list) and isinstance(text, list):
            for label, value in zip(label_name, text, strict=True):
                self.enter_text(self.__label_textbox(label), value, label)
        else:
            raise Exception(f"Mismatch in datatypes of 'label_name' and 'text' variables. Both must be 'str' or 'list'")

    def click_register_button(self):
        self.click_js(self.__register_button, "Register button", 1)

    def verify_success_note(self, user: str):
        welcome_text: str = self.get_text(self.__title, "Register user title")
        assert welcome_text.__contains__(user), f"'{welcome_text}' does not contains username '{user}'"
        self.logger.info(f"{welcome_text} verified successfully")
        success_note: str = self.get_text(self.__success_note, "Register success note")
        assert success_note.__contains__("successfully"), f"'{success_note}' does not contains 'successfully' text"
        self.logger.info(f"Success note '{success_note}' verified successfully")