from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

    def get_cart_item_names(self):
        return [item.text for item in self.get_cart_items()]

    def get_cart_items_count(self):
        return len(self.get_cart_items())

    def item_is_in_cart(self, item_name):
        return item_name in self.get_cart_item_names()

    def get_cart_item_price(self, item_name):

        item_xpath = (
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='cart_item']"
            f"//div[@class='inventory_item_price']"
        )

        return self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, item_xpath)
            )
        ).text

    def remove_item_from_cart(self, item_name):

        button_xpath = (
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='cart_item']"
            f"//button"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, button_xpath)
            )
        ).click()

    def proceed_to_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()