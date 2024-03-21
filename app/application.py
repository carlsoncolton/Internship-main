from pages.base_page import Page
from pages.header import Header
from pages.login_in_page import LoginPage
from pages.main_page import MainPage
from pages.cart_results_page import CartResultsPage
from pages.reely_product_page import ReelyProductPage
from pages.side_bar import SideBar
from pages.verify_product_page import ProductVerificationPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.cart_results = CartResultsPage(self.driver)
        self.login_in_page = LoginPage(self.driver)
        self.side_bar = SideBar(self.driver)
        self.reely_product_page = ReelyProductPage(self.driver)
        self.verify_product_page = ProductVerificationPage(self.driver)
        self.base_page = Page(self.driver)

