from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time



class HomePage(BasePage):
    #  LOCATORS
    BROWSE_TAB = (By.CSS_SELECTOR, 'a[href="/directory"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    STREAMER = (By.CSS_SELECTOR, 'img[src*="live_user_"]')

    # cookies
    TOP_APP_DISMISS = (By.XPATH, "//button[contains(text(), 'Dismiss')]")
    COOKIE_ACCEPT_BTN = (By.XPATH, "//button[contains(., 'Accept')]")

    def go_to_twitch(self):
        self.open_url("https://m.twitch.tv")

    def accept_cookies(self):
        print("Handling popups...")
        self.handle_potential_popup(self.TOP_APP_DISMISS)
        self.handle_potential_popup(self.COOKIE_ACCEPT_BTN)
        time.sleep(1)

    def search_for_game(self, game_name):
        print("Clicking Browse Tab...")
        self.click(self.BROWSE_TAB)

        print("Waiting for Search Input...")
        self.find(self.SEARCH_INPUT)

        print(f"Entering {game_name}...")
        self.send_keys(self.SEARCH_INPUT, game_name)

        print("Waiting 2 seconds for dropdown")
        time.sleep(2)

        print(f"Clicking suggestion: {game_name}")
        SUGGESTION_LOCATOR = (By.CSS_SELECTOR, f'p[title="{game_name}"]')
        self.click(SUGGESTION_LOCATOR)

    def select_first_streamer(self):
        print("Waiting for streamer list to appear...")
        self.find(self.STREAMER)

        print("Scrolling down (2 times)...")
        self.scroll_down(times=2)

        print("Selecting a random streamer from the results...")
        thumbnails = self.driver.find_elements(*self.STREAMER)

        if len(thumbnails) > 0:
            target_streamer = thumbnails[-1]
            clickable_parent = target_streamer.find_element(By.XPATH, "./ancestor::button | ./ancestor::a")
            print(f"Clicking streamer (Tag: {clickable_parent.tag_name})...")
            self.driver.execute_script("arguments[0].click();", clickable_parent)
        else:
            raise Exception("No streamers found after scrolling!")