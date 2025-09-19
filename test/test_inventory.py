import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from webdriver_manager.firefox import GeckoDriverManager
from config import config_for_login_page

@pytest.fixture(scope="function")
def inventory_page(request):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")
    firefox_options.add_argument("--headless")
    firefox_options.set_preference("security.password_lifetime", 0)
    firefox_options.set_preference("signon.rememberSignons", False)
    firefox_options.set_preference("signon.autofillForms", False)
    firefox_options.set_preference("privacy.trackingprotection.enabled", True)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])
    login_page.click_login_button()
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
    inventory_page = InventoryPage(driver)
    request.addfinalizer(driver.quit)
    return inventory_page

def test_add_product_to_cart(inventory_page):
        inventory_page.add_product_to_cart()
        badge_count = inventory_page.get_cart_badge_count()
        assert inventory_page.get_cart_badge_count() == "1"
        print(f"Badge count: {badge_count}")
        inventory_page.go_to_cart()
        cart_page = CartPage(inventory_page.driver)
        items = cart_page.get_cart_items()
        assert "Sauce Labs Bike Light" in items, f"Expected 'Sauce Labs Bike Light' in cart, but got {items}"
        print(f"Items: {items}")
        assert cart_page.is_checkout_button_visible(), "Checkout button is not visible"






