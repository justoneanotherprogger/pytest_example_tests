import allure
import pytest
from config.common import get_base_url

base_url = get_base_url('api')


@allure.parent_suite("API-тесты")
@allure.suite(f"Тесты сервиса {base_url}")
@allure.sub_suite("Тесты запросов в базу людей")
@pytest.mark.api
class TestApiPeople:

    @allure.title("Поиск на странице кнопки в контейнере")
    def test_people_list(self):
        pass
