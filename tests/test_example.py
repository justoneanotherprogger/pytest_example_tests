import allure
import pytest
from selenium.webdriver.common.by import By
from steps.browser import open_link_in_browser, find_element_in_browser
from config.common import base_url


@allure.parent_suite("Верхний уровень набора тестов")
@allure.suite("Средний уровень набора тестов")
@allure.sub_suite("Нижний уровень набора тестов")
class TestExample:
    
    @pytest.mark.xfail
    @allure.title("Поиск на странице кнопки в контейнере")
    def test_example_1(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        button = find_element_in_browser(driver, By.XPATH, "/div/button")
        assert button

    @allure.title("Проверка тайтла страницы")
    def test_example_2(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        assert driver.title.__contains__("Публикации")

    @pytest.mark.skip("Сейчас не нужен")
    @allure.title("Еще проверка тайтла")
    def test_example_3(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        assert not driver.title == "Skillbox"

    @pytest.mark.skip("Сейчас не нужен")
    @allure.title("Последняя проверка тайтла")
    def test_example_4(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        assert not driver.title.__contains__("Skillbox")
