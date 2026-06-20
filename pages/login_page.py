from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the SauceDemo login page."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container h3")

    def open(self, base_url):
        """Navigate to the login page URL."""
        self.logger.info(f"Opening login page: {base_url}")
        self.driver.get(base_url)

    def enter_username(self, username):
        """Type the provided username into the username input field."""
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Type the provided password into the password input field."""
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Perform a complete login flow: enter username, password, and click login."""
        self.logger.info(f"Logging in with user: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Return the text of the error message container."""
        self.logger.info("Getting error message text")
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Return True if the error message is visible, False otherwise."""
        self.logger.info("Checking if error message is displayed")
        return self.is_element_visible(self.ERROR_MESSAGE)
