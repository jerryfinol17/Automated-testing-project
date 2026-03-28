from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.Base_Page import BasePage
from config.locators import INVENTORY
from config.config_for_inventory_page import PRODUCTS


class InventoryPage (BasePage) :

	def add_product ( self , product_key: str ) -> bool :
		if product_key not in PRODUCTS :
			self.logger.warning (f"Product key '{product_key}' not found in PRODUCTS config")
			return False

		add_selector = PRODUCTS[product_key]["add"]

		try :
			self.click (add_selector)
			remove_selector = PRODUCTS[product_key]["remove"]
			self.wait.until (EC.visibility_of_element_located (remove_selector))

			self.logger.info (f"Product '{product_key}' added to cart successfully")
			return True
		except Exception as e :
			self.logger.error (f"Failed to add product '{product_key}': {e}")
			return False

	def add_multiple_products ( self , products_list: list ) -> bool :
		if not products_list :
			return True

		expected_count = len (products_list)

		for product in products_list :
			self.add_product (product)

		try :
			self.wait.until (EC.text_to_be_present_in_element (
				INVENTORY["SHOPPING_CART_BADGE"] ,
				str (expected_count)
			))
			self.logger.info (f"Successfully added {expected_count} products to cart")
			return True
		except TimeoutException as e :
			self.logger.error (f"Cart badge did not update to {expected_count}: {e}")
			return False

	def get_cart_badge_count ( self ) -> str :
		try :
			self.wait.until (EC.presence_of_element_located (INVENTORY["SHOPPING_CART_BADGE"]))
			return self.driver.find_element (*INVENTORY["SHOPPING_CART_BADGE"]).text
		except TimeoutException :
			return "0"

	def go_to_cart ( self ) -> bool :
		try :
			self.click (INVENTORY["SHOPPING_CART_LINK"])
			self.logger.info ("Navigated to cart page")
			return True
		except Exception as e :
			self.logger.error (f"Failed to go to cart: {e}")
			return False

	def sort_by_price ( self , option_value: str ) -> bool :
		try :
			self.click (INVENTORY["SORT_DROPDOWN"])
			option_locator = (By.CSS_SELECTOR , f'select option[value="{option_value}"]')
			option = self.wait.until (EC.element_to_be_clickable (option_locator))
			option.click ()
			self.wait.until (EC.presence_of_element_located (INVENTORY["PRICE_SELECTOR"]))

			self.logger.info (f"Products sorted by price option: {option_value}")
			return True
		except Exception as e :
			self.logger.error (f"Failed to sort by price '{option_value}': {e}")
			return False

	def get_prices ( self ) -> list[float] :
		try :
			price_elements = self.find_elements (INVENTORY["PRODUCT_PRICE"])
			prices = []
			for elem in price_elements :
				price_text = elem.text.strip ()
				price = float (price_text.replace ("$" , "").replace ("," , ""))
				prices.append (price)
			return prices
		except Exception as e :
			self.logger.error (f"Failed to get prices: {e}")
			return []

	def is_add_button_visible ( self , product_key: str ) -> bool :
		if product_key not in PRODUCTS :
			return False

		add_selector = PRODUCTS[product_key]["add"]
		return self.is_visible (add_selector)