import pytest
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = Options()
    mobile_emulation = {"deviceName": "Pixel 7"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        timestamp = datetime.now().strftime('%H-%M-%S')
        driver.save_screenshot(f"failure_{timestamp}.png")
        print(f"\nScreenshot saved as failure_{timestamp}.png")