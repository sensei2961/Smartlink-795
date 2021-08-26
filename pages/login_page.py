from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.ID, "submit")

    def open_login_page(self):
        self.open_url('https://smartlink.secure.direct/7.95/html/login.php')

    def enter_username(self, username):
        self.input_text(username, *self.USERNAME_FIELD)

    def enter_password(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def click_login_button(self):
        self.click(*self.LOGIN_BUTTON)