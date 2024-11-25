from behave import given, when, then
from pages.search_page import SearchPage


@given("the user is on the homepage")
def step_open_homepage(context):
    context.driver.get("http://127.0.0.1:8000/")
    context.search_page = SearchPage(context.driver)


@when("they enter a valid product name into the search bar")
def step_enter_valid_search_term(context):
    context.search_page.enter_search_term("denim")


@when("they enter a product name that does not exist")
def step_enter_invalid_search_term(context):
    context.search_page.enter_search_term("laptop")


@when("they leave the search bar empty")
def step_leave_search_empty(context):
    context.search_page.enter_search_term("")


@when("click the search button")
def step_click_search(context):
    context.search_page.click_search_button()


@then("they should see a list of results matching the product name")
def step_verify_results(context):
    results = context.search_page.get_results()
    assert len(results) > 0, "Expected search results, but found none."


@then('they should see a "No products match your search query" message')
def step_verify_no_results_message(context):
    no_results_message = context.search_page.get_no_results_message()
    assert "No products match your search query." in no_results_message, "Expected 'No results found' message."


@then("they should see a message prompting them to enter a search term")
def step_verify_empty_search_message(context):
    empty_search_message = context.search_page.get_empty_search_message()
    assert "Please enter a search term." in empty_search_message, "Expected prompt to enter a search term."
