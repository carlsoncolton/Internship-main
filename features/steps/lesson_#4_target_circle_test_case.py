import time
from selenium.webdriver.common.by import By
from behave import given, when, then

BENEFIT_BOXES = (By.CSS_SELECTOR, '[class="styles__BenefitsGrid-sc-9mx6dj-1 gXrXKV"] li')

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get("https://www.target.com/circle")


@then('Verify there are 5 benefit boxes')
def verify_benefit_boxes(context):
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == 5, f'Expected 5 benefit boxes, got {len(benefit_boxes)}'
