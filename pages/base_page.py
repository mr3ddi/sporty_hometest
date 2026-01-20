from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def scroll_down(self, times):
        body = self.driver.find_element(By.TAG_NAME, "body")
        for _ in range(times):
            body.send_keys(Keys.PAGE_DOWN)
            print("Scrolled down...")
            time.sleep(1)

    def handle_potential_popup(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
            self.click(locator)
        except TimeoutException:
            pass

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)