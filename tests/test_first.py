import pytest
from pages.mainpage import MainPage
from pages.productpage import ProductPage

@pytest.mark.usefixtures("setup")
class TestMain:

    def test_search_product(self):
        mainpage = MainPage(self.driver)

        self.driver.get("https://www.amazon.com.tr/ref=nav_logo")
        mainpage.close_popup()
        assert (mainpage.amazon_logo_control())
        assert (mainpage.is_displayed_login_button())
        assert (mainpage.is_displayed_order_button())
        mainpage.type_product("macbook")
        mainpage.search_product()

    def test_product_page(self):
        productpage = ProductPage(self.driver)

        assert productpage.text_control() == '"macbook"'
        productpage.click_cargo_button()
        productpage.click_product()





