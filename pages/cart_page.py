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
        """Click checkout button via JavaScript and wait for checkout form."""
        # Esperar que el botón esté presente y hacer click via JavaScript
        checkout_btn = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", checkout_btn)
        self.logger.info("Clicked checkout button via JavaScript")
        
        # Esperar que la URL cambie a checkout
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("checkout-step-one")
        )
        self.logger.info("Checkout step one page loaded")

    def click_continue_shopping(self):
        """Click the continue shopping button to return to the inventory page."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
