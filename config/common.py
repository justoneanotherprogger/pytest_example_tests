import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get_base_url(section: str) -> str:
    """
    Получает параметр BASE_URL из указанной секции файла config.ini из корня проекта
    :param section: название секции, например 'ui' или 'api'
    :return: строка, содержащая BASE_URL из указанной секции
    """
    base_url = config.get(section, "BASE_URL")
    return base_url
