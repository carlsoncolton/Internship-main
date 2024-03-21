from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, "email-2")
        self.password_locator = (By.ID, "field")
        self.login_button_locator = (By.CSS_SELECTOR, "[class='login-button w-button']")
        self.target_login_button = (By.CSS_SELECTOR, "[class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']")
        self.navigate_sign_in = (By.CSS_SELECTOR, "[class='styles__ListItemText-sc-diphzn-1 jaMNVl']")
        self.sign_in_button = (By.CSS_SELECTOR, "[class='styles__StyledHeading-sc-1xmf98v-0 "
                                                "styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']")
        self.terms_and_conditions = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')
        self.terms_and_conditions_page = (By.CSS_SELECTOR, '[class="styles__StyledHeading-sc-1xmf98v-0 lfA-Dem"]')
    username = 'carlsoncolton2012@gmail.com'
    password = 'Colton!123'

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_locator)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_locator)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        WebDriverWait(self.driver, 10).until(EC.title_is("Logged In Page Title"))

    def click_sign_in_target(self):
        target_login_button = self.driver.find_element(*self.target_login_button)
        target_login_button.click()

    def click_navigate_sign_in(self):
        navigate_sign_in_button = self.driver.find_element(*self.navigate_sign_in)
        navigate_sign_in_button.click()

    def verify_sign_in_target(self):
        verify_sign_in_button = self.driver.find_element(*self.sign_in_button)
        verify_sign_in_button.click()

    def click_on_target_terms_and_conditions_link(self):
        terms_and_conditions_button = self.driver.find_element(*self.terms_and_conditions)
        terms_and_conditions_button.click()

    def verify_terms_and_conditions_page(self):
        verify_terms_page = self.driver.find_element(*self.terms_and_conditions_page)
        verify_terms_page.click()

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
