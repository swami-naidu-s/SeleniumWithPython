from base import SeleniumBase
from common_imports import *

class AccountsOverviewPage(SeleniumBase):
    def __init__(self, driver: WebDriver, wait: WebDriverWait, logger: Logger):
        self.driver = driver
        self.wait = wait
        self.logger = logger

    __accounts: tuple[str, str] = (By.XPATH, "//table[@id='accountTable']//td/a")
    __primary_account: tuple[str, str] = (By.XPATH, "//table[@id='accountTable']//td[1]/a")

    def get_primary_account_number(self) -> str:
        return self.get_text(self.__primary_account, "Primary Account")