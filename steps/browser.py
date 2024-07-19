import allure
import pytest
from selenium.common import NoSuchElementException
from helpers.logging import take_screenshot, log_text


@allure.step("Открываю страницу {link}")
def open_link_in_browser(driver, link):
    driver.get(link)
    log_text(f"Открыл страницу {driver.current_url}")


@allure.step("Ищу элемент с локатором {locator_type} {locator}")
def find_element_in_browser(driver, locator_type, locator):
    try:
        elem = driver.find_element(locator_type, locator)
    except NoSuchElementException:
        take_screenshot(driver)
        pytest.fail(f"На странице {driver.current_url} не найден элемент с локатором {locator}")
    return elem
