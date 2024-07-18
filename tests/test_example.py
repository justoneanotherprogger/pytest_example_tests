from selenium.webdriver.common.by import By

class TestExample:
    def test_example_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://habr.com/")
        driver.find_element(By.XPATH, "/div/button")
        assert driver.title == "Публикации / Моя лента / Хабр"

    def test_example_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://habr.com/")
        assert driver.title.__contains__("Публикации")

    def test_example_3(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://habr.com/")
        assert not driver.title == "Skillbox"

    def test_example_4(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://habr.com/")
        assert not driver.title.__contains__("Skillbox")
