import time
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('Open target product page')
def open_product_page(context):
    context.driver.get("https://www.target.com/p/A-81540287 ")
    sleep(5)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    color_buttons_parent = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='children']")))
    color_buttons = color_buttons_parent.find_elements(By.XPATH, ".//div[@class='styles__ButtonWrapper-sc-519sqw-1 clSiPU']//a")

    for button in color_buttons:
        color_name = button.get_attribute("aria-label")
        print("Clicking on", color_name)
        button.click()
        sleep(1)



