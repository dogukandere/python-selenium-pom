from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    POPUP_ELEMENT = (By.XPATH, "//*[@id='sp-cc-accept']")
    AMAZON_LOGO = (By.XPATH, "//a[@id='nav-logo-sprites']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='nav-line-2 ']")
    ORDER_BUTTON = (By.XPATH, "//span[contains(text(),'ve Siparişler')]")
    SEARCH_BOX_ELEMENT = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")

    def close_popup(self):
        self.click(self.POPUP_ELEMENT)

    def amazon_logo_control(self):
        return (self.is_displayed(self.AMAZON_LOGO))

    def is_login_button_displayed(self):
        return (self.is_displayed(self.LOGIN_BUTTON))

    def is_order_button_displayed(self):
        return (self.is_displayed(self.ORDER_BUTTON))

    def type_product(self, product):
        self.send_keys(self.SEARCH_BOX_ELEMENT, product)

    def search_product(self):
        self.click(self.SEARCH_BUTTON)

