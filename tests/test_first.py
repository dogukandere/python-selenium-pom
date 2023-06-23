import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.mainpage import MainPage


@pytest.mark.usefixtures("setup")
class TestMainPage:

    def test_first(self):

        mainpage = MainPage(self.driver)

        self.driver.get("https://www.google.com/webhp?hl=tr&sa=X&ved=0ahUKEwim8rDz-tn_AhV_QvEDHflvDNYQPAgJ")

        mainpage.type_something("youtube")
        mainpage.click_search()




