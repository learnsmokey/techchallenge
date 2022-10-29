from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    context.driver = webdriver.Chrome(executable_path='C:\Vallikannu\Learning\Automation\drivers\chromedriver_win32\chromedriver.exe')

    # COMMENTED FOLLOWING FOR CHROME
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.driver.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    # def before_feature(context, scenario)
    # The above line is to run multiple scenario's written in one file, by clicking on feature
    # advantage work faster kill browser automatically and open again for nxt scenario
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    print('\nAfter Scenario ')
    context.driver.quit()
