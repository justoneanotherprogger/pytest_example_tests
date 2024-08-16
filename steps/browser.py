import allure
import pytest
from selenium.common import NoSuchElementException
from helpers.logging import take_screenshot, log_text


@allure.step("Открываю страницу {link}")
def open_link_in_browser(driver, link):
    """
    Открывает в браузере страницу, указанную в link
    :param driver: драйвер браузера, в котором нужно перейти по ссылке
    :param link: ссылка на страницу
    """
    driver.get(link)
    log_text(f"Открыл страницу {driver.current_url}")


@allure.step("Ищу элемент с локатором {locator_type} {locator}")
def find_element_in_browser(driver, locator_type, locator):
    """
    Ищет на странице браузера элемент по локатору.
    Типы локаторов описаны в 'from selenium.webdriver.common.by import By'
    :param driver: драйвер браузера, на странице которого нужно искать
    :param locator_type: тип локатора, по которому нужно искать
    :param locator: сам локатор для поиска
    :return: ссылка на элемент на странице браузера
    """
    try:
        elem = driver.find_element(locator_type, locator)
    except NoSuchElementException:
        take_screenshot(driver)
        pytest.fail(f"На странице {driver.current_url} не найден элемент с локатором {locator}")
    return elem
