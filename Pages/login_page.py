# pages/login_page.py
import logging
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Loactors.locators import LoginPageLocators
from Pages.Base import Base
from config.config_page import ConfigPage


class loginPage(Base):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')


    def __init__(self, config_page):
        super().__init__(config_page.driver)
        self.config_page = config_page
        self.logger = logging.getLogger(__name__)

    def open_login_page(self):
        self.config_page.set_url(self.config_page.base_url)
        self.logger.info(f"Opened login page with URL: {self.config_page.base_url}")

    def close_browser(self):
        self.config_page.close_driver()
        self.logger.info("Closed the browser")

    def wait_for_element_to_be_visible(self, locator, timeout=50):
        print("Before WebDriverWait")
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        print("After WebDriverWait")

    def wait_for_element_to_be_clickable(self, locator, timeout=50):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def enter_username(self, username):
        try:
            self.maximize_window()
            time.sleep(5)
            self.enter_text(self.USERNAME_FIELD, username)
            self.logger.info("Entered username successfully.")
        except TimeoutException:
            self.logger.error("TimeoutException: Element not visible. Unable to enter username.")
            raise

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_FIELD, password)
        self.logger.info("Enter Password")

    def click_login_button(self):
        #self.wait_for_element_to_be_clickable(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)
        self.logger.info("Clicked on login button")
