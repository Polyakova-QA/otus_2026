from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from faker import Faker


def test_page_clothes(browser, base_url):
    browser.get(base_url + "3-clothes")
    wait = WebDriverWait(browser, 10)
    email_field = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    faker = Faker()
    faker_email = faker.email()
    email_field.send_keys(faker_email)
    browser.find_element(By.CSS_SELECTOR, "input[name='submitNewsletter']").click()
    expected_text = "You have successfully subscribed to this newsletter."
    modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#blockEmailSubscription_displayFooterBefore > div > div > form > p",
            )
        )
    )
    assert expected_text in modal.text
    browser.find_element(By.CSS_SELECTOR, "input[name='submitNewsletter']").click()
    expected_text_error = "This email address is already registered."
    modal = wait.until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "#blockEmailSubscription_displayFooterBefore > div > div > form > p",
            )
        )
    )
    assert expected_text_error in modal.text
    have_footer = browser.find_element(
        By.CSS_SELECTOR, "#footer > div.footer-container"
    )
    assert have_footer
    have_subcategories = browser.find_element(By.CSS_SELECTOR, "#subcategories > h2")
    assert have_subcategories
    have_brends = browser.find_element(
        By.CSS_SELECTOR, "#search_filters_brands > section"
    )
    assert "Graphic Corner" in have_brends.text and "Studio Design" in have_brends.text
    browser.find_element(
        By.XPATH, "//*[@id='search_filters']//a[contains(normalize-space(.), 'Black')]"
    ).click()
    modal = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#js-active-search-filters > ul > li")
        )
    )
    assert "Black" in modal.text
