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
        self.sendKeys(MainPage.SEARCH_AREA,value)
        time.sleep(2)

    def is_search_button_displayed(self):
        return (self.isDisplayed(MainPage.SEARCH_BUTTON))

    def click_search(self):
        self.click(MainPage.SEARCH_BUTTON)
