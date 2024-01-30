# config_page.py
import logging

from selenium import webdriver

class ConfigPage:
    def __init__(self, browser='chrome'):
        self.browser = browser
        self.driver = self.setup_driver()
        self.base_url = 'https://practice.automationtesting.in/my-account/'  # Replace with your actual base URL

    logging.basicConfig(level=logging.INFO)

    def setup_driver(self):
        if self.browser == 'chrome':
            return webdriver.Chrome()
        elif self.browser == 'firefox':
            return webdriver.Firefox()

    def set_url(self, url):
        if self.driver:
            self.driver.get(url)
        else:
            print("Driver not initialized. Call setup_driver first.")

    def close_driver(self):
        if self.driver:
            self.driver.quit()