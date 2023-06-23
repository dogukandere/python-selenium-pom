from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.PageBase import PageBase


class MainPage(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_AREA = (By.XPATH, "//textarea[@id='APjFqb']")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='lJ9FBc']//input[@name='btnK']")

    def type_something(self, value):
        element = self.driver.find_element(*MainPage.SEARCH_AREA)
        element.send_keys(value)
        time.sleep(2)

    def click_search(self):
        # assert (MainPage.SEARCH_BUTTON.is_displayed())
        self.click(MainPage.SEARCH_BUTTON)
        #self.driver.find_element(*MainPage.SEARCH_BUTTON).click()
