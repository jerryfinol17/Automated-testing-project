from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class InventoryPage:
    ADD_CART_BUTTON= (By.ID, 'add-to-cart-sauce-labs-bike-light')
    REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-bike-light')
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)



    def add_product_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(InventoryPage.ADD_CART_BUTTON))
        self.driver.find_element(*InventoryPage.ADD_CART_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(InventoryPage.REMOVE_BUTTON))

    def get_cart_badge_count(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.CART_BADGE))
            return self.driver.find_element(*self.CART_BADGE).text
        except TimeoutException:
            return "0"


    def go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(InventoryPage.CART_BUTTON))
        self.driver.find_element(*InventoryPage.CART_BUTTON).click()


