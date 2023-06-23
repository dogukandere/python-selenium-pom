from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PageBase:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return element

    def click(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        element.click()

    def sendKeys(self, locator, value):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        element.send_keys(value)

    def isDisplayed(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return element.is_displayed()