import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class ProductVerificationPage(Page):
    # ARCHITECTURE = (By.XPATH, "//a[@class='tab w-inline-block w-tab-link w--current' and @data-w-tab='Tab 1']")
    ARCHITECTURE = (By.CSS_SELECTOR, "a[data-w-tab='Tab 1']")
    INTERIOR = (By.ID, 'w-tabs-0-data-w-tab-1')
    LOBBY = (By.ID, 'w-tabs-0-data-w-tab-2')

    def verify_product_text1(self):
        self.find_element(*self.ARCHITECTURE)

    def verify_product_text2(self):
        self.find_element(*self.INTERIOR)

    def verify_product_text3(self):
        self.find_element(*self.LOBBY)

    def click_product_text1(self):
        sleep(3)
        self.click(*self.ARCHITECTURE)

    def click_product_text2(self):
        sleep(3)
        self.click(*self.INTERIOR)

    def click_product_text3(self):
        sleep(3)
        self.click(*self.LOBBY)
