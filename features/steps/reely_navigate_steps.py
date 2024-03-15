import time
from itertools import product
from platform import architecture

import lobby
from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open reely main page")
def open_reely_main(context):
    context.app.main_page.open_main()
    time.sleep(3)


username = 'carlsoncolton2012@gmail.com'
password = 'Colton!123'


@when("Login to the page")
def login(context):
    context.app.login_page.enter_username(username)
    context.app.login_page.enter_password(password)
    context.app.login_page.click_login_button()
    time.sleep(3)


@then("Click on “off plan” at the left side menu")
def click_off_plan(context):
    context.app.side_bar.click_off_plan()
    time.sleep(3)


@then("Click on the first product")
def click_first_product(context):
    context.app.reely_product_page.click_product()
    time.sleep(5)
    # context.driver.execute_script("'window.scrollTo(0, document.body.scrollHeight);")

@then("Verify the three options of visualization are 'architecture', 'interior', 'lobby'")
def verify_three_options_of_visualization(context):
    context.app.verify_product_page.verify_product_text1()
    context.app.verify_product_page.verify_product_text2()
    context.app.verify_product_page.verify_product_text3()
    time.sleep(3)


@then("Verify the visualization options are clickable")
def verify_options_clickable(context):
     context.app.verify_product_page.click_product_text1()
     context.app.verify_product_page.click_product_text2()
     context.app.verify_product_page.click_product_text3()
