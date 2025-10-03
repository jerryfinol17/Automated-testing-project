from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.config_for_inventory_page import PRODUCTS

class InventoryPage:
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRICE_SELECTOR = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_product(self, product_key):
        add_selector = PRODUCTS[product_key]["add"]
        self.wait.until(EC.visibility_of_element_located(add_selector))
        self.driver.find_element(*add_selector).click()
        remove_selector = PRODUCTS[product_key]["remove"]
        self.wait.until(EC.visibility_of_element_located(remove_selector))

    def add_multiple_products(self, products_list):
        if len(products_list) == 0:
            return
        expected_count = len(products_list)
        for product in products_list:
            self.add_product(product)
        self.wait.until(EC.text_to_be_present_in_element(InventoryPage.CART_BADGE, str(expected_count)))

    def get_cart_badge_count(self):
        try:
            self.wait.until(EC.presence_of_element_located(InventoryPage.CART_BADGE))
            return self.driver.find_element(*InventoryPage.CART_BADGE).text
        except TimeoutException:
            return "0"

    def go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(InventoryPage.CART_BUTTON))
        self.driver.find_element(*InventoryPage.CART_BUTTON).click()

    def sort_by_price(self, option_value):
        self.wait.until(EC.visibility_of_element_located(InventoryPage.SORT_DROPDOWN))
        self.driver.find_element(*InventoryPage.SORT_DROPDOWN).click()
        option= self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'select option[value="{option_value}"]')))
        option.click()
        self.wait.until(EC.presence_of_element_located(InventoryPage.PRICE_SELECTOR))

    def get_prices(self):
        prices_elements= self.driver.find_elements(*InventoryPage.PRICE_SELECTOR)
        prices = []
        for elem in prices_elements:
            price_text = elem.text
            price = float(price_text.replace("$", ""))
            prices.append(price)
        return prices

    def is_add_button_visible(self, product_key):
        add_selector = PRODUCTS[product_key]["add"]
        try:
            add_button = self.wait.until(EC.visibility_of_element_located(add_selector))
            return add_button.is_displayed()
        except TimeoutException:
            return False

