from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver.maximize_window()
    #
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    # Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless=new")
    # options.add_argument("window-size=1920x1080")
    # driver_path = ChromeDriverManager().install()
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options=options, service=service)
    # context.driver.implicitly_wait(4)
    # context.app = Application(context.driver)

    # BrowserStack
    bs_user = 'coltoncarlson_m4Ig5d'
    bs_key = '6yzdT3Y8Yyc4pQdfy9Ge'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        'browser': 'Chrome',
        'browser_version': '115.0',
        'os': 'OS X',
        'os_version': 'Ventura',
        'name': 'User can open product detail and see three options of visualization'
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(url, options=options)

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
