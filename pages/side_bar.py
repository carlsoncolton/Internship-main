from typing import Tuple

from selenium.common import TimeoutException

from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideBar(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '[class="menu-twobutton"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_off_plan(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.OFF_PLAN))
            self.click(*self.OFF_PLAN)
        except TimeoutException:
            self.driver.find_element(*self.OFF_PLAN).click()

