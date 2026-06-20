from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger


class BasePage:
    """Base class for all page objects providing common interaction methods."""

    def __init__(self, driver):
        """Initialize BasePage with a WebDriver instance."""
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_element(self, locator, timeout=10):
        """Wait until the element identified by locator is visible and return it."""
        self.logger.info(f"Waiting for element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Wait for the element and perform a click action."""
        self.logger.info(f"Clicking element: {locator}")
        self.wait_for_element(locator).click()

    def type_text(self, locator, text):
        """Wait for the element, clear it, and type the provided text."""
        self.logger.info(f"Typing '{text}' into element: {locator}")
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Wait for the element and return its visible text."""
        self.logger.info(f"Getting text from element: {locator}")
        return self.wait_for_element(locator).text

    def is_element_visible(self, locator, timeout=5):
        """Return True if the element is visible within timeout, False otherwise."""
        self.logger.info(f"Checking visibility of: {locator}")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        """Return the current URL of the browser."""
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url
