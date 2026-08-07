from base import SeleniumBase
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
    __open_new_account_button: tuple[str, str] = (By.LINK_TEXT, "Open New Account")
    __accounts_overview_button: tuple[str, str] = (By.LINK_TEXT, "Accounts Overview")
    __transfer_funds_button: tuple[str, str] = (By.LINK_TEXT, "Transfer Funds")
    __bill_pay_button: tuple[str, str] = (By.LINK_TEXT, "Bill Pay")
    __find_transactions_button: tuple[str, str] = (By.LINK_TEXT, "Find Transactions")
    __update_contact_info_button: tuple[str, str] = (By.LINK_TEXT, "Update Contact Info")
    __request_loan_button: tuple[str, str] = (By.LINK_TEXT, "Request Loan")

    def login(self, username: str, password: str):
        self.enter_text(self.__username_textbox, username, "Username", True)
        self.enter_text(self.__password_textbox, password, "Password", True)
        self.click(self.__login_button, "Login")

    def verify_successfull_login(self, name: str | None = None):
        text: str = self.get_text(self.__welcome_text, "Welcome Text")
        self.verification(text.__contains__("Welcome"), f"'{text}' contains 'Welcome'", f"'{text}' does not contains 'Welcome'")
        if isinstance(name, str):
            self.verification(text.__contains__(name), f"'{text}' contains '{name}'", f"'{text}' does not contains '{name}'")

    def logout(self):
        self.click(self.__logout_button, "Log Out")

    def verify_successfull_logout(self):
        self.verification(self.is_element_displayed(self.__username_textbox), f"{self.__username_textbox} is displayed", f"{self.__username_textbox} is not displayed")

    def click_on_register(self):
        self.click(self.__register_button, "Register")

    def click_open_new_account(self):
        self.click(self.__open_new_account_button, "Open New Account")

    def click_accounts_overview(self):
        self.click(self.__accounts_overview_button, "Accounts Overview")

    def click_transfer_funds(self):
        self.click(self.__transfer_funds_button, "Transfer Funds")

    def click_bill_pay(self):
        self.click(self.__bill_pay_button, "Bill Pay")

    def click_find_transactions(self):
        self.click(self.__find_transactions_button, "Find Transactions")

    def click_update_contact_info(self):
        self.click(self.__update_contact_info_button, "Update Contact Info")

    def click_request_loan(self):
        self.click(self.__request_loan_button, "Request Loan")