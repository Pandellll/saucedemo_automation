import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
from utils.popup_handler import dismiss_password_popup

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_checkout_process(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    home_page = HomePage(driver)
    home_page.add_first_item_to_cart()
    home_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("John", "Doe", "12345")

    assert "Thank you for your order!" in checkout_page.get_success_message()