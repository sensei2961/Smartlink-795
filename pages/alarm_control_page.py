from selenium.webdriver.common.by import By
from pages.base_page import Page
import time


class AlarmControl(Page):

    STATUS = (By.CSS_SELECTOR, "div.alert_status_text")
    ARM_STAY = (By.ID, "armedStay_icon")
    ARMED_AWAY = (By.ID, "armedAway_icon")
    NIGHT_ARM = (By.ID, "nightArm_icon")
    DISARM = (By.ID, "disarm_icon")
    SILENT_BUTTON = (By.CSS_SELECTOR, "div.silentOption .iconText")
    DELAY_BUTTON = (By.CSS_SELECTOR, "div.delayOption .iconText")
    REFRESH = (By.ID, "refresh_button")
    GLOBAL_CHIME_TOGGLE = (By.ID, "global-chime")

    def click_arm_stay(self):
        self.wait_for_element_click(*self.ARM_STAY)

    def panel_status(self, expected_status):
        time.sleep(60)
        status_text = self.find_element(*self.STATUS).text
        assert expected_status in status_text, f'Incorrect Status'

    def click_disarm(self):
        self.wait_for_element_click(*self.DISARM)
