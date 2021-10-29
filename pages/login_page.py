from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.ID, "submit")
    INVALID_CREDENTIALS_ERROR = (By.CSS_SELECTOR, "div.error_box")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a.forgot-phrase-link")
    ACCOUNT_SELECTION_DIALOG = (By.ID,"#accountSelectionDialog")
    FIRST_ACCOUNT = (By.CSS_SELECTOR, ".selectAccount")

    def open_login_page(self):
        self.open_url('https://smartlink.secure.direct/7.95/html/login.php')

    def enter_username(self, username):
        self.input_text(username, *self.USERNAME_FIELD)

    def enter_invalid_username(self, invalid_username):
        self.input_text(invalid_username, *self.USERNAME_FIELD)

    def invalid_credentials_message(self):
        self.find_element(*self.INVALID_CREDENTIALS_ERROR)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)

    def click_forgot_password(self):
        self.click(*self.FORGOT_PASSWORD)



