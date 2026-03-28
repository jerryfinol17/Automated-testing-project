from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException , NoSuchElementException , ElementNotInteractableException , \
    StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from pages.Base_Page import BasePage
from config.locators import CART
from config.config_for_cart_page import PRODUCTS
class CartPage(BasePage):

    def get_cart_items ( self ) -> list :
        try :
            self.wait.until (EC.presence_of_all_elements_located (CART["CART_ITEMS"]))
        except TimeoutException :
            return []

        present_items = []
        for product_key in PRODUCTS :
            try :
                remove_selector = PRODUCTS[product_key]['remove']
                self.driver.find_element (*remove_selector)
                present_items.append (PRODUCTS[product_key]['display_name'])
            except NoSuchElementException :
                pass
        return present_items

    def get_cart_badge_count ( self ) -> str :
        try :
            self.wait.until (EC.presence_of_element_located (CART["SHOPPING_CART_BADGE"]))
            return self.driver.find_element (*CART["SHOPPING_CART_BADGE"]).text
        except TimeoutException :
            return "0"

    def is_checkout_button_visible ( self ) -> bool :
        return self.is_visible (CART["CHECKOUT_BUTTON"])

    def remove_item ( self , product_key: str ) -> bool :
        if PRODUCTS[product_key]['display_name'] not in self.get_cart_items () :
            self.logger.warning (f"Product '{product_key}' not found in cart.")
            return False

        remove_selector = PRODUCTS[product_key]['remove']

        try :
            self.click (remove_selector)
            remove_button = self.find_element (remove_selector)
            self.wait.until (EC.staleness_of (remove_button))

            self.logger.info (
                f"Product '{product_key}' removed successfully. New badge: {self.get_cart_badge_count ()}")
            return True
        except (TimeoutException , StaleElementReferenceException) as e :
            self.logger.error (f"Failed to remove product '{product_key}': {e}")
            return False

    def start_checkout ( self ) -> bool :
        if not self.is_checkout_button_visible () :
            self.logger.warning ("Checkout button is not visible")
            return False

        try :
            self.click (CART["CHECKOUT_BUTTON"])
            self.wait.until (EC.url_contains ("checkout-step-one"))
            return True
        except TimeoutException :
            self.logger.error ("Failed to navigate to checkout step one")
            return False