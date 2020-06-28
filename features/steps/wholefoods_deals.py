from behave import given, then
from selenium.webdriver.common.by import By

RESULTS = (By.CSS_SELECTOR, "#wfm-pmd_deals_section div:nth-child(6) li")
REGULAR = (By.CSS_SELECTOR, ".s-result-list.s-col-2 span.wfm-sales-item-card__regular-price")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@given('Open Amazon Wholefoods Deals')
def open_wh_deals(context):
    context.driver.get("https://www.amazon.com/wholefoodsdeals")


@then('Each item has {text} field and Product name')
def verify_regular_field(context, text):
    product_list = context.driver.find_elements(*RESULTS)
    print(product_list)
    context.driver.refresh()
    product_list = context.driver.find_elements(*RESULTS)
    print(product_list)
    for product_item in product_list:
        assert "Regular" in product_item.text, f"Expected Regular to be in element {product_item.text}"
        assert product_item.find_element(*PRODUCT_NAME)
