from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

POPUP = (By.CSS_SELECTOR, "#nav-signin-tooltip span")


@then("Verify Sing in popup is present and clickable")
def verify_clickable_popup(context):
    context.driver.wait.until(EC.visibility_of_element_located, POPUP)
    context.driver.wait.until(EC.element_to_be_clickable, POPUP)


@when("Sign in popup disappears")
def popup_disappeared(context):
    context.driver.wait.until(EC.invisibility_of_element_located, POPUP)


@then("Verify Sign in popup is not clickable")
def verify_not_clickable_popup(context):
    context.driver.wait.until_not(EC.element_to_be_clickable, POPUP)
    # assert EC.element_to_be_clickable(POPUP) == False, f"Expected element not to be clickable"
