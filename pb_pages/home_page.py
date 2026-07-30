from base.selenium_base import SeleniumBase
from common_imports import *

class HomePage(SeleniumBase):
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    __username_textbox: tuple[str, str] = (By.XPATH, "//input[@name='username']")
    __password_textbox: tuple[str, str] = (By.XPATH, "//input[@type='password']")
    __login_button: tuple[str, str] = (By.XPATH, "//input[@value='Log In']")
    __welcome_text: tuple[str, str] = (By.XPATH, "//div[@id='leftPanel']/p")
    __logout_button: tuple[str, str] = (By.LINK_TEXT, "Log Out")
    __register_button: tuple[str, str] = (By.LINK_TEXT, "Register")

    def login(self, username: str, password: str):
        self.enter_text(self.__username_textbox, username, "Username", True)
        self.enter_text(self.__password_textbox, password, "Password", True)
        self.click(self.__login_button, "Login")

    def verify_successfull_login(self, name: str | None = None):
        text: str = self.get_text(self.__welcome_text, "Welcome Text")
        assert text.__contains__("Welcome"), f"'{text}' does not contains 'Welcome'"
        self.logger.info(f"Verified successfully. '{text}' contains 'Welcome'")
        if isinstance(name, str):
            assert text.__contains__(name), f"'{text}' does not contains '{name}'"
            self.logger.info(f"Verified successfully. '{text}' contains '{name}'")

    def logout(self):
        self.click(self.__logout_button, "Log Out")

    def verify_successfull_logout(self):
        assert self.is_element_displayed(self.__username_textbox), f"{self.__username_textbox} is not displayed"
        self.logger.info(f"Verified successfully. {self.__username_textbox} is displayed")

    def click_on_register(self):
        self.click(self.__register_button, "Register")