import allure
# import pytest
from selenium.webdriver.common.by import By
from steps.browser import open_link_in_browser, find_element_in_browser
from config.common import base_url


@allure.parent_suite("UI-тесты")
@allure.suite(f"Тесты страницы {base_url}")
@allure.sub_suite("Тесты элементов страницы")
class TestBaseLinkPage:
    
    # @pytest.mark.xfail
    @allure.title("Поиск на странице кнопки в контейнере")
    def test_find_button_on_page(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        button = find_element_in_browser(driver, By.XPATH, "/div/button")
        assert button

    @allure.title("Проверка тайтла страницы")
    def test_page_title_1(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        assert driver.title.__contains__("Публикации")

    @allure.title("Еще проверка тайтла")
    def test_page_title_2(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        assert not driver.title == "Random title"

    @allure.title("Поиск элемента на странице по классу")
    def test_find_element_by_class(self, set_up_browser):
        driver = set_up_browser
        open_link_in_browser(driver, base_url)
        elem = find_element_in_browser(driver, By.CLASS_NAME, "tm-header__become-author-btn")
        assert elem
