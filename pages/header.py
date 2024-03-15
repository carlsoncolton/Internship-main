from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def click_cart(self):
        self.click(*self.CART_ICON)
