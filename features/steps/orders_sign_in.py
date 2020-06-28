from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@then('Sign-In logo is displayed')
def verify_found_results_text(context):
    sign_in_text = context.driver.find_element(*SIGN_IN_TEXT).text
    assert 'Sign-In' in sign_in_text, f'{sign_in_text} is displayed instead'


@then('Page title is correct')
def verify_page_title(context):
    title = context.driver.title
    assert 'Amazon Sign-In' in title, f'{title} is displayed instead'