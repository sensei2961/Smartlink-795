from behave import given, when, then


@given('Open Login page')
def open_login_page(context):
    context.app.login_page.open_login_page()

@when('Enter username {username}')
def enter_username(context, username):
    context.app.login_page.enter_username(username)

@when('Enter invalid username {invalid_username}')
def enter_invalid_username(context, invalid_username):
    context.app.login_page.enter_invalid_username(invalid_username)

@when('Enter password {password}')
def enter_password(context, password):
    context.app.login_page.enter_password(password)

@when('Click Login button')
def click_login_button(context):
    context.app.login_page.click_login_button()

@when('Click Forgot Password')
def click_forgot_password(context):
    context.app.login_page.click_forgot_password()

@when('Login {username}/{password}')
def login(context, username, password):
    context.app.login_page.enter_username(username)
    context.app.login_page.enter_password(password)
    context.app.login_page.click_login_button()

@then('Verify User can Log in')
def verify_user_can_log_in(context):
    context.app.side_menu.verify_user_can_log_in()

@then('User receives bad credentials error')
def user_receives_bad_credentials_error(context):
    context.app.login_page.invalid_credentials_message()