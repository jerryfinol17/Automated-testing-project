from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from config.config_for_cart_page import PRODUCTS
from selenium.common.exceptions import NoSuchElementException
class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_cart_items(self):
        try:
            self.wait.until(EC.presence_of_all_elements_located(CartPage.CART_ITEMS))
        except TimeoutException:
            return []
        present_items = []
        for product_key in PRODUCTS:
            try:
                remove_selector = PRODUCTS[product_key]['remove']
                self.driver.find_element(*remove_selector)
                present_items.append(PRODUCTS[product_key]['display_name'])
            except NoSuchElementException:
                pass
        return present_items


    def get_cart_badge_count(self):
        try:
            self.wait.until(EC.presence_of_element_located(CartPage.CART_BADGE))
            return self.driver.find_element(*CartPage.CART_BADGE).text
        except TimeoutException:
            return "0"


    def is_checkout_button_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(CartPage.CHECKOUT_BUTTON))
            return True
        except TimeoutException:
            return False


    def remove_item(self,product_key):
        if PRODUCTS[product_key]['display_name'] not in self.get_cart_items():
            print(f'Product {product_key} not found.')
            return False

        remove_selector= PRODUCTS[product_key]['remove']
        try:
            remove_button = self.wait.until(EC.element_to_be_clickable(remove_selector))
            remove_button.click()
            self.wait.until(EC.staleness_of(remove_button))
            print(f"Product '{product_key}' removed, new badge: {self.get_cart_badge_count()}")
            return True
        except (StaleElementReferenceException,TimeoutException):
            return False

    def start_checkout(self):
        if not self.is_checkout_button_visible():
            return False
        checkout_button = self.wait.until(EC.element_to_be_clickable(CartPage.CHECKOUT_BUTTON))
        checkout_button.click()
        try:
            self.wait.until(EC.url_contains("checkout-step-one"))
            return True
        except TimeoutException:
            return False
