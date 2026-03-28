from selenium.webdriver.support import expected_conditions as EC
from pages.Base_Page import BasePage
from config.locators import LOGIN
class LoginPage (BasePage) :
    def open_page ( self ) :
        self.go_to ("https://www.saucedemo.com/")
        self.wait.until (EC.visibility_of_element_located (LOGIN["LOGIN_BUTTON"]))
        self.logger.info ("Login page opened successfully")
    def login ( self , username: str , password: str ) -> bool :
        try :
            self.fill (LOGIN["USERNAME_INPUT"] , username)
            self.fill (LOGIN["PASSWORD_INPUT"] , password)
            self.click (LOGIN["LOGIN_BUTTON"])
            self.logger.info (f"Login attempted with user: {username}")
            return True
        except Exception as e :
            self.logger.error (f"Login failed for user {username}: {e}")
            return False
    def get_error_message ( self ) -> str :
        try :
            return self.get_text (LOGIN["ERROR_MESSAGE"])
        except Exception :
            return ""
    def is_error_message_visible ( self ) -> bool :
        return self.is_visible (LOGIN["ERROR_MESSAGE"])
    def logout ( self ) -> None :
            self.click (LOGIN["BURGER_MENU_BUTTON"])
            self.click (LOGIN["LOGOUT_LINK"])
            self.wait.until (EC.visibility_of_element_located (LOGIN["LOGIN_BUTTON"]))
    def is_login_button_visible ( self ) -> bool :
        return self.is_visible (LOGIN["LOGIN_BUTTON"])



