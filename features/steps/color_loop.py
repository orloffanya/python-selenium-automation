from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# SEARCH_ITEMS = (By.XPATH, "//li[@class='a-carousel-card']//div[@class='sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32']")
# COLOR_NAME = (By.CSS_SELECTOR, "#variation_color_name .selection")
COLOR_NAME = (By.CSS_SELECTOR, ".a-row .selection")
DIFFERENT_COLOR_ITEMS = (By.CSS_SELECTOR, "ul.a-unordered-list.a-nostyle.a-button-list.a-declarative li img")
IMAGE_COLOR = (By.CSS_SELECTOR, ".imgSwatch")
SEARCH_ITEMS = (By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

@when("click on search")
def click_search(context):
    context.driver.find_element(By.CSS_SELECTOR, ".nav-search-submit.nav-sprite").click()


# @when("Click on item number {number}")
# def click_on_item(context, number):
#     carousel = context.driver.find_elements(*SEARCH_ITEMS)
#     carousel[(int(number)-1)].click()


@when("Click on the first item of Amazon search")
def click_item(context):
    search_results = context.driver.find_elements(*SEARCH_ITEMS)
    search_results[0].click()


@then("Verify that color names correspond with item color")
def color_loop(context):
    all_items = context.driver.find_elements(*DIFFERENT_COLOR_ITEMS)
    # for counter in range(len(all_items)):
    #     current_item = context.driver.find_elements(*DIFFERENT_COLOR_ITEMS)[counter]
    #     current_item.click()
    #     sleep(5)
    #     current_color = context.driver.find_element(*COLOR_NAME)
    #     assert current_color.text == current_item.get_attribute("alt"), f"{current_color.text} is not {current_item.get_attribute('alt')}"

    for item in all_items:
        item.click()
        context.driver.wait.until(EC.element_to_be_clickable(COLOR_NAME))
        current_color = context.driver.find_element(*COLOR_NAME)
        assert current_color.text == item.get_attribute("alt"), f"{current_color.text} is not {item.get_attribute('alt')}"