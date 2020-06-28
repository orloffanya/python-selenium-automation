from behave import given, then
from selenium.webdriver.common.by import By

LINKS= (By.CSS_SELECTOR, "#zg_tabs li")


@given("Open Amazon Best Sellers page")
def open_best_sellers(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then("Check that {links} links are present")
def link_quantity(context, links):
    bs_links = context.driver.find_elements(*LINKS)
    assert len(bs_links) == int(links), f'{links} links should be displayed on Amazon Best Seller Header, but instead {len(bs_links)} are displayed'
