from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.XPATH, "//input[@value='Go']")
RESULTS_INFO = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
ORDERS = (By.XPATH, "//*[@id='nav-orders']/span[2]")



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@when('When click on orders')
def click_orders_button(context):
    context.driver.find_element(*ORDERS).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_INFO).text
    assert 'Dres' in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)