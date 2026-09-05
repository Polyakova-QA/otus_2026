import os

import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.options import ArgOptions

from pages.currency_selector import CurrencySelector

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--browser_version", default="128.0")
    parser.addoption("--base_url", default="http://localhost:8081/")
    parser.addoption(
        "--executor",
        default="local",
        help="local — браузер на этой машине, иначе имя хоста с WebDriver (например, ggr)",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")
        if browser is not None:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )


@pytest.fixture(scope="function")
def browser(request):
    browser_name: str = request.config.getoption("--browser")
    browser_version: str = request.config.getoption("--browser_version")
    executor: str = request.config.getoption("--executor")

    headless = os.getenv("HEADLESS", "").lower() in ("1", "true", "yes")

    if executor != "local":
        options = ArgOptions()
        options.set_capability("browserName", browser_name)
        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {"enableVNC": True})
        browser = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            options=options,
        )
    elif browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(options=options, service=ChromeService())
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        browser = webdriver.Edge()
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")

    browser.maximize_window()
    browser.base_url = request.config.getoption("--base_url")
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def currency(browser, request):
    page = CurrencySelector(browser, timeout=10).open(request.param)
    euro = page.price()
    page.switch_to_usd()
    usd = page.price()
    return {"euro": euro, "usd": usd}
