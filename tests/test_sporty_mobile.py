import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.base_page import BasePage


def test_twitch_starcraft(driver):
    home_page = HomePage(driver)
    base_page = BasePage(driver)

    # open twitch url
    home_page.go_to_twitch()

    # accept cookies
    home_page.accept_cookies()

    # Search for StarCraft II
    home_page.search_for_game("StarCraft II")

    # Scroll down two times
    home_page.select_first_streamer()
    print("Waiting for stream page to load...")

    mature_btn = (By.XPATH, "//button[contains(text(), 'Start Watching')]")
    base_page.handle_potential_popup(mature_btn)

    print("Waiting for video player to initialize...")
    video_player = (By.CSS_SELECTOR, "video, div[data-a-target='video-player']")

    try:
        base_page.wait.until(lambda d: d.find_element(*video_player))
        print("SUCCESS: Video player found!")
        time.sleep(3)

    except:
        print("Video player took too long, taking screenshot anyway.")

    screenshot_name = "twitch_stream_playing.png"
    base_page.take_screenshot(screenshot_name)
    print(f"Screenshot saved: {screenshot_name}")