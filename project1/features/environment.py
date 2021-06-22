from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from poms.login_page import LoginPage
from poms.knight_dashboard import KnightDashboard
from poms.lord_dashboard import LordDashboard

def before_all(context: Context):
    context.driver = webdriver.Firefox(executable_path=r'D:\Programs\Drivers\geckodriver.exe')
    context.driver.implicitly_wait(10)
    context.login_page = LoginPage(context.driver)
    context.knight_dashboard = KnightDashboard(context.driver)
    context.lord_dashboard = LordDashboard(context.driver)

def after_all(context):
    context.driver.quit()