import pytest
import allure
from allure_commons.types import AttachmentType
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config import config_for_login_page
from config.config_for_cart_page import PRODUCTS
import time


@pytest.fixture(scope="function")
def cart_page_with_items(browser_driver, request):
    login_page = LoginPage(browser_driver)
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])
    login_page.click_login_button()
    assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
    inventory = InventoryPage(browser_driver)
    inventory.add_multiple_products(["bike_light", "backpack"])
    inventory.go_to_cart()
    cart_page = CartPage(browser_driver)
    request.addfinalizer(browser_driver.quit)
    return cart_page


def test_verify_cart_items(cart_page_with_items):
    with allure.step("Obtener lista de ítems en el carrito"):
        items = cart_page_with_items.get_cart_items()
    with allure.step("Obtener número del badge del carrito"):
        badge = cart_page_with_items.get_cart_badge_count()
    with allure.step("Verificar que hay exactamente 2 ítems"):
        assert len(items) == 2
    with allure.step("Verificar que 'Sauce Labs Bike Light' está presente"):
        assert "Sauce Labs Bike Light" in items
    with allure.step("Verificar que el badge muestra '2'"):
        assert badge == '2'
    print(f"Items: {items}, Badge: {badge}")


@pytest.mark.parametrize("product_key, expected_badge_after", [("bike_light",'1'), ("backpack",'1')])
def test_remove_single_item(cart_page_with_items, product_key, expected_badge_after):
    with allure.step(f"Eliminar el producto con key: {product_key}"):
        success = cart_page_with_items.remove_item(product_key)
    with allure.step("Verificar que el remove devolvió True"):
        assert success == True
    with allure.step("Obtener ítems restantes después del remove"):
        items_after = cart_page_with_items.get_cart_items()
    with allure.step("Obtener badge después del remove"):
        badge_after = cart_page_with_items.get_cart_badge_count()
    with allure.step("Verificar que el badge ahora muestra 1"):
        assert badge_after == expected_badge_after
    with allure.step(f"Verificar que el producto '{PRODUCTS[product_key]['display_name']}' ya no está"):
        assert PRODUCTS[product_key]["display_name"] not in items_after


def test_remove_all_items(cart_page_with_items):
    products = ["bike_light", "backpack"]
    with allure.step("Eliminar todos los productos del carrito"):
        for p in products:
            cart_page_with_items.remove_item(p)
    with allure.step("Verificar que no quedan ítems en el carrito"):
        assert len(cart_page_with_items.get_cart_items()) == 0
    with allure.step("Verificar que el badge muestra '0' o desapareció"):
        assert cart_page_with_items.get_cart_badge_count() == '0'


def test_start_checkout(cart_page_with_items):
    with allure.step("Verificar que el botón Checkout está visible"):
        assert cart_page_with_items.is_checkout_button_visible() == True
    with allure.step("Hacer click en Checkout"):
        cart_page_with_items.start_checkout()
    with allure.step("Verificar redirección a checkout-step-one.html"):
        assert "checkout-step-one.html" in cart_page_with_items.driver.current_url
    print(f"Current URL after checkout: {cart_page_with_items.driver.current_url}")


@pytest.mark.parametrize("first_name, last_name, postal_code", [("Juanito", "Alimana", "1969"), ("Procura", "Peralta", "1997")])
def test_full_e2e_checkout(cart_page_with_items, first_name, last_name, postal_code):
    with allure.step("Iniciar checkout desde carrito"):
        assert cart_page_with_items.is_checkout_button_visible() == True
        cart_page_with_items.start_checkout()
        assert "checkout-step-one.html" in cart_page_with_items.driver.current_url

    with allure.step("Llenar información de envío"):
        checkout = CheckoutPage(cart_page_with_items.driver)
        checkout.fill_info(first_name, last_name, postal_code)

    with allure.step("Continuar al overview"):
        assert checkout.continue_to_overview() == True
        assert "checkout-step-two.html" in checkout.driver.current_url

    with allure.step("Finalizar la compra"):
        assert checkout.complete_checkout() == True
        assert "checkout-complete.html" in checkout.driver.current_url
        assert "Thank you for your order!" in checkout.driver.page_source
        print(f"E2E complete with user {first_name} {last_name}, final URL: {checkout.driver.current_url}")

    allure.attach(cart_page_with_items.driver.get_screenshot_as_png(), name="Checkout Complete",
                  attachment_type=allure.attachment_type.PNG)