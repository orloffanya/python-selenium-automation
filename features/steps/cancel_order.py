from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HELP_SEARCH = (By.ID, 'helpsearch')
GO = (By.CSS_SELECTOR, '.a-button-input')
HELP_RESULTS = (By.CSS_SELECTOR, ".a-color-secondary b")


@given('Open Amazon Help page')
def open_help_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into solutions search field')
def input_help_search(context, search_word):
    search = context.driver.find_element(*HELP_SEARCH)
    search.clear()
    search.send_keys(search_word)



@when('Click on Go')
def click_go(context):
    context.driver.find_element(*GO).click()



@then('Solution results are shown for {search_word}')
def verify_solution_results_text(context, search_word):
    results_msg = context.driver.find_element(*HELP_RESULTS).text
    assert 'Cancel order' in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)