# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.get("http://uitestingplayground.com/ajax")
#     yield driver
#     driver.quit()
#
# def test_ajax_request_explicit(driver):
#     wait = WebDriverWait(driver, 15)
#
#
#     ajax_button = driver.find_element(By.ID, "ajaxButton")
#     ajax_button.click()
#
#
#     ajax_text_element = wait.until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
#     )
#
#
#     assert "Data loaded with AJAX get request." in ajax_text_element.text


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_loading_images(driver):
    wait = WebDriverWait(driver, 20)

    wait.until(
        lambda d: any(
            img.get_attribute("alt") == "award"
            for img in d.find_elements(By.TAG_NAME, "img")
        )
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    assert any(img.get_attribute("alt") == "award" for img in images)