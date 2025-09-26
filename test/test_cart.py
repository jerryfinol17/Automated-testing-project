import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from webdriver_manager.firefox import GeckoDriverManager
from config import config_for_login_page
from config.config_for_cart_page import PRODUCTS

@pytest.fixture(scope="function")
def cart_page_with_items(request):
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
    inventory = InventoryPage(driver)
    inventory.add_multiple_products(["bike_light", "backpack"])
    inventory.go_to_cart()
    cart_page = CartPage(driver)
    request.addfinalizer(driver.quit)
    return cart_page


def test_verify_cart_items(cart_page_with_items):
    items = cart_page_with_items.get_cart_items()
    badge = cart_page_with_items.get_cart_badge_count()
    assert len(items)==2
    assert "Sauce Labs Bike Light" in items
    assert badge == '2'
    print(f"Items: {items}, Badge: {badge}")

@pytest.mark.parametrize("product_key, expected_badge_after", [("bike_light",'1'), ("backpack",'1')])

def test_remove_single_item(cart_page_with_items, product_key, expected_badge_after):
    success = cart_page_with_items.remove_item(product_key)
    items_after = cart_page_with_items.get_cart_items()
    badge_after = cart_page_with_items.get_cart_badge_count()
    assert success == True
    assert badge_after == expected_badge_after
    assert PRODUCTS [product_key]["display_name"] not in items_after

def test_remove_all_items(cart_page_with_items):
    products = ["bike_light", "backpack"]
    for p in products:
        cart_page_with_items.remove_item(p)

    assert len(cart_page_with_items.get_cart_items()) == 0
    assert cart_page_with_items.get_cart_badge_count() == '0'

def test_start_checkout(cart_page_with_items):
    assert cart_page_with_items.is_checkout_button_visible() == True
    cart_page_with_items.start_checkout()
    assert "checkout-step-one.html" in cart_page_with_items.driver.current_url
    print(f"Current URL after checkout: {cart_page_with_items.driver.current_url}")

