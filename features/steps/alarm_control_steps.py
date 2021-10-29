from behave import given, when, then


@when('Click Arm Stay')
def click_arm_stay(context):
    context.app.alarm_control_page.click_arm_stay()

@when('Click Disarm')
def click_disarm(context):
    context.app.alarm_control_page.click_disarm()

@then('Panel is {expected_status}')
def panel_is_armed_stay(context, expected_status):
    context.app.alarm_control_page.panel_status(expected_status)