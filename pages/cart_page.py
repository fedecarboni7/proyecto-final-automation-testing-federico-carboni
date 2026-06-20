from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the SauceDemo shopping cart page."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".cart_item button")

    def get_cart_item_count(self):
        """Return the number of items currently in the cart."""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def click_checkout(self):
        """Click the checkout button to proceed with the purchase."""
        self.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        """Click the continue shopping button to return to the inventory page."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
