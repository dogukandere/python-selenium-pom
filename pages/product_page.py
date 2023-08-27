from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    TEXT_ELEMENT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    CARGO_BUTTON = (By.XPATH, "//li[@id='p_n_free_shipping_eligible/21345962031']//i[@class='a-icon a-icon-checkbox']")
    FIRST_PRODUCT = (By.XPATH, "//img[@alt='Apple 2020 MacBook Air Laptop: Apple M1 Çip, 13 inç Retina Ekran, 8 GB RAM, 256 GB SSD Depolama, Arkadan Aydınlatmalı Klav...']")

    def text_control(self):
        return self.get_text(self.TEXT_ELEMENT)

    def click_cargo_button(self):
        self.click(self.CARGO_BUTTON)

    def click_product(self):
        self.click(self.FIRST_PRODUCT)




