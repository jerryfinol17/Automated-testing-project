import pytest
import allure
from allure_commons.types import AttachmentType
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from config import config_for_login_page


@pytest.fixture(scope="function")
def inventory_page(browser_driver, request):
    login_page = LoginPage(browser_driver)
    with allure.step("Abrir página de login"):
        login_page.open_page()
    with allure.step("Ingresar credenciales de standard_user"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])
        login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])
    with allure.step("Hacer click en Login"):
        login_page.click_login_button()
    with allure.step("Verificar redirección al inventory"):
        assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
    inventory_page = InventoryPage(browser_driver)
    request.addfinalizer(browser_driver.quit)
    return inventory_page


def test_add_product_to_cart(inventory_page):
    with allure.step("Agregar 'bike_light' al carrito"):
        inventory_page.add_product("bike_light")
    with allure.step("Verificar que el badge del carrito muestre '1'"):
        badge_count = inventory_page.get_cart_badge_count()
        assert inventory_page.get_cart_badge_count() == "1"
        print(f"Badge count: {badge_count}")
    with allure.step("Ir al carrito"):
        inventory_page.go_to_cart()
    with allure.step("Verificar que 'Sauce Labs Bike Light' está en el carrito"):
        cart_page = CartPage(inventory_page.driver)
        items = cart_page.get_cart_items()
        assert "Sauce Labs Bike Light" in items, f"Expected 'Sauce Labs Bike Light' in cart, but got {items}"
        print(f"Items: {items}")
    with allure.step("Verificar que el botón Checkout está visible"):
        assert cart_page.is_checkout_button_visible(), "Checkout button is not visible"


def test_multi_add(inventory_page):
    products = ["bike_light", "backpack", "fleece_jacket"]
    with allure.step(f"Iniciar adición de {len(products)} productos al carrito"):
        inventory_page.add_multiple_products(products)

    with allure.step("Verificar badge del carrito actualizado"):
        badge = inventory_page.get_cart_badge_count()
        assert badge == "3"
        allure.attach(f"Badge final: {badge}", name="Badge Count", attachment_type=AttachmentType.TEXT)


@pytest.mark.parametrize("sort_option, expected_order", [("lohi", "asc"), ("hilo", "desc")])
def test_sort_order(inventory_page, sort_option, expected_order):
    with allure.step("Obtener precios antes de ordenar"):
        prices_before = inventory_page.get_prices()
    with allure.step(f"Aplicar ordenamiento: {sort_option}"):
        inventory_page.sort_by_price(sort_option)
    with allure.step("Obtener precios después de ordenar"):
        prices_after = inventory_page.get_prices()
    with allure.step("Verificar que hay 6 productos"):
        assert len(prices_after) == 6
    with allure.step("Verificar orden correcto (asc/desc)"):
        expected_sorted = sorted(prices_before, reverse=(expected_order == "desc"))
        assert prices_after == expected_sorted


def test_get_prices(inventory_page):
    with allure.step("Obtener lista de precios"):
        prices = inventory_page.get_prices()
    with allure.step("Verificar que hay exactamente 6 precios"):
        assert len(prices) == 6
    with allure.step("Verificar que todos son float"):
        assert all(isinstance(p, float) for p in prices)
    with allure.step("Verificar que ningún precio es menor o igual a 0"):
        assert min(prices) > 0


@pytest.mark.parametrize("viewport", [("desktop", 1920, 1080), ("mobile", 375, 667)])
@pytest.mark.responsive
def test_add_item_responsive(inventory_page, viewport):
    name, w, h = viewport
    with allure.step(f"Resize a {name} viewport({w}x{h})"):
        inventory_page.driver.set_window_size(w, h)
    product_key = 'bike_light'
    with allure.step(f"Check add button is visible on {name}"):
        visible = inventory_page.is_add_button_visible(product_key)
        assert visible, f"Not visible on {name}"
        allure.attach(str(visible), name="Visibility Check", attachment_type=AttachmentType.TEXT)
    with allure.step(f"add product {product_key}"):
        inventory_page.add_product(product_key)
    with allure.step("Check Badge=1"):
        badge = inventory_page.get_cart_badge_count()
        assert badge == "1", f"Expected '1', got {badge} en {name}"
        print(f"{name}: {badge}")
        allure.attach(badge, name="Badge Count", attachment_type=AttachmentType.TEXT)