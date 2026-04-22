import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()


def test_payment_methods_section(driver):
    driver.get("https://itcareerhub.de/ru")

    wait = WebDriverWait(driver, 15)

    # Переход в раздел "Способы оплаты"
    payment_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Способы оплаты"))
    )
    payment_link.click()

    # Ждём загрузку страницы
    body = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Скриншот всей секции страницы
    body.screenshot("screenshots/payment_methods.png")