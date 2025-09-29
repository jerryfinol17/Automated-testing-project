import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from webdriver_manager.firefox import GeckoDriverManager
from config import config_for_login_page

#realiza pruebas a diario, y escribe codigo para mejorar.


@pytest.fixture(scope="function")
def login_page(request):
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")
    firefox_options.add_argument("--headless")
    firefox_options.set_preference("security.password_lifetime", 0)
    firefox_options.set_preference("signon.rememberSignons", False)
    firefox_options.set_preference("signon.autofillForms", False)
    firefox_options.set_preference("privacy.trackingprotection.enabled", True)
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
    login_page = LoginPage(driver)
    request.addfinalizer(driver.quit)
    return login_page


def test_successful_login(login_page):
    with allure.step("Abrir página de login"):
        login_page.open_page()

    with allure.step("Ingresar username válido"):
        login_page.insert_user_name(config_for_login_page.CREDENTIALS["standard_user"]["username"])

    with allure.step("Ingresar password válido"):
        login_page.insert_password(config_for_login_page.CREDENTIALS["standard_user"]["password"])

    with allure.step("Hacer clic en login y verificar redirección"):
        login_page.click_login_button()
        assert login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"

    with allure.step("Cerrar sesión para cleanup"):
        login_page.logout()

def test_locked_out_user(login_page):
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["locked_out_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["locked_out_user"]["password"])
    login_page.click_login_button()
    error_message= login_page.get_error_message()
    print(f"error_message: {error_message}")
    assert error_message == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_user(login_page):
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["invalid_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["invalid_user"]["password"])
    login_page.click_login_button()
    error_message= login_page.get_error_message()
    print(f"error_message: {error_message}")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_empty_user(login_page):
    login_page.open_page()
    login_page.insert_user_name(config_for_login_page.CREDENTIALS["empty_user"]["username"])
    login_page.insert_password(config_for_login_page.CREDENTIALS["empty_user"]["password"])
    login_page.click_login_button()
    error_message= login_page.get_error_message()
    print(f"error_message: {error_message}")
    assert error_message == "Epic sadface: Username is required"






