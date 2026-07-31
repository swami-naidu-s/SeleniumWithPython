# from base.utilities import *
# from ..base import generate_timestamp_without_space, generate_random_number, generate_random_upper_string
from base import generate_timestamp_without_space, generate_random_number, generate_random_upper_string

class TestSmoke:
    @staticmethod
    def test_login(pages):
        username: str = "User" + generate_timestamp_without_space()
        password: str = "JackSully420"
        # password: str = generate_random_string(12)
        labels: list[str] = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "SSN", "Username", "Password", "Confirm"]
        values: list[str] = ["Jack" + generate_random_number(3), "Sully", generate_random_upper_string(), generate_random_upper_string(4), generate_random_upper_string(), generate_random_number(5), generate_random_number(10), username, password, password]
        print(pages.driver.title)
        pages.home_page.click_on_register()
        pages.sign_up_page.enter_label_textbox(labels, values)
        pages.sign_up_page.click_register_button()
        pages.sign_up_page.verify_success_note(username)
        pages.home_page.logout()
        pages.home_page.verify_successfull_logout()
        
        pages.home_page.login(username, password)
        pages.home_page.verify_successfull_login()
        pages.home_page.logout()
        pages.home_page.verify_successfull_logout()