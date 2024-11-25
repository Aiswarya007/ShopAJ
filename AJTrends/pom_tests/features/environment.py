from selenium import webdriver


def before_all(context):
    # Setup the browser driver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_all(context):
    # Teardown: close the browser
    context.driver.quit()
