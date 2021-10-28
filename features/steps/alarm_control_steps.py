from behave import given, when, then


@when('Click Arm Stay')
def click_arm_stay(context):
    context.app.alarm_control_page.click_arm_stay()


@then('Panel is Armed Stay')
def panel_is_armed_stay(context):
