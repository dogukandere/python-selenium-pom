from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

class PageBase:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(locator))
        return element

    def click(self, locator):
        element = self.wait_element_visibility(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_element_visibility(locator)
        element.send_keys(value)

    def is_displayed(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_displayed()

    def is_enabled(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_enabled()

    def is_selected(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_selected()

    def scroll_to_element(self, locator):
        element = self.wait_element_visibility(locator)
        ActionChains(self.driver).scroll_to_element(element).perform()

    def double_click(self, locator):
        element = self.wait_element_visibility(locator)
        ActionChains(self.driver).double_click(element).perform()

    def hover_over(self, locator):
        element = self.wait_element_visibility(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def click_and_hold(self, locator):
        element = self.wait_element_visibility(locator)
        ActionChains(self.driver).click_and_hold(element).perform()

    def get_text(self, locator):
        element = self.wait_element_visibility(locator)
        return element.text
