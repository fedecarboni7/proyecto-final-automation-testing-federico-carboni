import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_users_from_json

users = load_users_from_json()
ids = [u["description"] for u in users]


@pytest.mark.ui
@pytest.mark.parametrize("user_data", users, ids=ids)
def test_login_parametrizado(driver, base_url, user_data):
    """Test login with multiple users loaded from an external JSON file."""
    login_page = LoginPage(driver)
    login_page.open(base_url)
    login_page.login(user_data["username"], user_data["password"])

    if user_data["expected_result"] == "success":
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded(), f"Se esperaba inventario para {user_data['description']}"
    else:
        assert login_page.is_error_displayed(), f"Se esperaba error para {user_data['description']}"
