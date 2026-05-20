import pytest
from selenium import webdriver
from Lesson6.pages.inventory_page import InventoryPage
from Lesson6.pages.login_page import LoginPage

# @pytest.mark.usefixtures("driver")
class TestInventory:
    @pytest.fixture()
    # @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    # @pytest.fixture(scope="class")
    @pytest.fixture(autouse=True)
    def inventory_page(self, driver):
        return InventoryPage(driver)

    # @pytest.fixture(scope="class")
    @pytest.fixture(autouse=True)
    def login_page(self, driver):
        return LoginPage(driver)

    def test_items_amount(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_all_items_are_displayed(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_items_are_displayed(), "Не все товары отображаются."

    def test_all_items_names_are_displayed(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."