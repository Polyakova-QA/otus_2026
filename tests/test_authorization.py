from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import os

PASSWORD = os.getenv("TEST_PASSWORD")


def test_authorization(browser, base_url):
    wait = WebDriverWait(browser, 4)
    browser.get(base_url + "login")
    browser.find_element(By.NAME, "email").send_keys("mail@mail.com")
    browser.find_element(By.NAME, "password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, "#submit-login").click()
    modal = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#_desktop_user_info > div > a.account > span")
        )
    )
    assert modal.text == "Nadezhda P."
    browser.find_element(
        By.CSS_SELECTOR, "#_desktop_user_info > div > a.logout.hidden-sm-down"
    ).click()
    sign_in = browser.find_element(
        By.CSS_SELECTOR, "#_desktop_user_info > div > a > span"
    )
    assert sign_in.text == "Sign in"
