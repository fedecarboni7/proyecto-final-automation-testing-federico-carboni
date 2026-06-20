from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the SauceDemo shopping cart page."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_item button")

    def get_cart_item_count(self):
        """Return the number of items currently in the cart."""
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CART_ITEMS)
        )
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        """Click checkout and wait until the checkout form is ready."""
        self.click(self.CHECKOUT_BUTTON)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

    def click_continue_shopping(self):
        """Click the continue shopping button to return to the inventory page."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
