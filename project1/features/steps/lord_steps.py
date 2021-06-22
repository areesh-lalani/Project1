from behave import given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver
import time

@given('The Lord is on the Login Page')
def open_up_login_page(context):
    context.driver.get("file:///D:/Documents/Jobs/Revature/knight_login.html")

@when('The Lord enters their username')
def enter_username(context):
    user = context.login_page.username()
    user.click()
    user.clear()
    user.send_keys("arthur")

@when('The Lord enters their password')
def enter_password(context):
    password = context.login_page.password()
    password.click()
    password.clear()
    password.send_keys("excalibur")

@when('The Lord checks the lord button')
def check_lord(context):
    context.login_page.lord_checkbox().click()

@when('The Lord clicks the login button')
def click_login_button(context):
    context.login_page.login_button().click();

@then('The Lord should be on the Lord Dashboard Page')
def verify_on_lord_dashboard(context):
    time.sleep(1)
    assert "Lord Dashboard" == context.driver.title


