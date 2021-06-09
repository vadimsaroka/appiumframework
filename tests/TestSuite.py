import unittest
from AppiumFrameWork.tests.Login_test import LoginTest
from AppiumFrameWork.tests.ContactUsForm_test import ContactFormTest

lf = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

regressionTest = unittest.TestSuite((lf, cf))

unittest.TextTestRunner(verbosity=1).run(regressionTest)
