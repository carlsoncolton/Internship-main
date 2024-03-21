import time
from selenium.webdriver.common.by import By
from behave import given, when, then


@when("Click on sign in")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
    time.sleep(3)


@then("From right side navigation menu, click sign in")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='styles__ListItemText-sc-diphzn-1 jaMNVl']").click()


@then("Verify sign in form opened")
def verify_sign_in(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
    assert "Sign into your Target account" in actual_text
    print("Test case passed")
