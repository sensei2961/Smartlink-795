from selenium.webdriver.common.by import By
from pages.base_page import Page

class ForgotPassword(Page):

    USERNAME = (By.NAME, "username")
    PHONE_NUMBER = (By.NAME, "phone_number")
    EMAIL = (By.NAME, "email_address")
    BACK = (By.NAME, "form[back]")
    NEXT = (By.NAME, "form[next]")
    EMAIL_SENT_MESSAGE = (By.CSS_SELECTOR, "div.notice_box")

    def enter_username(self, username):
        self.input_text(username, *self.USERNAME)

    def enter_phone_number(self, phone_number):
        self.input_text(phone_number, *self.PHONE_NUMBER)

    def enter_email(self, email):
        self.input_text(email, *self.EMAIL)

    def click_next(self):
        self.click(*self.NEXT)

    def click_back(self):
        self.click(*self.BACK)

    def email_sent_message(self):
        self.find_element(*self.EMAIL_SENT_MESSAGE)
