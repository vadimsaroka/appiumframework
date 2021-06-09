import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFrameWork.utilities.customLogger as cl


class BasePage:
    log = cl.customLogger()
    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotSelectableException,
            NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorValue))
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorValue))
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_andriod_uiautomator('UiSelector().description("%s")' % locatorValue))
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().index(%d)' % int(locatorValue)))
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorValue))
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath("%s" % locatorValue))
        else:
            self.log.info(f"Locator value '{locatorValue}' not found")
        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info(f"Element found with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")
        except:
            self.log.info(f"Element not found with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(f"Clicked on element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")
        except:
            self.log.info(f"Unable to click on element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(f"Send text on element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")
        except:
            self.log.info(f"Unable to send text on element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}'")
            self.takeScreenShot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(f"Element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}' is displayed")
            return True
        except:
            self.log.info(f"Element with LocatorType: '{locatorType}' and locatorValue: '{locatorValue}' is not displayed")
            self.takeScreenShot(locatorType)
            return False

    def screenShots(self, screenshotName):
        filename = screenshotName + "_" + (time.strftime("%m_%d_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshootPath = screenshotDirectory + filename

        try:
            self.driver.save_screenshot(screenshootPath)
            self.log.info("Screenshot save to Path: " + screenshootPath)
        except:
            self.log.info("Unable to save Screenshot to Path: " + screenshootPath)

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCodes(self, value):
        self.driver.press_keycode(value)
