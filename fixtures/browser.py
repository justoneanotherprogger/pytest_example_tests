import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(name="set_up_browser")
@allure.title("Подготовка браузера")
def fixture_set_up_browser(install_webdriver, set_browser_options):
    service = Service(executable_path=install_webdriver, service_args=['--silent'])
    driver = webdriver.Chrome(service=service, options=set_browser_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(name="set_browser_options", scope="session")
@allure.title("Настройка опций браузера")
def fixture_set_browser_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    options.add_argument("--enable-automation")
    # options.add_argument("--disable-in-process-stack-traces")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options


@pytest.fixture(name="install_webdriver", scope="session")
@allure.title("Установка драйвера")
def fixture_install_webdriver():
    webdriver_path = ChromeDriverManager().install()
    return webdriver_path
