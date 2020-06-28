from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By

PRODUCTS = (By.CSS_SELECTOR, "a.menu__link.menu--main__link[href*='products']")
FIND_STORE = (By.CSS_SELECTOR, ".Input-InputField--KUzM1")
#FIND_STORE2 = (By.CLASS_NAME, "StoreSelector-Option--mQyct")
FIND_STORE2 = (By.CSS_SELECTOR, ".StoreSelector-Option--mQyct")
#FIND_STORE2= (By.XPATH, "//div[@class='StoreSelector-DropdownOptions--vrkEe']/div[1]")
CATEGORY = (By.XPATH, "//div[@class='LandingPage-Root--1b1TW']/div[1]/div[2]/a")


@given('Open Wholefoods page')
def open_wh_page(context):
    context.driver.get("https://www.wholefoodsmarket.com/")


@when("Click on Browse Products")
def click_browse_products(context):
    context.driver.find_element(*PRODUCTS).click()


@when("Choose the store")
def choose_store(context):
    context.driver.find_element(*FIND_STORE).send_keys("75019")
    sleep(3)
    context.driver.find_element(*FIND_STORE2).click()


@then("Number of products per page is {number_products}")
def product_number(context, number_products):
    product_num = context.driver.find_elements(By.CSS_SELECTOR, "a[store='[object Object]']")
    assert len(product_num) == int(number_products), f'Supposed to be {number_products}, but got {len(product_num)} products per page'


@then('{prod_cat} products are shown for each category')
def prod_cat_number(context, prod_cat):
    list_cat = context.driver.find_elements(*CATEGORY)
    assert len(list_cat) == int(prod_cat), f'{prod_cat} products should be shown for each category, but {len(list_cat)}'
