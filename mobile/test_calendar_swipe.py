import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

TITLE_ID = "com.csdroid.pkg:id/tv_title"


def find_and_click(driver, app_name):
    driver.find_element(AppiumBy.ID, TITLE_ID)
    swipes = 0

    while True:
        elements = driver.find_elements(AppiumBy.ID, TITLE_ID)
        names_before = [element.text for element in elements]

        if app_name in names_before:
            with allure.step(f"«{app_name}» найден после {swipes} свайпов, кликаем"):
                elements[names_before.index(app_name)].click()
            return

        with allure.step(f"Свайп №{swipes + 1}"):
            first, start = elements[0].rect, elements[-2].rect
            driver.swipe(start["x"], start["y"], first["x"], first["y"], 1500)
        swipes += 1

        names_after = [element.text for element in driver.find_elements(AppiumBy.ID, TITLE_ID)]
        print(f"Свайп №{swipes}: {names_after}")

        if names_after == names_before:
            raise Exception(f"Достигнут конец списка после {swipes} свайпов, приложение «{app_name}» не найдено")


@allure.title("Поиск «Календаря» свайпами в PNV")
def test_find_calendar(driver):
    find_and_click(driver, "Календарь")

    with allure.step("Проверить, что открылось окно Календаря"):
        allure.attach(driver.get_screenshot_as_png(), name="Окно Календаря",
                      attachment_type=allure.attachment_type.PNG)
        title = driver.find_element(AppiumBy.ID, "com.csdroid.pkg:id/alertTitle").text
        assert title == "Календарь"


@allure.title("Несуществующее приложение: в конце списка выбрасывается исключение")
def test_missing_app(driver):
    with pytest.raises(Exception, match="Достигнут конец списка"):
        find_and_click(driver, "Несуществующее приложение")
