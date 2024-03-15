import time
from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")


@when('Search for {product}')
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()


@then('Search results for {product} are shown')
def search_for_product(context, product):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']").text
    assert product in actual_text, f'Expected {product} not in {actual_text}'




