from behave import given, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR_NAME = (By.CSS_SELECTOR, "div#variation_color_name span.selection")

@given('Open Amazon {product_id} product page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')



@then("All expected color options are present")
def color_verification(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Wash', 'Indigo Wash', 'Light Wash', 'Medium Wash', 'Rinse', 'Vintage Light Wash']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for x in range(len(color_options)):
        color_options[x].click()
        selected_color_text = context.driver.find_element(*SELECTED_COLOR_NAME).text
        assert selected_color_text == expected_colors[x]