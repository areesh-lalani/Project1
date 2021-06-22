from behave import given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver

@when("The Lord clicks a view request button")
def view_request(context):
    context.lord_dashboard.edit_button().click()

@then("The view request form should appear")
def verify_form(context):
    assert "active" in context.knight_dashboard.form().get_attribute("class")

@when("The Lord clicks the approve button")
def approve(context):
    radio = context.lord_dashboard.approve().click()

@when("The Lord clicks the deny button")
def deny(context):
    radio = context.lord_dashboard.deny().click()

@when("The Lord clicks the submit button")
def submit(context):
    context.lord_dashboard.submit_button().click()

@then("The edit form should close")
def close_form(context):
    assert "active" not in context.lord_dashboard.form().get_attribute("class")

@when("The Lord leaves a message")
def message(context):
    message_text = context.lord_dashboard.message()
    message_text.click()
    message_text.clear()
    message_text.send_keys("You are being tested")

