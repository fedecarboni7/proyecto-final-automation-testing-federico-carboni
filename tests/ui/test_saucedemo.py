import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_USER = "invalid_user"
INVALID_PASSWORD = "wrong_password"


@pytest.mark.ui
def test_login_exitoso(driver, base_url):
    """Verify that a user can log in with valid credentials and reach the inventory page."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    assert "inventory" in driver.current_url


@pytest.mark.ui
def test_login_credenciales_invalidas(driver, base_url):
    """Verify that invalid credentials display the expected error message."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(INVALID_USER, INVALID_PASSWORD)

    assert login_page.is_error_displayed()
    assert "Epic sadface" in login_page.get_error_message()


@pytest.mark.ui
def test_cantidad_productos_inventario(driver, base_url):
    """Verify that the inventory page displays exactly 6 products."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_product_count() == 6


@pytest.mark.ui
def test_agregar_producto_al_carrito(driver, base_url):
    """Verify that adding a product to the cart updates the cart badge count to 1."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == "1"


@pytest.mark.ui
def test_flujo_checkout_completo(driver, base_url):
    """Verify the complete checkout flow: add item, go to cart, fill info, and confirm order."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_cart_item_count() == 1
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("John", "Doe", "12345")
    checkout_page.click_continue()
    assert "$" in checkout_page.get_total()
    checkout_page.click_finish()
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"


@pytest.mark.ui
def test_logout(driver, base_url):
    """Verify that the user can log out and is returned to the login page."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(VALID_USER, VALID_PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.logout()

    assert driver.current_url.rstrip('/') == "https://www.saucedemo.com"
    assert login_page.is_element_visible(login_page.LOGIN_BUTTON)
