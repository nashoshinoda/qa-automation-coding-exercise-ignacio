import json
from pytest import fixture
from selenium import webdriver

environment_file = json.load(open("./resources/environment.json"))


@fixture(scope="session")
def driver():
    """
    `Description:`
        Make Chromedriver accesible to this project. We can also add browser options with variable chrome_options.

    `Return:`
        `driver:` Selenium Webdriver Object.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()  # Maximize window in every execution.

    yield driver

    driver.close()

    return driver


@fixture(scope="session")
def url_to_test():
    """
    `Description:`
        Pass the URL of the application to use it in the test case.

    `Return:`
        `String:` The URL of the application.
    """
    return environment_file["url_to_test"]
