from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_BAR = (By.NAME, "q")  # Locator for search bar
    SEARCH_BUTTON = (By.XPATH, "//form[@action='/search/']//button[@type='submit']")  # Locator for search button
    RESULT_LIST = (By.XPATH, "/html/body/div[@class='container my-4']//img[@alt='Classic Denim Jeans']")  # Adjusted
    # locator for results
    NO_RESULTS_MESSAGE = (By.XPATH, "//p[text()='No products match your search query.']")  # Locator for "No products
    # match your search query." message
    EMPTY_SEARCH_MESSAGE = (By.XPATH, "//p[text()='Please enter a search term.']")  # Locator for empty search message

    def enter_search_term(self, term):
        search_input = self.wait_for_element(self.SEARCH_BAR)
        search_input.clear()
        search_input.send_keys(term)

    def click_search_button(self):
        search_button = self.wait_for_element(self.SEARCH_BUTTON)
        search_button.click()

    def get_results(self):
        return self.driver.find_elements(*self.RESULT_LIST)

    def get_no_results_message(self):
        return self.wait_for_element(self.NO_RESULTS_MESSAGE).text

    def get_empty_search_message(self):
        return self.wait_for_element(self.EMPTY_SEARCH_MESSAGE).text
