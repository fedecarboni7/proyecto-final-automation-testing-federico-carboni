from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the SauceDemo checkout flow (step one, step two, and confirmation)."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Fill in the customer information form."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.FIRST_NAME)
        )
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        """Click continue and wait for order summary to load."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        self.click(self.CONTINUE_BUTTON)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )

    def click_finish(self):
        """Click the finish button to complete the purchase."""
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        """Return the confirmation header text displayed after a successful purchase."""
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_total(self):
        """Return the total summary label text from the order summary page."""
        return self.get_text(self.SUMMARY_TOTAL)
