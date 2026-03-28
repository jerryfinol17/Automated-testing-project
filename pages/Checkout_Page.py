from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_Page import BasePage
from config.locators import CHECKOUT


class CheckoutPage(BasePage):

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> bool:
        try:
            self.wait.until(EC.url_contains("checkout-step-one"))

            self.fill(CHECKOUT["FIRST_NAME"], first_name)
            self.fill(CHECKOUT["LAST_NAME"], last_name)
            self.fill(CHECKOUT["ZIP_CODE"], postal_code)

            self.logger.info(f"Checkout info filled: {first_name} {last_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to fill checkout info: {e}")
            return False

    def continue_to_overview(self) -> bool:
        try:
            self.click(CHECKOUT["CONTINUE_BUTTON"])
            self.wait.until(EC.url_contains("checkout-step-two"))
            self.logger.info("Navigated to checkout overview (step two)")
            return True
        except TimeoutException as e:
            self.logger.error(f"Failed to continue to overview: {e}")
            return False

    def complete_checkout(self) -> bool:
        try:
            self.click(CHECKOUT["FINISH_BUTTON"])
            self.wait.until(EC.url_contains("checkout-complete"))
            self.logger.info("Checkout completed successfully")
            return True
        except TimeoutException as e:
            self.logger.error(f"Failed to complete checkout: {e}")
            return False

    def is_complete_header_visible(self) -> bool:
        return self.is_visible(CHECKOUT["COMPLETE_HEADER"])

    def get_complete_header_text(self) -> str:
        return self.get_text(CHECKOUT["COMPLETE_HEADER"])