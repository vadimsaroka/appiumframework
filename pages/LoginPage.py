from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.customLogger as cl


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _login_page = "com.code2lead.kwad:id/Login"  # id
    _enter_email = "com.code2lead.kwad:id/Et4"  # id
    _enter_password = "com.code2lead.kwad:id/Et5"  # id
    _submit_form = "com.code2lead.kwad:id/Btn3"  # id
    _wrong_credentials = "com.code2lead.kwad:id/Tv8"  # id
    _enter_admin = "com.code2lead.kwad:id/Edt_admin"  # id
    _submit_admin = "com.code2lead.kwad:id/Btn_admin_sub"  # id

    def click_on_login_button(self):
        self.clickElement(self._login_page, "id")
        cl.allureLogs("Click on Login Button")

    def enter_email(self):
        self.sendText("admin@gmail.com", self._enter_email, "id")
        cl.allureLogs("Entered email id")

    def enter_password(self):
        self.sendText("admin123", self._enter_password, "id")
        cl.allureLogs("Entered password")

    def enter_wrong_password(self):
        self.sendText("admin", self._enter_password, "id")
        cl.allureLogs("Entered password")

    def click_on_submit_button(self):
        self.clickElement(self._submit_form, "id")
        cl.allureLogs("Clicked Submit button")

    def enter_text(self):
        self.sendText("Appium", self._enter_admin, "id")
        cl.allureLogs("Entered text")

    def click_on_submit_admin(self):
        self.clickElement(self._submit_admin, "id")
        cl.allureLogs("Submit button is clicked")

    def wrong_credentials_is_displayed(self):
        alert = self.isDisplayed(self._wrong_credentials)
        assert alert == True
        cl.allureLogs("Wrong credentials is displayed")

