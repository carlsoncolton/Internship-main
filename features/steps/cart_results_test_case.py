import time
from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
CART_RESULTS = (By.CSS_SELECTOR, "[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']")


@given("Open target main page")
def open_target_main(context):
    # context.driver.get("https://www.target.com/")
    context.app.main_page.open_main()


@when("Click on cart icon")
def click_on_cart_icon(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_cart()
    time.sleep(3)


@then("Verify cart empty icon is shown")
def verify_cart_empty(context):
    # actual_text = context.driver.find_element(*CART_RESULTS).text
    # assert 'Your cart is empty' in actual_text
    context.app.cart_results.cart_results()
    print('Test case passed')
