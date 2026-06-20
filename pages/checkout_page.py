from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the SauceDemo checkout flow."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Fill in the customer information form."""
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        """Click continue via JavaScript and wait for order summary."""
        btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", btn)
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("checkout-step-two")
        )

    def click_finish(self):
        """Click finish via JavaScript and wait for confirmation."""
        btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.FINISH_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", btn)
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("checkout-complete")
        )

    def get_confirmation_message(self):
        """Return the confirmation header text."""
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_total(self):
        """Return the order total label text."""
        return self.get_text(self.SUMMARY_TOTAL)
