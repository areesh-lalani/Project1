from behave import given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver

@given('The Knight is on the Login Page')
def open_up_login_page(context):
    context.driver.get("file:///D:/Documents/Jobs/Revature/knight_login.html")

@when('The Knight enters their username')
def enter_username(context):
    user = context.login_page.username()
    user.click()
    user.clear()
    user.send_keys("uther")

@when('The Knight enters their password')
def enter_password(context):
    password = context.login_page.password()
    password.click()
    password.clear()
    password.send_keys("pendragon")

@when('The Knight clicks the login button')
def click_login_button(context):
    context.login_page.login_button().click();

@then('The Knight should be on the Knight Dashboard Page')
def verify_on_knight_dashboard(context):
    title = context.driver.title
    print(title)
    assert title == 'Knight Dashboard'