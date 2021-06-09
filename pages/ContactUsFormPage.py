from AppiumFrameWork.base.BasePage import BasePage
import AppiumFrameWork.utilities.customLogger as cl


class ContactForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _contactFormButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pageTitle = "Contact Us form"  # text
    _enterName = "com.code2lead.kwad:id/Et2"  # id
    _enterEmail = "com.code2lead.kwad:id/Et3"  # id
    _enterAdress = "com.code2lead.kwad:id/Et6"  # id
    _enterMobileNumber = "com.code2lead.kwad:id/Et7"  # id
    _submitButton = "com.code2lead.kwad:id/Btn2"  # id

    def clickContactFormButton(self):
        self.clickElement(self._contactFormButton, "id")
        cl.allureLogs("Clicked on Contact us Form Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, "text")
        assert element == True
        cl.allureLogs("Contact Us Form page opened")

    def enterName(self):
        self.sendText("Python", self._enterName, "id")
        cl.allureLogs("Entered Name")

    def enterEmail(self):
        self.sendText("email@python.com", self._enterEmail, "id")
        cl.allureLogs("Entered Email")

    def enterAdress(self):
        self.sendText("San Francisco", self._enterAdress, "id")
        cl.allureLogs("Entered Adress")

    def enterMobileNumber(self):
        self.sendText("+415 123 45 6789", self._enterMobileNumber, "id")
        cl.allureLogs("Entered Phone Number")

    def submitForm(self):
        self.clickElement(self._submitButton, "id")
        cl.allureLogs("Clicked on Submit button")
