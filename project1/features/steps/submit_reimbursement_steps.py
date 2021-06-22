from behave import given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver


@when("The Knight clicks the new request button")
def new_request(context):
    context.knight_dashboard.request_aid().click()

@then("The request form should appear")
def verify_form(context):
    assert "active" in context.knight_dashboard.form().get_attribute("class")

@when("The Knight enters their requested amount")
def enter_amount(context):
    amount = context.knight_dashboard.amount()
    amount.click()
    amount.clear()
    amount.send_keys("75")

@when("The Knight enters the reason for their request")
def enter_reason(context):
    reason = context.knight_dashboard.reason()
    reason.click()
    reason.clear()
    reason.send_keys("Keeping the Peace")

@when("The Knight clicks the submit button")
def submit(context):
    context.knight_dashboard.submit_button().click()

@when("The Knight clicks the close button")
def close(context):
    context.knight_dashboard.close_button().click()


@then("The form should close")
def verify_form_closed(context):
    assert "active" not in context.knight_dashboard.form().get_attribute("class")

