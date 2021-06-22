from behave import given, when, then
from selenium.webdriver.firefox.webdriver import WebDriver
import time


@when('The Lord clicks the statistics button')
def click_statistics_button(context):
    context.lord_dashboard.stats().click()

@then('The Lord should be on the statistics page')
def click_statistics_button(context):
    time.sleep(1)
    assert "Statistics" == context.driver.title