import allure
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    # Приложение PNV (Package Names)
    "appium:appPackage": "com.csdroid.pkg",
    "appium:appActivity": "com.csdroid.pkg.MainActivity",
    "appium:noReset": True,
    # Перезапускать PNV, чтобы список всегда начинался сверху
    "appium:forceAppLaunch": True,
    "appium:shouldTerminateApp": True,
    # Всегда вертикальная ориентация экрана
    "appium:orientation": "PORTRAIT",
})

appium_server_url = "http://localhost:4723"


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    android_driver.implicitly_wait(10)
    yield android_driver
    android_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            allure.attach(driver.get_screenshot_as_png(), name="Скриншот при падении",
                          attachment_type=allure.attachment_type.PNG)
