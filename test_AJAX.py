import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
     driver = webdriver.Chrome()
     driver.get("http://uitestingplayground.com/ajax")
     yield driver
     driver.quit()

def test_button_text_change(driver):

    driver.get("http://uitestingplayground.com/textinput")


    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")


    button = driver.find_element(By.ID, "updatingButton")
    button.click()


    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "updatingButton"),
            "ITCH"
        )
    )


    assert button.text == "ITCH"


# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
#
# @pytest.fixture
# def driver():
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#     yield driver
#     driver.quit()
#
#
# def test_loading_images(driver):
#     wait = WebDriverWait(driver, 20)
#
#     wait.until(
#         lambda d: any(
#             img.get_attribute("alt") == "award"
#             for img in d.find_elements(By.TAG_NAME, "img")
#         )
#     )
#
#     images = driver.find_elements(By.TAG_NAME, "img")
#
#     assert any(img.get_attribute("alt") == "award" for img in images)

#