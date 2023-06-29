import pytest
from pages.mainpage import MainPage
from pages.productpage import ProductPage

@pytest.mark.usefixtures("setup")
class TestMain:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.mainpage = MainPage(self.driver)
        self.productpage = ProductPage(self.driver)

    def test_search_product(self):
        self.driver.get("https://www.amazon.com.tr/ref=nav_logo")
        self.mainpage.close_popup()
        assert (self.mainpage.amazon_logo_control())
        assert (self.mainpage.is_login_button_displayed())
        assert (self.mainpage.is_order_button_displayed())
        self.mainpage.type_product("macbook")
        self.mainpage.search_product()

    def test_product_page(self):
        assert self.productpage.text_control() == '"macbook"'
        self.productpage.click_cargo_button()
        self.productpage.click_product()





