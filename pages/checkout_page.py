from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.url_contains("checkout-step-one"))
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME))
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        return True

    def continue_to_overview(self):
        try:
            continue_btn = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
            continue_btn.click()
            self.wait.until(EC.url_contains("checkout-step-two"))
            return True
        except TimeoutException:
            return False

    def complete_checkout(self):
        try:
            finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
            finish_btn.click()
            self.wait.until(EC.url_contains("checkout-complete"))
            return True
        except TimeoutException:
            return False