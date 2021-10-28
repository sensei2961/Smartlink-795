from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideMenu(Page):
    WELCOME_MESSAGE = (By.CSS_SELECTOR, 'div.lite-welcome-msg')
    ALARM_CONTROL = (By.CSS_SELECTOR, "a[href*='alarm_control']")
    ZONES = (By.CSS_SELECTOR, "a[href*='sensors']")
    LIVE_VIDEO = (By.CSS_SELECTOR, "a.menu_item_account_lite_video")
    RECORDINGS = (By.CSS_SELECTOR, "a.menu_item_account_lite_video_archive")
    CAMERA_SETTINGS = (By.CSS_SELECTOR, "a[href*='camera_settings']")
    DEVICE_CONTROL = (By.CSS_SELECTOR, "a[href*='device_control']")
    DEVICE_SETTINGS = (By.CSS_SELECTOR, "a[href*='device_update']")
    PERSONALIZE_SCENE = (By.CSS_SELECTOR, "a[href*='scene_setup']")
    EVENT_SCHEDULE = (By.CSS_SELECTOR, "a[href*='scene_schedule']")
    ACCOUNT_DETAILS = (By.CSS_SELECTOR, "a[href*='lite_details']")
    PROPERTY_DETAILS = (By.CSS_SELECTOR, "a[href*='lite_property_details']")
    USERS = (By.CSS_SELECTOR, "a[href*='contacts']")
    ACTIVITY = (By.CSS_SELECTOR, "a[href*='lite_history']")
    SWITCH_ACCOUNT = (By.ID, 'switchAccount')
    LOGOUT = (By.CSS_SELECTOR, "a[href*='logout']")
    VERSION = (By.CSS_SELECTOR, "div.lite-menu-version-box")

    def verify_user_can_log_in(self):
        self.find_element(*self.WELCOME_MESSAGE)