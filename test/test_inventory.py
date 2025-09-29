import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from webdriver_manager.firefox import GeckoDriverManager
from config import config_for_login_page

@pytest.fixture(scope="function")
def inventory_page(browser_driver, request):
    login_page = LoginPage(browser_driver)
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])
    login_page.click_login_button()
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
    inventory_page = InventoryPage(browser_driver)
    request.addfinalizer(browser_driver.quit)
    return inventory_page

def test_add_product_to_cart(inventory_page):
        inventory_page.add_product("bike_light")
        badge_count = inventory_page.get_cart_badge_count()
        assert inventory_page.get_cart_badge_count() == "1"
        print(f"Badge count: {badge_count}")
        inventory_page.go_to_cart()
        cart_page = CartPage(inventory_page.driver)
        items = cart_page.get_cart_items()
        assert "Sauce Labs Bike Light" in items, f"Expected 'Sauce Labs Bike Light' in cart, but got {items}"
        print(f"Items: {items}")
        assert cart_page.is_checkout_button_visible(), "Checkout button is not visible"


def test_multi_add(inventory_page):
    products = ["bike_light", "backpack", "fleece_jacket"]
    with allure.step(f"Iniciar adición de {len(products)} productos al carrito"):
        inventory_page.add_multiple_products(products)

    with allure.step("Verificar badge del carrito actualizado"):
        badge = int(inventory_page.get_cart_badge_count())
        assert badge == 3
        allure.attach(f"Badge final: {badge}", name="Badge Count", attachment_type=allure.attachment_type.TEXT)
@pytest.mark.parametrize("sort_option, expected_order", [("lohi", "asc"), ("hilo", "desc")])

def test_sort_order(inventory_page, sort_option, expected_order):
    prices_before = inventory_page.get_prices()
    inventory_page.sort_by_price(sort_option)
    prices_after = inventory_page.get_prices()
    assert len(prices_after) == 6
    expected_sorted = sorted(prices_before, reverse=(expected_order == "desc"))
    assert prices_after == expected_sorted

def test_get_prices(inventory_page):
	prices = inventory_page.get_prices()
	assert len(prices) == 6
	assert all(isinstance(p, float) for p in prices)
	assert min(prices) >0
