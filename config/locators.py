
from selenium.webdriver.common.by import By

# ==================== LOGIN PAGE ====================
LOGIN = {
    "USERNAME_INPUT": (By.ID, "user-name"),
    "PASSWORD_INPUT": (By.ID, "password"),
    "LOGIN_BUTTON": (By.ID, "login-button"),
    "ERROR_MESSAGE": (By.CSS_SELECTOR, "[data-test='error']"),
    "SWAG_LABS_LOGO": (By.CLASS_NAME, "login_logo"),
    "BURGER_MENU_BUTTON": (By.ID, "react-burger-menu-btn"),
    "LOGOUT_LINK": (By.CSS_SELECTOR, "[data-test='logout-sidebar-link']"),
}

# ==================== INVENTORY PAGE ====================
INVENTORY = {
    "TITLE": (By.CLASS_NAME, "title"),
    "PRIMARY_HEADER": (By.CSS_SELECTOR, "[data-test='primary-header']"),
    "SHOPPING_CART_LINK": (By.CSS_SELECTOR, "[data-test='shopping-cart-link']"),
    "SHOPPING_CART_BADGE": (By.CLASS_NAME, "shopping_cart_badge"),
    "BURGER_MENU_BUTTON": (By.ID, "react-burger-menu-btn"),
    "CROSS_BURGER_BUTTON": (By.ID, "react-burger-cross-btn"),
    "SORT_DROPDOWN": (By.CLASS_NAME, "product_sort_container"),
    "PRODUCT_ITEM": (By.CLASS_NAME, "inventory_item"),
    "PRODUCT_NAME": (By.CLASS_NAME, "inventory_item_name"),
    "PRODUCT_PRICE": (By.CLASS_NAME, "inventory_item_price"),
    "PRODUCT_DESCRIPTION": (By.CSS_SELECTOR, "[data-test='inventory-item-desc']"),
    "ADD_TO_CART_PREFIX": (By.CSS_SELECTOR, "[data-test^='add-to-cart-']"),
}

# ==================== CART PAGE ====================
CART = {
    "TITLE": (By.CSS_SELECTOR, "[data-test='title']"),
    "CART_ITEMS": (By.CLASS_NAME, "cart_item"),
    "ITEM_NAME": (By.CLASS_NAME, "inventory_item_name"),
    "CHECKOUT_BUTTON": (By.ID, "checkout"),
    "CONTINUE_SHOPPING_BTN": (By.CSS_SELECTOR, "[data-test='continue-shopping']"),
    "SHOPPING_CART_BADGE": (By.CLASS_NAME, "shopping_cart_badge"),
    "REMOVE_BTN_PREFIX": (By.CSS_SELECTOR, "[data-test^='remove-']"),
    "CART_QUANTITY": (By.CSS_SELECTOR, "[data-test='item-quantity']"),
}

# ==================== CHECKOUT PAGE ====================
CHECKOUT = {
    # Step One
    "FIRST_NAME": (By.ID, "first-name"),
    "LAST_NAME": (By.ID, "last-name"),
    "ZIP_CODE": (By.ID, "postal-code"),
    "CONTINUE_BUTTON": (By.ID, "continue"),
    "CANCEL_BUTTON": (By.CSS_SELECTOR, "[data-test='cancel']"),
    "ERROR_MESSAGE": (By.CSS_SELECTOR, "[data-test='error']"),

    # Step Two (Overview)
    "PAYMENT_INFO_LABEL": (By.CSS_SELECTOR, "[data-test='payment-info-label']"),
    "PAYMENT_INFO_VALUE": (By.CSS_SELECTOR, "[data-test='payment-info-value']"),
    "SHIPPING_INFO_LABEL": (By.CSS_SELECTOR, "[data-test='shipping-info-label']"),
    "SHIPPING_INFO_VALUE": (By.CSS_SELECTOR, "[data-test='shipping-info-value']"),
    "TOTAL_INFO_LABEL": (By.CSS_SELECTOR, "[data-test='total-info-label']"),
    "SUBTOTAL_LABEL": (By.CLASS_NAME, "summary_subtotal_label"),
    "TAX_LABEL": (By.CLASS_NAME, "summary_tax_label"),
    "TOTAL_LABEL": (By.CLASS_NAME, "summary_total_label"),
    "FINISH_BUTTON": (By.ID, "finish"),

    # Step Three (Complete)
    "COMPLETE_HEADER": (By.CSS_SELECTOR, "[data-test='complete-header']"),
    "COMPLETE_TEXT": (By.CSS_SELECTOR, "[data-test='complete-text']"),
    "BACK_HOME_BUTTON": (By.CSS_SELECTOR, "[data-test='back-to-products']"),
}