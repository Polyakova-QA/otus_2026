import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from pages.currency_selector import CurrencySelector

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://localhost:8081/")


@pytest.fixture(scope="function")
def browser(request):
    browser_name: str = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = ChromeOptions()
        service = ChromeService()
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
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
