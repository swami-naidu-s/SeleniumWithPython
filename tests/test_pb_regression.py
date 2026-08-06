from base import generate_timestamp_without_space, generate_random_number, generate_random_upper_string
from common_imports import pytest

@pytest.mark.regression
class TestRegression:
    @staticmethod
    def test_bill_pay(pages):
        username: str = "JS" + generate_timestamp_without_space()
        password: str = "JackSully420"
        signup_labels: list[str] = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "SSN", "Username", "Password", "Confirm"]
        signup_values: list[str] = ["Jack" + generate_random_number(3), "Sully", generate_random_upper_string(), generate_random_upper_string(4), generate_random_upper_string(), generate_random_number(5), generate_random_number(10), username, password, password]
        bill_labels: list[str] = ["Payee Name", "Address", "City", "State", "Zip Code", "Phone", "Account", "Verify Account", "Amount"]
        bill_values: list[str] = ["John Wick", "Alaska", "Alaska", "Alaska", generate_random_number(5), generate_random_number(10), "764837483", "764837483", "100"]
        bill_dropdown_label: str = "From account"

        pages.home_page.click_on_register()
        pages.sign_up_page.enter_label_textbox(signup_labels, signup_values)
        pages.sign_up_page.click_register_button()
        pages.sign_up_page.verify_success_note(username)

        pages.home_page.click_accounts_overview()
        account_number = pages.overview_page.get_primary_account_number()
        pages.home_page.click_bill_pay()
        pages.bill_pay_page.enter_label_textbox(bill_labels, bill_values)
        pages.bill_pay_page.select_label_dropdown(bill_dropdown_label, account_number)
        pages.bill_pay_page.click_send_payment()
        pages.bill_pay_page.verify_successfull_payment(bill_values[0])

        pages.home_page.logout()
        pages.home_page.verify_successfull_logout()