from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")
        self.wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON))


    def insert_user_name(self, username):
        self.wait.until(EC.visibility_of_element_located(LoginPage.USER_NAME))
        element = self.driver.find_element(*LoginPage.USER_NAME)
        element.clear()
        element.send_keys(username)


    def insert_password(self, password):
        self.wait.until(EC.visibility_of_element_located(LoginPage.PASSWORD))
        element = self.driver.find_element(*LoginPage.PASSWORD)
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON))
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()


    def get_error_message(self):
        self.wait.until(EC.visibility_of_element_located(LoginPage.ERROR_MESSAGE))
        return self.driver.find_element(*LoginPage.ERROR_MESSAGE).text

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(LoginPage.MENU_BUTTON))
        self.driver.find_element(*LoginPage.MENU_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(LoginPage.LOGOUT_BUTTON))
        self.driver.find_element(*LoginPage.LOGOUT_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON))





