import allure


@allure.step("Открываю страницу {link}")
def open_link_in_browser(driver, link):
    driver.get(link)


@allure.step("Ищу элемент с локатором {locator_type} {locator}")
def find_element_in_browser(driver, locator_type, locator):
    elem = driver.find_element(locator_type, locator)
    return elem
