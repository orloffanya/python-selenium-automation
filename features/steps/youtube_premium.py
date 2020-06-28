from behave import then, when, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

FIRST_VIDEO = (By.ID, "dismissable")
PREMIUM_POPUP = (By.CSS_SELECTOR, "ytd-button-renderer#action-button")
VERIFY_PAGE = (By.CSS_SELECTOR, ".style-scope.yt-music-pass-small-feature-info-renderer.no-transition")
SIGN_IN_BTN = (By.CSS_SELECTOR, "#contentWrapper #button")
LIKE_BTN = (By.CSS_SELECTOR, ".style-scope.ytd-menu-renderer.force-icon-button")
SKIP_ADD_BTN = (By.CSS_SELECTOR, ".ytp-ad-skip-button")

@given('Open Youtube page')
def open_youtube(context):
    context.driver.get("https://www.youtube.com/")


@when("Click on the first youtube video")
def click_video(context):
    context.driver.find_element(*FIRST_VIDEO).click()


@then("Check Youtube popup")
def close_prime_popup(context):
    add = context.driver.find_elements(*SKIP_ADD_BTN)
    sleep(5)
    popup = context.driver.find_elements(*PREMIUM_POPUP)
    if len(popup) > 0:
        popup[0].click()
        assert len(context.driver.find_elements(*VERIFY_PAGE)) > 0, f"Expected to find the icons"
        print("premium page is fine")
    elif len(add) > 0:
    # if len(add) > 0:
        context.driver.wait.until(EC.element_to_be_clickable(SKIP_ADD_BTN))
        add.click()
        print("add was skipped")
    else:
        context.driver.find_element(*LIKE_BTN).click()
        assert context.driver.find_element(*SIGN_IN_BTN), f"No popup appeared"
        print("there was a popup after like")