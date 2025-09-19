from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_cart_items(self):
        self.wait.until(EC.presence_of_all_elements_located(CartPage.CART_ITEMS))
        items = self.driver.find_elements(*CartPage.CART_ITEMS)
        item_name = [item.find_element(*self.ITEM_NAME).text for item in items]
        return item_name


    def is_checkout_button_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(CartPage.CHECKOUT_BUTTON))
            return True
        except TimeoutException:
            return False

