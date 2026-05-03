import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_itcareerhub_ui(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Открываем сайт
    driver.get("https://itcareerhub.de/ru")

    # 2. Проверяем логотип (обычно это img внутри header)
    logo = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a img"))
    )
    assert logo.is_displayed()

    # 3. Проверяем пункты меню (через link text CSS не умеет, поэтому используем partial match через атрибуты)
    menu_texts = [
        "Программы",
        "Способы оплаты",
        "О нас",
        "Контакты",
        "Отзывы",
        "Блог"
    ]
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    for text in menu_texts:
        wait.until(
            lambda d: text in d.find_element(By.TAG_NAME, "body").text
        )

    # 4. Проверяем переключатели языка
    lang_buttons = driver.find_elements(By.CSS_SELECTOR, "a")

    assert any("ru" in el.text.lower() for el in lang_buttons)
    assert any("de" in el.text.lower() for el in lang_buttons)

    # 5. Клик по "Контакты"
    about = wait.until(
        lambda d: next(el for el in d.find_elements(By.CSS_SELECTOR, "*") if "О нас" in el.text)
    )

    ActionChains(driver).move_to_element(about).perform()

    contacts = wait.until(
        lambda d: next(
            el for el in d.find_elements(By.CSS_SELECTOR, "a") if "contact-us" in (el.get_attribute("href") or ""))
    )

    driver.execute_script("arguments[0].click();", contacts)
    # 6. Клик по "Обратный звонок"
    callback_button = wait.until(
        lambda d: next(
            (el for el in d.find_elements(By.CSS_SELECTOR, "span.tn-atom__button-text")
             if "ОБРАТНЫЙ ЗВОНОК" in (el.get_attribute("innerText") or "").upper()),
            None
        )
    )

    driver.execute_script("arguments[0].click();", callback_button)
    # 7. Проверка текста в модальном окне
    modal = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )
    try:
        accept = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'ПОДТВЕРДИТЬ')]"))
        )
        accept.click()
    except:
        pass
    assert "Запишитесь на бесплатную карьерную консультацию" in modal.text
