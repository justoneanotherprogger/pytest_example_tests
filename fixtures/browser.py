from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(name="set_up_browser")
def fixture_set_up_browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    # options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--fullscreen")
    options.add_argument("--enable-automation")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()