import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
   driver = webdriver.Chrome()
   # Максимизация окна
   driver.maximize_window()
   driver.get("https://www.saucedemo.com/")
   # Передача драйвера в тест
   yield driver
   # Закрытие браузера
   driver.quit()

def test_success_login_valid_data(driver):
   user_name_input_field = driver.find_element(By.ID, "user-name")
   user_name_input_field.send_keys("standard_user")

   password_input_field = driver.find_element(By.ID, "password")
   password_input_field.send_keys("secret_sauce")

   login_button = driver.find_element(By.ID, "login-button")
   login_button.click()

   assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Не удалось войти в систему."

   inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
   assert inventory_list, "Список товаров не найден на странице."


def test_invalid_password(driver):
   user_name_input_field = driver.find_element(By.ID, "user-name")
   user_name_input_field.send_keys("standard_user")
   password_input_field = driver.find_element(By.ID, "password")
   password_input_field.send_keys("wrong_password")

   login_button = driver.find_element(By.ID, "login-button")
   login_button.click()

   error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
   assert error_message, "Сообщение об ошибке не отображается."
   assert "Username and password do not match" in error_message.text, "Неверное сообщение об ошибке."

def test_locked_out_user(driver):
   user_name_input_field = driver.find_element(By.ID, "user-name")
   user_name_input_field.send_keys("locked_out_user")

   password_input_field = driver.find_element(By.ID, "password")
   password_input_field.send_keys("secret_sauce")

   login_button = driver.find_element(By.ID, "login-button")
   login_button.click()
   error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
   assert error_message, "Сообщение об ошибке не отображается."
   assert "Sorry, this user has been locked out." in error_message.text, "Неверное сообщение об ошибке."

def test_empty_username(driver):
   password_input_field = driver.find_element(By.ID, "password")
   password_input_field.send_keys("secret_sauce")

   login_button = driver.find_element(By.ID, "login-button")
   login_button.click()

   error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
   assert error_message, "Сообщение об ошибке не отображается."
   assert "Username is required" in error_message.text, "Неверное сообщение об ошибке."

def test_empty_password(driver):
   user_name_input_field = driver.find_element(By.ID, "user-name")
   user_name_input_field.send_keys("standard_user")

   login_button = driver.find_element(By.ID, "login-button")
   login_button.click()
   error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
   assert error_message, "Сообщение об ошибке не отображается."
   assert "Password is required" in error_message.text, "Неверное сообщение об ошибке."

