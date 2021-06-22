from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class KnightDashboard:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def request_aid(self):
        element: WebElement = self.driver.find_element_by_id("send")
        return element

    def form(self):
        element: WebElement = self.driver.find_element_by_id("popup")
        return element

    def close_button(self):
        element: WebElement = self.driver.find_element_by_id("exit")
        return element

    def submit_button(self):
        element: WebElement = self.driver.find_element_by_id("submit")
        return element

    def amount(self):
        element: WebElement = self.driver.find_element_by_id("amount")
        return element

    def reason(self):
        element: WebElement = self.driver.find_element_by_id("reason")
        return element

