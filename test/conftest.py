import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.firefox import GeckoDriverManager
import allure


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get("browser_driver")
        if driver:
            try:
                screenshot_dir = "../screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
                driver.save_screenshot(screenshot_path)
                if "allure" in globals():
                    allure.attach(driver.get_screenshot_as_png(),
                                  name=f"screenshot on fail: {item.name}",
                                  attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(f"Error en screenshot: {e}")


@pytest.fixture(params=["firefox", "edge"], scope="function")
def browser_driver(request):
    driver = None
    browser_name = request.param

    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        firefox_options.add_argument("--headless")
        firefox_options.set_preference("security.password_lifetime", 0)
        firefox_options.set_preference("signon.rememberSignons", False)
        firefox_options.set_preference("signon.autofillForms", False)
        firefox_options.set_preference("privacy.trackingprotection.enabled", True)
        firefox_options.set_preference("dom.disable_open_during_load", True)
        firefox_options.page_load_strategy = 'normal'
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )

    elif browser_name == "edge":
        edge_options = EdgeOptions()

        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-popup-blocking")
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")

        prefs = {
            "profile.password_manager_enabled": False,
            "credentials_enable_service": False,
            "profile.default_content_setting_values.notifications": 2,
        }

        edge_options.add_experimental_option("prefs", prefs)
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Edge(options=edge_options)
    def fin():
        if driver:
            try:
                driver.quit()
            except Exception:
                pass

    request.addfinalizer(fin)
    yield driver