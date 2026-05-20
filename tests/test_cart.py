import pytest
from selenium import webdriver
from Lesson6.pages.inventory_page import InventoryPage
from Lesson6.pages.login_page import LoginPage
from Lesson6.pages.cart_page import CartPage


class TestInventory:
   @pytest.fixture(scope="class")
   def driver(self):
       driver = webdriver.Chrome()
       driver.get("https://www.saucedemo.com/")
       yield driver
       driver.quit()


   @pytest.fixture(scope="class")
   def inventory_page(self, driver):
       return InventoryPage(driver)


   @pytest.fixture(scope="class")
   def login_page(self, driver):
       return LoginPage(driver)


   @pytest.fixture(scope="class")
   def cart_page(self, driver):
       return CartPage(driver)


   def test_backpack_cost(self, login_page, inventory_page, cart_page):
       # 1. Login with valid data
       login_page.success_login("standard_user", "secret_sauce")


       # 2. Remember the cost of the item "Backpack"
       backpack_price = inventory_page.get_item_price("Sauce Labs Backpack")


       # 3. Add item "Backpack" to the cart
       inventory_page.add_item_to_cart("Sauce Labs Backpack")


       # 4. Click on the cart button
       inventory_page.go_to_cart()


       # 5. Check that the cost of the item in the cart equals to the cost of the item on the Inventory page
       cart_price = cart_page.get_cart_item_price("Sauce Labs Backpack")
       assert backpack_price == cart_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
