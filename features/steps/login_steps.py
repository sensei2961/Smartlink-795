from behave import given, when, then


@given('Open Login page')
def open_login_page(context):
    context.app.login_page.open_login_page()

@when('Enter username {username}')
def enter_username(context, username):
    context.app.login_page.enter_username(username)

@when('Enter password {password}')
def enter_password(context, password):
    context.app.login_page.enter_password(password)

@when('Click Login button')
def click_login_button(context):
    context.app.login_page.click_login_button()