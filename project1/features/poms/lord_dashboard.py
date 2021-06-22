from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class LordDashboard:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def edit_button(self):
        element: WebElement = self.driver.find_element_by_class_name("editButton")
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

    def stats(self):
        element :WebElement = self.driver.find_element_by_id("stats")
        return element

    def approve(self):
        element:WebElement = self.driver.find_element_by_id("approve")
        return element

    def deny(self):
        element:WebElement = self.driver.find_element_by_id("deny")
        return element

    def message(self):
        element:WebElement = self.driver.find_element_by_id("message")
        return element
