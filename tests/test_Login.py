from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestSearch(BaseTest):

    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel("ExcelFiles/TestData.xlsx","LoginTest"))
    def test_login_with_valid_credentials(self,email_address,password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(email_address,password)
        assert account_page.display_status_of_edit_your_account_information_option()




