from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

LINKS = (By.CSS_SELECTOR, "#zg_tabs li")


@given("Open Amazon Bestseller page")
def open_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("Count links")
def count_links(context):
    all_links = context.driver.find_elements(*LINKS)
    assert len(all_links) == 5, f"You are a fool"