from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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

    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def currency(browser, base_url, request):
    path = request.param
    price = ".product-price-and-shipping .price"
    browser.get(base_url + path)
    wait = WebDriverWait(browser, 10)
    euro = browser.find_element(By.CSS_SELECTOR, price).text
    browser.find_element(
        By.CSS_SELECTOR, "#_desktop_currency_selector > div > button"
    ).click()
    modal = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#_desktop_currency_selector > div > ul > li:nth-child(2) > a",
            )
        )
    )
    modal.click()
    usd = browser.find_element(By.CSS_SELECTOR, price).text
    return {"euro": euro, "usd": usd}
