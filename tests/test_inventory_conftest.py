import pytest

@pytest.mark.usefixtures("setup")
class TestInventory:

    def test_items_amount(self):
        self.login_page.success_login("standard_user", "secret_sauce")
        assert self.inventory_page.get_items_amount() == 6

    def test_backpack_cost(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        price = self.inventory_page.get_item_price("Sauce Labs Backpack")
        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        self.inventory_page.go_to_cart()

        cart_price = self.cart_page.get_cart_item_price("Sauce Labs Backpack")
        assert price == cart_price
