from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


def test_administration(browser, base_url):
    browser.get(base_url + "administration")
    wait = WebDriverWait(browser, 5)
    have_email = browser.find_element(
        By.CSS_SELECTOR, "#login_form > div:nth-child(2) > label"
    )
    assert "Email address" in have_email.text
    have_password = browser.find_element(
        By.CSS_SELECTOR, "#login_form > div:nth-child(3) > label"
    )
    assert "Password" in have_password.text
    browser.find_element(By.CSS_SELECTOR, "#submit_login").click()
    error = browser.find_element(
        By.CSS_SELECTOR, "#login_form > div:nth-child(2) > span"
    )
    assert error.get_attribute("class") == "help-block"
    assert "This field is required." in error.text
    checkbox = browser.find_element(By.CSS_SELECTOR, "#stay_logged_in")
    checkbox.click()
    assert checkbox.is_selected()
    browser.find_element(By.CSS_SELECTOR, "#forgot-password-link").click()
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#reset-password-button"))
    )
    email_field = browser.find_element(By.CSS_SELECTOR, "#email_forgot")
    email_field.send_keys("mail@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#reset-password-button").click()
    error = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#error > p"))
    )
    text_error = (
        "You can reset your password every 360 minute(s) only. Please try again later."
    )
    assert text_error in error.text
