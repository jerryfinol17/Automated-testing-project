import pytest
import allure
from pages.login_page import LoginPage
from config import config_for_login_page


@pytest.fixture(scope="function")
def login_page(browser_driver, request):
    login_page = LoginPage(browser_driver)
    request.addfinalizer(browser_driver.quit)
    return login_page


def test_successful_login(login_page):
    with allure.step("Abrir página de login"):
        login_page.open_page()

    with allure.step("Ingresar username válido (standard_user)"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])

    with allure.step("Ingresar password válido"):
        login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])

    with allure.step("Hacer clic en el botón Login"):
        login_page.click_login_button()

    with allure.step("Verificar redirección exitosa al inventory"):
        assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"

    with allure.step("Cerrar sesión para limpieza del test"):
        login_page.logout()


def test_locked_out_user(login_page):
    with allure.step("Abrir página de login"):
        login_page.open_page()

    with allure.step("Ingresar credenciales de usuario bloqueado"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["locked_out_user"]["username"])
        login_page.insert_password(config_for_login_page.CREDENTIALS["locked_out_user"]["password"])

    with allure.step("Intentar hacer login"):
        login_page.click_login_button()

    with allure.step("Obtener mensaje de error"):
        error_message = login_page.get_error_message()
        print(f"error_message: {error_message}")

    with allure.step("Verificar mensaje de usuario bloqueado"):
        assert error_message == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_user(login_page):
    with allure.step("Abrir página de login"):
        login_page.open_page()

    with allure.step("Ingresar credenciales inválidas"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["invalid_user"]["username"])
        login_page.insert_password(config_for_login_page.CREDENTIALS["invalid_user"]["password"])

    with allure.step("Intentar hacer login"):
        login_page.click_login_button()

    with allure.step("Obtener mensaje de error"):
        error_message = login_page.get_error_message()
        print(f"error_message: {error_message}")

    with allure.step("Verificar mensaje de credenciales incorrectas"):
        assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_empty_user(login_page):
    with allure.step("Abrir página de login"):
        login_page.open_page()

    with allure.step("Dejar campos vacíos (o usar credenciales vacías del config)"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["empty_user"]["username"])
        login_page.insert_password(config_for_login_page.CREDENTIALS["empty_user"]["password"])

    with allure.step("Intentar hacer login sin usuario"):
        login_page.click_login_button()

    with allure.step("Obtener mensaje de error"):
        error_message = login_page.get_error_message()
        print(f"error_message: {error_message}")

    with allure.step("Verificar mensaje de campo obligatorio"):
        assert error_message == "Epic sadface: Username is required"