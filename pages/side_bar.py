from typing import Tuple

from pages.base_page import Page
from selenium.webdriver.common.by import By


class SideBar(Page):
    OFF_PLAN = (By.CSS_SELECTOR, '[class="menu-twobutton"]')

    def click_off_plan(self):
        self.click(*self.OFF_PLAN)

