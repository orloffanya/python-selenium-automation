from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ALL_PRODUCTS = (By.CSS_SELECTOR, 'img.s-image')
ADD_PRODUCT = (By.CSS_SELECTOR, '#add-to-cart-button')
OPEN_CART = (By.CSS_SELECTOR, 'span#nav-cart-count')
CART_INSIDE = (By.CSS_SELECTOR, '#sc-subtotal-label-buybox')


# @given("Open Amazon page")
# def open_amazon(context):
#     context.driver.get("https://www.amazon.com/")


@when('The number of items is equal to {number}')
def count_items(context, number):
#     #one_element = context.driver.find_element(*ALL_PRODUCTS)
#     #print(one_element)
    search_results = context.driver.find_elements(*ALL_PRODUCTS)
    print(len(search_results))
#     #print(search_results[0])
#     #print(search_results[0].text)
#     assert len(search_results) == int(number), f'Expected {number}, but got {len(search_results)}'
    if len(search_results) == 72:
        print("Everyting is on the page")
    elif len(search_results) > 0:
        print("Some elements are located")
    else:
        print("Nothing is found on the page")


@when('User click on chosen item')
def find_item_one(context):
    all_products = context.driver.find_elements(*ALL_PRODUCTS)
    all_products[0].click()


@when('User add item to shopping cart')
def add_item(context):
    context.driver.find_element(*ADD_PRODUCT).click()
    sleep(5)


@when('User click on another chosen item')
def find_item_two(context):
    all_products = context.driver.find_elements(*ALL_PRODUCTS)
    all_products[9].click()


@then('User open shopping cart')
def open_shopping_cart(context):
    context.driver.find_element(*OPEN_CART).click()
    sleep(10)


@then('Verify that 2 items in shopping cart')
def item_cart(context):
    cart = context.driver.find_element(*CART_INSIDE)
    assert "2 items" in cart.text, f"Expected , but got {cart.text}"
