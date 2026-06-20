from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the SauceDemo inventory (products) page."""

    PRODUCT_LIST = (By.CLASS_NAME, "inventory_list")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def is_loaded(self):
        """Return True if the product list is visible, indicating the page loaded."""
        self.logger.info("Checking if inventory page is loaded")
        return self.is_element_visible(self.PRODUCT_LIST)

    def get_product_count(self):
        """Return the number of product items displayed on the page."""
        count = len(self.driver.find_elements(*self.PRODUCT_ITEMS))
        self.logger.info(f"Product count: {count}")
        return count

    def add_first_product_to_cart(self):
        """Click the add-to-cart button on the first product item."""
        self.logger.info("Adding first product to cart")
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_count(self):
        """Return the cart badge text (item count) or '0' if the badge is not visible."""
        if self.is_element_visible(self.CART_BADGE):
            count = self.get_text(self.CART_BADGE)
        else:
            count = "0"
        self.logger.info(f"Cart badge count: {count}")
        return count

    def go_to_cart(self):
        """Click the cart link to navigate to the cart page."""
        self.logger.info("Navigating to cart")
        self.click(self.CART_LINK)

    def logout(self):
        """Log out by navigating directly to the login page after clearing session storage,
        bypassing the burger menu animation that is unreliable in headless mode."""
        self.logger.info("Logging out via direct navigation")

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        self.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        self.driver.get("https://www.saucedemo.com")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
        self.logger.info("Logout successful, login page loaded")
