import libs.messages as expected_msg
import libs.web_elements as web_element
import time
from actions.repo_browser_page import RepoBrowserPage
from libs.custom_libs import CustomLibs
from pytest import mark
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

username = "nashoshinoda"


@mark.test_repo_browser
class RepoBrowserTests:
    def test_elements_are_displayed(self, driver, url_to_test):
        driver.get(url_to_test)
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, web_element.HEADER))
        )

        assert ec.presence_of_element_located(
            (By.XPATH, web_element.HEADER)
        ), "The Header is not presented in the page."
        assert (
            RepoBrowserPage.get_header_title(self, driver) == "Get Github Repos"
        ), "The Header doesn't display the title of the app."
        assert ec.presence_of_element_located(
            (By.XPATH, web_element.SEARCH_FIELD)
        ), "The Search field is not presented in the page."
        assert ec.presence_of_element_located(
            (By.XPATH, web_element.GO_BTN)
        ), "The GO button is not presented in the page."

    def test_username_not_found(self, driver):
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, web_element.HEADER))
        )
        RepoBrowserPage.search_repo_by_name(
            self, driver, CustomLibs.get_random_name(self)
        )

        time.sleep(3)

        assert RepoBrowserPage.validate_username_result(
            self, driver, expected_msg.USERNAME_NOT_FOUND
        ), f"The username {username} was found."

    def test_no_repos(self, driver):
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, web_element.HEADER))
        )

        time.sleep(3)

        assert RepoBrowserPage.validate_repo_results_appears(
            self, driver, expected_msg.NO_REPOS
        ), f"The user {username} has one or more repositories."

    def test_valid_username(self, driver):
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.XPATH, web_element.HEADER))
        )
        RepoBrowserPage.clean_search_field(self, driver)
        RepoBrowserPage.search_repo_by_name(self, driver, username)

        time.sleep(3)

        assert RepoBrowserPage.validate_username_result(
            self, driver, expected_msg.USERNAME_FOUND
        ), f"The user {username} was not found."

    def test_validate_number_of_repos(self, driver):
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, web_element.HEADER))
        )
        total_repos_number = RepoBrowserPage.number_of_repos_in_list(self, driver)

        time.sleep(3)

        assert (
            RepoBrowserPage.total_repos_text(self, driver)
            == f"Found {total_repos_number} Repos"
        ), f"The number of repositories is not equals to {total_repos_number}."
