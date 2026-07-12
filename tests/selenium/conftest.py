from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless", action='store_true')

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")

    browser = None

    if browser_name == "chrome":
        options = ChromeOptions()
        service = ChromeService()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Invalid browser name")

    yield browser

    browser.quit()