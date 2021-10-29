from pages.login_page import LoginPage
from pages.side_menu import SideMenu
from pages.forgot_password_page import ForgotPassword
from pages.alarm_control_page import AlarmControl


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.login_page = LoginPage(self.driver)
        self.side_menu = SideMenu(self.driver)
        self.forgot_password_page = ForgotPassword(self.driver)
        self.alarm_control_page = AlarmControl(self.driver)