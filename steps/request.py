import allure
import requests


@allure.title("Запрашиваю ответ по адресу {url}")
def get_response_by_url(url, query=None, headers=None):
    result = requests.get(url, params=query, headers=headers)
    return result
