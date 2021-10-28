from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


password = "Gospod20123."

LIST_OF_EMAILS = (By.CSS_SELECTOR, "tr")

@when('Enter forgot username {username}')
def enter_username(context, username):
    context.app.forgot_password_page.enter_username(username)

@when('Enter Phone Number {phone_number}')
def enter_phone_number(context, phone_number):
    context.app.forgot_password_page.enter_phone_number(phone_number)

@when('Enter Email Address {email}')
def enter_email(context, email):
    context.app.forgot_password_page.enter_email(email)

@when('Click Next')
def click_next(context):
    context.app.forgot_password_page.click_next()

# @when('Click Back')
# def click_back(context):
#     context.app.forgot_password_page.click_back()

@when('Open Gmail {email}')
def open_gmail(context, email):
    wait = WebDriverWait(context.driver, 30)

    context.driver.get("https://gmail.com")
    gmail = context.driver.find_element(By.ID, "identifierId")
    gmail.send_keys(email)
    context.driver.find_element(By.ID, "identifierNext").click()
    context.driver.find_element(By.NAME, "email").send_keys(email)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "button[class*=LoginActionButton]").click()
    context.driver.find_element(By.XPATH, "//span[text()='Continue']").click()
    list_of_emails = context.driver.find_elements(*LIST_OF_EMAILS)
    list_of_emails[4].click()
    # for i in range(len(list_of_emails)):
    #     current_email = context.driver.find_elements(*LIST_OF_EMAILS)[i]
    #     email_text = current_email.text
    #     print(email_text)
    #     if "Password Reset" in email_text:
    #         current_email.click()
    #         break
    # #click on link from email
    current_window = context.driver.current_window_handle
    context.driver.find_element(By.CSS_SELECTOR, "div.h7.ie a[href*='7.95']").click()
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)








@then('Verify Email has been sent')
def verify_email_sent(context):
    context.app.forgot_password_page.email_sent_message()