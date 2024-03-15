from pages.base_page import Page
from selenium.webdriver.common.by import By

class ReelyProductPage(Page):
    def __init__(self, driver):
        self.driver = driver
        self.product_locator = (By.CSS_SELECTOR, '[w-el-text="Business Bay"]')

    PRODUCT_LOCATOR = (By.CSS_SELECTOR, '[w-el-text="Business Bay"]')

    def click_product(self):
        product = self.driver.find_element(*self.PRODUCT_LOCATOR)
        product.click()




