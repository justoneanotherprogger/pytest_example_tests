import allure


def take_screenshot(driver):
    allure.attach(
        driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def log_text(string):
    allure.attach(
        string,
        name='loginfo',
        attachment_type=allure.attachment_type.TEXT
    )
