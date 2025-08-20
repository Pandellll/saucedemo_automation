import pytest
from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.popup_handler import dismiss_password_popup

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")
    error = login_page.get_error_messege()
    assert "Epic sadface" in error