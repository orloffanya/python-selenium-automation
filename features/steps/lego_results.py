from time import sleep

from selenium.webdriver.common.by import By
from behave import when, then

COMPONENT = (By.CSS_SELECTOR, "[data-component-type = 's-search-result']")


@then('Number of elements is equal to {number}')
def count_elements(context, number):
    search_results = context.driver.find_elements(*COMPONENT)
    # print(len(search_results))
    assert len(search_results) == int(number), f'Got {len(search_results)}, instead of {number}'
    if len(search_results) == 60:
        print("Everything is on the page")
    elif len(search_results) > 0:
        print("Some elements are located")
    else:
        print("Nothing is found")