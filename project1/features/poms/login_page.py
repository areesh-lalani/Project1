from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        element: WebElement = self.driver.find_element_by_id("user")
        return element

    def password(self):
        element: WebElement = self.driver.find_element_by_id("pass")
        return element

    def login_button(self):
        element: WebElement = self.driver.find_element_by_id("loginButton")
        return element

    def lord_checkbox(self):
        element: WebElement = self.driver.find_element_by_id("lord")
        return element