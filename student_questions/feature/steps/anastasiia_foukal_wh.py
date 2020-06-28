from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

# student's code

PRODUCTS = (By.CSS_SELECTOR, "a.menu__link.menu--main__link[href*='products']")
FIND_STORE = (By.CSS_SELECTOR, ".Input-InputField--KUzM1")
FIND_STORE2 = (By.CLASS_NAME, "StoreSelector-Option--mQyct")
# FIND_STORE2 = (By.CSS_SELECTOR, ".StoreSelector-Option--mQyct")
# FIND_STORE2= (By.XPATH, "//div[@class='StoreSelector-DropdownOptions--vrkEe']/div[1]")


@given('Open Whole Foods page')
def open_wh_page(context):
    context.driver.get("https://www.wholefoodsmarket.com/")


@when("Click on Browse Products")
def click_browse_products(context):
    context.driver.find_element(*PRODUCTS).click()


@when("Choose the store")
def choose_store(context):
    context.driver.find_element(*FIND_STORE).send_keys("75019")
    sleep(4)
    context.driver.find_element(*FIND_STORE2).click()
    sleep(4)


@then("Number of products per page is {number_products}")
def product_number(context, number_products):
    product_num = context.driver.find_elements(By.CSS_SELECTOR, "a[store='[object Object]']")
    assert len(product_num) == int(number_products), f'Supposed to be {number_products}, but got {len(product_num)} products per page'

# student's code
#
# @given("Open Wholefoods page")
# def open_page(context):
#     context.driver.get("https://www.wholefoodsmarket.com/")
#
#
# @when("Click on Browse Products link")
# def click_browse_products(context):
#     link = context.driver.find_element(By.XPATH, "//a[contains(text(), 'Browse Products')]")
#     link.click()
#
#
# @when("Chose a store at {zip} zip")
# def choose_store(context, zip):
#     search_bar = context.driver.find_element(By.CSS_SELECTOR, ".Input-InputField--KUzM1")
#     search_bar.send_keys(zip)
#     sleep(6)
#     context.wait.until(EC.element_to_be_clickable, ".StoreSelector-Option--mQyct")
#     store = context.driver.find_element(By.CSS_SELECTOR, ".StoreSelector-Option--mQyct")
#     store.click()
#     sleep(6)
#
#
# @then("Count products on a page")
# def count_products(context):
#     all_products = context.driver.find_elements(By.CSS_SELECTOR, ".ProductCard-Name--1o2Gg")
#     print(len(all_products))
#
@then("Number of products per group is {number}")
def count_products(context, number):
    all_products = context.driver.find_elements(By.CSS_SELECTOR, ".ProductCard-Name--1o2Gg")
    print(len(all_products))
