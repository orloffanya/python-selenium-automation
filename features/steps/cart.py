from time import sleep

from selenium.webdriver.common.by import By
from behave import when, then

CART = (By.ID, "nav-cart")
EMPTY_MSG = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")
SHOES = (By.CSS_SELECTOR, "a[href*='B07KK58WGX']")
DROP_DOWN = (By.CSS_SELECTOR, ".a-dropdown-prompt")
SIZE = (By.ID, "native_dropdown_selected_size_name_6")
ADD_TO_CART = (By.ID, "add-to-cart-button")
SUBTOTAL = (By.ID, "sc-subtotal-label-activecart")


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART).click()


@then('Shopping cart is empty')
def verify_card_empty(context):
    result_msg = context.driver.find_element(*EMPTY_MSG).text
    assert 'empty' in result_msg, "Expected to be empty, but it is not"


@when('Choose any item')
def choose_item(context):
    context.driver.find_element(*SHOES).click()
    sleep(2)


@when('Choose the size')
def choose_size(context):
    context.driver.find_element(*DROP_DOWN).click()
    context.driver.find_element(*SIZE).click()
    sleep(2)


@when('Add to cart')
def add_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()


@when('Open Cart')
def open_cart(context):
    context.driver.find_element(*CART).click()


@then('Check the quantity of the items')
def quantity_of_items_text(context):
    results_msg = context.driver.find_element(*SUBTOTAL).text
    assert '1 item' in results_msg, "Expected Subtotal (1 item), but got '{}'".format(results_msg)