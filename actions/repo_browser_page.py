import libs.web_elements as web_element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class RepoBrowserPage:
    def get_header_title(self, driver):
        return driver.find_element(By.XPATH, web_element.HEADER).text

    def clean_search_field(self, driver):
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, web_element.SEARCH_FIELD))
        )
        driver.find_element(By.XPATH, web_element.SEARCH_FIELD).send_keys(
            Keys.CONTROL + "a", Keys.BACKSPACE
        )

    def search_repo_by_name(self, driver, username):
        driver.find_element(By.XPATH, web_element.SEARCH_FIELD).send_keys(username)
        driver.find_element(By.XPATH, web_element.GO_BTN).click()

    def validate_username_result(self, driver, expected_value):
        if (
            expected_value
            in driver.find_element(By.XPATH, web_element.USERNAME_MSG_AREA).text
        ):
            return True
        else:
            return False

    def validate_repo_results_appears(self, driver, expected_value):
        if (
            expected_value
            in driver.find_element(By.XPATH, web_element.REPO_MSG_AREA).text
        ):
            return True
        else:
            return False

    def total_repos_text(self, driver):
        total_number = driver.find_element(By.XPATH, "//p[@class='repo-amount']").text

        return total_number

    def number_of_repos_in_list(self, driver):
        repo_items = driver.find_elements(By.XPATH, web_element.REPO_ITEM)

        return len(repo_items)
