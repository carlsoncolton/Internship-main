from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
driver.find_element(By.CSS_SELECTOR, "H1.a-spacing-small")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "[class=‘a-alert-content’]")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, "[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

git status
git add <file_name>
git commit -m 'Commit message'
git push origin main
