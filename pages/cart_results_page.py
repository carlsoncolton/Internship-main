from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartResultsPage(Page):
    CART_RESULTS = (By.CSS_SELECTOR, "[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")

    def cart_results(self):
        actual_text = self.driver.find_element(*self.CART_RESULTS).text
        assert 'Your cart is empty' in actual_text, f'Expected cart is empty, got {actual_text}'
