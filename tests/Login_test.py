import unittest
import pytest
import AppiumFrameWork.utilities.customLogger as cl
from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_login_with_correct_credentials(self):
        cl.allureLogs("App Launched")
        self.lp.click_on_login_button()
        self.lp.enter_email()
        self.lp.enter_password()
        self.lp.click_on_submit_button()
        self.lp.enter_text()
        self.lp.click_on_submit_admin()

    @pytest.mark.run(order=2)
    def test_login_with_wrong_credentials(self):
        self.bp.keyCodes(4)
        self.lp.click_on_login_button()
        self.lp.enter_email()
        self.lp.enter_wrong_password()
        self.lp.wrong_credentials_is_displayed()
