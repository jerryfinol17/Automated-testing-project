from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import logging
from typing import Tuple, Optional

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

# ==============Element Finders ======================================
    def find_element(self, locator: Tuple[str, str]):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Element not found within {self.timeout} seconds: {locator}")
            raise
    def find_elements(self, locator: Tuple[str, str]):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"Element not found within {self.timeout} seconds: {locator}")
            raise

# =============Actions =======================================================

    def click(self, locator: Tuple[str, str]):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except (TimeoutException, ElementNotInteractableException):
            try:
                element = self.find_element(locator)
                self.driver.execute_script("arguments[0].click();", element)
                self.logger.info(f"Used JavaScript click for locator: {locator}")
            except Exception as e:
                self.logger.error(f"Failed to click element {locator}: {e}")
                raise

    def fill(self, locator: Tuple[str, str], text: str):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.error(f"Failed to fill text in {locator}: {e}")
            raise
    def get_text(self, locator: Tuple[str, str]) -> str:
        element = self.find_element(locator)
        return element.text.strip()

    def is_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> bool:
        try:
            wait_time = timeout or self.timeout
            WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.driver.current_url

    def go_to ( self , url: str ) :
        self.driver.get (url)
