from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from tests.constans import TestData
from tests.constans import Urls


class TestCheckoutTotal:

    def test_total_price(self, driver):

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # LOGIN
        login_page.open()
        login_page.login(
            TestData.USERNAME,
            TestData.PASSWORD
        )

        assert "inventory" in driver.current_url

        # ADD PRODUCTS
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_item_to_cart("Sauce Labs Onesie")

        assert inventory_page.get_cart_badge_count() == "3"

        # GO TO CART
        inventory_page.go_to_cart()

        assert cart_page.get_cart_items_count() == 3

        # CHECKOUT
        cart_page.proceed_to_checkout()

        assert "checkout-step-one" in driver.current_url

        # FILL FORM
        checkout_page.fill_checkout_form(
            TestData.FIRST_NAME,
            TestData.LAST_NAME,
            TestData.ZIP_CODE
        )

        checkout_page.click_continue()

        assert "checkout-step-two" in driver.current_url

        # GET TOTAL
        total = checkout_page.get_total_price()

        # ASSERT TOTAL
        assert total == TestData.EXPECTED_TOTAL