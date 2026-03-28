import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
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


@pytest.fixture(params=["firefox", "edge"], scope="class")
def browser_driver(request):
    driver = None
    browser_name = request.param

    if browser_name == "firefox":
        options = FirefoxOptions ()
        options.add_argument ("--headless")
        options.add_argument ("--disable-notifications")
        options.add_argument ("--disable-gpu")
        options.page_load_strategy = "normal"
        driver = webdriver.Firefox (options = options)

    elif browser_name == "edge":
        options = EdgeOptions ()
        options.add_argument ("--headless")
        options.add_argument ("--disable-notifications")
        options.add_argument ("--disable-gpu")
        options.add_experimental_option ("excludeSwitches" , ["enable-automation"])
        driver = webdriver.Edge (options = options)
    def fin():
        if driver:
            try:
                driver.quit()
            except Exception:
                pass

    request.addfinalizer(fin)
    yield driver