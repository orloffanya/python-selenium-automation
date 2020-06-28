from behave import then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

HM = (By.ID, "nav-hamburger-menu")
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")



@when("Click on hamburger menu")
def locate_item(context):
    context.driver.find_element(*HM).click()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.driver.wait.until(EC.element_to_be_clickable(AMAZON_MUSIC_MENU_ITEM)).click()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    expected_item_count = int(expected_item_count)  # 6
    context.driver.wait.until(correct_menu_items_present(AMAZON_MUSIC_MENU_ITEM_RESULTS, expected_item_count), "Amount of items is incorrect")
    actual = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
    assert expected_item_count == actual, f'Expected {expected_item_count} items, but got {actual} items'


class correct_menu_items_present(object):
    def __init__(self, locator, amount):
        self.locator = locator
        self.amount = amount

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)  # Finding the referenced element
        if len(elements) == self.amount:
            return elements
        else:
            return False