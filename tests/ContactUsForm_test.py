import unittest
import pytest
import AppiumFrameWork.utilities.customLogger as cl
from AppiumFrameWork.pages.ContactUsFormPage import ContactForm

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=3)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=4)
    def test_enterDataForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAdress()
        self.cf.enterMobileNumber()
        self.cf.submitForm()
