from base import SeleniumBase
from common_imports import *

class BillPayPage(SeleniumBase):
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    __label_textbox = lambda self, label: (By.XPATH, f"//td[starts-with(.,'{label}')]/following-sibling::td/input")
    __label_dropdown = lambda self, label: (By.XPATH, f"//td[starts-with(.,'{label}')]/following-sibling::td/select")
    __send_payment_button: tuple[str, str] = (By.XPATH, f"//input[@value='Send Payment']")

    def enter_label_textbox(self, label_name: str | list[str], text: str | list[str]):
        if isinstance(label_name, str) and isinstance(text, str):
            self.enter_text(self.__label_textbox(label_name), text, label_name)
        elif isinstance(label_name, list) and isinstance(text, list):
            for label, value in zip(label_name, text, strict=True):
                self.enter_text(self.__label_textbox(label), value, label)
        else:
            raise Exception(f"Mismatch in datatypes of 'label_name' and 'text' variables. Both must be 'str' or 'list'")

    def select_label_dropdown(self, label_name: str | list[str], text: str | list[str]):
        if isinstance(label_name, str) and isinstance(text, str):
            self.select_dropdown_by_text(self.__label_dropdown(label_name), text, label_name)
        elif isinstance(label_name, list) and isinstance(text, list):
            for label, value in zip(label_name, text, strict=True):
                self.select_dropdown_by_text(self.__label_textbox(label), value, label)
        else:
            raise Exception(f"Mismatch in datatypes of 'label_name' and 'text' variables. Both must be 'str' or 'list'")

    def click_send_payment(self):
        self.click(self.__send_payment_button, "Send Payment", 2)
        sleep(4)