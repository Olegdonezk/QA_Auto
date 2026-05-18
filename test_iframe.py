import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_iframe_text(browser):
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
    )

    wait = WebDriverWait(browser, 10)

    iframes = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
    )

    target_text = "semper posuere integer et senectus justo curabitur."

    found = False

    for iframe in iframes:
        browser.switch_to.default_content()
        browser.switch_to.frame(iframe)

        body_text = browser.find_element(By.TAG_NAME, "body").text

        if target_text in body_text:
            found = True
            break

    browser.switch_to.default_content()

    assert found



def test_drag_and_drop(browser):
    browser.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(browser, 15)

    iframe = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame"))
    )

    browser.switch_to.frame(iframe)

    source = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#gallery li"))
    )

    trash = wait.until(
        EC.presence_of_element_located((By.ID, "trash"))
    )

    ActionChains(browser) \
        .click_and_hold(source) \
        .move_to_element_with_offset(trash, 50, 50) \
        .release() \
        .perform()

    moved_item = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#trash img"))
    )

    assert moved_item.is_displayed()