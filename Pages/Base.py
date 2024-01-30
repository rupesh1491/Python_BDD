# pages/base_page.py
from selenium.common import NoSuchWindowException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        self.logger.info(f"Clicked on element with locator: {locator}")

    def enter_text(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            assert element.get_attribute("value") == text, "Entered text doesn't match"
            self.logger.info(f"Entered text '{text}' in element with locator: {locator}")
        except Exception as e:
            self.logger.error(f"An error occurred while entering text: {e}")
            raise

    def maximize_window(self):
        self.driver.maximize_window()
        self.logger.info("Window maximized successfully")

    def select_dropdown_option_by_visible_text(self, locator, option_text):
        select = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)))
        select.select_by_visible_text(option_text)
        self.logger.info(
            f"Selected dropdown option '{option_text}' by visible text from element with locator: {locator}")

    def switch_to_frame(self, frame_locator):
        frame = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
        self.logger.info(f"Switched to frame with locator: {frame_locator}")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        self.logger.info("Switched back to the default content")

    def switch_to_window_by_index(self, window_index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[window_index])
        self.logger.info(f"Switched to window with index: {window_index}")

    def switch_to_window_by_title(self, window_title):
        current_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if window_title in self.driver.title:
                self.logger.info(f"Switched to window with title: {window_title}")
                return
        self.driver.switch_to.window(current_handle)
        raise NoSuchWindowException(f"Window with title '{window_title}' not found.")

    def verify_title(self, expected_title):
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Title mismatch. Expected: '{expected_title}', Actual: '{actual_title}'"
        self.logger.info(f"Title verified: '{expected_title}'")

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"URL mismatch. Expected: '{expected_url}', Actual: '{actual_url}'"
        self.logger.info(f"URL verified: '{expected_url}'")

    def verify_text(self, locator, expected_text):
        actual_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f"Text mismatch. Expected: '{expected_text}', Actual: '{actual_text}'"
        self.logger.info(f"Text verified: '{expected_text}'")