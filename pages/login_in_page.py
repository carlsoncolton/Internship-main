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
