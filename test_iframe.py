# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()
#
#
# def test_iframe_text(browser):
#     browser.get(
#         "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
#     )
#
#     wait = WebDriverWait(browser, 10)
#
#     iframes = wait.until(
#         EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
#     )
#
#     target_text = "semper posuere integer et senectus justo curabitur."
#
#     found = False
#
#     for iframe in iframes:
#         browser.switch_to.default_content()
#         browser.switch_to.frame(iframe)
#
#         body_text = browser.find_element(By.TAG_NAME, "body").text
#
#         if target_text in body_text:
#             found = True
#             break
#
#     browser.switch_to.default_content()
#
#     assert found




import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver_js():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_drag_and_drop(driver_js):
    driver_js.get(
        "https://www.globalsqa.com/demoSite/practice/droppable/photo-manager.html"
    )

    wait = WebDriverWait(driver_js, 10)

    first_photo = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#gallery li")
        )
    )

    trash = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "trash")
        )
    )

    ActionChains(driver_js).drag_and_drop(
        first_photo,
        trash
    ).perform()

    photos_in_trash = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#trash ul li")
        )
    )

    assert len(photos_in_trash) == 1, (
        f"В корзине должна быть 1 фотография, "
        f"а не {len(photos_in_trash)}"
    )

    photos_in_gallery = driver_js.find_elements(
        By.CSS_SELECTOR,
        "#gallery li"
    )

    assert len(photos_in_gallery) == 3, (
        f"В галерее должно остаться 3 фотографии, "
        f"а не {len(photos_in_gallery)}"
    )