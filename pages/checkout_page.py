from selenium.webdriver.common.by import By
from base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_total_price(self):
        total_text = self.get_text(self.TOTAL_PRICE)

        return float(
            total_text.replace("Total: $", "").strip()
        )