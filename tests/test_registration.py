from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


def test_registration(browser, base_url):
    browser.get(base_url + "registration")
    wait = WebDriverWait(browser, 5)
    have_title = browser.find_element(By.CSS_SELECTOR, "#main > header > h1")
    assert have_title.is_displayed()
    input_password = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    input_password.send_keys("123")
    browser.find_element(
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > div.col-md-6.js-input-column > div.input-group.js-parent-focus > span > button",
    ).click()
    assert input_password.get_attribute("value") == "123"
    good_password = browser.find_element(
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > div.col-md-6.js-input-column > div:nth-child(2) > div > div.password-requirements > p.password-requirements-length",
    )
    assert (
        "Enter a password between 8 and 72 characters"
        in good_password.get_attribute("textContent")
    )
    min_password = browser.find_element(
        By.CSS_SELECTOR,
        "#customer-form > div > div.field-password-policy > div > div.col-md-6.js-input-column > div:nth-child(2) > div > div.password-requirements > p.password-requirements-score > span",
    )
    assert "The minimum score must be: Strong" in min_password.get_attribute(
        "textContent"
    )
    browser.find_element(By.CSS_SELECTOR, "#customer-form > footer > button").click()
    first_name = browser.find_element(By.CSS_SELECTOR, "#field-firstname")
    assert first_name.get_attribute("validationMessage") == "Заполните это поле."
